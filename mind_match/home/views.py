from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,DeleteView,View,FormView
from django.contrib.auth.models import User
from .models import Profile, Image
from .forms import UserForm, ProfileForm, UpdateUserForm,ImageForm ,CustomLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
# Create your views here.

from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "myauth/register.html" ## ваш template
    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password)
        login(self.request, user)
        return response

def asd(request: HttpRequest ) -> HttpResponse:
    return HttpResponse("asdasd")

def main(request: HttpRequest) -> HttpResponse:
    return render(request, 'home/main.html', context={})

class AboutMeView(LoginRequiredMixin,TemplateView):
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
            context['image_form'] = ImageForm()
        return context

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        image_form = ImageForm(request.POST,request.FILES)
        print(user_form.is_valid())
        print(profile_form.is_valid())
        print(image_form.is_valid())

        if user_form.is_valid() and profile_form.is_valid() and image_form.is_valid():
            username =  user_form.cleaned_data.get("username")
            password =  user_form.cleaned_data.get("password")
            print(username)
            print(password)

            #user = authenticate(request,username=username, password=password)
            user = user_form.save()
            print(user)

            login(request, user)
            profile = profile_form.save(commit=False)
            profile.user = user
            image  = image_form.save(commit=False)
            image.user = user
            image.save()
            profile.save()
            return HttpResponseRedirect(reverse('home:about-me'))
        else:
            return render(request, self.template_name, {'user_form': user_form, "profile_form" :profile_form, 'image_form': image_form } )

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

"""class ProfileUpdateView(UpdateView):
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
"""
class ProfileUpdateView(LoginRequiredMixin,View):
    def get(self,request):
        user_form = UpdateUserForm(instance=request.user)
        profile_form = ProfileForm(instance= Profile.objects.get_or_create(user=request.user)[0])

        print(profile_form)
        user_form['username'].label_tag(attrs={'class': "asasasasasasas"})

        return render(request, 'home/update-about-me.html', {'user_form': user_form, 'profile_form': profile_form})
    def post(self,request):
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)


        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('home:about-me'))

class AddImageView(LoginRequiredMixin,TemplateView):
    template_name = "home/add-image.html"
    success_url = reverse_lazy("home:about-me")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not self.request.POST:
            context['image_form'] = ImageForm()
        return context

    def post(self, request, *args, **kwargs):
        image_form = ImageForm(request.POST,request.FILES)
        print(image_form['title'].label_tag(attrs = {'class' : "asd"}))
        print(image_form.is_valid())

        if image_form.is_valid():
            print(request.user.image_set.all())
            if request.user:
                user = request.user
                image  = image_form.save(commit=False)
                image.user = user
                image.save()
                return HttpResponseRedirect(reverse('home:about-me'))
        else:
            return render(request, self.template_name, {'image_form': image_form } )
def logout_view(request: HttpRequest)-> HttpResponse:
    logout(request)
    return redirect(reverse('home:login'))

class CustomLoginView(FormView):
    form_class = CustomLoginForm
    template_name = 'home/login.html'
    success_url = reverse_lazy('home:main')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)
    #redirect_authenticated_user = True

@login_required
def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id, user=request.user)  # Ensuring only the owner can delete
    image.delete()
    return redirect('home:about-me')