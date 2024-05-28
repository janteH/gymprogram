from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin
from .models import *

class AboutView(TemplateView):
	template_name = "gymapp/about.html"

#move 
class MoveListView(LoginRequiredMixin, ListView):
	model = Move

	def get_queryset(self):
			return Move.objects.all()

class MoveCreateView(LoginRequiredMixin, CreateView):
	model = Move
	fields = ["name", "reps", "sets", "weight", "description"]
	success_url = "/"

	def form_valid(self, form):
		return super().form_valid(form)
	
class MoveUpdateView(UserPassesTestMixin, UpdateView):
	model = Move
	fields = ["name", "reps", "sets", "weight", "description"]
	success_url = "/"

	def test_func(self):
		return self.request.user.is_authenticated

class MoveDeleteView(UserPassesTestMixin, DeleteView):
	model = Move
	success_url = "/"
	
	def test_func(self):
		return self.request.user.is_authenticated

#program
class ProgramListView(LoginRequiredMixin, ListView):
	model = Program

	def get_queryset(self):
			return Program.objects.all()

class ProgramCreateView(LoginRequiredMixin, CreateView):
	model = Program
	fields = ["name", "info", "move"]
	success_url = "/program"

	def form_valid(self, form):
		return super().form_valid(form)

class ProgramUpdateView(UserPassesTestMixin, UpdateView):
	model = Program
	fields = ["name", "info", "move"]
	success_url = "/program"

	def test_func(self):
		return self.request.user.is_authenticated

class ProgramDeleteView(UserPassesTestMixin, DeleteView):
	model = Program
	success_url = "/program"

	def test_func(self):
		return self.request.user.is_authenticated

#auth
class RegisterView(SuccessMessageMixin, CreateView):
	form_class = UserCreationForm
	template_name = "registration/register.html"
	success_url = "/login"
	success_message = "Registration accepted. You can now log in. "
