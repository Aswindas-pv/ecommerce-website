from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from user_app.models import Customer
from admin_app.models import *

from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages

from django.contrib.auth.decorators import login_required 
from django.views.decorators.cache import never_cache




@never_cache
def admin_login_page(request):
    if request.user.is_authenticated and request.user.is_superuser:
            user_list = User.objects.all().order_by('username').values()
            return render(request, 'admin_index.html', {'user_list': user_list})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            auth.login(request, user)
            user_list = User.objects.all().order_by('username').values()
            return render(request, 'admin_index.html', {'user_list': user_list})
        else:
            messages.error(request, 'Invalid credentials, please try logging in again.')
            return redirect('admin_login_page')
 
    return render(request, 'admin_login.html')






@login_required
@never_cache     
def admin_logout(request):
    if request.method == 'POST' :
        auth.logout(request)
        messages.info(request, 'Login again!')
        return redirect('admin_login_page')
    else:
        return redirect('admin_login_page')

 



# PAGE NOT FOUND   
@login_required
@never_cache
def page_not_found(request):
    if request.user.is_superuser:
        return redirect('admin_login_page')
    else:
        return render(request, 'pages/samples/error-404.html')







# CUSTOMER
@login_required
@never_cache
def admin_customers(request):
    if request.user.is_superuser:
        user_list = User.objects.all().order_by('username').values()
        customer_list = Customer.objects.all().order_by('user__first_name').values()
        return render(request, 'pages/customers/customers.html',{'user_list' : user_list, 'customer_list' : customer_list})
    else:
        return redirect('admin_login_page')
        
        
        
@login_required
@never_cache       
def block_user(request, user_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            user_to_block = User.objects.get(id=user_id)
            user_to_block.is_active = False
            user_to_block.save()
            return redirect(admin_customers)
        else:
            return redirect(admin_customers)
    else:
        return redirect('admin_login_page')
    


@login_required
@never_cache
def unblock_user(request, user_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            user_to_unblock = User.objects.get(id=user_id)
            user_to_unblock.is_active = True
            user_to_unblock.save()
            return redirect(admin_customers)
        else:
            return redirect(admin_customers)
    else:
        return redirect('admin_login_page')
        
        
        
        
@login_required
@never_cache
def search_user(request):
    if request.user.is_superuser:
        query = request.GET.get('query', '')
        
        if query:
             user_list = User.objects.filter(username__icontains = query)
        else:
            user_list = User.objects.all().order_by('username').values()
        
        return render(request,'pages/customers/customers.html' ,{'user_list' : user_list})
    
    
    
    
    
    
    
# CATEGORIES PAGES
@login_required
@never_cache
def admin_categories(request):
    if request.user.is_superuser:
        category_list = Category.objects.filter(is_deleted = False).order_by('name').values()
        return render(request, 'pages/category/category.html', {'category_list' : category_list})
    else:
        return redirect('admin_login_page')
    
    
    
@login_required
@never_cache
def add_category_page(request):
    if request.user.is_superuser:
        return render(request, 'pages/category/add_category_page.html')
    else:
        return redirect('admin_login_page')
    
    
    
    
 
@login_required
@never_cache
def add_categories(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST['category_name']
            description = request.POST['category_description']
            
            if not Category.objects.filter(name__icontains = name, is_deleted = False).exists():
                category = Category.objects.create(name = name, description = description)
                category.save()
                messages.success(request, 'New category was added!')
                return redirect(admin_categories)
            else:
                messages.error(request, 'Category already exists, create new category')
                return redirect(add_category_page)
    else:
        return redirect('admin_login_page')
    
    
    
    
@login_required
@never_cache    
def delete_category(request, cat_id):
    if request.user.is_superuser:
        if cat_id:
            category_to_delete = Category.objects.get(id = cat_id)
            category_to_delete.is_deleted = True
            category_to_delete.save()
            messages.success(request, 'Category has been deleted!')
            return redirect(admin_categories)
        else:
            messages.error(request, 'id cannot be found!')
            return redirect(admin_categories)
    else:
        return redirect('admin_login_page')
    
    
    
    
@login_required
@never_cache   
def list_category(request, cat_id):
    if request.user.is_superuser:
        if cat_id:
            category_to_list = Category.objects.get(id = cat_id)
            category_to_list.is_listed = True
            category_to_list.save()
            messages.success(request, 'Category updated successfully!')
            return redirect(admin_categories)
        else:
            messages.error(request, 'id cannot be found!')
            return redirect(admin_categories)
    else:
        return redirect('admin_login_page')





@login_required
@never_cache
def un_list_category(request, cat_id):
    if request.user.is_superuser:
        if cat_id:
            category_to_list = Category.objects.get(id = cat_id)
            category_to_list.is_listed = False
            category_to_list.save()
            messages.success(request, 'Category updated successfully!')
            return redirect(admin_categories)
        else:
            messages.error(request, 'id cannot be found!')
            return redirect(admin_categories)
    else:
        return redirect('admin_login_page')
    
    

@login_required
@never_cache
def deleted_cat_view(request):
    if request.user.is_superuser:
        category_list = Category.objects.filter(is_deleted = True).order_by('name').values()
        return render(request, 'pages/category/deleted_categories.html', {'category_list' : category_list})
    else:
        return redirect('admin_login_page')
    
    


@login_required
@never_cache
def restore_categories(request, cat_id):
    if request.user.is_superuser:
        if cat_id:
            category_to_restore = Category.objects.get(id = cat_id)
            category_to_restore.is_deleted = False
            category_to_restore.save()
            messages.success(request, 'Category have been restored successfully!')
            return redirect(deleted_cat_view)
        else:
            messages.error(request, ' id cannot be found!')
            return redirect(deleted_cat_view)
    else:
        return redirect('admin_login_page')
    
    
    


# PRODUCT
@login_required
@never_cache
def list_product_page(request):
    if request.user.is_superuser:
        product_list = Product.objects.filter(is_deleted = False).order_by('name').values()
        return render(request, 'pages/products/product.html', {'product_list' : product_list})
    else:
        return redirect('admin_login_page')



@login_required
@never_cache
def admin_add_product(request):
    if request.user.is_superuser:
        return render(request, 'pages/products/add_products.html')
    else:
        return redirect('admin_login_page')




@login_required
@never_cache
def add_products(request):
    if request.user.is_superuser:
        if request.method == 'POST' :
            name = request.POST['product_name']
            quantity = request.POST['quantity']
            description = request.POST['description']
            price = request.POST['price']
            category_id = request.POST['category']
            brand_id = request.POST['brand']
            main_image = request.POST['main_image']
            side_view_image = request.POST['side_view_image']
            back_view_image = request.POST['back_view-image']
            
            if Product.objects.filter(name__icontains = name).exists():
                messages.error(request, 'Product already exits!')
            else:
                Product.objects.create(
                    name = name, 
                    description = description, 
                    quantity = quantity, 
                    price = price, 
                    category_id = category_id, 
                    brand_id = brand_id,
                    main_image = main_image,
                    side_view_image = side_view_image,
                    back_view_image = back_view_image,
                    )
                messages.success(request, 'New Product was created!')
                return redirect(list_product_page)
        
    else:
        return redirect('admin_login_page')
    
    
    
    



# BRAND
@login_required
@never_cache
def list_brand_page(request):
    if request.user.is_superuser:
        brand_list = Brand.objects.filter(is_deleted = False).order_by('name').values()
        return render(request, 'pages/products/brand.html', {'brand_list' : brand_list})
    else:
        return redirect('admin_login_page')


@login_required
@never_cache
def admin_add_brand(request):
    if request.user.is_superuser:
        return render(request, 'pages/products/add_brand.html')
    else:
        return redirect('admin_login_page')


@login_required
@never_cache
def add_brand(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST['name']
            country_of_origin = request.POST['country_of_origin']
            manufacturer_details = request.POST['manufacturer_details']
            
            
            
            if not Brand.objects.filter(name__icontains = name).exists():
                brand = Brand.objects.create(
                name = name,
                country_of_origin = country_of_origin,
                manufacturer_details = manufacturer_details,
                )
                brand.save()
                messages.success(request, 'New brand added!')
                return redirect(list_brand_page)
            else:
                messages.error(request, 'Brand already exits, add new brand')
                return redirect(admin_add_brand)
    else:
        return redirect('admin_login_page')
    
    
 
@login_required
@never_cache
def edit_brand(request, brand_id):
    if request.user.is_superuser:
        brand_list = Brand.objects.filter(id = brand_id).values()
        return render(request, 'pages/products/edit_brand.html', {'brand_list' : brand_list})
    else:
        return redirect('admin_login_page')
    

@login_required
@never_cache
def delete_brand(request, brand_id):
    if request.user.is_superuser:
        if brand_id:
            brand_to_delete = Brand.objects.get(id = brand_id)
            brand_to_delete.is_deleted = True
            brand_to_delete.save()
            messages.success(request, 'Brand has been deleted!')
            return redirect(list_brand_page)
        else:
            messages.error(request, 'id cannot be found!')
            return redirect(list_brand_page)
    else:
        return redirect('admin_login_page')
    



@login_required
@never_cache
def restore_brand(request, brand_id):
    if request.user.is_superuser:
        if brand_id:
            brand_to_restore = Brand.objects.get(id = brand_id)
            brand_to_restore.is_deleted = False
            brand_to_restore.save()
            messages.success(request, 'Brand has been restored!')
            return redirect(list_brand_page)
        else:
            messages.error(request, 'id cannot be found!')
            return redirect(list_brand_page)
    else:
        return redirect('admin_login_page')
    
    


@login_required
@never_cache
def deleted_brand_view(request):
    if request.user.is_superuser:
        brand_list = Brand.objects.filter(is_deleted = True).order_by('name').values()
        return render(request, 'pages/products/deleted_brand.html', {'brand_list' : brand_list})
    else:
        return redirect('admin_login_page')
    
    

    

@login_required
@never_cache
def list_the_brand(request, brand_id):
    if request.user.is_superuser:
        if brand_id:
            brand_to_list = Brand.objects.get(id = brand_id)
            brand_to_list.is_listed = True
            brand_to_list.save()
            messages.success(request, 'Brand updated successfully!')
            return redirect(list_brand_page)
        else:
            messages.error(request, 'id cannot be found!')
            return redirect(list_brand_page)
    else:
        return redirect('admin_login_page')
    
    
    
    
    
@login_required
@never_cache
def un_list_the_brand(request, brand_id):
    if request.user.is_superuser:
        if brand_id:
            brand_to_un_list = Brand.objects.get(id = brand_id)
            brand_to_un_list.is_listed = False
            brand_to_un_list.save()
            messages.success(request, 'Brand updated successfully!')
            return redirect(list_brand_page)
        else:
            messages.error(request, 'id cannot be found!')
            return redirect(list_brand_page)
    else:
        return redirect('admin_login_page')