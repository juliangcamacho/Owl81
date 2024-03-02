from django.db import models

class   Novedades(models.Model):
    date = models.DateField (verbose_name="Fecha")
    tipe_novedad = models.CharField(max_length = 45, verbose_name="Tipo Novedad")

    def __str__(self):
        return self.tipe_novedad

    class Meta:
        verbose_name = 'Novedad'
        verbose_name_plural = 'Novedades'
        db_table = 'Novedades'
        ordering = ['id']

class Incapacidad(models.Model):
    date_inability = models.DateField (verbose_name="Fecha Incapacidad")
    tipe_inability = models.CharField(max_length = 46, verbose_name="Tipo Incapacidad")
    no_contact = models.IntegerField(verbose_name="Numero Contacto")
    Novedades = models.ForeignKey (Novedades, on_delete=models.CASCADE, verbose_name="Tipo de novedad")



    def __str__(self):
        return self.tipe_inability

    class Meta:
        verbose_name = 'Incapacidad'
        verbose_name_plural = 'Incapacidades'
        db_table = 'Incapacidad'
        ordering = ['id']


class Activity(models.Model):
    name_teacher = models.CharField(max_length = 45, verbose_name="Nombre instructor")
    date_activity = models.DateField (verbose_name="Fecha Actividad")
    name_activity = models.CharField (max_length =45, verbose_name = "Nombre de actividad")
    Novedades = models.ForeignKey (Novedades, on_delete=models.CASCADE, verbose_name="Tipo de novedad")

    def __str__(self):
        return self.name_activity

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        db_table = 'Actividad'
        ordering = ['id']


class Inscription(models.Model):
    number_id = models.BigIntegerField(verbose_name="Numero de documento")
    name = models.CharField(max_length = 40, verbose_name="Nombre")
    last_name = models.CharField(max_length = 40, verbose_name="Apellido")
    nationality = models.CharField(max_length = 25, verbose_name="Nacionalidad")
    date_born = models.DateField(verbose_name="Fecha de nacimiento")
    Novedades = models.ForeignKey (Novedades, on_delete=models.CASCADE, verbose_name="Tipo de novedad")

    def __str__(self):
        return self.number_id

    class Meta:
        verbose_name = 'Inscripcion'
        verbose_name_plural = 'Inscripciones'
        db_table = 'Inscripciones'
        ordering = ['id']

class Inventory(models.Model):
    date_register = models.DateField(verbose_name="Fecha de registro")
    quantity = models.SmallIntegerField(verbose_name="Cantidad")
    description = models.CharField(max_length=100, verbose_name="Descripción")

    def __str__(self):
        return self.date_register

    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
        db_table = 'Inventario'
        ordering = ['id']

class Donation(models.Model):
    date_donation = models.DateField(verbose_name="Fecha de donacón")
    quantity = models.SmallIntegerField(verbose_name="Cantidad")
    tipe_donation = models.CharField(max_length=15, verbose_name="Tipo de donación")
    inventory = models.ForeignKey (Inventory, on_delete=models.CASCADE, verbose_name="Descripción")

    def __str__(self):
        return self.date_donation

    class Meta:
        verbose_name = 'Donacion'
        verbose_name_plural = 'Donaciones'
        db_table = 'Donaciones'
        ordering = ['id']
