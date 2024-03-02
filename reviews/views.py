from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import Review
from django.views.generic import CreateView
from .forms import ReviewForm


class ReviewList(generic.ListView):
    """
    Class to show existing reviews
    """

    model = Review
    queryset = Review.objects.filter(status=1).order_by('-date_created')
    template_name = 'reviews/reviews.html'
    paginate_by = 6


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """
    VIEW TO CREATE A REVIEW
    """

    form_class = ReviewForm
    template_name = 'reviews/add_review.html'

    def form_valid(self, form):
        form.instance.reviewer = self.request.user
        from checkout.models import Order
        order = Order.objects.get(order_number=self.kwargs['order_number'])

        if form.instance.reviewer.id != order.user_profile.id:
            messages.error(self.request, "Logged user does not match the order details.")  # noqa E501
            return redirect('profile')  # Redirect to the profile page or another appropriate page # noqa E501

        # Check if the order has already been reviewed
        if order.reviewed:
            messages.error(self.request, "This order has already been reviewed.")  # noqa E501
            return redirect('profile')  # Redirect to the profile page or another appropriate page # noqa E501

        form.instance.order = order
        super().form_valid(form)
        if not order.reviewed:
            order.reviewed = True
            order.save()

        messages.success(self.request, "Added a new Review! Please wait for our admin to accept and publish.")  # noqa E501
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super(ReviewCreateView, self).get_context_data(**kwargs)
        context['order_number'] = self.kwargs['order_number']
        return context

    def get_success_url(self):
        return reverse('reviews')


@login_required
def update_review(request, review_id):
    """ Update a review in the store """

    review = get_object_or_404(Review, pk=review_id)
    if review.reviewer == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                review.status = 0
                form.save()
                messages.success(request, 'Successfully updated review! Please wait for our admin to accept and publish.')  # noqa E501
                return redirect(reverse('reviews'))
            else:
                messages.error(request, 'Failed to update review. Please ensure the form is valid.')  # noqa E501
        else:
            form = ReviewForm(instance=review)
            messages.info(request, f'You are updating {review.review_title}')
    else:
        messages.error(request, 'Logged user is not the reviewer. Update request denied.')  # noqa E501
        return redirect(reverse('reviews'))

    template = 'reviews/update_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


class DeleteReview(LoginRequiredMixin, generic.DeleteView):
    """
    View that allows logged in users to delete a review.
    The user us prompted with a warning.
    """
    model = Review
    template_name = 'reviews/delete_review.html'

    def delete(self, request, *args, **kwargs):
        """
        Method to validate owner against logged in user.
        """
        review = self.get_object()
        if review.reviewer != request.user:
            messages.error(self.request, 'You are not the reviewer!')
            return redirect(reverse('reviews'))
        return super(DeleteReview, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        messages.success(self.request, 'You have deleted a review!')
        return reverse_lazy('reviews')