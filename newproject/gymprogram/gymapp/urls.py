from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
	path('about', AboutView.as_view()),
	
	path('', MoveListView.as_view()),
	path('move/new', MoveCreateView.as_view()),
	path('move/<int:pk>/delete', MoveDeleteView.as_view()),
	path('move/<int:pk>', MoveUpdateView.as_view()),

	path('program', ProgramListView.as_view()),
	path('program/new', ProgramCreateView.as_view()),
	path('program/<int:pk>', ProgramUpdateView.as_view()),
	path('program/<int:pk>/delete', ProgramDeleteView.as_view()),

	path('register', RegisterView.as_view()),	
	path('login', LoginView.as_view(next_page="/")),
	path('accounts/login/', LoginView.as_view(next_page="/")),
	path('logout', LogoutView.as_view(next_page="/")),
]
