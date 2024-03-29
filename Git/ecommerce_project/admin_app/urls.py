from django.urls import path
from admin_app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('sneakerheads/admin/login/', views.admin_login_page, name='admin_login_page'),
    path('sneakerheads/admin/logout/', views.admin_logout, name = 'admin_logout'),
    
    
    path('page_not_found/', views.page_not_found, name='page_not_found'),
    
    path('sneakerheads/admin/get_quantity/<str:size>/', views.get_quantity, name='get_quantity'),
    
    path('sneakerheads/admin/product/', views.list_product_page, name='list_product_page'),
    path('sneakerheads/admin/product/add-products/', views.admin_add_product, name='admin_add_product'),
    path('sneakerheads/admin/product/add-product/page/', views.add_products, name='add_products'),
    path('sneakerheads/admin/product/edit-product-page/<int:p_id>/', views.edit_product_page, name='edit_product_page'),
    path('sneakerheads/admin/product/edit-product/update/<int:p_id>/', views.edit_product_update, name='edit_product_update'),
    path('sneakerheads/admin/product/delete-product/<int:pdt_id>/', views.delete_product, name='delete_product'),
    path('sneakerheads/admin/product/deleted-product-view/', views.deleted_product_page, name='deleted_product_page'),
    path('sneakerheads/admin/product/restore-product/<int:pdt_id>/', views.restore_product, name='restore_product'),
    path('sneakerheads/admin/product/add-product-variant/', views.admin_add_variants, name='admin_add_variants'),
    path('sneakerheads/admin/product/add-product-size/', views.add_size, name = 'add_size'),
    path('sneakerheads/admin/product/add-product-image/', views.admin_add_image_page, name='admin_add_image_page'),
    path('sneakerheads/admin/product/add-product-color-image/', views.add_product_image, name='add_product_image'),
    path('sneakerheads/admin/product/get-colors/', views.get_colors, name='get_colors'),
    path('sneakerheads/admin/product/list-product/<int:pdt_id>/', views.list_product, name='list_product'),
    path('sneakerheads/admin/product/un-list-product/<int:pdt_id>/', views.un_list_product, name='un_list_product'),
    path('sneakerheads/admin/product/get-sizes/', views.get_sizes_view, name='get_sizes'),
    
    path('sneakerheads/admin/product/edit-product-color/page/<int:p_id>/', views.edit_product_color_page, name='edit_product_color_page'),
    path('sneakerheads/admin/product/edit-product-size-page/<int:p_id>/', views.edit_product_size_page, name='edit_product_size_page'),
    
    path('sneakerheads/admin/product/product-color-edit/<int:p_id>/', views.edit_product_color, name='edit_product_color'),
    path('sneakerheads/admin/product/product-size-edit/<int:p_id>/', views.edit_product_size, name='edit_product_size'),
    
    
    
    path('sneakerheads/admin/brand/', views.list_brand_page, name='list_brand_page'),
    path('sneakerheads/admin/brand/add-brand/', views.admin_add_brand, name='admin_add_brand'),
    path('sneakerheads/admin/brand/add-brand/page/', views.add_brand, name='add_brand'),
    path('sneakerheads/admin/brand/list-brand/<int:brand_id>/', views.list_the_brand, name='list_the_brand'),
    path('sneakerheads/admin/brand/un-list-brand/<int:brand_id>/', views.un_list_the_brand, name='un_list_the_brand'),
    path('sneakerheads/admin/brand/delete-brand/<int:brand_id>/', views.delete_brand, name='delete_brand'),
    path('sneakerheads/admin/brand/deleted-brand-view/', views.deleted_brand_view, name='deleted_brand_view'),
    path('sneakerheads/admin/brand/restore-brand/<int:brand_id>/', views.restore_brand, name='restore_brand'),
    path('sneakerheads/admin/brand/edit-brand-page/<int:brand_id>/', views.edit_brand_page, name='edit_brand_page'),
    path('sneakerheads/admin/brand/edit-brand/<int:brand_id>/', views.edit_brand, name='edit_brand'),
    
    
    
    
    
    path('sneakerheads/admin/category/', views.admin_categories, name = 'admin_categories'),
    path('sneakerheads/admin/category/add-category/page', views.admin_add_category_page, name = 'admin_add_category_page'),
    path("sneakerheads/admin/category/add-categories/", views.add_categories ,name="add_categories"),
    path('sneakerheads/admin/category/edit-category-page/<int:cat_id>/', views.edit_category_page, name='edit_category_page'),
    path('sneakerheads/admin/category/edit-category/<int:cat_id>/', views.edit_category, name='edit_category'),
    path('sneakerheads/admin/category/delete-category/<int:cat_id>/', views.delete_category, name='delete_category'),
    path('sneakerheads/admin/category/list-category/<int:cat_id>/', views.list_category, name='list_category'),
    path('sneakerheads/admin/category/un-list-category/<int:cat_id>/', views.un_list_category, name='un_list_category'),
    path('sneakerheads/admin/category/deleted-category-view', views.deleted_cat_view, name='deleted_cat_view'),
    path('sneakerheads/admin/category/restore-categories/<int:cat_id>/', views.restore_categories, name='restore_categories'),
    
    
    
    path('sneakerheads/admin/customers/', views.admin_customers, name = 'admin_customers'),
    path('sneakerheads/admin/customers/block-user/<int:user_id>/', views.block_user, name='block_user'),
    path('sneakerheads/admin/customers/unblock-user/<int:user_id>/', views.unblock_user, name='unblock_user'),
    path('sneakerheads/admin/customers/sneakerheads/admin/customer/search/', views.search_user, name='search_user'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)