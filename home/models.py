import uuid
from django.db import models

# Create your models here.
#class Aluno(models.Model):
    #nome = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.nome
class Campus(models.Model):
    # id_campus = models.AutoField(primary_key=True)
    campus = models.CharField(verbose_name="Nome do Campus", help_text="Preencher com a cidade do campus universitário.", max_length=50)

    class Meta:
        verbose_name_plural: "Campi"

    def __str__(self):
        return self.campus

class Curso(models.Model):
    # id_curso = models.AutoField(primary_key=True)
    nome = models.CharField(verbose_name='Nome do Curso', max_length=50)
    classificacao = models.CharField(max_length=12, choices=[('Bacharelado', 'Bacharelado'), ('Licenciatura', 'Licenciatura'), ('Tecnólogo', 'Tecnólogo')])
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    modalidade = models.CharField(max_length=10, choices=[('Presencial', 'Presencial'), ('EAD', 'Ensino a Distância')])
    periodo = models.CharField(verbose_name="Período", max_length=8, choices=[('Matutino', 'Matutino'), ('Noturno', 'Noturno'), ('Integral', 'Integral')])

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(help_text="Informe com pontos e traços.", max_length=14)
    matricula = models.CharField(verbose_name='Matrícula', max_length=9)
    
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)    
    # dataDeNascimento
    # MODELO_DE_CADATSRO=True
    dataDeNasc = models.DateField(help_text='DD/MM/AAAA',verbose_name= 'Data de Nascimento')
    foto = models.ImageField(upload_to='home/media')
    situacao = models.CharField(max_length=10)
    formaDeIngresso = models.CharField(verbose_name='Forma de Ingresso', max_length=10, choices=[('ENEM', 'Exame Nacional do Ensino Médio'), ('PSC', 'Processo Seletivo Complementar'), ('Vestibular', 'Vestibular')])
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])
    raca = models.CharField(verbose_name='Raça', max_length=10, choices=[('Amarela', 'Amarela'), ('Branca', 'Branca'), ('Indigena', 'Indigena'), ('Parda', 'Parda'), ('Preta', 'Preta')])

    #class Meta:
        #managed = False 

    def __str__(self):
        return self.nome


