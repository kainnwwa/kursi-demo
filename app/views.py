from django.views.generic import FormView, ListView, TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import UserWithPhoneCreationForm
from .models import Service, Application


class MyRegistrationView(FormView):
    form_class = UserWithPhoneCreationForm
    template_name = "registration.html"
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class MyLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    next_page = reverse_lazy('course_list')


class CourseListView(ListView):
    model = Service
    template_name = "course_list.html"
    context_object_name = "courses"
    paginate_by = 3 


class PersonalCabinetView(LoginRequiredMixin, TemplateView):
    template_name = "cabinet.html"


class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['service']
    template_name = "application_form.html"
    success_url = reverse_lazy('cabinet')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)