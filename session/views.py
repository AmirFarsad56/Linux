from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView
from django.shortcuts import get_object_or_404, get_list_or_404
from jdatetime import date, timedelta
from jdatetime import datetime as JDATETIMETOOL
from datetime import datetime as DATETIMETOOL
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import jdatetime
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

#handmade
from session.forms import DaysForm, TimesForm, PriceForm, SessionDeleteForm
from session.models import (SessionModel, LastDataModel, SessionCategoryModel)
from salon.models import SalonModel
from sportclub.decorators import sportclub_required
from session.datetimetools import (AllSaturdays, AllSundays, AllMondays,
                                AllTuesdays, AllWednesdays, AllThursdays,
                                AllFridays, TotalMinutes)


@login_required
@sportclub_required
def SessionCreateView(request, pk):
    salon_instance = get_object_or_404(SalonModel, pk = pk)
    try:
        lastdata_instance = get_object_or_404(LastDataModel, salon = salon_instance)
    except:
        lastdata_instance = LastDataModel.objects.create(salon=salon_instance)
    if request.method == 'POST':
        days_form = DaysForm(data = request.POST )
        times_form = TimesForm(data = request.POST )
        if times_form.is_valid() and days_form.is_valid():
            if lastdata_instance.last_length:
                length = lastdata_instance.last_length
                first_day = lastdata_instance.first_day
                last_day = lastdata_instance.last_day

            else:
                if lastdata_instance.first_day_2:
                    first_day = lastdata_instance.first_day_2
                else:
                    first_day = jdatetime.datetime.now().date()
                last_day = days_form.cleaned_data['last_day']
                last_day = jdatetime.date(last_day.year,last_day.month,last_day.day)
                length = last_day - first_day
                length = length.days
            if length < 6 :
                return HttpResponseRedirect(reverse('session:lengtherror'))

            saturdays = days_form.cleaned_data['saturdays']
            sundays = days_form.cleaned_data['sundays']
            mondays = days_form.cleaned_data['mondays']
            tuesdays = days_form.cleaned_data['tuesdays']
            wednesdays = days_form.cleaned_data['wednesdays']
            thursdays = days_form.cleaned_data['thursdays']
            fridays = days_form.cleaned_data['fridays']
            start_time = times_form.cleaned_data['start_time']
            duration = times_form.cleaned_data['duration']
            stop_time = times_form.cleaned_data['stop_time']

            x = int(( TotalMinutes(stop_time) - TotalMinutes(start_time) ) / TotalMinutes(duration))

            #Creating the SessionCategory Instance
            session_category = SessionCategoryModel.objects.create(salon=salon_instance,
                                    range_start_day = first_day, range_end_day = last_day)

            if saturdays:
                session_category.saturdays = True
                session_category.save()
                if lastdata_instance.last_saturday_2:
                    begining_day = lastdata_instance.last_saturday_2 + timedelta(days=1)
                else:
                    begining_day = jdatetime.datetime.now()
                goal_num = len(list(AllSaturdays(length, begining_day)))
                counter_1 = 0
                for days in AllSaturdays(length, begining_day):
                    if days <= last_day :
                        counter_1 += 1
                        for i in range(x):
                            total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                            hours = int(total_minutes/60)
                            minutes = total_minutes - (hours * 60)
                            time = str(hours)+':'+str(minutes)

                            session = SessionModel.objects.create(salon=salon_instance, duration=duration, session_category = session_category,
                                                        day = str(days), time = time)
                            session.save()
                        if counter_1 == goal_num:
                            first_day = jdatetime.date(first_day.year,first_day.month,first_day.day)
                            last_day = jdatetime.date(last_day.year,last_day.month,last_day.day)
                            lastdata_instance.first_day = first_day
                            lastdata_instance.last_day = last_day
                            lastdata_instance.last_length = length
                            lastdata_instance.last_saturday = days
                            lastdata_instance.save()

            if sundays:
                session_category.sundays = True
                session_category.save()
                if lastdata_instance.last_sunday_2:
                    begining_day = lastdata_instance.last_sunday_2 + timedelta(days=1)
                else:
                    begining_day = jdatetime.datetime.now()
                goal_num = len(list(AllSundays(length, begining_day)))
                counter_1 = 0
                for days in AllSundays(length, begining_day):
                    if days <= last_day :
                        counter_1 += 1
                        for i in range(x):
                            total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                            hours = int(total_minutes/60)
                            minutes = total_minutes - (hours * 60)
                            time = str(hours)+':'+str(minutes)

                            session = SessionModel.objects.create(salon=salon_instance, duration=duration, session_category = session_category,
                                                        day = str(days), time = time)
                            session.save()
                        if counter_1 == goal_num:
                            first_day = jdatetime.date(first_day.year,first_day.month,first_day.day)
                            last_day = jdatetime.date(last_day.year,last_day.month,last_day.day)
                            lastdata_instance.first_day = first_day
                            lastdata_instance.last_day = last_day
                            lastdata_instance.last_length = length
                            lastdata_instance.last_sunday = days
                            lastdata_instance.save()
            if mondays:
                session_category.mondays = True
                session_category.save()
                if lastdata_instance.last_monday_2:
                    begining_day = lastdata_instance.last_monday_2 + timedelta(days=1)
                else:
                    begining_day = jdatetime.datetime.now()
                goal_num = len(list(AllMondays(length, begining_day)))
                counter_1 = 0
                for days in AllMondays(length, begining_day):
                    if days <= last_day :
                        counter_1 += 1
                        for i in range(x):
                            total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                            hours = int(total_minutes/60)
                            minutes = total_minutes - (hours * 60)
                            time = str(hours)+':'+str(minutes)

                            session = SessionModel.objects.create(salon=salon_instance, duration=duration, session_category = session_category,
                                                        day = str(days), time = time)
                            session.save()
                        if counter_1 == goal_num:
                            first_day = jdatetime.date(first_day.year,first_day.month,first_day.day)
                            last_day = jdatetime.date(last_day.year,last_day.month,last_day.day)
                            lastdata_instance.first_day = first_day
                            lastdata_instance.last_day = last_day
                            lastdata_instance.last_length = length
                            lastdata_instance.last_monday = days
                            lastdata_instance.save()
            if tuesdays:
                session_category.tuesdays = True
                session_category.save()
                if lastdata_instance.last_tuesday_2:
                    begining_day = lastdata_instance.last_tuesday_2 + timedelta(days=1)
                else:
                    begining_day = jdatetime.datetime.now()
                goal_num = len(list(AllTuesdays(length, begining_day)))
                counter_1 = 0
                for days in AllTuesdays(length, begining_day):
                    if days <= last_day :
                        counter_1 += 1
                        for i in range(x):
                            total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                            hours = int(total_minutes/60)
                            minutes = total_minutes - (hours * 60)
                            time = str(hours)+':'+str(minutes)

                            session = SessionModel.objects.create(salon=salon_instance, duration=duration, session_category = session_category,
                                                        day = str(days), time = time)
                            session.save()
                        if counter_1 == goal_num:
                            first_day = jdatetime.date(first_day.year,first_day.month,first_day.day)
                            last_day = jdatetime.date(last_day.year,last_day.month,last_day.day)
                            lastdata_instance.first_day = first_day
                            lastdata_instance.last_day = last_day
                            lastdata_instance.last_length = length
                            lastdata_instance.last_tuesday = days
                            lastdata_instance.save()
            if wednesdays:
                session_category.wednesdays = True
                session_category.save()
                if lastdata_instance.last_wednesday_2:
                    begining_day = lastdata_instance.last_wednesday_2 + timedelta(days=1)
                else:
                    begining_day = jdatetime.datetime.now()
                goal_num = len(list(AllWednesdays(length, begining_day)))
                counter_1 = 0
                for days in AllWednesdays(length, begining_day):
                    if days <= last_day :
                        counter_1 += 1
                        for i in range(x):
                            total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                            hours = int(total_minutes/60)
                            minutes = total_minutes - (hours * 60)
                            time = str(hours)+':'+str(minutes)

                            session = SessionModel.objects.create(salon=salon_instance, duration=duration, session_category = session_category,
                                                        day = str(days), time = time)
                            session.save()
                        if counter_1 == goal_num:
                            first_day = jdatetime.date(first_day.year,first_day.month,first_day.day)
                            last_day = jdatetime.date(last_day.year,last_day.month,last_day.day)
                            lastdata_instance.first_day = first_day
                            lastdata_instance.last_day = last_day
                            lastdata_instance.last_length = length
                            lastdata_instance.last_wednesday = days
                            lastdata_instance.save()
            if thursdays:
                session_category.thursdays = True
                session_category.save()
                if lastdata_instance.last_thursday_2:
                    begining_day = lastdata_instance.last_thursday_2 + timedelta(days=1)
                else:
                    begining_day = jdatetime.datetime.now()
                goal_num = len(list(AllThursdays(length, begining_day)))
                counter_1 = 0
                for days in AllThursdays(length, begining_day):
                    if days <= last_day :
                        counter_1 += 1
                        for i in range(x):
                            total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                            hours = int(total_minutes/60)
                            minutes = total_minutes - (hours * 60)
                            time = str(hours)+':'+str(minutes)

                            session = SessionModel.objects.create(salon=salon_instance, duration=duration, session_category = session_category,
                                                        day = str(days), time = time)
                            session.save()
                        if counter_1 == goal_num:
                            first_day = jdatetime.date(first_day.year,first_day.month,first_day.day)
                            last_day = jdatetime.date(last_day.year,last_day.month,last_day.day)
                            lastdata_instance.first_day = first_day
                            lastdata_instance.last_day = last_day
                            lastdata_instance.last_length = length
                            lastdata_instance.last_thursday = days
                            lastdata_instance.save()
            if fridays:
                session_category.fridays = True
                session_category.save()
                if lastdata_instance.last_friday_2:
                    begining_day = lastdata_instance.last_friday_2  + timedelta(days=1)
                else:
                    begining_day = jdatetime.datetime.now()
                goal_num = len(list(AllFridays(length, begining_day)))
                counter_1 = 0
                for days in AllFridays(length, begining_day):
                    if days <= last_day :
                        counter_1 += 1
                        for i in range(x):
                            total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                            hours = int(total_minutes/60)
                            minutes = total_minutes - (hours * 60)
                            time = str(hours)+':'+str(minutes)

                            session = SessionModel.objects.create(salon=salon_instance, duration=duration, session_category = session_category,
                                                        day = str(days), time = time)
                            session.save()
                        if counter_1 == goal_num:
                            first_day = jdatetime.date(first_day.year,first_day.month,first_day.day)
                            last_day = jdatetime.date(last_day.year,last_day.month,last_day.day)
                            lastdata_instance.first_day = first_day
                            lastdata_instance.last_day = last_day
                            lastdata_instance.last_length = length
                            lastdata_instance.last_friday = days
                            lastdata_instance.save()
            return HttpResponseRedirect(reverse('salon:salondetail',
                                            kwargs={'pk':pk}))
            session_category.range_finish_day = last_day
            session_category.save()
        else:
            print(days_form.errors)
            print(times_form.errors)
            return HttpResponseRedirect(reverse('salon:salondetail',
                                            kwargs={'pk':pk}))
    else:
        days_form = DaysForm()
        times_form = TimesForm()
        return render(request,'session/createsession.html',
                              {'days_form':days_form,
                              'times_form':times_form,
                              'lastdata_instance':lastdata_instance,})


@login_required
@sportclub_required
def SessionListView(request,pk):
    salon = get_object_or_404(SalonModel,pk = pk)
    sessions = get_list_or_404(SessionModel.objects.order_by('day'), salon = salon)
    return render(request,'session/sessionlist.html',
                  {'sessions':sessions,
                   'salon':salon})


class LengthError(TemplateView):
    template_name = 'session/lengtherror.html'


@login_required
@sportclub_required
def SessionCategoriesView(request,pk):
    salon = get_object_or_404(SalonModel,pk = pk)
    sessioncategory_instances = get_list_or_404(SessionCategoryModel, salon = salon)
    return render(request, 'session/categories.html',{'categories':sessioncategory_instances})


@login_required
@sportclub_required
def SetPriceView(request,pk):
    if request.method == "POST":
        checks = request.POST.getlist('checks')
        days = request.POST.getlist('days')
        price_form = PriceForm(data = request.POST )
        if price_form.is_valid():
            range_start = price_form.cleaned_data['range_start']
            range_start = jdatetime.date(range_start.year,range_start.month,range_start.day)
            range_end = price_form.cleaned_data['range_end']
            range_end = jdatetime.date(range_end.year,range_end.month,range_end.day)
            price = price_form.cleaned_data['price']
            sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
            sessions = sessioncategory_instance.sessions.all()
            for session in sessions:
                x1 = session.day - range_start
                x2 = session.day - range_end
                if int(x1.days) >= 0 and int(x2.days) <= 0 :
                    if str(session.day.weekday()) in days:
                        for check in checks:
                            check_time = DATETIMETOOL.strptime(check,'%H:%M')
                            check_time = check_time.time()
                            if session.time.minute - check_time.minute == 0 and session.time.hour - check_time.hour == 0:
                                session.price = price
                                session.save()
            #for reverse
            salon_pk = sessioncategory_instance.salon.pk
            return HttpResponseRedirect(reverse('session:categories',
                                                kwargs={'pk':salon_pk}))

    else:
        price_form = PriceForm()
        sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
        list = sessioncategory_instance.sessions.all()
        obj = list[0]
        session_instances = get_list_or_404(SessionModel,day = obj.day,
                                            session_category = sessioncategory_instance)
    return render(request,'session/setprice.html',{'sessions':session_instances,
                  'session_category':sessioncategory_instance,'form':price_form})


def CategorizedSessionListView(request,pk):
    sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
    sessions = sessioncategory_instance.sessions.order_by('day')
    return render(request,'session/categorizedsessionlist.html',{'sessions':sessions,
                  'session_category':sessioncategory_instance})


@method_decorator([login_required, sportclub_required], name='dispatch')
class SessionUpdateView(UpdateView):
    model = SessionModel
    fields = ['is_ready','price',]
    template_name = 'session/sessionupdate.html'

    def get_queryset(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(SessionModel,pk = pk)
        if obj.salon.sportclub.user == self.request.user:
            return self.model._default_manager.all()

    def get_success_url(self):
        pk = self.object.session_category.pk
        return reverse('session:categorizedsessions', kwargs={'pk':pk})



@login_required
@sportclub_required
def SessionDeleteView(request,pk):
    if request.method == "POST":
        checks = request.POST.getlist('checks')
        days = request.POST.getlist('days')
        form = SessionDeleteForm(data = request.POST )
        if form.is_valid():
            range_start = form.cleaned_data['range_start']
            range_start = jdatetime.date(range_start.year,range_start.month,range_start.day)
            range_end = form.cleaned_data['range_end']
            range_end = jdatetime.date(range_end.year,range_end.month,range_end.day)
            sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
            sessions = sessioncategory_instance.sessions.all()
            for session in sessions:
                x1 = session.day - range_start
                x2 = session.day - range_end
                if int(x1.days) >= 0 and int(x2.days) <= 0 :
                    if str(session.day.weekday()) in days:
                        for check in checks:
                            check_time = DATETIMETOOL.strptime(check,'%H:%M')
                            check_time = check_time.time()
                            if session.time.minute - check_time.minute == 0 and session.time.hour - check_time.hour == 0:
                                session.delete()
            #for reverse
            salon_pk = sessioncategory_instance.salon.pk
            return HttpResponseRedirect(reverse('session:categories',
                                                kwargs={'pk':salon_pk}))

    else:
        form = SessionDeleteForm()
        sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
        list = sessioncategory_instance.sessions.all()
        obj = list[0]
        session_instances = get_list_or_404(SessionModel,day = obj.day,
                                            session_category = sessioncategory_instance)
    return render(request,'session/setprice.html',{'sessions':session_instances,
                  'session_category':sessioncategory_instance,'form':form})
