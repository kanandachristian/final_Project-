from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from .models import (contactu,  Category, Landlord, Propertie,
                     Property_image, Property_Taken, BookedPropertie, Employee, Signup)

# Admin site
admin.site.site_header = 'Houserental Admin'
admin.site.site_title = 'Houserental Admin'
admin.site.index_title = ''

# Database tables.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class PropertieAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'Advert_type', 'available', 'vaccant', 'landlord_Id', 'image', 'property_price', 'Bedroom', 'Bathroom'
                    ]

    list_filter = ['category', 'Advert_type', 'landlord_Id', 'available', 'vaccant',
                   'Bedroom', 'property_price', 'sector', 'cell', 'created', 'updated']

    list_editable = ['property_price', 'available',
                     'vaccant']

    prepopulated_fields = {'slug': ('name',)}

    search_fields = ['name', 'Advert_type']

    date_hierarchy = 'created'

    # change_list_template = 'admin/base_site.html'


PropertieAdmin.change_list_template


admin.site.register(Propertie, PropertieAdmin)


class LandlordAdmin(admin.ModelAdmin):
    list_display = ['landlord_type', 'landlord_id',
                    'landlord_name', 'landlord_phone', 'landlord_email']
    list_filter = ['landlord_type', 'landlord_id']

    search_fields = ['landlord_name']


admin.site.register(Landlord, LandlordAdmin)


class Property_imageAdmin(admin.ModelAdmin):
    list_display = ['pro_id', 'images', 'available']
    list_filter = ['pro_id', 'available', 'created', 'updated']


admin.site.register(Property_image, Property_imageAdmin)


class Property_TakenAdmin(admin.ModelAdmin):
    list_display = ['customer_type', 'customer_id', 'customer_name', 'customer_email',
                    'customer_phon', 'customer_dob', 'customer_sex', 'customer_notionality', 'customer_ocupation']
    list_filter = ['customer_type', 'customer_id']

    search_fields = ['customer_name']


admin.site.register(Property_Taken, Property_TakenAdmin)


class BookedPropertieAdmin(admin.ModelAdmin):
    list_display = ['customer_type', 'customer_id', 'customer_name', 'customer_email', 'customer_phon', 'booking_period',
                    'property_booked', 'available', 'created', 'updated']
    list_filter = ['customer_id', 'property_booked', 'booking_period', 'available', 'vaccant', 'created',
                   'updated']
    search_fields = ['customer_name']


admin.site.register(BookedPropertie, BookedPropertieAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['Employee_id', 'Employee_name', 'Employee_email',
                    'Employee_phon', 'Employee_dob', 'Employee_sex', 'Employee_function']

    search_fields = ['Employee_name']


admin.site.register(Employee, EmployeeAdmin)


class SignupAdmin(admin.ModelAdmin):
    list_display = ['U_username', 'U_email', 'U_Userpassword']
    search_fields = ['U_username']


admin.site.register(Signup, SignupAdmin)


class contactuAdmin(admin.ModelAdmin):
    list_display = ['message', 'email']
    list_editable = ['email']

    search_fields = ['email']


admin.site.register(contactu, contactuAdmin)
admin.site.unregister(Group)
