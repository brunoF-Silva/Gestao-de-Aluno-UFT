import uuid
from django.db import models

# Create your models here.
#class Aluno(models.Model):
    #nome = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.nome
class Campus(models.Model):
    # id_campus = models.AutoField(primary_key=True)
    campus = models.CharField(verbose_name="Nome do Campus", help_text="Preencher com a cidade do campus universiatrio.", max_length=50)

    def __str__(self):
        return self.campus

class Curso(models.Model):
    # id_curso = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    classificacao = models.CharField(max_length=12, choices=[('Bacharelado', 'Bacharelado'), ('Licenciatura', 'Licenciatura'), ('Tecnologo', 'Tecnólogo')])
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    modalidade = models.CharField(max_length=10, choices=[('Presencial', 'Presencial'), ('EAD', 'Ensino a Distância')])
    periodo = models.CharField(max_length=8, choices=[('Matutino', 'Matutino'), ('Noturno', 'Noturno'), ('Integral', 'Integral')])

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    # id = models.UUIDField(primary_key=True, defaultk=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    matricula = models.CharField(max_length=9)
    
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)    
    # dataDeNascimento
    # MODELO_DE_CADATSRO=True
    data_de_nasc = models.DateField()
    foto = models.ImageField(upload_to='home/img/')
    situacao = models.CharField(max_length=10)
    forma_de_ingresso = models.CharField(max_length=10, choices=[('ENEM', 'Exame Nacional do Ensino Médio'), ('PSC', 'Processo Seletivo Complementar'), ('Vestibular', 'Vestibular')])
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])
    raca = models.CharField(max_length=10, choices=[('Amarelo', 'Amarelo(a)'), ('Branco', 'Branco(a)'), ('Indigina', 'Indigena'), ('Pardo', 'Pardo(a)'), ('Preto', 'Preto(a)')])

    #class Meta:
        #managed = False 

    def __str__(self):
        return self.nome
    
    def gerarMatricula(self):
        pass


