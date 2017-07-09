from django.shortcuts import render
from rango.models import Category,Page
from rango.forms import CategoryForm,PageForm
# Create your views here.
from django.http import HttpResponse


def index(request):
    category_list = Category.objects.order_by('-like')[:5]
    all_dict ={'categories':category_list}
    return render(request,'rango/index.html',all_dict)

def about(request):
    all_dict={'twomessage':"it is best/"}
    return render(request,'rango/about.html',all_dict)

def category(request,category_name_slug):
    context_dict={}

    try:
        category = Category.objects.get(slug=category_name_slug)

        context_dict['category_name']=category.name

        pages=Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category']=category
    except Category.DoesNotExist:
        return render(request,'rango/404.html',context_dict)
    return render(request,'rango/category.html',context_dict)

def add_category(request):
    if request.method == 'POST':
        form =CategoryForm(request.POST)


        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors

    else:

        form = CategoryForm()

    return render(request,'rango/add_category.html',{'form':form})
def add_page(request):
    try:
        cat= Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat=0

    if request.method == 'POST':
        form =PageForm((request.POST)
        if form.is_valid():
            if cat:
                page=form.save(commit=False)
                page.category=cat
    return render(request,'rango/add_pages.html',{'form'}:form)