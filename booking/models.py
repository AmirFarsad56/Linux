from django.db import models
from django.conf import settings
from django_jalali.db import models as jmodels
import jdatetime

#handmade
from session.models import SessionModel


class ProfitPercentageModel(models.Model):
    profit_percentage = models.IntegerField(null = False , default = 0)

class BookingModel(models.Model):
    session = models.ForeignKey(SessionModel, on_delete = models.PROTECT , null = False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True)
    date = jmodels.jDateTimeField(null = False)
    price = models.IntegerField(null = False)
    profit_percantage = models.IntegerField(null = False)

    def __str__(self):
        return str(user.username)
