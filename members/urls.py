from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_user, name="login"),
    path("question1/<str:name>", views.question1, name="question1"),
    path("question2/<str:name>", views.question2, name="question2"),
    path("complete/<str:name>", views.complete, name="complete"),
    path('logout/', views.logout_user, name='logout'),
]
