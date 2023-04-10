from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm 

urlpatterns = [
    path("",views.home),
    path("category/<slug:val>",views.CategoryView.as_view(),name = "category"),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(),name = "product-detail"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('add-to-cart/',views.add_to_cart, name='add-to-cart'),
    path('cart/',views.show_cart, name='showcart'),
    path('checkout/',views.checkout.as_view(), name='checkout'), 
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('paymentdone/',views.payment_done, name = 'paymentdone'),
    path('orders/', views.home, name='orders'),

    #login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view. LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm),name='password_reset'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name = 'logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)