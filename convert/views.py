from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
from rental.models import (contactu,  Category, Landlord, Propertie, Property_image,
                           Property_Taken,  BookedPropertie, Employee, Signup)
from django.db.models import Q
# Create your views here.


def events(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    properties = Propertie.objects.filter(available=True, vaccant=True)

    if category_slug:

        category = get_object_or_404(
            Category, slug=category_slug)

        properties = Propertie.objects.filter(
            category=category, available=True, vaccant=True)

    currencies = ['RWF', 'USD', 'FC']
    currencie = ['USD', 'FC', 'RWF']

    # return render(request,'converter.html',{'currencies':currencies,'currencie':currencie})
    return render(request, 'converter.html', {'category': category, 'categories': categories, 'properties': properties})


def actionconv(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    properties = Propertie.objects.filter(available=True, vaccant=True)

    if category_slug:

        category = get_object_or_404(
            Category, slug=category_slug)

        properties = Propertie.objects.filter(
            category=category, available=True, vaccant=True)

    if request.method == 'GET':
        amount = float(request.GET['montant'])
        currence1 = int(request.GET['selection1'])
        currence2 = int(request.GET['selection2'])
        rwf = 'RWF'
        usd = 'USD'
        fc = 'FC'
        tauxA = 932
        tauxV = 1600
        value = 0.0

        if currence1 != currence2:
            if currence1 == 1 and currence2 == 2:
                value = amount * tauxA
                x = 1 * tauxA
                y = 1 / tauxA
                tot = {"am": amount, "tauxA": tauxA, "tauxV": tauxV,
                       "value": value, "usd": usd, "rwf": rwf, "fc": fc, "x": x, "y": y}
                return render(request, 'converter2.html', {'total': tot, 'category': category, 'categories': categories, 'properties': properties})
            if currence1 == 2 and currence2 == 1:
                value = amount / tauxA
                x = 1 * tauxA
                y = 1 / tauxA

                tot = {"am": amount, "tauxA": tauxA, "tauxV": tauxV,
                       "value": value, "usd": usd, "rwf": rwf, "fc": fc, "x": x, "y": y}
                return render(request, 'converter3.html', {'total': tot, 'category': category, 'categories': categories, 'properties': properties})
                ############################# USD RWF ####################################################
            if currence1 == 1 and currence2 == 3:
                value = amount * tauxV
                x = 1 * tauxV
                y = 1 / tauxV

                tot = {"am": amount, "tauxA": tauxA, "tauxV": tauxV,
                       "value": value, "usd": usd, "rwf": rwf, "fc": fc, "x": x, "y": y}
                return render(request, 'converter4.html', {'total': tot, 'category': category, 'categories': categories, 'properties': properties})
            if currence1 == 3 and currence2 == 1:
                value = amount / tauxV
                x = 1 * tauxV
                y = 1 / tauxV

                tot = {"am": amount, "tauxA": tauxA, "tauxV": tauxV,
                       "value": value, "usd": usd, "rwf": rwf, "fc": fc, "x": x, "y": y}
                return render(request, 'converter5.html', {'total': tot, 'category': category, 'categories': categories, 'properties': properties})
                ############################ USD FC ####################################################
            if currence1 == 2 and currence2 == 3:
                value = amount * 2
                x = 1 * 2
                y = 1 / 2

                tot = {"am": amount, "tauxA": tauxA, "tauxV": tauxV,
                       "value": value, "usd": usd, "rwf": rwf, "fc": fc, "x": x, "y": y}
                return render(request, 'converter6.html', {'total': tot, 'category': category, 'categories': categories, 'properties': properties})
            if currence1 == 3 and currence2 == 2:
                value = amount / 2
                x = 1 * 2
                y = 1 / 2

                tot = {"am": amount, "tauxA": tauxA, "tauxV": tauxV,
                       "value": value, "usd": usd, "rwf": rwf, "fc": fc, "x": x, "y": y}
                return render(request, 'converter7.html', {'total': tot, 'category': category, 'categories': categories, 'properties': properties})
            else:
                return redirect('conversion:Error')
                ############################ RWF FC ####################################################
        else:
            return redirect('conversion:Error')

    else:
        return render(request, 'converter1.html', {'total': tot, 'category': category, 'categories': categories, 'properties': properties})

    #      if currence0 and currence1:
    #           t = 992
    #           amountConverted = am * t
    #           amof1D = 1
    #           amof1R = 1*992
    #           amofR2 = 1
    #           amofD2 = 1/992
    #           {"USD":'USD'}
    #           {"RWF":'RWF'}
    #           # tot={'amountConverted': amountConverted ,'amof1D':amof1D,'amof1R': amof1R,
    #           # 'amofR2':amofR2,'amofD2':amofD2,'cur1':cur1,'cur2':cur2,'am':am}
    #           tot={'amount':am}
    #
    #           return render(request,'converter2.html',{'tot':tot})
    #      else:
    #          return redirect('conversion:conv2')
    #
    # else:
    #    return render(request,"converter.html")
