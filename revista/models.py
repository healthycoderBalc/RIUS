from tabnanny import verbose
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Edition(models.Model):
    year = models.IntegerField(verbose_name="Año")
    volume = models.IntegerField(verbose_name="Volumen")
    number = models.IntegerField(verbose_name="Número")

    def __str__(self):
        return f"V{self.volume} - N{self.number}, A{self.year}"

class Profession(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")

class Status(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=200, verbose_name="Descripción")

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    profesion = models.ForeignKey(Profession, on_delete=models.SET_DEFAULT, default= '', verbose_name="Profesión", blank=True, null=True)
    cargo = models.CharField(max_length=200, verbose_name="Cargo")
    institution = models.CharField(max_length=200, verbose_name="Institución")
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=200, verbose_name="Teléfono")

    def __str__(self):
        return self.user.first_name



class Revisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=200, verbose_name="Teléfono")
    areas = models.ManyToManyField(Area, through='revisor_area', blank=True)

    def __str__(self):
        return self.user.first_name


class Manuscript(models.Model):
    edicion = models.ForeignKey(Edition, on_delete=models.SET_DEFAULT, default= '', verbose_name="Edición")
    titulo_largo = models.CharField(max_length=300)
    titulo_corto = models.CharField(max_length=200)
    documento_manuscrito = models.FileField(upload_to = 'uploads/manuscrito')
    documento_lista_cotejo = models.FileField(upload_to = 'uploads/cotejo')
    documento_originalidad = models.FileField(upload_to = 'uploads/originalidad')
    documento_carta_presentacion = models.FileField(upload_to = 'uploads/presentacion')
    fecha_recibido = models.DateField(verbose_name="Fecha de recepción")
    fecha_aceptado = models.DateField(verbose_name="Fecha de aceptación")
    autores = models.ManyToManyField(Author, through='author_manuscript', blank=True)
    revisores = models.ManyToManyField(Revisor, through='revisor_manuscript', blank=True)

    def __str__(self):
        return self.titulo_corto


class author_manuscript(models.Model):
    autor = models.ForeignKey(Author, on_delete=models.CASCADE) # revisar el on_delete
    manuscrito = models.ForeignKey(Manuscript, on_delete=models.CASCADE)
    orden_autor = models.IntegerField(verbose_name="Posición del autor en este manuscrito")

    def __str__(self):
        return self.author.user.first_name


class revisor_manuscript(models.Model):
    revisor = models.ForeignKey(Revisor, on_delete=models.CASCADE) # revisar el on_delete
    manuscrito = models.ForeignKey(Manuscript, on_delete=models.CASCADE)
    recomendacion = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default= '', verbose_name="Recomendación", blank=True, null=True)
    fecha_recibido = models.DateField(verbose_name="Fecha de recepción por el revisor")
    fecha_devolucion = models.DateField(verbose_name="Fecha de devolución por el revisor")
    manuscrito_a_revisar = models.FileField(upload_to = 'uploads/manuscritorevisar')
    manuscrito_revisado = models.FileField(upload_to = 'uploads/manuscritorevisado')
    lista_cotejo = models.FileField(upload_to = 'uploads/revisorlistacotejo')

    def __str__(self):
        return self.revisor.user.first_name


class revisor_area(models.Model):
    revisor = models.ForeignKey(Revisor, on_delete=models.CASCADE) # revisar el on_delete
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    comentarios = models.CharField(max_length=300)
    
    def __str__(self):
        return f"{self.revisor.user.first_name} - {self.area.name}"