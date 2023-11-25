from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,ListView,UpdateView,DetailView,TemplateView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate,login,logout

from delight.forms import RegistrationForm,LoginForm,CategorycreateForm,CakeAddForm,CakeVarientForm,OfferAddForm
from delight.models import User,Category,cakes,cakevarients,offers


def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session !")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
    
def is_admin(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            messages.error(request,"permission denied for current user !")    
            return redirect("signin")
        else:
             return fn(request,*args,**kwargs)
    return wrapper
decs=[signin_required,is_admin]   



class SingnupView(CreateView):
    template_name="delight/register.html" 
    form_class=RegistrationForm
    model=User
    success_url=reverse_lazy("signin")
    def form_valid(self,form):
        messages.success(self.request,"account created")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)


class SigninView(FormView):
    template_name="delight/login.html"  
    form_class=LoginForm
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)  
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login successfull")
                return redirect("index")
            else:
                messages.error(request,"invalid credential")
                return render(request,self.template_name,{"form":form})
            

@signin_required
def Signoutview(request,*args,**kwargs):
    logout(request)
    return redirect("signin")



@method_decorator(decs,name="dispatch")
class CategoryCreateView(CreateView,ListView):
    template_name="delight/category_add.html"
    form_class=CategorycreateForm
    model=Category
    context_object_name="categories"
    success_url=reverse_lazy("add-category")
    def form_valid(self, form):
        messages.success(self.request,"category added successfully")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"category adding failed")
        return super().form_invalid(form) 
    
    def get_queryset(self):
        return Category.objects.filter(is_active=True)
    
@signin_required
@is_admin
def remove_category(request,*args,**kwargs):
    id=kwargs.get("pk")
    Category.objects.filter(id=id).update(is_active=False)
    messages.success(request,"remove category")
    return redirect("add-category")    

    
@method_decorator(decs,name="dispatch")
class CakeAddview(CreateView):
    template_name="delight/cake_add.html"
    model=cakes
    form_class=CakeAddForm
    success_url=reverse_lazy("cake-list")
    def form_valid(self,form):
        messages.success(self.request,"cake has been added")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request," cake adding Failed")
        return super().form_invalid(form)  
      
    
@method_decorator(decs,name="dispatch")
class CakeListView(ListView):
    template_name="delight/cake_list.html"    
    model=cakes
    context_object_name="cake"   

       

@method_decorator(decs,name="dispatch")
class CakeUpdateView(UpdateView):
    template_name="delight/cake_edit.html"    
    model=cakes
    form_class=CakeAddForm
    success_url=reverse_lazy("cake-list")
    def form_valid(self,form):
        messages.success(self.request,"cake updated successfully  ")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"cake updating failed ")
        return super().form_invalid(form)
    
    
@method_decorator(decs,name="dispatch")   
class CakeDetailView(DetailView):
    template_name="delight/cake_detail.html"    
    model=cakes
    context_object_name="cake"   


@signin_required
@is_admin
def remove_cakeView(request,*args,**kwargs):
    id=kwargs.get("pk")
    cakes.objects.filter(id=id).delete()
    return redirect("cake-list") 


@method_decorator(decs,name="dispatch")
class CakeVarientCreateView(CreateView):
    template_name="delight/cakevarient_add.html"
    form_class=CakeVarientForm
    model=cakevarients
    success_url=reverse_lazy("cake-list")

    def form_valid(self,form):
        id=self.kwargs.get("pk")
        obj=cakes.objects.get(id=id)
        form.instance.cake=obj
        messages.success(self.request,"varient has been added")
        return super().form_valid(form)   
    

@method_decorator(decs,name="dispatch")
class CakeVarientUpdateView(UpdateView):
    template_name="delight/cakevarient_update.html"
    form_class=CakeVarientForm
    model=cakevarients
    success_url=reverse_lazy("cake-list")
    def form_valid(self, form):
        messages.success(self.request,"cake varient added successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"cake varient updating failed")
        return super().form_invalid(form)
    

    def get_success_url(self):
        # localhost:cloths/<int:pk>/
       id=self.kwargs.get("pk")
       cake_varient_object=cakevarients.objects.get(id=id)
       cakes_id=cake_varient_object.cake.id
       return reverse("cake-detail",kwargs={"pk":cakes_id})

@signin_required
@is_admin   
def remove_cakeVarientView(request,*args,**kwargs):
    id=kwargs.get("pk")
    cake_object=cakevarients.objects.get(id=id)
    cake_id=cake_object.cake.id
    cake_object.delete()
    return redirect("cake-detail",pk=cake_id)

   
@method_decorator(decs,name="dispatch")
class OfferCreateView(CreateView):
    template_name="delight/offer_add.html"
    form_class=OfferAddForm
    model=offers
    success_url=reverse_lazy("cake-list")

    def form_valid(self,form):
        id=self.kwargs.get("pk")
        obj=cakevarients.objects.get(id=id)
        form.instance.cakevarient=obj
        messages.success(self.request,"offer added successfully ")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"offer added failed ")
        return super().form_invalid(form)
    
    def get_success_url(self):
       id=self.kwargs.get("pk")
       cake_varient_object=cakevarients.objects.get(id=id)
       cake_id=cake_varient_object.cake.id
       return reverse("cake-detail",kwargs={"pk":cake_id})

@signin_required
@is_admin   
def offer_delete_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    offer_object=offers.objects.get(id=id)
    cake_id=offer_object.cakevarient.cake.id
    offer_object.delete()
    return redirect("cake-detail",pk=cake_id)


class IndexView(TemplateView):
    template_name="delight/index.html"