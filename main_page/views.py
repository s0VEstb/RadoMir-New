from django.shortcuts import render, HttpResponse
import datetime
from . import models
from django.views import generic
from .forms import CommentForm
from django.shortcuts import redirect

def about_me(request):
    return render(request, 'main_page/about_me.html')


def about_my_pets(request):
    return render(request, 'main_page/about_my_pets.html')


def time(request):
    return HttpResponse(f"Текущее время: {datetime.datetime.now()}")


class BookListView(generic.ListView):
    template_name = 'book/book.html'
    context_object_name = 'books'
    model = models.Book

    def get_queryset(self):
        return models.Book.objects.all()


class BookDetailView(generic.DetailView):
    template_name = 'book/book_detail.html'
    model = models.Book
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = self.object
            comment.save()
            return redirect('book-detail', pk=self.object.pk)  # Редирект на ту же страницу
        return self.get(request, *args, **kwargs)
