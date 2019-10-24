from django.db import models
from amigos_da_comunidade.edicao.models import *
import datetime

class Setor(AuditModel):

    nome_setor = models.CharField('Nome do Setor', blank=False, null=False, max_length=255)
    edicao = models.ForeignKey(Edicao, verbose_name='Edição', blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('atendimento:setor_list')

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        ordering = ['-created_on']