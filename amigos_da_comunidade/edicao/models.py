from django.db import models
from django.urls import reverse  
import datetime
class AuditModel(models.Model):
	created_on = models.DateTimeField('Criado em', auto_now_add=True)
	updated_on = models.DateTimeField('Autalizado em', auto_now=True)

	class Meta:
		abstract=True 


class Edicao(AuditModel):
    
    nome_edicao = models.CharField('Nome da edição', max_length=200, blank=False, null=False)
    data_inicio = models.DateField("Data de Inicio da Edição", default=datetime.date.today)
    data_fim = models.DateField("Data Final da Edição")
    local = models.CharField('Local da Edição', max_length=200, blank=False, null=False)
    imagem_logo = models.FileField('Logo(png,jpeg,jpg..)', blank=True, null=True, upload_to='uploads/%Y/%m/%d/')
    ativo = models.BooleanField('Ativo' , default=True,blank=False, null=False)
    # logo = models.FileField('/uploads')

    def __str__(self):
        return self.nome_edicao

    def get_absolute_url(self):
        return reverse('edicao:edicao_list')

    class Meta:
        verbose_name = 'Edicao'
        verbose_name_plural = 'Edicoes'
        ordering = ['-data_inicio'] 



