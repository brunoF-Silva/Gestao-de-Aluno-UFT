from django.db import models

class Campus(models.Model):
    # id_campus = models.AutoField(primary_key=True)
    campus = models.CharField(verbose_name="Nome do Campus", help_text="Preencher com a cidade do campus universitário.", max_length=50)

    class Meta:
        verbose_name = "Campus"
        verbose_name_plural = "Campi"

    def __str__(self):
        return self.campus