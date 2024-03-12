# No arquivo models.py

from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    classificacao = models.CharField(max_length=50)
    campus = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=50)
    periodo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    matricula = models.CharField(max_length=20)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    campus = models.CharField(max_length=100)
    data_de_nasc = models.DateField()
    foto = models.ImageField(upload_to='aluno_fotos/')
    situacao = models.CharField(max_length=50)
    forma_de_ingresso = models.CharField(max_length=50)
    curso_classificacao = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    raca = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
