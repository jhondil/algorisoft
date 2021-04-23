from django.forms import *

from core.erp.models import *

class CategoryForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #recorrido del formulario
        for form in self.visible_fields():
            form.field.widget.attrs.update({'class': 'form-control'})
            form.field.widget.attrs.update({'autocomplete': 'off'})
            

    class Meta:
        model = Category
        fields = '__all__'
        #para cambiar nombre de las etiquetas
        labels = {
            'name': 'Nombre Categoría', #igual el nombre aparece en por el verbose_name en la models
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder':  'Nombre de la categoría',
                    
                }
            ), #si hubiera otro campo
            # 'desc': TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder':  'Nombre de la categoría',
            #         'autocomplete' : 'off'
            #     }
            # ),


        }

    def clean(self):
        cleaned = super().clean()
        if len(cleaned['name']) <= 50:
            self.add_error('name', 'Le faltan caracteres')
        return cleaned