from django.contrib import admin
from django.urls import path
from AppEcommerce.views import *
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("profil/", profil, name="profil"),
    path("category/", category, name="category"),
    path("favorite/", favorite, name="favorite"),
    path("product-detail/<int:product_id>", product_detail, name="product_detail"),
    path("favori/", favori, name="favori"),
    path("sendMail/", sendMail , name="sendMail"),
    path('forsale/', forsale, name='forsale'),
    path('forrent/', forrent, name='forrent'),
    path('idea/', idea, name='idea'),
    path('chatbot/', chatbot, name='chatbot'),

    #authenticationed
    path("login/", Login, name="login"),
    path("register/", Register, name="register"),
    path("logout/", Logout, name="logout"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set_language/<str:language>", set_language, name="set-language"),
    ]








