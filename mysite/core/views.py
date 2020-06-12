from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from xlwings import books

from .forms import DocForm
from .models import Doc, Category


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


def get_by_category(request, category_id=None):
    if category_id:
        docs = Category.objects.get(id=category_id).doc_set.all()
    else:
        docs = Doc.objects.all()
    cats = Category.objects.all()
    context = {
        'docs': docs,
        'cats': cats,
    }
    return render(request, 'doc_list.html', context=context)


