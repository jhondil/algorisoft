from django.db import models
from datetime import datetime

from django.forms import model_to_dict

from core.erp.choices import gender_choices

# Create your models here.
class  Empleado(models.Model):
    names = models.CharField( max_length=150,verbose_name='Nombres')
    dni = models.CharField( max_length=15, unique=True, verbose_name='dni' )
    date_joined = models.DateField(default=datetime.now, verbose_name='fecha Registro')
    date_created = models.DateField(auto_now=True)#auto_now= fecha que se registre 
    date_update = models.DateField(auto_now_add=True)#auto_now= fecha actualice cada ves
    #age = models.IntegerField(default=0)#sse pueden colocar valores negativos
    age = models.PositiveIntegerField(default=0)#solo valores positivos
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2 )#solo valores positivos
    state =models.BooleanField(default=True)
    #gender = models.CharField(max_length=50, verbose_name='genero')
    avatar = models.ImageField(upload_to = 'avatar/%Y/%m/%d', null=True, blank=True)#update_to guardar en una carpeta
    cvitae= models.FileField(upload_to = 'cvitae/%Y/%m/%d', null=True, blank=True) #null=True, blank=True que sea por defecto

    #que valor va a devolver
    def __str__(self):
        return self.names

    #colocar propiedades
    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        db_table='empleado'
        ordering=['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    def __str__(self):
        #return 'Nro:{} / Nombre: {} '.format(self.id, self.name) #lo que devuelve la base de datos/para devolver dos valores
        return self.name #lo que devuelve la base de datos
    
    def toJSON(self):
        # item = {'id':self.id, 'name':self.name}
        item = model_to_dict(self) #cuando se tienen muchisimos registros
        return item

    class Meta:
        verbose_name= 'Categoria'
        verbose_name_plural = "Categorias"
        ordering = ['id']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate =  models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural = "Productos"
        ordering = ['id']

class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length = 150, verbose_name='Apellidos')
    dni = models.CharField(max_length = 10, unique=True, verbose_name='DNI')
    birthday = models.DateField(default = datetime.now, verbose_name='Fecha de Nacimiento' )
    address = models.CharField(max_length = 150,null=True, blank=True, verbose_name='Direccion')
    sexo = models.CharField(max_length = 10, choices = gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name= 'Cliente'
        verbose_name_plural = "Clientes"
        ordering = ['id']


class Sale(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cliente.names


    class Meta:
        verbose_name= 'Venta'
        verbose_name_plural = "Ventas"
        ordering = ['id']

class DetSale(models.Model):

    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00 ,max_digits=9, decimal_places=2)

    def __str__(self):
        return self.producto.name
    
    
    
    class Meta:
        verbose_name= 'Detalle_venta'
        verbose_name_plural = "Detalles_ventas"
        ordering = ['id']
