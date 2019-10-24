# -*- coding: utf-8 -*-

import re 
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.urls import reverse
from easy_thumbnails.fields import ThumbnailerImageField


class AuditModel(models.Model):

    created_on = models.DateTimeField('Criado em', auto_now_add=True)
    updated_on = models.DateTimeField('Autalizado em', auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, PermissionsMixin, AuditModel):

    username  = models.CharField('Usuário', max_length=100, blank=False, null=False, unique=True)
    name = models.CharField('Nome', max_length=100, blank=False, null=False)
    email = models.EmailField('E-mail', unique=True, blank=False, null=False)
    is_superuser = models.BooleanField('Super-Usuário', default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = ((MALE, 'Masculino'), (FEMALE, 'Feminino'),)
    sex = models.CharField('Sexo', max_length=1, choices=SEX_CHOICES, default=FEMALE)

    phone = models.CharField('Celular', max_length=16, blank=True, null=True)
    
    avatar = ThumbnailerImageField(
        upload_to="avatar",
        blank=True,
        resize_source=dict(size=(215, 215), crop=True)
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['name']

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]


