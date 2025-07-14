from django.urls import path

from . import views
from .views import pay_order

urlpatterns = [
    path('',views.UserPanelDashboardPage.as_view(),name='user_panel_dashboard'),
    path('change-pass',views.ChangePasswordPage.as_view(),name='change_password_page'),
    path('edit-profile',views.EditUserProfilePage.as_view(),name='edit_profile_page'),
    path('user-basket',views.user_basket,name='user_basket_page'),
    path('my-shopping',views.MyShopping.as_view(),name='user-shopping-page'),
    path('my-shopping-detail/<order_id>',views.my_shopping_detail,name='user-shopping-detail-page'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail_ajax'),
    path('change-order-detail', views.change_order_detail_count, name='change_order_detail_ajax'),
    path('pay/<int:order_id>/', pay_order, name='pay_order'),
]