import uuid
from django.db import models
#####
from home.models.curso.Curso import Curso

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
    raca = models.CharField(verbose_name='Raça', max_length=10, choices=[('1', 'Amarela'), ('Branca', 'Branca'), ('Indigena', 'Indigena'), ('Parda', 'Parda'), ('Preta', 'Preta')])

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering = ['nome']

    def __str__(self):
        return self.nome
