from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from books.models import Book
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from checkout.models import Order


@login_required
def book_reviews(request, book_id):
    """
    View for reviews
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

    if existing_review:
        messages.error(
            request,
            f'You have already review this book!'
        )
        return redirect('book_detail', book_id=book_id)

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