from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render ,reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserForm, ProfileForm
# Create your views here.
def main(request: HttpRequest) -> HttpResponse:
    return render(request, 'home/main.html', context={})

class AboutMeView(TemplateView):
    model = User
    template_name = "home/about-me.html"
class RegisterView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = "home/register.html"
    success_url = reverse_lazy("home:about-me")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['user_form'] = UserForm(self.request.POST)
            context['profile_form'] = ProfileForm(self.request.POST)
        else:
            context['user_form'] = UserForm()
            context['profile_form'] = ProfileForm()
        return context

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        print(user_form.is_valid())
        print(profile_form.is_valid())

        if user_form.is_valid() and profile_form.is_valid():
            username =  user_form.cleaned_data.get("username")
            password =  user_form.cleaned_data.get("password")
            print(username)
            print(password)

            user = authenticate(request, username=username, password=password)
            user_form.save()
            print(user)
            login(request, user)
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('home:about-me'))
        else:
            return render(request, self.template_name, {'user_form': user_form, "profile_form" :profile_form } )

            """self.render_to_response(self.get_context_data(
                user_form=user_form,
                profile_form=profile_form
            ))"""

    """def form_valid(self, form):
        response = super().form_valid(form)
        asd = Profile.objects.create(user=self.object)
        asd.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password)
        login(self.request, user)
        return response"""

class ProfileUpdateView(UpdateView):
    model = User
    fields = '__all__'
    # form_class = ProductForm
    #template_name_suffix = '_update_form'
    template_name = 'home/update-about-me.html'
    def get_success_url(self):
        return reverse_lazy(
            'home:about-me'
            #kwargs={'pk': self.object.user.pk}
        )

