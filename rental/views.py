from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
from .models import (contactu,  Category, Landlord, Propertie, Property_image,
                     Property_Taken,  BookedPropertie, Employee, Signup)
from django.db.models import Q

# Create your views here.


def home_page(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    properties = Propertie.objects.filter(available=True, vaccant=True)

    p = Paginator(properties, 9)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    if category_slug:

        category = get_object_or_404(
            Category, slug=category_slug)

        properties = Propertie.objects.filter(
            category=category, available=True, vaccant=True)

    return render(request, 'Properties/home_page.html', {'category': category, 'categories': categories, 'properties': properties,
                                                         'items': page})


def secondpage(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    properties = Propertie.objects.filter(available=True, vaccant=True)
    allproperties = Propertie.objects.filter(available=True, vaccant=True)

    if category_slug:

        category = get_object_or_404(
            Category, slug=category_slug)

        properties = Propertie.objects.filter(
            category=category, available=True, vaccant=True)

    p = Paginator(properties, 3)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request, 'Properties/fourth.html', {'category': category, 'categories': categories, 'properties': properties,  'item': page, 'allproperties': allproperties})


# def advert(request, type_slug=None, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     Advert_type = None
#     properties = Propertie.objects.filter(available=True, vaccant=True)

#     if type_slug:
#         Advert_type = get_object_or_404(Type, slug=type_slug)

#         properties = Propertie.objects.filter(
#             Advert_type=Advert_type, available=True, vaccant=True)

#     if category_slug:
#         category = get_object_or_404(
#             Category, slug=category_slug)

#         properties = Propertie.objects.filter(
#             category=category, available=True, vaccant=True)

#     return render(request, 'Properties/fourth.html', {'category': category, 'categories': categories, 'properties': properties,  'Advert_type': Advert_type})


def ByType(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    allproperties = Propertie.objects.filter(available=True, vaccant=True)
    properties = Propertie.objects.filter(
        Advert_type=('other'), available=True, vaccant=True)

    p = Paginator(properties, 6)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    if category_slug:

        category = get_object_or_404(
            Category, slug=category_slug)

        properties = Propertie.objects.filter(
            category=category, available=True, vaccant=True)

    return render(request, 'Properties/fourth.html', {'category': category, 'categories': categories, 'properties': properties,  'item': page, 'allproperties': allproperties})


def thirdpage(request, id, slug, category_slug=None):
    category = None
    categories = Category.objects.all()
    allproperties = Propertie.objects.filter(available=True, vaccant=True)
    properties = get_object_or_404(
        Propertie, id=id, slug=slug, available=True, vaccant=True)

    detailImages = Property_image.objects.filter(
        pro_id=id, available=True)
    if category_slug:
        category = get_object_or_404(
            Category, slug=category_slug)
    return render(request, 'Properties/third.html', {'detailImages': detailImages, 'category': category, 'categories': categories, 'properties': properties, 'allproperties': allproperties})


def postproperty(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    landlords = Landlord.objects.all()
    properties = Propertie.objects.filter(available=True, vaccant=True)

    if category_slug:

        category = get_object_or_404(
            Category, slug=category_slug)
        properties = Propertie.objects.filter(
            category=category, available=True, vaccant=True)
    return render(request, 'Properties/post.html', {'category': category, 'categories': categories, 'properties': properties,  'landlords': landlords})


def book_form(request):

    book = BookedPropertie.objects.all()
    client = Customer.objects.all()
    response_data = {}

    if request.method == 'POST':
        kind = request.POST["kind"]
        name = request.POST["name"]
        idi = request.POST['idnumber']
        phone = request.POST['phone']
        email = request.POST['email']
        proId = request.POST['proId']

        response_data['kind'] = kind
        response_data['name'] = name
        response_data['idnumber'] = idi
        response_data['phone'] = phone
        response_data['email'] = email
        response_data['proId'] = proId

        Customer.objects.create(
            customer_type=kind,
            customer_id=idi,
            customer_name=name,
            customer_email=email,
            customer_phon=phone,
        )
        BookedPropertie.objects.create(
            customer_booker=idi,
            property_booked=proId,
        )

        return JsonResponse(response_data)

    return render(request, 'Properties/third.html')


def register_form(request):

    book = Signup.objects.all()
    response_data = {}

    if request.method == 'POST':

        name = request.POST["name"]
        username = request.POST["username"]
        password = request.POST['password']
        emaille = request.POST['email']

        Signup.objects.create(
            U_name=name,
            U_username=username,
            U_Userpassword=password,
            U_email=emaille,
        )
        return render(request, 'Properties/third.html')

    return render(request, 'Properties/third.html')


def login_form(request):
    return render(request, 'Properties/login.html')


def signup_form(request):
    return render(request, 'Properties/register.html')


def search_result_form(request):
    return render(request, 'Properties/searchResult.html')


def contact_form(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    properties = Propertie.objects.filter(available=True, vaccant=True)

    p = Paginator(properties, 6)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    if category_slug:

        category = get_object_or_404(
            Category, slug=category_slug)

        properties = Propertie.objects.filter(
            category=category, available=True, vaccant=True)

    if request.method == "POST":
        email = request.POST['email']
        message = request.POST['message']

        contactu.objects.create(
            message=message,
            email=email
        )
        return render(request, 'Properties/home_page.html', {'category': category, 'categories': categories, 'properties': properties, 'items': page})

    return render(request, 'Properties/home_page.html', {'category': category, 'categories': categories, 'properties': properties, 'items': page})


def search(request, category_slug=None):
    category = None
    category = Category.objects.all()
    categories = Category.objects.all()
    properties = Propertie.objects.all()
    result = Propertie.objects.all()
    allproperties = Propertie.objects.filter(available=True, vaccant=True)

    if category_slug:

        category = get_object_or_404(
            Category, slug=category_slug)

        properties = Propertie.objects.filter(
            category=category, available=True, vaccant=True)

    p = Paginator(properties, 8)
    page_num = request.GET.get('page', 1)

    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    if request.method == 'GET':

        cat = request.GET.get('categorization')
        prop = request.GET.get('adverttype')
        place = request.GET.get('place')
        bed = request.GET.get('room')
        price = request.GET.get('price')

        if cat and prop and place and bed:
            result = Propertie.objects.filter(
                category=cat, Advert_type=prop, cell=place, Bedroom=bed, available=True, vaccant=True)

            if result:

                return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'properties': properties, 'values': page, 'cat': cat, 'prop': prop, 'place': place, 'bed': bed})

            else:
                return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'values': page, 'properties': properties, 'cat': cat, 'prop': prop, 'place': place, 'bed': bed})

        if cat and prop and bed:

            result = Propertie.objects.filter(
                category=cat, Advert_type=prop, Bedroom=bed, available=True, vaccant=True)

            if result:

                return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'properties': properties, 'values': page, 'cat': cat, 'prop': prop, 'bed': bed})

            else:
                return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'values': page, 'properties': properties, 'cat': cat, 'prop': prop, 'bed': bed})

        if cat and prop and place:

            result = Propertie.objects.filter(
                category=cat, Advert_type=prop, cell=place, available=True, vaccant=True)

            if result:

                return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'properties': properties, 'values': page, 'cat': cat, 'prop': prop, 'place': place})

            else:
                return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'values': page, 'properties': properties, 'cat': cat, 'prop': prop, 'place': place})

        if cat and prop:

            result = Propertie.objects.filter(
                category=cat, Advert_type=prop, available=True, vaccant=True)

            if result:

                return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'properties': properties, 'values': page, 'cat': cat, 'prop': prop})

            else:
                return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'values': page, 'properties': properties, 'cat': cat, 'prop': prop})

        if cat:

            result = Propertie.objects.filter(
                category=cat, available=True, vaccant=True)

            if result:
                return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'properties': properties, 'values': page, 'cat': cat})

            else:
                return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'values': page, 'cat': cat, 'properties': properties, 'cat': cat})
        if prop:

            result = Propertie.objects.filter(
                Advert_type=prop, available=True, vaccant=True)

            if result:
                return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'properties': properties, 'values': page, 'prop': prop})

            else:
                return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'values': page, 'cat': cat, 'properties': properties, 'prop': prop})

        else:
            return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'result': result, 'allproperties': allproperties, 'values': page, 'properties': properties, 'cat': cat})

    else:

        return render(request, 'Properties/searchResult.html', {'category': category, 'categories': categories, 'properties': properties,  'values': page, 'allproperties': allproperties})
