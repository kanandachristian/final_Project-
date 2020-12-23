from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Categorie'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rental:property_list_by_category', args=[self.slug])

class Landlord(models.Model):
    landlord_type = models.CharField(max_length=200, db_index=True)
    landlord_id = models.CharField(max_length=200, db_index=True, unique=True)
    landlord_name = models.CharField(max_length=200, db_index=True)
    landlord_phone = models.CharField(max_length=200, db_index=True)
    landlord_email = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('landlord_id',)
        verbose_name = 'Landlord'

    def __str__(self):
        return self.landlord_id


class Propertie(models.Model):
    category = models.ForeignKey(
        Category, related_name='property', on_delete=models.CASCADE)
    Advert_type = models.CharField(max_length=200, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    property_price = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.CharField(
        max_length=200, null=True, db_index=True, blank=True)
    payable = models.CharField(
        max_length=200, null=True, db_index=True, blank=True)
    description = models.TextField(blank=True)
    Bedroom = models.IntegerField(db_index=True, null=True, blank=True)
    Bathroom = models.IntegerField(db_index=True, null=True, blank=True)
    sector = models.CharField(
        max_length=200, db_index=True, null=True, blank=True)
    cell = models.CharField(
        max_length=200, db_index=True, null=True, blank=True)
    village = models.CharField(
        max_length=200, db_index=True, null=True, blank=True)
    number = models.CharField(
        max_length=200, db_index=True, null=True, blank=True)
    image = models.ImageField(
        upload_to='properties/%Y/%m/%d', blank=True)
    landlord_Id = models.ForeignKey(
        Landlord, related_name='landlord', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    vaccant = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Propertie'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rental:property_detail', args=[self.id, self.slug])


class Property_image(models.Model):
    pro_id = models.ForeignKey(
        Propertie, related_name='PropertyId', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='properties/', null=True, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Property_Taken(models.Model):
    customer_type = models.CharField(max_length=100, db_index=True)
    customer_id = models.CharField(max_length=100, db_index=True, unique=True)
    customer_name = models.CharField(max_length=100, db_index=True)
    customer_email = models.EmailField(max_length=100, db_index=True)
    customer_phon = models.CharField(max_length=100, db_index=True)
    customer_dob = models.DateField(
        max_length=100, db_index=True, null=True, blank=True)
    customer_sex = models.CharField(
        max_length=100, db_index=True, null=True, blank=True)
    customer_notionality = models.CharField(
        max_length=100, db_index=True, null=True, blank=True)
    customer_ocupation = models.CharField(
        max_length=100, db_index=True, null=True, blank=True)
    property_taken_id = models.ForeignKey(
        Propertie, related_name='identity', on_delete=models.CASCADE)
    Date_taken = models.DateField(
        max_length=50, db_index=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('customer_id',)
        verbose_name = 'Property_Taken'

    def __str__(self):
        return self.customer_name


class BookedPropertie(models.Model):
    customer_type = models.CharField(max_length=100, db_index=True)
    customer_id = models.CharField(max_length=100, db_index=True, unique=True)
    customer_name = models.CharField(max_length=100, db_index=True)
    customer_email = models.EmailField(max_length=100, db_index=True)
    customer_phon = models.CharField(max_length=100, db_index=True)
    booking_period = models.CharField(max_length=100, db_index=True)
    property_booked = models.ForeignKey(
        Propertie, related_name='Advert', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    vaccant = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    Employee_id = models.CharField(max_length=200, db_index=True, unique=True)
    Employee_email = models.CharField(max_length=200, db_index=True)
    Employee_phon = models.CharField(max_length=200, db_index=True)
    Employee_name = models.CharField(max_length=200, db_index=True)
    Employee_dob = models.DateField(
        max_length=200, db_index=True, null=True, blank=True)
    Employee_sex = models.CharField(
        max_length=200, db_index=True, null=True, blank=True)
    Employee_function = models.CharField(
        max_length=200, db_index=True, blank=True)

    class Meta:
        ordering = ('Employee_id',)
        verbose_name = 'Employee'

    def __str__(self):
        return self.Employee_name


class Signup(models.Model):
    U_name = models.CharField(max_length=50, db_index=True)
    U_username = models.CharField(max_length=50, db_index=True)
    U_Userpassword = models.CharField(
        max_length=50, db_index=True,  unique=True)
    U_email = models.CharField(max_length=50, null=True, db_index=True)


class contactu(models.Model):
    message = models.CharField(max_length=500, null=True, db_index=True)
    email = models.CharField(max_length=50, db_index=True, unique=True)
