"""Alter_Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .Alter_01_Registration import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.Insertrecord),
    # path('', views.Userregistration),
    path('', index.webpage1, name='index'),
    path('', include('Alter_Backend.Alter_05_Test_HCI_Rules.urls')),
    path('user-login', index.webpage2, name='user-login'),
    path('login-wireframe', index.webpage3, name='login-wireframe'),
    path('generate-umls', index.webpage4, name='generate-umls'),
    path('wireframe-intro', index.webpage5, name='wireframe-intro'),
    path('payment-wireframe', index.webpage6, name='payment-wireframe'),
    path('contact-wireframe-wireframe', index.webpage7, name='contact-us-wireframe'),
    path('HCI_Test', index.webpage8, name='HCI_Test'),
    path('web-interface', index.webpage9, name='web-interface'),
    path('wireframes-suggestion', index.webpage10, name='wireframes-suggestion'),
    path('HCI-rule-based', index.webpage11, name='HCI-rule-based'),
    path('video-conference', index.webpage12, name='video-conference'),
    path('UML-API', index.webpage13, name='UML-API'),
    path('home-wireframe', index.webpage14, name='home-wireframe'),
    path('video-display-wireframe', index.webpage15, name='video-display-wireframe'),
    path('about-us-wireframe', index.webpage16, name='about-us-wireframe'),
    path('add-to-cart-wireframe', index.webpage17, name='add-to-cart-wireframe'),
    path('feedback-wireframe', index.webpage18, name='feedback-wireframe'),
    path('paper-prototype', index.webpage19, name='paper-prototype'),
    path('HCI-results-representation', index.webpage20, name='HCI-results-representation'),
    path('web-interface-preview', index.webpage21, name='web-interface-preview'),
    path('video_display', index.webpage22, name='video_display'),
    path('Location_Wireframe', index.webpage23, name='Location_Wireframe'),
    path('Settings_Wireframe', index.webpage24, name='Settings_Wireframe'),
    path('Blog_Wireframe', index.webpage25, name='Blog_Wireframe'),
    path('register', index.webpage26, name='register'),
    path('web-interface-editor', index.webpage27, name='web-interface-editor'),
    path('generate-requirement-doc', index.webpage28, name='generate-requirement-doc'),
    path('Undefined-wireframe', index.webpage29, name='Undefined-wireframe')
]

urlpatterns += staticfiles_urlpatterns()
