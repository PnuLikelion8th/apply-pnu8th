"""apply_pnu_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import apply_pnu.views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', apply_pnu.views.index, name="index"),
    path('admin/', admin.site.urls),
    path('login', apply_pnu.views.PnuLogin.as_view(), name="login"),
    path('signup', apply_pnu.views.signup, name ="signup"),
    path('profile_update', apply_pnu.views.profile_update, name ="profile_update"),
    
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    path('apply/', apply_pnu.views.Apply.as_view(), name="apply"),
    path('apply_detail/<int:pk>',
         apply_pnu.views.ApplyDetail.as_view(), name="apply_detail"),

    
         
    path('apply_edit/<int:pk>', apply_pnu.views.ApplyEdit.as_view(), name="apply_edit"),

    path('cajsdvkuwqjnuxnehhb/', apply_pnu.views.ApplyList.as_view(), name="tjh_show_apply"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
