from django import template
from django.shortcuts import get_object_or_404
from jdatetime import timedelta
from jdatetime import datetime as JDATETIMETOOL

register = template.Library()


from session.models import SessionModel

@register.filter(name='session_end')
def session_end(value):
    session = get_object_or_404(SessionModel,pk=value)
    duration = JDATETIMETOOL.strptime(session.duration,'%H:%M')
    session_end = duration + timedelta(hours = session.time.hour,
                                                    minutes = session.time.minute)
    if session_end.minute == 0:
        session_end_str = str(session_end.hour)+':'+str(session_end.minute)+'0'
    else:
        session_end_str = str(session_end.hour)+':'+str(session_end.minute)

    return session_end_str


@register.filter(name='the_past_day')
def the_past_day(value):
    day = value + timedelta(days=-1)
    return day

@register.filter(name='only_day')
def only_day(value):
    values = value.split('-')
    day = values[2]
    return day


@register.filter(name='cutbr')
def cutbr(value):
    value = value.replace('-br','')
    return value


@register.filter(name='only_month')
def only_month(value):
    values = value.split('-')
    month = values[1]
    if month == '1' :
        month = 'فروردین'
    if month == '2' :
        month = 'اردیبهشت'
    if month == '3' :
        month = 'خرداد'
    if month == '4' :
        month = 'تیر'
    if month == '5' :
        month = 'مرداد'
    if month == '6' :
        month = 'شهریور'
    if month == '7' :
        month = 'مهر'
    if month == '8' :
        month = 'آبان'
    if month == '9' :
        month = 'آذر'
    if month == '10' :
        month = 'دی'
    if month == '11' :
        month = 'بهمن'
    if month == '12' :
        month = 'اسفند'
    return month


@register.filter(name='only_year')
def only_year(value):
    values = value.split('-')
    year = values[0]
    return year
