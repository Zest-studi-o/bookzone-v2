from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Case, When, F, DecimalField, Avg, Value
from .models import Book, Category
from django.db.models.functions import Lower
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from profiles.models import UserProfile
from reviews.models import Review
from checkout.models import Order
from .forms import BookForm
from django.http import HttpResponseBadRequest
from datetime import date


def all_books(request):
    """
    All books
    """
    books = Book.objects.annotate(
        average_rating=Avg('reviews__rating')
    )

    for book in books:
        book.average_rating = book.calculate_average_rating()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                books = books.annotate(
                    lower_name=Lower('name')
                    )
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
            if sortkey == 'price':
                if direction == 'asc':
                    books = books.annotate(
                        sorted_price=Case(
                            default='price',
                            output_field=DecimalField()
                        )
                    ).order_by(F('sorted_price').asc(nulls_last=True))
                elif direction == 'desc':
                    books = books.annotate(
                        sorted_price=Case(
                            default='price',
                            output_field=DecimalField()
                        )
                    ).order_by(F('sorted_price').desc(nulls_last=True))
            elif sortkey == 'rating':
                if direction == 'asc':
                    books = books.annotate(
                        rating_is_null=Case(
                            When(average_rating__isnull=True, then=Value(1)),
                            default=Value(0),
                            output_field=DecimalField()
                        )
                    ).order_by('rating_is_null', 'average_rating')
                elif direction == 'desc':
                    books = books.annotate(
                        rating_is_null=Case(
                            When(average_rating__isnull=True, then=Value(1)),
                            default=Value(0),
                            output_field=DecimalField()
                        )
                    ).order_by('rating_is_null', '-average_rating')
            else:
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                books = books.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            books = books.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                )
                return redirect(reverse('books'))

            queries = \
                Q(title__icontains=query) | Q(description__icontains=query)
            books = books.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'books': books,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'books/books.html', context)


def book_detail(request, book_id):
    """
    Book details

    """
    book = get_object_or_404(Book, pk=book_id)
    reviews = book.reviews.all()
    average_rating = book.calculate_average_rating()
    user = request.user
    has_ordered_book = False
    has_reviewed = False

    if user.is_authenticated:
        has_ordered_book = Order.objects.filter(
            user_profile=user.userprofile, lineitems__book=book
        ).exists()
        has_reviewed = Review.objects.filter(
            reviewer=user, book=book
        ).exists()

    context = {
        'book': book,
        'reviews': reviews,
        'average_rating': average_rating,
        'has_ordered_book': has_ordered_book,
        'has_reviewed': has_reviewed,
    }

    return render(request, 'books/book_detail.html', context)


@login_required
def add_book(request):
    """
    Add a book to the store.
 
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only store owners can do that.'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            messages.success(request, 'Successfully added book!')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            messages.error(
                request,
                'Failed to add book. Please ensure the form is valid.'
            )
    else:
        form = BookForm()
    template = 'books/add_book.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_book(request, book_id):
    """
    Edit a book
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only admins can do that.'
        )
        return redirect(reverse('home'))

    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated book!')
            return redirect(reverse('book_detail', args=[book.id]))
        else:
            messages.error(
                request,
                'Failed to update book. Please ensure the form is valid.'
            )
    else:
        form = BookForm(instance=book)
        messages.info(request, f'You are editing {book.title}')

    template = 'books/edit_book.html'
    context = {
        'form': form,
        'book': book,
    }

    return render(request, template, context)


@login_required
def delete_book(request, book_id):
    """
    Delete a book
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only adminss can do that.'
        )
        return redirect(reverse('home'))

    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        if book_id:
            book = get_object_or_404(Book, pk=book_id)
            book.delete()
            messages.success(request, 'Book deleted successfully.')
            return redirect('books')
        else:
            return HttpResponseBadRequest('Invalid request')
    else:
        return HttpResponseBadRequest('Invalid request')


@login_required
def admin_books(request):
    """
    View all books for administrators.
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only administrators can access this page.'
        )
        return redirect(reverse('home'))

    books = Book.objects.all()

    context = {
        'books': books
    }
    return render(request, 'books/admin_books.html', context)