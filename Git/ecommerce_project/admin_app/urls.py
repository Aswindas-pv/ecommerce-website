from django.urls import path
from admin_app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('sneakerheads/admin/login/', views.admin_login_page, name='admin_login_page'),
    path('sneakerheads/admin/logout/', views.admin_logout, name = 'admin_logout'),
    
    
    path('page_not_found/', views.page_not_found, name='page_not_found'),
    
    
    path('sneakerheads/admin/products/', views.list_product_page, name='list_product_page'),
    path('sneakerheads/admin/add-products/', views.admin_add_product, name='admin_add_product'),
    path('add-product/page/', views.add_products, name='add_products'),
    path('edit-product-page/<int:pdt_id>/', views.edit_product_page, name='edit_product_page'),
    path('edit-product/<int:pdt_id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:pdt_id>/', views.delete_product, name='delete_product'),
    path('deleted-product-view/', views.deleted_product_page, name='deleted_product_page'),
    path('restore-product/<int:pdt_id>/', views.restore_product, name='restore_product'),
    path('product-variants-add-page/', views.admin_add_variants, name='admin_add_variants'),
    path('add-product-size/', views.add_size, name = 'add_size'),
    path('product-image-add-page/', views.admin_add_image_page, name='admin_add_image_page'),
    path('add-product-color-image/', views.add_product_image, name='add_product_image'),
    path('get-colors/', views.get_colors, name='get_colors'),
    path('list-product/<int:pdt_id>/', views.list_product, name='list_product'),
    path('un-list-product/<int:pdt_id>/', views.un_list_product, name='un_list_product'),
    path('get-sizes/', views.get_sizes_view, name='get_sizes'),
    
    
    
    
    
    path('sneakerheads/admin/brands/', views.list_brand_page, name='list_brand_page'),
    path('sneakerheads/admin/add-brand/', views.admin_add_brand, name='admin_add_brand'),
    path('add-brand/page/', views.add_brand, name='add_brand'),
    path('list-brand/<int:brand_id>/', views.list_the_brand, name='list_the_brand'),
    path('un-list-brand/<int:brand_id>/', views.un_list_the_brand, name='un_list_the_brand'),
    path('delete-brand/<int:brand_id>/', views.delete_brand, name='delete_brand'),
    path('deleted-brand-view/', views.deleted_brand_view, name='deleted_brand_view'),
    path('restore-brand/<int:brand_id>/', views.restore_brand, name='restore_brand'),
    path('edit-brand-page/<int:brand_id>/', views.edit_brand_page, name='edit_brand_page'),
    path('edit-brand/<int:brand_id>/', views.edit_brand, name='edit_brand'),
    
    
    
    
    
    path('sneakerheads/admin/categories/', views.admin_categories, name = 'admin_categories'),
    path('add-category/page', views.add_category_page, name = 'add_category_page'),
    path("add-categories/", views.add_categories ,name="add_categories"),
    path('edit-category-page/<int:cat_id>/', views.edit_category_page, name='edit_category_page'),
    path('edit-category/<int:cat_id>/', views.edit_category, name='edit_category'),
    path('delete-category/<int:cat_id>/', views.delete_category, name='delete_category'),
    path('list-category/<int:cat_id>/', views.list_category, name='list_category'),
    path('un-list-category/<int:cat_id>/', views.un_list_category, name='un_list_category'),
    path('deleted-category-view', views.deleted_cat_view, name='deleted_cat_view'),
    path('restore-categories/<int:cat_id>/', views.restore_categories, name='restore_categories'),
    
    
    
    path('sneakerheads/admin/customers/', views.admin_customers, name = 'admin_customers'),
    path('block-user/<int:user_id>/', views.block_user, name='block_user'),
    path('unblock-user/<int:user_id>/', views.unblock_user, name='unblock_user'),
    path('sneakerheads/admin/customer/search/', views.search_user, name='search_user'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)