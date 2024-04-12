from django.db import models
from home.models.campus.Campus import Campus

class Curso(models.Model):
    # id_curso = models.AutoField(primary_key=True)
    nome = models.CharField(verbose_name='Nome do Curso', max_length=50)
    classificacao = models.CharField(max_length=12, choices=[('Bacharelado', 'Bacharelado'), ('Licenciatura', 'Licenciatura'), ('Tecnólogo', 'Tecnólogo')])
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    modalidade = models.CharField(max_length=10, choices=[('Presencial', 'Presencial'), ('EAD', 'Ensino a Distância')])
    periodo = models.CharField(verbose_name="Período", max_length=8, choices=[('Matutino', 'Matutino'), ('Noturno', 'Noturno'), ('Integral', 'Integral')])

    def __str__(self):
        return self.nome