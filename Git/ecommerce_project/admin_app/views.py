from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from user_app.models import Customer
from admin_app.models import *

from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages

from django.contrib.auth.decorators import login_required 
from django.views.decorators.cache import never_cache

from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.http import HttpResponse




is_active_dashboard = True
is_active_customer = True
is_active_product = True
is_active_brand = True
is_active_category = True
is_active_order = True
is_active_return = True
is_active_coupon = True
is_active_banner = True



# ---------------------------------------------------------------- ADMIN LOGIN FUNCTIONS STARTING FROM HERE ----------------------------------------------------------------



# ADMIN LOGIN PAGE
def admin_login_page(request):
    if request.user.is_authenticated and request.user.is_superuser:
            user_list = User.objects.all().order_by('username').values()
            return render(request, 'admin_index.html', {'user_list': user_list, 'is_active_dashboard' : is_active_dashboard})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            auth.login(request, user)
            user_list = User.objects.all().order_by('username').values()
            return render(request, 'admin_index.html', {'user_list': user_list, 'is_active_dashboard' : is_active_dashboard})
        else:
            messages.error(request, 'Invalid credentials, please try logging in again.')
            return redirect('admin_login_page')
 
    return render(request, 'admin_login.html')





# ADMIN LOGOUT FUNCTION
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




# ---------------------------------------------------------------- ADMIN CUSTOMER PAGE FUNCTIONS STARTING FROM HERE ----------------------------------------------------------------




# CUSTOMER SHOW FUNCTION
@login_required
@never_cache
def admin_customers(request):
    if request.user.is_superuser:
        user_list = User.objects.all().order_by('username').values()
        customer_list = Customer.objects.all().order_by('user__first_name').values()
        return render(request, 'pages/customers/customers.html',{'user_list' : user_list, 'customer_list' : customer_list, 'is_active_customer' : is_active_customer})
    else:
        return redirect('admin_login_page')
        
        
        
 
 
# BLOCK CUSTOMER FUNCTION    
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
    





# UNBLOCK CUSTOMER FUNCTION
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
        
        
        


# SEARCH CUSTOMER FUNCTION    
@login_required
@never_cache
def search_user(request):
    if request.user.is_superuser:
        query = request.GET.get('query', '')
        
        if query:
             user_list = User.objects.filter(username__icontains = query)
        else:
            user_list = User.objects.all().order_by('username').values()
        
        return render(request,'pages/customers/customers.html' ,{'user_list' : user_list, 'is_active_customer' : is_active_customer})
    
    
    


# ---------------------------------------------------------------- ADMIN CATEGORIES PAGE FUNCTIONS STARTING FROM HERE ----------------------------------------------------------------
    
    
    
    
# CATEGORIES PAGES FUNCTION
@login_required
@never_cache
def admin_categories(request):
    if request.user.is_superuser:
        category_list = Category.objects.filter(is_deleted = False).order_by('name').values()
        return render(request, 'pages/category/category.html', {'category_list' : category_list, 'is_active_category' : is_active_category})
    else:
        return redirect('admin_login_page')
    
    
    
    
    
# ADD CATEGORY PAGE FUNCTION   
@login_required
@never_cache
def admin_add_category_page(request):
    if request.user.is_superuser:
        return render(request, 'pages/category/add_category_page.html', { 'is_active_category' : is_active_category })
    else:
        return redirect('admin_login_page')
    
    
    
    

# ADD CATEGORY FUNCTION 
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
                return redirect(admin_add_category_page)
    else:
        return redirect('admin_login_page')
    


# EDIT BRAND PAGE FUNCTION 
@login_required
@never_cache
def edit_category_page(request, cat_id):
    if request.user.is_superuser:
        category = Category.objects.get(pk = cat_id)
        return render(request, 'pages/category/edit_category.html', {'category' : category,'countries' : countries, 'is_active_category' : is_active_category })
    else:
        return redirect('admin_login_page') 


# EDIT CATEGORIES FUNCTION   
@login_required
@never_cache
def edit_category(request, cat_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST['category_name']
            description = request.POST['category_description']
            
            category = Category.objects.get(id = cat_id)
            
            if not Category.objects.filter(name__icontains = name).exists():
                category.name = name
                category.description = description
                category.save()
                messages.success(request, 'Category updated successfully!')
                return redirect(admin_categories)
            else:
                messages.error(request, 'Category already exits, add new category')
                return redirect(edit_category_page)
    else:
        return redirect('admin_login_page') 



# DELETE CATEGORY FUNCTION 
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
    
    


   
# LIST CATEGORY FUNCTION 
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




# UNLIST CATEGORY FUNCTION
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
    
    
    
    
    
# DELETED CATEGORIES VIEW PAGE FUNCTION
@login_required
@never_cache
def deleted_cat_view(request):
    if request.user.is_superuser:
        category_list = Category.objects.filter(is_deleted = True).order_by('name').values()
        return render(request, 'pages/category/deleted_categories.html', {'category_list' : category_list, 'is_active_category' : is_active_category })
    else:
        return redirect('admin_login_page')
    
    


# RESTORE CATEGORIES FUNCTION
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
    
    

# ---------------------------------------------------------------- ADMIN PRODUCT PAGE FUNCTIONS STARTING FROM HERE ----------------------------------------------------------------
   


# PRODUCTS VIEW PAGE FUNCTION
@login_required
@never_cache
def list_product_page(request):
    if request.user.is_superuser:
        product_color = ProductColorImage.objects.filter(is_deleted=False).prefetch_related('productsize_set').annotate(total_quantity=Sum('productsize__quantity'))
        return render(request, 'pages/products/product.html', {'product_color': product_color, 'is_active_product' : is_active_product})
    else:
        return redirect('admin_login_page')


@login_required
@never_cache
def get_quantity(request, size):
    try:
        quantity = ProductSize.objects.get(size=size).quantity
        return JsonResponse({'quantity': quantity})
    except ProductSize.DoesNotExist:
        return JsonResponse({'quantity': 'Size not found'})


# ADD PRODUCT PAGE FUNCTION
@login_required
@never_cache
def admin_add_product(request):
    if request.user.is_superuser:
        brand_list = Brand.objects.all().order_by('name').values()
        category_list = Category.objects.all().order_by('name').values()
        return render(request, 'pages/products/add_products.html', {'brand_list' : brand_list, 'category_list' : category_list, 'is_active_product' : is_active_product})
    else:
        return redirect('admin_login_page')



# ADD PRODUCT FUNCTION
@login_required
@never_cache
def add_products(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST.get('product_name')
            description = request.POST.get('description')
            information = request.POST.get('information')
            type = request.POST.get('type')
            category_id = request.POST.get('category')
            brand_id = request.POST.get('brand')

            category = Category.objects.get(pk = category_id)
            brand = Brand.objects.get(pk = brand_id)
            
            if Products.objects.filter(name__icontains=name).exists():
                messages.error(request, 'Product already exists!')
                return redirect(admin_add_product)
            else:
                product = Products.objects.create(
                    name=name,
                    description=description,
                    information= information,
                    type=type,
                    category=category,
                    brand=brand,
                )
                product.save()
                messages.success(request, 'New Product was created, Add product image')
                return redirect(admin_add_image_page)

    else:
        return redirect('admin_login_page')
    
    
    

# EDIT PRODUCT VIEW PAGE FUNCTION
@login_required
@never_cache
def edit_product_page(request, p_id):
    if request.user.is_superuser:
        try:
            product_color_image = ProductColorImage.objects.get(id=p_id)
            product = product_color_image.products
            product_sizes = ProductSize.objects.filter(product_color_image=product_color_image)
        except (ProductColorImage.DoesNotExist):
            return HttpResponse("One or more objects do not exist.", status=404)
        
        category_list = Category.objects.all()
        brand_list = Brand.objects.all()
        
        context = {
            'category_list': category_list,
            'brand_list': brand_list,
            'product': product,
            'product_color_image': product_color_image,
            'product_sizes': product_sizes,
            'is_active_product' : is_active_product,
        }
        return render(request, 'pages/products/edit_product.html', context)
    else:
        return redirect('admin_login_page')








# EDIT PRODUCT VIEW FUNCTION
@login_required
@never_cache
def edit_product_update(request, p_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST.get('product_name')
            description = request.POST.get('description')
            information = request.POST.get('information')
            category_id = request.POST.get('category')
            brand_id = request.POST.get('brand')
            
            
            product = Products.objects.get(pk=p_id)
            category = Category.objects.get(pk=category_id)
            brand = Brand.objects.get(pk=brand_id)
            
            product.name = name
            product.description = description
            product.information = information
            product.category = category
            product.brand = brand
            
            product.save()
            
            messages.success(request, 'Product Updated successfully!')
            return redirect(list_product_page)
    else:
        return redirect(admin_login_page)

            


# DELETED PRODUCTS VIEW PAGE FUNCTION   
@login_required
@never_cache
def deleted_product_page(request):
    if request.user.is_superuser:
        deleted_product_colors = ProductColorImage.objects.filter(is_deleted=True).select_related('products__category', 'products__brand').annotate(total_quantity=Sum('productsize__quantity'))
        return render(request, 'pages/products/deleted_products.html', {'product_colors': deleted_product_colors, 'is_active_product' : is_active_product})
    else:
        return redirect('admin_login_page')

    

    
# RESTORE PRODUCT FUNCTION
@login_required
@never_cache
def restore_product(request, pdt_id):
    if request.user.is_superuser:
        if pdt_id:
            product_to_delete = ProductColorImage.objects.get(pk=pdt_id)
            product_to_delete.is_deleted = False
            product_to_delete.save()
            messages.success(request, 'Product have been restored!')
            return redirect(list_product_page)
        else:
            messages.error()
    else:
        return redirect('admin_login_page')
        






# ---------------------------------------------------------------- ADMIN EDIT PRODUCT COLOR & IMAGE PAGE FUNCTIONS STARTING FROM HERE ----------------------------------------------------------------


# EDIT PRODUCT COLOR PAGE VIEW FUNCTION
@login_required
@never_cache
def edit_product_color_page(request, p_id):
    if request.user.is_superuser:
        try:
            product_color_image = ProductColorImage.objects.get(id=p_id)
            product = product_color_image.products
            product_sizes = ProductSize.objects.filter(product_color_image=product_color_image)
        except (ProductColorImage.DoesNotExist):
            return HttpResponse("One or more objects do not exist.", status=404)
        
        category_list = Category.objects.all()
        brand_list = Brand.objects.all()
        
        context = {
            'category_list': category_list,
            'brand_list': brand_list,
            'product': product,
            'product_color_image': product_color_image,
            'product_sizes': product_sizes,
            'is_active_product' : is_active_product
        }
        return render(request, 'pages/products/edit_product_color.html', context)
    else:
        return redirect('admin_login_page')



# EDIT PRODUCT COLOR FUNCTION
@login_required
@never_cache
def edit_product_color(request, p_id):
    if request.user.is_superuser:
        product_color_image = ProductColorImage.objects.get(pk=p_id)
        if request.method == 'POST':
            color = request.POST.get('color')
            price = request.POST.get('price')
            main_image = request.FILES.get('main_image')
            side_image = request.FILES.get('side_image')
            top_image = request.FILES.get('top_image')
            back_image = request.FILES.get('back_image')
            
            product_color_image.color = color
            product_color_image.price = price
            
            if main_image:
                product_color_image.main_image = main_image
            if side_image:
                product_color_image.side_image = side_image
            if top_image:
                product_color_image.top_image = top_image
            if back_image:
                product_color_image.back_image = back_image
                
            product_color_image.save()
            
            messages.success(request, 'Product color & images have been updated successfully')
            return redirect(list_product_page)
        else:
            return render(request, 'edit_product_color.html', {'product_color_image': product_color_image , 'is_active_product' : is_active_product})
    else:
        return redirect(admin_login_page)



# For list_product function
@login_required
@never_cache
def list_product(request, pdt_id):
    if request.user.is_superuser:
        if pdt_id:
            product_to_list = ProductColorImage.objects.get(pk=pdt_id)
            if product_to_list.products.brand.is_listed and product_to_list.products.category.is_listed:
                product_to_list.is_listed = True
                product_to_list.save()
                messages.success(request, 'Product updated successfully!')
            else:
                if product_to_list.products.brand.is_listed == False and product_to_list.products.category.is_listed == False:
                    messages.error(request, 'Cannot list product: Brand and Category is not listed.')
                elif product_to_list.products.brand.is_listed == False:
                    messages.error(request, 'Cannot list product: Brand is not listed.')
                else:
                    messages.error(request, 'Cannot list product: Category is not listed.')
            return redirect(list_product_page)
        else:
            messages.error(request, 'ID cannot be found.')
            return redirect(list_product_page)
    else:
        return redirect(admin_login_page)


# For un_list_product function
@login_required
@never_cache
def un_list_product(request, pdt_id):
    if request.user.is_superuser:
        if pdt_id:
            product_to_un_list = ProductColorImage.objects.get(pk=pdt_id)
            product_to_un_list.is_listed = False
            product_to_un_list.save()
            messages.success(request, 'Product updated successfully!')
            return redirect(list_product_page)
        else:
            messages.error(request, 'id cannot be found.')
            return redirect(list_product_page)
    else:
        return redirect(admin_login_page)
    
    

# DELETE PRODUCT FUNCTION
@login_required
@never_cache
def delete_product(request, pdt_id):
    if request.user.is_superuser:
        if pdt_id:
            product_to_delete = ProductColorImage.objects.get(pk=pdt_id)
            product_to_delete.is_deleted = True
            product_to_delete.save()
            messages.success(request, 'Product have been deleted!')
            return redirect(list_product_page)
        else:
            messages.error()
    else:
        return redirect('admin_login_page')



# ---------------------------------------------------------------- ADMIN EDIT PRODUCT SIZE PAGE FUNCTIONS STARTING FROM HERE ----------------------------------------------------------------


# EDIT PRODUCT SIZE PAGE VIEW FUNCTION
@login_required
@never_cache
def edit_product_size_page(request, p_id):
    if request.user.is_superuser:
        try:
            product_color_image = ProductColorImage.objects.get(id=p_id)
            product = product_color_image.products
            product_sizes = ProductSize.objects.filter(product_color_image=product_color_image)
        except (ProductColorImage.DoesNotExist):
            return HttpResponse("One or more objects do not exist.", status=404)
        
        category_list = Category.objects.all()
        brand_list = Brand.objects.all()
        context = {
            'category_list': category_list,
            'brand_list': brand_list,
            'product': product,
            'product_color_image': product_color_image,
            'product_sizes': product_sizes
        }
        
        return render(request, 'pages/products/edit_variant_page.html', context)
    else:
        return redirect('admin_login_page')
        


# EDIT PRODUCT SIZE FUNCTION
@login_required
@never_cache
def edit_product_size(request, p_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            size = request.POST.get('product_size')
            quantity = request.POST.get('product_quantity')
            
            print("Size:", size)
            print("Quantity:", quantity)
            
            product_size = ProductSize.objects.get(pk=p_id)
            
            if size and quantity:  # Check if size and quantity are not empty
                product_size.size = size
                product_size.quantity = quantity
                product_size.save()
                
                messages.success(request, 'Product sizes & quantity updated')
                return redirect(list_product_page)
            else:
                messages.error(request, 'Size or quantity is empty')
                return redirect('edit_product_size', p_id=p_id)
    else:
        return redirect(admin_login_page)



# ---------------------------------------------------------------- ADMIN ADD PRODUCT IMAGE PAGE FUNCTIONS STARTING FROM HERE ----------------------------------------------------------------


# ADD PRODUCT IMAGE PAGE VIEW FUNCTION
@login_required
@never_cache
def admin_add_image_page(request):
    if request.user.is_superuser:
        product_list = Products.objects.all()
        return render(request, 'pages/products/add_product_image.html', {'product_list' : product_list, 'is_active_product' : is_active_product})
    else:
        return redirect(admin_login_page)



# ADD PRODUCT IMAGE FUNCTION
@login_required
@never_cache
def add_product_image(request):
    if request.user.is_superuser:
        if request.method == 'POST':
                products_id = request.POST.get('product')
                color = request.POST.get('color')
                price = request.POST.get('price')
                main_image = request.FILES.get('main_image')
                side_image = request.FILES.get('side_image')
                top_image = request.FILES.get('top_image')
                back_image = request.FILES.get('back_image')
                
                products = Products.objects.get(pk = products_id)
                existing_color = ProductColorImage.objects.filter(products=products, color=color).exists()
                if existing_color:
                    messages.error(request, f"A product image with the color '{color}' already exists for this product.")
                    return redirect('admin_add_image_page')
                else:
                    product_color_image = ProductColorImage.objects.create(
                        color = color,
                        price = price,
                        main_image = main_image,
                        side_image = side_image,
                        top_image = top_image,
                        back_image = back_image,
                        products = products
                        )
                    product_color_image.save()
                    messages.success(request, "Product Color and Image was added, now add product size")
                    return redirect(admin_add_variants)
        else:
            return redirect(admin_add_image_page)
    else:
        return redirect('admin_login_page')               
                

# ---------------------------------------------------------------- ADMIN PRODUCT VARIANTS PAGE FUNCTIONS STARTING FROM HERE ----------------------------------------------------------------



adult_sizes = [6, 7, 8, 9, 10, 11, 12]
kids_sizes = ['8C', '9C', '10C', '11C', '12C', '13C']

# PRODUCT SIZE ADD PAGE VIEW PAGE FUNCTION
@login_required
@never_cache
def admin_add_variants(request):
    if request.user.is_superuser:
        sizes = adult_sizes
        products = Products.objects.all().order_by('name')
        product_color = ProductColorImage.objects.all().order_by('color')
        return render(request, 'pages/products/add_product_variant.html', {'products': products, 'product_color' : product_color, 'sizes': sizes, 'is_active_product' : is_active_product})
    else:
        return redirect(admin_login_page)


# GET COLOR FUNCTION
@login_required
@never_cache
def get_colors(request):
    if request.user.is_superuser:
        if request.method == 'GET' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
            product_id = request.GET.get('product_id')
            if product_id:
                colors = ProductColorImage.objects.filter(products_id=product_id).order_by('color').values('id', 'color')
                return JsonResponse({'colors': list(colors)})
        return JsonResponse({}, status=400)




# GET SIZES FUNCTION
@login_required
@never_cache
@require_GET
def get_sizes_view(request):
    if request.user.is_superuser:
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            product_id = request.GET.get('product_id')
            if product_id:
                try:
                    product = Products.objects.get(pk=product_id)
                    if product.category.name.lower() == "kid's":
                        sizes = ['8C', '9C', '10C', '11C', '12C', '13C']
                    else:
                        sizes = ['6', '7', '8', '9', '10', '11', '12']
                    return JsonResponse({'sizes': sizes})
                except Products.DoesNotExist:
                    pass
            return JsonResponse({'error': 'Invalid request'}, status=400)



# ADD PRODUCT SIZE FUNCTION
@login_required
@never_cache
def add_size(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            product_id = request.POST.get('product')
            color_id = request.POST.get('color')
            size = request.POST.get('size')
            quantity = request.POST.get('quantity')
            
            product_color_image = ProductColorImage.objects.get(pk=color_id)
            
            existing_size = ProductSize.objects.filter(product_color_image=product_color_image, size=size).exists()
            
            if existing_size:
                messages.error(request, 'This size is already added')
                return redirect('admin_add_variants')
            else:
                product_size = ProductSize.objects.create(
                product_color_image=product_color_image,
                size=size,
                quantity=quantity
                )                
                product_size.save()
                messages.success(request, 'Added size to the product')
                return redirect(list_product_page)
        else:
            return redirect('admin_add_variants')
    else:
        return redirect('admin_login_page')

            
            
# ---------------------------------------------------------------- ADMIN BRAND PAGE FUNCTIONS STARTING FROM HERE ----------------------------------------------------------------

# BRAND PAGE FUNCTION
@login_required
@never_cache
def list_brand_page(request):
    if request.user.is_superuser:
        brand_list = Brand.objects.filter(is_deleted = False).order_by('name').values()
        return render(request, 'pages/brands/brand.html', {'brand_list' : brand_list, 'is_active_brand' : is_active_brand})
    else:
        return redirect('admin_login_page')


countries = [
    "Select a country", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", 
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", 
    "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", 
    "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", 
    "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", 
    "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", 
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czechia (Czech Republic)", 
    "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", 
    "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini (fmr. 'Swaziland')", 
    "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", 
    "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", 
    "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", 
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", 
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", 
    "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", 
    "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", 
    "Mozambique", "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", 
    "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia (formerly Macedonia)", "Norway", 
    "Oman", "Pakistan", "Palau", "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru", 
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", 
    "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", 
    "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", 
    "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", 
    "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", 
    "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", 
    "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", 
    "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
    ]

        
        
# ADD BRAND PAGE FUNCTION
@login_required
@never_cache
def admin_add_brand(request):
    if request.user.is_superuser:
        return render(request, 'pages/brands/add_brand.html', {'countries' : countries, 'is_active_brand' : is_active_brand})
    else:
        return redirect('admin_login_page')



# ADD BRAND FUNCTION
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
    




# EDIT BRAND PAGE FUNCTION 
@login_required
@never_cache
def edit_brand_page(request, brand_id):
    if request.user.is_superuser:
        brand = get_object_or_404(Brand, id=brand_id)
        selected_country = brand.country_of_origin if brand.country_of_origin in countries else None
        return render(request, 'pages/brands/edit_brand.html', {'brand': brand, 'countries': countries, 'selected_country': selected_country, 'is_active_brand' : is_active_brand})
    else:
        return redirect('admin_login_page')

    



# EDIT BRAND FUNCTION   
@login_required
@never_cache
def edit_brand(request, brand_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST['name']
            country_of_origin = request.POST['country_of_origin']
            manufacturer_details = request.POST['manufacturer_details']
            
            brand = Brand.objects.get(id = brand_id)
            brand.name = name
            brand.country_of_origin = country_of_origin
            brand.manufacturer_details = manufacturer_details
            brand.save()
            messages.success(request, 'Brand updated successfully!')
            return redirect(list_brand_page)
    else:
        return redirect('admin_login_page')
            
            


# DELETE BRAND FUNCTION
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
    


#  RESTORE BRAND FUNCTION
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
    
    

#  DELETED BRAND VIEW PAGE
@login_required
@never_cache
def deleted_brand_view(request):
    if request.user.is_superuser:
        brand_list = Brand.objects.filter(is_deleted = True).order_by('name').values()
        return render(request, 'pages/brands/deleted_brand.html', {'brand_list' : brand_list, 'is_active_brand' : is_active_brand})
    else:
        return redirect('admin_login_page')
    
    

    
# LIST BRAND FUNCTION
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
    
    
    
    

# UNLIST BRAND FUNCTION   
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
    


