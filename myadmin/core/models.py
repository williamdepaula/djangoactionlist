from django.db import models

class Artigo(models.Model):
    titulo = models.CharField('Título', max_length=200)
    texto = models.TextField('Artigo')
    data_publicacao = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.titulo