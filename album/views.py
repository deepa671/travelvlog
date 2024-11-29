from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Image
from django.contrib import messages

def home_page(request):
    category = request.GET.get('category')

    if category == None:
        images = Image.objects.all()
    else:
        images = Image.objects.filter(category__name=category)

    categories = Category.objects.all()

    context = {"categories": categories, 'images': images}
    return render(request, 'album/album_index.html', context)

def viewPics(request, pk):
    image = Image.objects.get(id=pk)

    return render(request, "album/view_photo.html", {"image": image})

@login_required
def addPics(request):
    categories = Category.objects.all()

    if request.method == "POST":
        data = request.POST
        picture = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        image = Image.objects.create(
            category=category,
            description=data['description'],
            picture=picture,
        )
        return redirect('all')

    context = {'categories': categories}
    return render(request, 'album/add_photo.html', context)

def deletePics(request, pk):
    image = Image.objects.get(id=pk)

    if request.method == "POST":
        image.delete()
        return redirect('all')
    return render(request, "album/del_photo.html", {"image": image})