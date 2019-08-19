from django.db import models

class TermsModel(models.Model):
    terms_condition = models.TextField(null = False)
