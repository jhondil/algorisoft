
from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView, DeleteView, FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import  csrf_exempt
from django.http import JsonResponse
from django.urls import reverse_lazy 

from core.erp.models import Category
from core.erp.forms import *

from django.contrib.auth.mixins import LoginRequiredMixin

# vista basada en funcion 
def category_list(request):
    date = {
        'title': 'Listado de Categorías',
        'categories' : Category.objects.all()

    }
    return render(request, 'category/list.html', date)
    

# vista basada en clases

class CategoryListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Category
    template_name = 'category/list.html'

    #decorador
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
            
            
        except Exception as e:
            data['error']= str(e)
        
        return JsonResponse(data)


    # def def get_queryset(self):
    #     return Category.Objets.filter(name__startswith='L') #para listar por letra las que inicien

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Listado de Categorías" 
        # context['hola'] = "hola putito" enviar otra variable 
        context['create_url'] = reverse_lazy('category_create')
        context['entity'] = 'Categoría'
        context['entity_url'] = reverse_lazy('category_list')
        context['entity_next'] = ''
        return context


class CategoryCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model= Category
    form_class =  CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category_list')# hace como una redireccion absoluta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Agregar Categoría" 
        # context['hola'] = "hola putito" enviar otra variable 
        context['entity'] = 'Categoría'
        context['entity_url'] = reverse_lazy('category_list')
        context['entity_next'] = 'Agregar Categoría'
        context['entity_next_url'] = reverse_lazy('category_create')
        return context


class CategoryUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    model= Category
    form_class =  CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('category_list')# hace como una redireccion absoluta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Actualizar Categoría" 
        # context['hola'] = "hola putito" enviar otra variable 
        context['entity'] = 'Categoría'
        context['entity_url'] = reverse_lazy('category_list')
        context['entity_next'] = 'Actualizar Categoría'
       
        return context

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model= Category
    form_class =  CategoryForm
    template_name = 'category/delete.html'
    success_url = reverse_lazy('category_list')# hace como una redireccion absoluta

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Eliminar Categoría" 
        # context['hola'] = "hola putito" enviar otra variable 
        context['entity'] = 'Categoría'
        context['entity_url'] = reverse_lazy('category_list')
        context['entity_next'] = 'Eliminar Categoría'

        return context


class CategoryFormView( LoginRequiredMixin, FormView): 
    form_class= CategoryForm
    template_name='category/create.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form): #si el formulario es valido
        print(form) #imprime todo lo del formulario
        return super().form_valid(form)

    def form_invalid(self, form): #si el formulario es invalido
        print(form)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Form | Categoría" 
        # context['hola'] = "hola putito" enviar otra variable 
        context['entity'] = 'Categoría'
        context['entity_url'] = reverse_lazy('category_list')
        context['entity_next'] = 'Agregar Categoría'

        return context