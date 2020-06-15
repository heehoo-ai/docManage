from django.shortcuts import render, redirect
from django.views.generic import ListView

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
        file_name = request.FILES.get('pdf').name

        new_file = form.save(commit=False)
        if not new_file.title:
            new_file.title = file_name
        new_file.save()
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
        category = Category.objects.get(id=category_id)
        docs = category.doc_set.all()
    else:
        docs = Doc.objects.all()
    cats = Category.objects.all()
    context = {
        'docs': docs,
        'cats': cats,
        'category': category,
    }
    return render(request, 'doc_list.html', context=context)


def get_by_serch(request):
    keyword = request.GET.get('keyword')
    if keyword:
        docs = Doc.objects.filter(title__icontains=keyword)
    else:
        docs = Doc.objects.all()
    cats = Category.objects.all()
    context = {
        'docs': docs,
        'cats': cats,
    }
    return render(request, 'doc_list.html', context=context)


class SearchView(ListView):
    model = Doc
    template_name = 'doc_list.html'
    context_object_name = 'docs'
    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'keyword': self.request.GET.get('keyword'),
        })
        return context

    def get_queryset(self):
        """重写queryset，根据标题搜索"""
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(title__icontains=keyword)