from django.db import models

class AuditModel(models.Model):
	created_on = models.DateTimeField('Criado em', auto_now_add=True)
	updated_on = models.DateTimeField('Autalizado em', auto_now=True)

	class Meta:
		abstract=True


class Permissao(AuditModel):
	
	nome = models.CharField('Nome do usuário', max_length=100, blank=False, null=False)

	def __str__(self):
		return self.nome

	def get_absolute_url(self):
		return reverse('usuarios:permissao_list')

	class Meta:
		verbose_name = 'Permissao'
		verbose_name_plural = 'Permissoes'
		ordering = ['-created_on']
