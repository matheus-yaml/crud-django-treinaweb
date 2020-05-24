from django.db import models

# Create your models here.
class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('a', 'Alta'),
        ('b', 'Baixa'),
        ('n', 'Normal')
    ]
    titulo = models.CharField(max_length=30, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    data_expiracao = models.DateTimeField(null=False, blank=False)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADE_CHOICES, null=False, blank=False)