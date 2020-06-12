from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from xlwings import books

from .forms import DocForm
from .models import Doc, Category


class Home(TemplateView):
    template_name = 'home.html'


def doc_list(request):
    docs = Doc.objects.all()
    cats = Category.objects.all()
    return render(request, 'doc_list.html', {
        'docs': docs,
        'cats': cats,
    })


def upload_doc(request):
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doc_list')
    else:
        form = DocForm()
    return render(request, 'upload_doc.html', {
        'form': form
    })


def delete_doc(request, pk):
    if request.method == 'POST':
        doc = Doc.objects.get(pk=pk)
        doc.delete()
    return redirect('doc_list')


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(Category.get_navs())
        return context


class IndexView(CommonViewMixin, ListView):
    model = Doc
    template_name = 'doc_list.html'
    context_object_name = 'doc_list'


class CategoryView(IndexView):
    def get_queryset(self):
        """重写queryset，根据分类过滤"""
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })
        return context


