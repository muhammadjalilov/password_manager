from django.db import models


class PasswordManage(models.Model):
    site_name = models.CharField(max_length=255, verbose_name='Site Name')
    username = models.CharField(max_length=255, verbose_name='Username')
    password = models.CharField(max_length=255, verbose_name='Password')
    account = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, verbose_name='Account')

    def __str__(self):
        return self.site_name
