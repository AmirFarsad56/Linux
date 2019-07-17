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
from session.forms import (DaysForm, TimesForm, PriceForm, SessionDeleteForm, DaysForm_2)
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
                print('333333333333333')
                print(first_day)

            else:
                if lastdata_instance.first_day_2:
                    first_day = lastdata_instance.first_day_2
                    print('222222222222222')
                else:
                    first_day = jdatetime.datetime.now().date()
                    print('1111111111111111')
                print(first_day)
                last_day_str = days_form.cleaned_data['last_day']
                last_day_list = last_day_str.split('-')
                last_day = jdatetime.date(int(last_day_list[0]),int(last_day_list[1]),int(last_day_list[2]))
                length = last_day - first_day
                length = length.days
                print(first_day,';;;;;;;;;;')
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
    return render(request, 'session/categories.html',
                {'categories':sessioncategory_instances,'salon':salon})


@login_required
@sportclub_required
def SetPriceView(request,pk):
    if request.method == "POST":
        checks = request.POST.getlist('checks')
        days = request.POST.getlist('days')
        price_form = PriceForm(data = request.POST )
        if price_form.is_valid():
            range_start_str = price_form.cleaned_data['range_start']
            range_start_list = range_start_str.split('-')
            range_start = jdatetime.date(int(range_start_list[0]),int(range_start_list[1]),int(range_start_list[2]))
            range_end_str = price_form.cleaned_data['range_end']
            range_end_list = range_end_str.split('-')
            range_end = jdatetime.date(int(range_end_list[0]),int(range_end_list[1]),int(range_end_list[2]))
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
    sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
    if request.method == "POST":
        checks = request.POST.getlist('checks')
        days = request.POST.getlist('days')
        form = SessionDeleteForm(data = request.POST )
        if form.is_valid():
            range_start_str = form.cleaned_data['range_start']
            range_start_list = range_start_str.split('-')
            range_start = jdatetime.date(int(range_start_list[0]),int(range_start_list[1]),int(range_start_list[2]))
            range_end_str = form.cleaned_data['range_end']
            range_end_list = range_end_str.split('-')
            range_end = jdatetime.date(int(range_end_list[0]),int(range_end_list[1]),int(range_end_list[2]))
            sessions = sessioncategory_instance.sessions.all()
            ##########
            session_category_1 = SessionCategoryModel.objects.create(salon=sessioncategory_instance.salon,
                                    range_start_day = sessioncategory_instance.range_start_day,
                                    range_end_day = range_start+timedelta(days=-1))
            session_category_1.save()
            session_category_2 = SessionCategoryModel.objects.create(salon=sessioncategory_instance.salon,
                                    range_start_day = range_end+timedelta(days=1),
                                    range_end_day = sessioncategory_instance.range_end_day)
            session_category_2.save()
            session_category_3 = SessionCategoryModel.objects.create(salon=sessioncategory_instance.salon,
                                    range_start_day = range_start,
                                    range_end_day = range_end)
            session_category_3.save()
            ###########
            for session in sessions:
                x1 = session.day - range_start
                x2 = session.day - range_end
                x3 = session.day - sessioncategory_instance.range_start_day
                x4 = session.day - sessioncategory_instance.range_end_day
                if int(x3.days) >= 0 and int(x1.days) < 0 :
                    session.session_category = session_category_1
                    session.save()
                if int(x1.days) >= 0 and int(x2.days) <= 0 :
                    if str(session.day.weekday()) in days:
                        for check in checks:
                            check_time = DATETIMETOOL.strptime(check,'%H:%M')
                            check_time = check_time.time()
                            if session.time.minute - check_time.minute == 0 and session.time.hour - check_time.hour == 0:
                                session.delete()
                if int(x2.days) > 0 and int(x4.days) <= 0 :
                    session.session_category = session_category_2
                    session.save()
            #for reverse
            salon_pk = sessioncategory_instance.salon.pk
            sessioncategory_instance.delete()
            return HttpResponseRedirect(reverse('session:categories',
                                                kwargs={'pk':salon_pk}))
        else:
            print(form.errors)

    else:
        form = SessionDeleteForm()
        list = sessioncategory_instance.sessions.all()
        obj = list[0]
        session_instances = get_list_or_404(SessionModel,day = obj.day,
                                            session_category = sessioncategory_instance)
    return render(request,'session/sessiondelete.html',{'sessions':session_instances,
                  'session_category':sessioncategory_instance,'form':form})


@login_required
@sportclub_required
def SessionCreateView_2(request,pk):
    salon_instance = get_object_or_404(SalonModel, pk = pk)

    if request.method == 'POST':
        selected_days = request.POST.getlist('selected_days')
        days_form_2 = DaysForm_2(data = request.POST )
        times_form = TimesForm(data = request.POST )
        if times_form.is_valid() and days_form_2.is_valid():

            first_day_str = days_form_2.cleaned_data['first_day']
            first_day_list = first_day_str.split('-')
            first_day = jdatetime.date(int(first_day_list[0]),int(first_day_list[1]),int(first_day_list[2]))
            #last_day is treating as final day (last_day is sessioning :) )
            last_day_str = days_form_2.cleaned_data['last_day']
            last_day_list = last_day_str.split('-')
            last_day = jdatetime.date(int(last_day_list[0]),int(last_day_list[1]),int(last_day_list[2]))


            last_data_instance = salon_instance.lastdatas.all()
            if not last_data_instance[0].first_day_2:
                return HttpResponseRedirect(reverse('session:boundaryerror'))
            if last_day >= last_data_instance[0].first_day_2:
                return HttpResponseRedirect(reverse('session:boundaryerror'))
            start_time = times_form.cleaned_data['start_time']
            duration = times_form.cleaned_data['duration']
            stop_time = times_form.cleaned_data['stop_time']

            jstart_time = JDATETIMETOOL.strptime(str(start_time),'%H:%M')
            jstop_time = JDATETIMETOOL.strptime(str(stop_time),'%H:%M')
            #Checking interferences in sessions we want to create
            existing_sessions = salon_instance.sessions.all()

            for existing_session in existing_sessions:
                x1 = existing_session.day - first_day
                x2 = existing_session.day - last_day
                if int(x1.days) >= 0 and int(x2.days) <= 0 :
                    if str(existing_session.day.weekday()) in selected_days:
                        existing_duration = JDATETIMETOOL.strptime(existing_session.duration,'%H:%M')
                        time_var = existing_duration + timedelta(hours = existing_session.time.hour,
                                                                        minutes = existing_session.time.minute)
                        try:
                            if time_var > ceil :
                                ceil = time_var
                                interferenced_session_pk =  existing_session.pk
                        except:
                            ceil = existing_duration +  timedelta(hours = existing_session.time.hour,
                                                                            minutes = existing_session.time.minute)
                            interferenced_session_pk =  existing_session.pk
                        try:
                            if JDATETIMETOOL.strptime(str(existing_session.time),'%H:%M') < floor:
                                floor = existing_session.time
                                interferenced_session_pk =  existing_session.pk

                        except:
                            floor = JDATETIMETOOL.strptime(str(existing_session.time),'%H:%M')
                            interferenced_session_pk =  existing_session.pk

            try:
                if jstart_time < ceil and jstop_time > floor:
                    return HttpResponseRedirect(reverse('session:interferenceerror',
                                                    kwargs={'pk':interferenced_session_pk}))
            except:
                pass

            #Creating the SessionCategory Instance
            session_category = SessionCategoryModel.objects.create(salon=salon_instance,
                                    range_start_day = first_day, range_end_day = last_day)

            if 0 in selected_days:
                session_category.saturdays = True
                session_category.save()
            if 1 in selected_days:
                session_category.sundays = True
                session_category.save()
            if 2 in selected_days:
                session_category.mondays = True
                session_category.save()
            if 3 in selected_days:
                session_category.tuesdays = True
                session_category.save()
            if 4 in selected_days:
                session_category.wednesdays = True
                session_category.save()
            if 5 in selected_days:
                session_category.thursdays = True
                session_category.save()
            if 6 in selected_days:
                session_category.fridays = True
                session_category.save()


            #creating sessions
            x = int(( TotalMinutes(stop_time) - TotalMinutes(start_time) ) / TotalMinutes(duration))
            day = first_day
            while True:
                if str(day.weekday()) in selected_days:
                    for i in range(x):
                        total_minutes = TotalMinutes(start_time) + i*TotalMinutes(duration)
                        hours = int(total_minutes/60)
                        minutes = total_minutes - (hours * 60)
                        time = str(hours)+':'+str(minutes)

                        session = SessionModel.objects.create(salon=salon_instance, duration=duration, session_category = session_category,
                                                    day = day, time = time)
                        session.save()
                day = day + timedelta(days = 1)
                if day > last_day:
                    break

            return HttpResponseRedirect(reverse('salon:salondetail',
                                            kwargs={'pk':pk}))
        else:
            print(times_form.errors)
            return HttpResponseRedirect(reverse('salon:salondetail',
                                            kwargs={'pk':pk}))
    else:
        days_form_2 = DaysForm_2
        times_form = TimesForm()
        last_data_instance = get_object_or_404(LastDataModel,salon = salon_instance)
        return render(request,'session/sessioncreate_2.html',
                              {'times_form':times_form,
                              'last_data':last_data_instance,'days_form':days_form_2})


def InterferenceErrorView(request,pk):
    session_instance = get_object_or_404(SessionModel,pk = pk)
    return render(request,'session/interferenceerror.html',{'session':session_instance})


class BoundaryErrorView(TemplateView):
    template_name = 'session/boundaryerror.html'
