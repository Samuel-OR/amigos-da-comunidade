from django.db import models
from amigos_da_comunidade.edicao.models import *
import datetime
from amigos_da_comunidade.accounts.models import *

class Setor(AuditModel):

    nome_setor = models.CharField('Nome do Setor', blank=False, null=False, max_length=255)
    edicao = models.ForeignKey(Edicao, verbose_name='Edição', blank=True, null=True, on_delete=models.DO_NOTHING)
    membros = models.ManyToManyField(User,related_name='editions', verbose_name='Voluntários', blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('atendimento:setor_list')

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        ordering = ['-created_on']



class Triagem(AuditModel):

    edicao = models.ForeignKey(Edicao, verbose_name='Edição', blank=True, null=True, on_delete=models.DO_NOTHING)
    membros = models.ManyToManyField(User,related_name='membros', verbose_name='Membros da Triagem', blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('atendimento:triagem_list')

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = 'Setores'
        ordering = ['-created_on']