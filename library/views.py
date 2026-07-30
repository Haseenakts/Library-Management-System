from django.shortcuts import render, redirect
from .models import Book, Member, Issue


def home(request):
    total_books = Book.objects.count()
    total_members = Member.objects.count()
    total_issues = Issue.objects.filter(returned=False).count()

    context = {
        'total_books': total_books,
        'total_members': total_members,
        'total_issues': total_issues,
    }

    return render(request, 'library/home.html', context)


def books(request):
    all_books = Book.objects.all()

    return render(
        request,
        'library/books.html',
        {'books': all_books}
    )


def add_book(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')

        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            category=category,
            quantity=quantity,
            available_quantity=quantity
        )

        return redirect('books')

    return render(request, 'library/add_book.html')


def members(request):

    all_members = Member.objects.all()

    return render(
        request,
        'library/members.html',
        {'members': all_members}
    )


def issues(request):

    all_issues = Issue.objects.all()

    return render(
        request,
        'library/issues.html',
        {'issues': all_issues}
    )