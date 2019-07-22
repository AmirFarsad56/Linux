from django.db import models
from django_jalali.db import models as jmodels
from salon.models import SalonModel
from django.utils.text import slugify
from django.conf import settings
from jdatetime import timedelta


class SessionCategoryModel(models.Model):
    salon = models.ForeignKey(SalonModel, on_delete = models.CASCADE,
                              related_name = 'sessioncategories', blank = False,
                              null = False)
    saturdays = models.BooleanField(default = False)
    sundays = models.BooleanField(default = False)
    mondays = models.BooleanField(default = False)
    tuesdays = models.BooleanField(default = False)
    wednesdays = models.BooleanField(default = False)
    thursdays = models.BooleanField(default = False)
    fridays = models.BooleanField(default = False)
    range_start_day = jmodels.jDateField(null = False, blank = False)
    range_end_day = jmodels.jDateField(null = False, blank = False)
    is_closed = models.BooleanField(null = False, default = False)


class SessionModel(models.Model):
    salon = models.ForeignKey(SalonModel, on_delete = models.CASCADE,
                                  related_name = 'sessions',blank = False,
                                  null = False)
    booker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,
                               related_name='sessions', blank = True, null = True)
    session_category = models.ForeignKey(SessionCategoryModel, on_delete = models.CASCADE,
                                  related_name = 'sessions',blank = False,
                                  null = False)
    day = jmodels.jDateField(null = True)
    time = models.TimeField(null = True)
    duration = models.CharField(max_length = 264, blank = False , null = False)
    price = models.IntegerField(blank = True, null = True)
    is_booked = models.BooleanField(blank = False, default = False)
    is_ready = models.BooleanField(blank = False, default = False)


class LastDataModel(models.Model):
    salon = models.ForeignKey(SalonModel, on_delete = models.CASCADE,
                              related_name = 'lastdatas', blank = False,
                              null = False)
    last_length = models.IntegerField(null = True, blank = True)
    first_day = jmodels.jDateField(null = True, blank = True)
    first_day_2 = jmodels.jDateField(null = True, blank = True)
    last_day = jmodels.jDateField(null = True, blank = True)
    last_saturday = models.BooleanField(default = False)
    last_sunday = models.BooleanField(default = False)
    last_monday = models.BooleanField(default = False)
    last_tuesday = models.BooleanField(default = False)
    last_wednesday = models.BooleanField(default = False)
    last_thursday = models.BooleanField(default = False)
    last_friday = models.BooleanField(default = False)

    def save(self, *args, **kwargs):
        if self.last_saturday and self.last_sunday and self.last_monday and self.last_tuesday and self.last_wednesday and self.last_thursday and self.last_friday:
            self.first_day_2 = self.last_day + timedelta(days = 1)
            self.first_day = None
            self.last_day = None
            self.last_length = None
            self.last_saturday = False
            self.last_sunday = False
            self.last_monday = False
            self.last_tuesday = False
            self.last_wednesday = False
            self.last_thursday = False
            self.last_friday = False
        super(LastDataModel, self).save(*args, **kwargs)
