from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICE = [
       ("aberto", "Em aberto"),
       ("em andamento", "Em andamento"),
       ("concluído", "Concluído")
    ]

class Documentos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.TextField()
    data_de_criacao =  models.DateTimeField(auto_now_add=True)
    departamento = models.CharField(max_length=45, blank=True, null=True)
    arquivo = models.FileField(upload_to='Documentos/', blank=True, null=True) 
    atualizado_pela_ultima_vez = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default="aberto")   
    
    def __str__(self):
        return self.titulo

class ListaChamado(models.Model):

   titulo = models.CharField(max_length=100, blank=False, null=False)
   descricao = models.TextField()
   status = models.CharField(max_length=20, choices=STATUS_CHOICE, default="aberto")   
   usuario = models.ForeignKey
   departamento = models.ForeignKey
   data_de_criacao = models.DateTimeField(auto_now_add=True)
   atualizado_pela_ultima_vez = models.DateTimeField(auto_now=True)

   def __str__(self):
       return f"{self.pk} - {self.titulo}"

