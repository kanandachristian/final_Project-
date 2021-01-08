
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.db import IntegrityError

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

    response_data = {}

    if request.method == 'POST':
        customer_type = request.POST["kind"]
        customer_id = request.POST['idnumber']
        name = request.POST["name"]
        email = request.POST['email']
        phone = request.POST['phone']
        period = request.POST['period']
        proId = request.POST['proId']
        property_id_id = Propertie.objects.get(id=proId)

        response_data['kind'] = customer_type
        response_data['idnumber'] = customer_id
        response_data['name'] = name
        response_data['email'] = email
        response_data['phone'] = phone
        response_data['period'] = period
        response_data['proId'] = property_id_id

        try:
            BookedPropertie.objects.create(
                customer_type=customer_type,
                customer_id=customer_id,
                customer_name=name,
                customer_email=email,
                customer_phon=phone,
                booking_period=period,
                property_booked=property_id_id,
            )

            messages.success(
                request, 'Property booked successfuly')
            return render(request, 'Properties/success.html')

        except IntegrityError:

            messages.error(
                request, 'Sorry the property has already been Booked')
            return render(request, 'Properties/error.html')

    return HttpResponse('Please fill properly the booking Fields')


def save_form(request):

    if request.method == "POST":
        landlord_kind = request.POST['l-kind']
        landlord_name = request.POST['l-name']
        landlord_email = request.POST['l-email']
        landlord_id = request.POST['l-id']
        landlord_id_id = Landlord.objects.get(id=landlord_id)
        landlord_phone = request.POST['l-phone']

        property_category = request.POST['p-category']
        property_category_id = Category.objects.get(id=property_category)
        property_type = request.POST['p-type']
        property_name = request.POST['p-title']
        property_price = request.POST['p-price']
        property_currency = request.POST['p-currency']
        property_payable = request.POST['p-payable']
        property_room = request.POST['p-room']
        property_bathroom = request.POST['p-bathroom']
        property_description = request.POST['p-description']
        property_sector = request.POST['p-sector']
        property_cell = request.POST['p-cell']
        property_village = request.POST['p-village']
        property_number = request.POST['p-number']
        property_image = request.POST['p-profile']

        Landlord.objects.create(
            landlord_type=landlord_kind,
            landlord_id=landlord_id,
            landlord_name=landlord_name,
            landlord_phone=landlord_phone,
            landlord_email=landlord_email,
        )

        Propertie.objects.create(
            category=property_category_id,
            Advert_type=property_type,
            name=property_name,
            property_price=property_price,
            currency=property_currency,
            payable=property_payable,
            description=property_description,
            Bedroom=property_room,
            Bathroom=property_bathroom,
            sector=property_sector,
            cell=property_cell,
            village=property_village,
            number=property_number,
            image=property_image,
            landlord_Id=landlord_id_id,
            available=False,
            vaccant=False
        )

        return HttpResponse('Post sent successfuly')
    return HttpResponse('Post is not send')


def register_form(request):
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
        message = request.POST['messageM']

        contactu.objects.create(
            message=message,
            email=email
        )
        return render(request, 'Properties/home_page.html', {'category': category, 'categories': categories, 'properties': properties, 'items': page})

    return render(request, 'Properties/home_page.html', {'category': category, 'categories': categories, 'properties': properties, 'items': page})


def sendMail(request):
    messageM = request.POST.get('messageM', 'message')
    from_email = request.POST.get('from_email', 'email')

    if messageM and from_email:
        try:
            send_mail('subject',
                      messageM,
                      from_email,

                      ['kanandachristian@gmail.com'],
                      fail_silently=False,)

            messages.success(
                request, 'Message sent successfuly ')
            return render(request, 'Properties/success.html')

        except BadHeaderError and UnicodeError:
            messages.error(
                request, 'Invalid header found and UnicodeError')
            return render(request, 'Properties/error.html')

        messages.error(
            request, 'Make sure you have you entered right values')
        return render(request, 'Properties/error.html')

    else:
        return HttpResponse('Make sure all fields are entered and valid.')


def search(request, category_slug=None):
    category = None
    category = Category.objects.all()
    categories = Category.objects.all()
    properties = Propertie.objects.all()
    result = Propertie.objects.all()
    cat = request.GET.get('categorization')
    allproperties = Propertie.objects.filter(
        category=cat, available=True, vaccant=True)

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
