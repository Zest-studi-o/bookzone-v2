from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import Review
from .forms import ReviewForm
from books.models import Book
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from checkout.models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import CreateView
from django.views import generic
from django.urls import reverse_lazy


class ReviewList(generic.ListView):
    """
    Class to show existing reviews
    """

    model = Review
    template_name = 'reviews/book-reviews.html'
    paginate_by = 6


@login_required
def book_reviews(request, book_id):
    """
    View to create a review
    Update user to custom
    """
    book = Book.objects.get(pk=book_id)
    existing_review = Review.objects.filter(
        book=book,
        reviewer=request.user
    ).first()
    user = request.user
    has_ordered_book = Order.objects.filter(
        user_profile=user.userprofile,
        lineitems__book=book
    ).exists()

    reviews = book.reviews.all()

    if has_ordered_book:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.book = book
                review.reviewer = request.user
                review.save()
                return redirect('book_detail', book_id=book_id)
        else:
            form = ReviewForm()
    else:
        messages.error(
            request,
            f'You havent purchased this book'
        )
        return redirect('book_detail', book_id=book_id)
    context = {
        'book': book,
        'reviews': reviews,
        'form': form
    }

    return render(request, 'reviews/book_reviews.html', context)


@login_required
def update_review(request, review_id):
    """ View to update a review """

    review = get_object_or_404(Review, pk=review_id)
    if review.reviewer or user.is_superuser == request.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated review!')

                return redirect(reverse('book_detail', kwargs={'book_id': review.book.id}))
            else:
                messages.error(request, 'Failed to update review. Please ensure the form is valid.')
        else:
            form = ReviewForm(instance=review)
            messages.info(request, f'You are updating: {review.book}')
    else:
        messages.error(request, 'Logged user is not the author of this review. Update request denied.')
      
        return redirect(reverse('book_reviews', args=[review.book.id]))

    template = 'reviews/update_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


class DeleteReview(LoginRequiredMixin, generic.DeleteView):
    """ View to update a review """

    model = Review
    template_name = 'reviews/delete_review.html'

    def delete(self, request, *args, **kwargs):
        review = self.get_object()
        if review.reviewer != request.user:
            messages.error(self.request, 'You are not the author of this review!')
            return redirect(reverse('book-reviews'))
        return super(DeleteReview, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        review = self.get_object()
        book_id = review.book.id
        messages.success(self.request, 'You have deleted a review!')
        return reverse('book_detail', kwargs={'book_id': book_id})
