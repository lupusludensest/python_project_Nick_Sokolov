from django.db import models

# 1
class Contact(models.Model):
    class Meta:
        db_table = 'contacts'  # Starts from the lowercase letter and can be plural
        verbose_name = 'Contact'  # Starts from the capital letter and always singular
        verbose_name_plural = 'Contacts'  # Starts from the capital letter and always plural

    first_name = models.CharField(blank=False, null=False, max_length=60, editable=False, verbose_name='First name')
    last_name = models.CharField(blank=False, null=False, max_length=60, editable=False, verbose_name='Last name')
    middle_name = models.CharField(blank=False, null=False, max_length=60, editable=False, verbose_name='Middle name')
    prefix_name = models.CharField(blank=False, null=False, max_length=10, editable=False, verbose_name='Prefix name')
    company_name = models.CharField(blank=False, null=False, max_length=80, editable=False, verbose_name='Company name')
    contact_type = models.CharField(blank=False, null=False, max_length=80, editable=False, verbose_name='Contact type')
    address = models.CharField(blank=False, null=False, max_length=200, editable=False, verbose_name='Address')
    city = models.CharField(blank=False, null=False, max_length=40, editable=False, verbose_name='City')
    state = models.CharField(blank=False, null=False, max_length=40, editable=False, verbose_name='State')
    country = models.CharField(blank=False, null=False, max_length=40, editable=False, verbose_name='Country')
    postal_code = models.CharField(blank=False, null=False, max_length=5, editable=False, verbose_name='Postal code')
    phone = models.CharField(blank=False, null=False, max_length=12, editable=False, verbose_name='Phone')
    email = models.EmailField(blank=False, null=False, max_length=30, editable=False, verbose_name='Email')
    create_time = models.DateField(blank=False, null=False, editable=False, verbose_name='Creation time')

# 2
class Supplier(models.Model):
    class Meta:
        db_table = 'suppliers'
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    contact_id = models.ForeignKey(Contact, blank=False, null=False, verbose_name='Contact ID', on_delete=models.CASCADE)
    contract_no = models.CharField(blank=False, null=False, max_length=45, editable=False, verbose_name='Contract number')
    contract_title = models.CharField(blank=False, null=False, max_length=50, editable=False, verbose_name='Contract title')
    supplier_type = models.CharField(blank=False, null=False, max_length=40, editable=False, verbose_name='Supplier type')
    contr_eff_date = models.DateField(blank=False, null=False, editable=False, verbose_name='Contract effective date')
    contr_exp_date = models.DateField(blank=False, null=False, editable=False, verbose_name='Contract expiration date')

# 3
class Client(models.Model):
    class Meta:
        db_table = 'clients'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    contact_id = models.ForeignKey(Contact, blank=False, null=False, default="", editable=False, verbose_name='Contact ID', on_delete=models.CASCADE)
    date_entered = models.DateField(blank=False, null=False, default="", editable=False, verbose_name='Date entered')
    password = models.CharField(blank=False, null=False, max_length=25, default="", editable=False, verbose_name='Password')
    birthday = models.DateField(blank=False, null=False, default="", editable=False, verbose_name='Date of birth')
    client_type = models.CharField(blank=False, null=False, max_length=25, default="", editable=False, verbose_name='Client type')

# 4
class Shipper(models.Model):
    class Meta:
        db_table = 'shippers'
        verbose_name = 'Shipper'
        verbose_name_plural = 'Shippers'

    contact_id = models.ForeignKey(Contact, blank=False, null=False, verbose_name='Contact ID', on_delete=models.CASCADE)
    contract_no = models.CharField(blank=False, null=False, max_length=45, editable=False, verbose_name='Contract number')
    contract_title = models.CharField(blank=False, null=False, max_length=50, editable=False, verbose_name='Contract title')
    shipper_type = models.CharField(blank=False, null=False, max_length=40, editable=False, verbose_name='Shipper type')
    contr_eff_date = models.DateField(blank=False, null=False, editable=False, verbose_name='Contract effective date')
    contr_exp_date = models.DateField(blank=False, null=False, editable=False, verbose_name='Contract expiration date')
    logo = models.ImageField(blank=True, null=True, editable=False, verbose_name='Logo of the shipper')

# 5
class Product(models.Model):
    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    supplier_id = models.ForeignKey(Supplier, blank=False, null=False, default="", editable=False, verbose_name='Supplier ID', on_delete=models.CASCADE)
    product_name = models.CharField(blank=False, null=False, max_length=50, default="", editable=False, verbose_name='Product name')
    product_brand = models.CharField(blank=False, null=False, max_length=40, default="", editable=False, verbose_name='Product brand')
    year_of_manufacture = models.IntegerField(blank=False, null=False, default="", editable=True, verbose_name='Year of manufacture')
    color = models.CharField(blank=False, null=False, max_length=25, default="", editable=False, verbose_name='Color')
    description = models.TextField(blank=False, null=False, max_length=999, default="", editable=False, verbose_name='Description')
    quantity_per_unit = models.IntegerField(blank=False, null=False, default="", editable=True, verbose_name='Quantity per unit')
    unit_price = models.FloatField(blank=False, null=False, default="", editable=False, verbose_name='Unit price')
    product_image = models.ImageField(blank=True, null=True, default="", editable=True, verbose_name='Image of the product')
    size = models.CharField(blank=False, null=False, max_length=25, default="", editable=True, verbose_name='Size x*y*z')
    weight = models.FloatField(blank=False, null=False, max_length=7, default="", editable=True, verbose_name='Weight of the product in KGs')

# 6
class Category(models.Model):
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    category = models.CharField(blank=False, null=False, max_length=30, editable=False, verbose_name='Category')
    description = models.TextField(blank=False, null=False, max_length=999, editable=True, verbose_name='Description')

# 7
class ProductCategory(models.Model):
    class Meta:
        db_table = 'products_categories'
        verbose_name = 'Product category'
        verbose_name_plural = 'Product categories'

    product_id = models.ForeignKey(Product, blank=False, null=False,default="", editable=False, verbose_name='Product ID', on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, blank=False, null=False, default="", editable=False, verbose_name='Category ID', on_delete=models.CASCADE)

# 8
class Rating(models.Model):
    class Meta:
        db_table = 'ratings'
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

    client_id = models.ForeignKey(Client, blank=False, null=False, default="", editable=False, verbose_name='Client ID', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, blank=False, null=False, default="", editable=False, verbose_name='Product ID', on_delete=models.CASCADE)
    date_posted = models.DateField(blank=False, null=False, default="", editable=False, verbose_name='Date posted')
    rating = models.FloatField(blank=False, null=False, max_length=2,  default="", editable=True, verbose_name='Rating')
    comment = models.CharField(blank=False, null=False, max_length=999,  default="", editable=True, verbose_name='Comment')

# 9
class Order(models.Model):
    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
    client_id = models.ForeignKey(Client, blank=False, null=False, default="", editable=False, verbose_name='Client ID', on_delete=models.CASCADE)
    shipper_id = models.ForeignKey(Shipper, blank=False, null=False, default="", editable=False, verbose_name='Shipper ID', on_delete=models.CASCADE)
    order_date = models.DateField(blank=False, null=False, default="", editable=False, verbose_name='Data of order')
    pyment_method = models.CharField(blank=False, null=False, max_length=20, default="", editable=False, verbose_name='Payment method')
    delivery_method = models.CharField(blank=False, null=False, max_length=30, default="", editable=True, verbose_name='Delivery method')
    delivery_date = models.DateField(blank=False, null=False, default="", editable=False, verbose_name='Delivery date')
    total_price = models.FloatField(blank=False, null=False, default="", editable=False, verbose_name='Total price')
    sale_tax = models.FloatField(blank=False, null=False, default="", editable=False, verbose_name='Sale tax')
    discount = models.FloatField(blank=False, null=False, default="", editable=True, verbose_name='Discount')
    total_discount = models.FloatField(blank=False, null=False, default="", editable=True, verbose_name='Total discount')
    paid = models.FloatField(blank=False, null=False, default="", editable=False, verbose_name='Paid')
    transaction_status = models.CharField(blank=False, null=False, max_length=20, default="", editable=True, verbose_name='Transaction status')

# 10
class Cart(models.Model):
    class Meta:
        db_table = 'carts'
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
    order_id = models.ForeignKey(Order, blank=False, null=False, default="", editable=False, verbose_name='Order ID', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, blank=False, null=False,  default="", editable=False, verbose_name='Product ID', on_delete=models.CASCADE)
    date = models.DateField(blank=False, null=False, editable=False, verbose_name='Data')
    item_price = models.FloatField(blank=False, null=False, editable=False, verbose_name='Item price')
    product_quantity = models.IntegerField(blank=False, null=False, editable=False, verbose_name='Product quantity')
    sub_total = models.FloatField(blank=False, null=False, editable=False, verbose_name='Total spent')
    sale_tax = models.FloatField(blank=False, null=False,  default="", editable=True, verbose_name='Sale tax')
    discount = models.FloatField(blank=False, null=False, default="", editable=True, verbose_name='Discount')
    total_discount = models.FloatField(blank=False, null=False,  default="", editable=True, verbose_name='Total discount')

# # 1
# class Product(models.Model): # Starts from the capital letter and always singular
#     class Meta:
#         db_table = 'products' # Starts from the lowercase letter and can be plural
#         verbose_name = 'Product' # Starts from the capital letter and always singular
#         verbose_name_plural = 'Products' # Starts from the capital letter and always plural
#
#     product_name = models.CharField(blank=False, null=False, max_length=50, editable=False, verbose_name='Product name')
#     product_brand = models.CharField(blank=False, null=False, max_length=40, editable=False, verbose_name='Product brand')
#     year_of_manufacture = models.IntegerField(blank=False, null=False, editable=True, verbose_name='Year of manufacture')
#     color = models.CharField(blank=False, null=False, max_length=25, editable=False, verbose_name='Color')
#     description = models.TextField(blank=False, null=False, max_length=999, editable=False, verbose_name='Description')
#     price = models.FloatField(blank=False, null=False, editable=False, verbose_name='Price')
#
# # 2
# class Category(models.Model):
#     class Meta:
#         db_table = 'categories'
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'
#
#     category = models.CharField(blank=False, null=False, max_length=30, editable=False, verbose_name='Category')
#     description = models.TextField(blank=False, null=False, max_length=999, editable=False, verbose_name='Description')
#
# # 3
# class ProductCategory(models.Model):
#     class Meta:
#         db_table = 'products_categories'
#         verbose_name = 'Product category'
#         verbose_name_plural = 'Product categories'
#
#     product = models.ForeignKey(Product, blank=False, null=False, verbose_name='Product', on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, blank=False, null=False, verbose_name='Category', on_delete=models.CASCADE)
#
# # 4
# class Client(models.Model):
#     class Meta:
#         db_table = 'client'
#         verbose_name = 'Client'
#         verbose_name_plural = 'Clients'
#     first_name = models.CharField(blank=False, null=False, max_length=60, editable=False, verbose_name='First name')
#     last_name = models.CharField(blank=False, null=False, max_length=60, editable=False, verbose_name='Last name')
#     nick_name = models.CharField(blank=False, null=False, max_length=60, editable=False, verbose_name='Nick name')
#     email = models.EmailField(blank=False, null=False, max_length=60, editable=False, verbose_name='Email')
#     password = models.CharField(blank=False, null=False, max_length=25, editable=False, verbose_name='Password')
#     address = models.CharField(blank=False, null=False, max_length=40, editable=False, verbose_name='Address')
#     city = models.CharField(blank=False, null=False, max_length=80, editable=False, verbose_name='City')
#     state = models.CharField(blank=False, null=False, max_length=50, editable=False, verbose_name='State')
#     country = models.CharField(blank=False, null=False, max_length=40, editable=False, verbose_name='Country')
#     postal_code = models.CharField(blank=False, null=False, max_length=5, editable=False, verbose_name='Postal code')
#
# # 5
# class Order(models.Model):
#     class Meta:
#         db_table = 'orders'
#         verbose_name = 'Order'
#         verbose_name_plural = 'Orders'
#     client = models.ForeignKey(Client, blank=False, null=False, verbose_name='Client', on_delete=models.CASCADE)
#     date = models.DateField(blank=False, null=False, editable=False, verbose_name='Data')
#     pyment_method = models.CharField(blank=False, null=False, max_length=20, editable=False, verbose_name='Payment method')
#     delivery_method = models.CharField(blank=False, null=False, max_length=30, editable=False, verbose_name='Delivery method')
#     delivery_date = models.DateField(blank=False, null=False, editable=False, verbose_name='Delivery date')
#     total_price = models.FloatField(blank=False, null=False, editable=False, verbose_name='Total price')
#
# # 6
# class Cart(models.Model):
#     class Meta:
#         db_table = 'carts'
#         verbose_name = 'Cart'
#         verbose_name_plural = 'Carts'
#     order = models.ForeignKey(Order, blank=False, null=False, verbose_name='Order', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, blank=False, null=False, verbose_name='Product', on_delete=models.CASCADE)
#     date = models.DateField(blank=False, null=False, editable=False, verbose_name='Data')
#     item_price = models.FloatField(blank=False, null=False, editable=False, verbose_name='Item price')
#     product_quantity = models.IntegerField(blank=False, null=False, editable=False, verbose_name='Product quantity')
#     sub_total = models.FloatField(blank=False, null=False, editable=False, verbose_name='Total spent')



