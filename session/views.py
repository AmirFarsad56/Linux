from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
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
from session.forms import (DaysForm, TimesForm, PriceForm, SessionDeleteForm,
                            DaysForm_2, LastDataSetForm, DiscountPercentageForm,
                            StatusForm,)
from session.models import (SessionModel, LastDataModel, SessionCategoryModel)
from salon.models import SalonModel
from sportclub.decorators import sportclub_required
from session.datetimetools import (AllSaturdays, AllSundays, AllMondays,
                                AllTuesdays, AllWednesdays, AllThursdays,
                                AllFridays, TotalMinutes)




@login_required
@sportclub_required
def SessionWorkSpaceView(request,pk):
    salon = get_object_or_404(SalonModel,pk = pk)
    if request.user == salon.sportclub.user:
        ### creating days

        from jdatetime import date as jdate
        ##################################################################################################### 0
        now = jdatetime.datetime.now()
        if now.month == 12:
            month_length =  (jdate(now.year+1, 1, 1) - jdate(now.year, 12, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
            this_date = str(now.year)+'-12-'
            next_date = str(now.year+1)+'-1-'
            prev_date = str(now.year)+'-11-'
        elif now.month == 1:
            month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year-1, 12, 1)).days
            this_date = str(now.year)+'-1-'
            next_date = str(now.year)+'-2-'
            prev_date = str(now.year-1)+'-12-'
        else:
            month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
            this_date = str(now.year)+'-'+str(now.month)+'-'
            next_date = str(now.year)+'-'+str(now.month+1)+'-'
            prev_date = str(now.year)+'-'+str(now.month-1)+'-'

        first_day_of_month_weekday = jdate(now.year, now.month, 1).weekday()
        array = [0,]
        days_1 = [0,]
        if (month_length == 30 and first_day_of_month_weekday == 6) or (month_length == 31 and first_day_of_month_weekday >=5):
            for i in range(41):
                array.append(0)
                days_1.append(0)
        else:
            for i in range(34):
                array.append(0)
                days_1.append(0)


        for i in range(first_day_of_month_weekday):
            array[first_day_of_month_weekday-i-1] = prev_date + '' #str(previous_month_length - i)

        for i in range(month_length):
            array[first_day_of_month_weekday+i] = this_date + str(i + 1)

        for i in range(len(array) - array.index(0)):
            array[array.index(0)] = next_date+ '' #str(i+1)
        for i in range(len(array)):
            days_1[i] = array[(int(i/7)+1)*7-1-(i-int(i/7)*7)]
        for i in range(len(days_1)):
            if int((i)/7) == ((i)/7):
                days_1[i] = days_1[i]+'-br'
        ##################################################################################################### 1
        now = jdate(now.year,now.month,15)+timedelta(days=30)


        if now.month == 12:
            month_length =  (jdate(now.year+1, 1, 1) - jdate(now.year, 12, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
            this_date = str(now.year)+'-12-'
            next_date = str(now.year+1)+'-1-'
            prev_date = str(now.year)+'-11-'
        elif now.month == 1:
            month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year-1, 12, 1)).days
            this_date = str(now.year)+'-1-'
            next_date = str(now.year)+'-2-'
            prev_date = str(now.year-1)+'-12-'
        else:
            month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
            this_date = str(now.year)+'-'+str(now.month)+'-'
            next_date = str(now.year)+'-'+str(now.month+1)+'-'
            prev_date = str(now.year)+'-'+str(now.month-1)+'-'

        first_day_of_month_weekday = jdate(now.year, now.month, 1).weekday()
        array = [0,]
        days_2 = [0,]
        if (month_length == 30 and first_day_of_month_weekday == 6) or (month_length == 31 and first_day_of_month_weekday >=5):
            for i in range(41):
                array.append(0)
                days_2.append(0)
        else:
            for i in range(34):
                array.append(0)
                days_2.append(0)


        for i in range(first_day_of_month_weekday):
            array[first_day_of_month_weekday-i-1] = prev_date + '' #str(previous_month_length - i)

        for i in range(month_length):
            array[first_day_of_month_weekday+i] = this_date + str(i + 1)

        for i in range(len(array) - array.index(0)):
            array[array.index(0)] = next_date+ '' #str(i+1)
        for i in range(len(array)):
            days_2[i] = array[(int(i/7)+1)*7-1-(i-int(i/7)*7)]
        for i in range(len(days_2)):
            if int((i)/7) == ((i)/7):
                days_2[i] = days_2[i]+'-br'
        ##################################################################################################### 2
        now = jdate(now.year,now.month,15)+timedelta(days=30)


        if now.month == 12:
            month_length =  (jdate(now.year+1, 1, 1) - jdate(now.year, 12, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
            this_date = str(now.year)+'-12-'
            next_date = str(now.year+1)+'-1-'
            prev_date = str(now.year)+'-11-'
        elif now.month == 1:
            month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year-1, 12, 1)).days
            this_date = str(now.year)+'-1-'
            next_date = str(now.year)+'-2-'
            prev_date = str(now.year-1)+'-12-'
        else:
            month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
            this_date = str(now.year)+'-'+str(now.month)+'-'
            next_date = str(now.year)+'-'+str(now.month+1)+'-'
            prev_date = str(now.year)+'-'+str(now.month-1)+'-'

        first_day_of_month_weekday = jdate(now.year, now.month, 1).weekday()
        array = [0,]
        days_3 = [0,]
        if (month_length == 30 and first_day_of_month_weekday == 6) or (month_length == 31 and first_day_of_month_weekday >=5):
            for i in range(41):
                array.append(0)
                days_3.append(0)
        else:
            for i in range(34):
                array.append(0)
                days_3.append(0)


        for i in range(first_day_of_month_weekday):
            array[first_day_of_month_weekday-i-1] = prev_date + '' #str(previous_month_length - i)

        for i in range(month_length):
            array[first_day_of_month_weekday+i] = this_date + str(i + 1)

        for i in range(len(array) - array.index(0)):
            array[array.index(0)] = next_date+ '' #str(i+1)
        for i in range(len(array)):
            days_3[i] = array[(int(i/7)+1)*7-1-(i-int(i/7)*7)]
        for i in range(len(days_3)):
            if int((i)/7) == ((i)/7):
                days_3[i] = days_3[i]+'-br'

        ##################################################################################################### 1
        now = jdate(now.year,now.month,15)+timedelta(days=30)


        if now.month == 12:
            month_length =  (jdate(now.year+1, 1, 1) - jdate(now.year, 12, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
            this_date = str(now.year)+'-12-'
            next_date = str(now.year+1)+'-1-'
            prev_date = str(now.year)+'-11-'
        elif now.month == 1:
            month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year-1, 12, 1)).days
            this_date = str(now.year)+'-1-'
            next_date = str(now.year)+'-2-'
            prev_date = str(now.year-1)+'-12-'
        else:
            month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
            this_date = str(now.year)+'-'+str(now.month)+'-'
            next_date = str(now.year)+'-'+str(now.month+1)+'-'
            prev_date = str(now.year)+'-'+str(now.month-1)+'-'

        first_day_of_month_weekday = jdate(now.year, now.month, 1).weekday()
        array = [0,]
        days_4 = [0,]
        if (month_length == 30 and first_day_of_month_weekday == 6) or (month_length == 31 and first_day_of_month_weekday >=5):
            for i in range(41):
                array.append(0)
                days_4.append(0)
        else:
            for i in range(34):
                array.append(0)
                days_4.append(0)


        for i in range(first_day_of_month_weekday):
            array[first_day_of_month_weekday-i-1] = prev_date + '' #str(previous_month_length - i)

        for i in range(month_length):
            array[first_day_of_month_weekday+i] = this_date + str(i + 1)

        for i in range(len(array) - array.index(0)):
            array[array.index(0)] = next_date+ '' #str(i+1)
        for i in range(len(array)):
            days_4[i] = array[(int(i/7)+1)*7-1-(i-int(i/7)*7)]
        for i in range(len(days_4)):
            if int((i)/7) == ((i)/7):
                days_4[i] = days_4[i]+'-br'
        ##################################################################################################### 1
        now = jdate(now.year,now.month,15)+timedelta(days=30)


        if now.month == 12:
            month_length =  (jdate(now.year+1, 1, 1) - jdate(now.year, 12, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
            this_date = str(now.year)+'-12-'
            next_date = str(now.year+1)+'-1-'
            prev_date = str(now.year)+'-11-'
        elif now.month == 1:
            month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year-1, 12, 1)).days
            this_date = str(now.year)+'-1-'
            next_date = str(now.year)+'-2-'
            prev_date = str(now.year-1)+'-12-'
        else:
            month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
            this_date = str(now.year)+'-'+str(now.month)+'-'
            next_date = str(now.year)+'-'+str(now.month+1)+'-'
            prev_date = str(now.year)+'-'+str(now.month-1)+'-'

        first_day_of_month_weekday = jdate(now.year, now.month, 1).weekday()
        array = [0,]
        days_5 = [0,]
        if (month_length == 30 and first_day_of_month_weekday == 6) or (month_length == 31 and first_day_of_month_weekday >=5):
            for i in range(41):
                array.append(0)
                days_5.append(0)
        else:
            for i in range(34):
                array.append(0)
                days_5.append(0)


        for i in range(first_day_of_month_weekday):
            array[first_day_of_month_weekday-i-1] = prev_date + '' #str(previous_month_length - i)

        for i in range(month_length):
            array[first_day_of_month_weekday+i] = this_date + str(i + 1)

        for i in range(len(array) - array.index(0)):
            array[array.index(0)] = next_date+ '' #str(i+1)
        for i in range(len(array)):
            days_5[i] = array[(int(i/7)+1)*7-1-(i-int(i/7)*7)]
        for i in range(len(days_5)):
            if int((i)/7) == ((i)/7):
                days_5[i] = days_5[i]+'-br'
        ##################################################################################################### 1
        now = jdate(now.year,now.month,15)+timedelta(days=30)


        if now.month == 12:
            month_length =  (jdate(now.year+1, 1, 1) - jdate(now.year, 12, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
            this_date = str(now.year)+'-12-'
            next_date = str(now.year+1)+'-1-'
            prev_date = str(now.year)+'-11-'
        elif now.month == 1:
            month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year-1, 12, 1)).days
            this_date = str(now.year)+'-1-'
            next_date = str(now.year)+'-2-'
            prev_date = str(now.year-1)+'-12-'
        else:
            month_length =  (jdate(now.year, now.month+1, 1) - jdate(now.year, now.month, 1)).days
            previous_month_length = (jdate(now.year, now.month, 1) - jdate(now.year, now.month-1, 1)).days
            this_date = str(now.year)+'-'+str(now.month)+'-'
            next_date = str(now.year)+'-'+str(now.month+1)+'-'
            prev_date = str(now.year)+'-'+str(now.month-1)+'-'

        first_day_of_month_weekday = jdate(now.year, now.month, 1).weekday()
        array = [0,]
        days_6 = [0,]
        if (month_length == 30 and first_day_of_month_weekday == 6) or (month_length == 31 and first_day_of_month_weekday >=5):
            for i in range(41):
                array.append(0)
                days_6.append(0)
        else:
            for i in range(34):
                array.append(0)
                days_6.append(0)


        for i in range(first_day_of_month_weekday):
            array[first_day_of_month_weekday-i-1] = prev_date + '' #str(previous_month_length - i)

        for i in range(month_length):
            array[first_day_of_month_weekday+i] = this_date + str(i + 1)

        for i in range(len(array) - array.index(0)):
            array[array.index(0)] = next_date+ '' #str(i+1)
        for i in range(len(array)):
            days_6[i] = array[(int(i/7)+1)*7-1-(i-int(i/7)*7)]
        for i in range(len(days_6)):
            if int((i)/7) == ((i)/7):
                days_6[i] = days_6[i]+'-br'

        try:
            sessions = get_list_or_404(SessionModel.objects.order_by('day'), salon = salon)
            for session in sessions:
                duration = JDATETIMETOOL.strptime(session.duration,'%H:%M')
                time_var = duration + timedelta(hours = session.time.hour,
                                                                minutes = session.time.minute)
                try:
                    if time_var > ceil :
                        ceil = time_var
                except:
                    ceil = duration +  timedelta(hours = session.time.hour,
                                                                    minutes = session.time.minute)
                try:
                    if JDATETIMETOOL.strptime(str(session.time),'%H:%M') < floor:
                        floor = session.time
                except:
                    floor = JDATETIMETOOL.strptime(str(session.time),'%H:%M')
            session_days=['',]
            i=0
            for session in sessions:
                str_1 = str(session.day)
                str_1 = str_1.replace('-0','-',2)
                session_days.append(str_1)
            return render(request,'session/workspace.html',
                          {'sessions':sessions,'days_1':days_1,'session_days':session_days,
                           'salon':salon,'floor':floor,'ceil':ceil,'duration':duration,
                           'days_2':days_2,'days_6':days_6,'days_5':days_5,'days_4':days_4,
                           'days_3':days_3})
        except:
            return render(request,'session/workspace.html',
                          {'salon':salon,'days':days})
    else:
        return HttpResponseRedirect(reverse('login'))



@login_required
@sportclub_required
def SessionListView(request,pk):
    salon = get_object_or_404(SalonModel,pk = pk)
    if request.user == salon.sportclub.user:
        sessions = get_list_or_404(SessionModel.objects.order_by('day'), salon = salon)
        return render(request,'session/sessionlist.html',
                      {'sessions':sessions,
                       'salon':salon})
    else:
        return HttpResponseRedirect(reverse('login'))


class LengthError(TemplateView):
    template_name = 'session/lengtherror.html'


@login_required
@sportclub_required
def SessionCategoriesView(request,pk):
    salon = get_object_or_404(SalonModel,pk = pk)
    if request.user == salon.sportclub.user:
        sessioncategory_instances = get_list_or_404(SessionCategoryModel, salon = salon)
        return render(request, 'session/categories.html',
                    {'categories':sessioncategory_instances,'salon':salon})
    return HttpResponseRedirect(reverse('login'))


@login_required
@sportclub_required
def SetPriceView(request,pk):
    sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
    if sessioncategory_instance.salon.sportclub.user == request.user:
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
                if len(checks) == 0 or sessioncategory_instance.range_start_day > range_start or range_start > range_end or sessioncategory_instance.range_end_day < range_end :
                    return HttpResponseRedirect(reverse('session:logicalerror'))
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
                                    if not session.is_booked:
                                        session.price = price
                                        session.is_ready = True
                                        session.save()
                #for reverse
                salon_pk = sessioncategory_instance.salon.pk
                return HttpResponseRedirect(reverse('session:categories',
                                                    kwargs={'pk':salon_pk}))

        else:
            price_form = PriceForm()
            list = sessioncategory_instance.sessions.all()
            obj = list[0]
            session_instances = get_list_or_404(SessionModel,day = obj.day,
                                                session_category = sessioncategory_instance)
        return render(request,'session/setprice.html',{'sessions':session_instances,
                      'session_category':sessioncategory_instance,'form':price_form})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@sportclub_required
def SetDiscountPercentageView(request,pk):
    sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
    if sessioncategory_instance.salon.sportclub.user == request.user:
        if request.method == "POST":
            checks = request.POST.getlist('checks')
            days = request.POST.getlist('days')
            discount_percentage_form = DiscountPercentageForm(data = request.POST )
            if discount_percentage_form.is_valid():
                range_start_str = discount_percentage_form.cleaned_data['range_start']
                range_start_list = range_start_str.split('-')
                range_start = jdatetime.date(int(range_start_list[0]),int(range_start_list[1]),int(range_start_list[2]))
                range_end_str = discount_percentage_form.cleaned_data['range_end']
                range_end_list = range_end_str.split('-')
                range_end = jdatetime.date(int(range_end_list[0]),int(range_end_list[1]),int(range_end_list[2]))
                discount_percentage = discount_percentage_form.cleaned_data['discount_percentage']
                sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
                if discount_percentage > 100 or len(checks) == 0 or sessioncategory_instance.range_start_day > range_start or range_start > range_end or sessioncategory_instance.range_end_day < range_end :
                    return HttpResponseRedirect(reverse('session:logicalerror'))
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
                                    if not session.is_booked:
                                        session.discount_percentage = discount_percentage
                                        session.save()
                #for reverse
                salon_pk = sessioncategory_instance.salon.pk
                return HttpResponseRedirect(reverse('session:categories',
                                                    kwargs={'pk':salon_pk}))

        else:
            discount_percentage_form = DiscountPercentageForm()
            list = sessioncategory_instance.sessions.all()
            obj = list[0]
            session_instances = get_list_or_404(SessionModel,day = obj.day,
                                                session_category = sessioncategory_instance)
        return render(request,'session/setdiscountpercentage.html',{'sessions':session_instances,
                      'session_category':sessioncategory_instance,'form':discount_percentage_form})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@sportclub_required
def StatusChangeView(request,pk):
    sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
    if sessioncategory_instance.salon.sportclub.user == request.user:
        if request.method == "POST":
            checks = request.POST.getlist('checks')
            days = request.POST.getlist('days')
            status_form = StatusForm(data = request.POST )
            is_ready = request.POST.get('is_ready')
            if status_form.is_valid():
                range_start_str = status_form.cleaned_data['range_start']
                range_start_list = range_start_str.split('-')
                range_start = jdatetime.date(int(range_start_list[0]),int(range_start_list[1]),int(range_start_list[2]))
                range_end_str = status_form.cleaned_data['range_end']
                range_end_list = range_end_str.split('-')
                range_end = jdatetime.date(int(range_end_list[0]),int(range_end_list[1]),int(range_end_list[2]))
                sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
                if sessioncategory_instance.range_start_day > range_start or range_start > range_end or sessioncategory_instance.range_end_day < range_end :
                    return HttpResponseRedirect(reverse('session:logicalerror'))
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
                                    if not session.is_booked:
                                        if is_ready == 'true':
                                            if session.price:
                                                session.is_ready == True
                                                session.save()
                                        else:
                                            session.is_ready = False
                                            session.save()

                #for reverse
                salon_pk = sessioncategory_instance.salon.pk
                return HttpResponseRedirect(reverse('session:categories',
                                                    kwargs={'pk':salon_pk}))

        else:
            status_form = StatusForm()
            list = sessioncategory_instance.sessions.all()
            obj = list[0]
            session_instances = get_list_or_404(SessionModel,day = obj.day,
                                                session_category = sessioncategory_instance)
        return render(request,'session/statuschange.html',{'sessions':session_instances,
                      'session_category':sessioncategory_instance,'form':status_form})
    else:
        return HttpResponseRedirect(reverse('login'))



def CategorizedSessionListView(request,pk):
    sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
    sessions = sessioncategory_instance.sessions.order_by('day','time')
    return render(request,'session/categorizedsessionlist.html',{'sessions':sessions,
                  'session_category':sessioncategory_instance})


@method_decorator([login_required, sportclub_required], name='dispatch')
class SessionUpdateView(UpdateView):
    model = SessionModel
    fields = ['is_ready','price','discount_percentage',]
    template_name = 'session/sessionupdate.html'

    def form_valid(self, form):
        if form.cleaned_data['discount_percentage'] > 100:
            return super(SessionUpdateView, self).form_invalid(form)
        if form.cleaned_data['is_ready']:
            if not self.object.price:
                 return super(SessionUpdateView, self).form_invalid(form)
        if self.object.is_booked:
            return super(SessionUpdateView, self).form_invalid(form)
        self.object = form.save()
        return super().form_valid(form)

    def get_queryset(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = get_object_or_404(SessionModel,pk = pk)
        if obj.salon.sportclub.user == self.request.user:
            return self.model._default_manager.all()

    def get_success_url(self):
        pk = self.object.session_category.salon.pk
        return reverse('session:workspace', kwargs={'pk':pk})



@login_required
@sportclub_required
def SessionDeleteView(request,pk):
    sessioncategory_instance = get_object_or_404(SessionCategoryModel,pk = pk)
    if sessioncategory_instance.salon.sportclub.user == request.user:
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
                ########## chekc if deleting doesn't start from range start day
                if sessioncategory_instance.range_start_day > range_start or range_start > range_end or sessioncategory_instance.range_end_day < range_end :
                    return HttpResponseRedirect(reverse('session:logicalerror'))

                for session in sessions:
                    x1 = session.day - range_start
                    x2 = session.day - range_end
                    x3 = session.day - sessioncategory_instance.range_start_day
                    x4 = session.day - sessioncategory_instance.range_end_day
                    if int(x1.days) >= 0 and int(x2.days) <= 0 :
                        if str(session.day.weekday()) in days:
                            for check in checks:
                                check_time = DATETIMETOOL.strptime(check,'%H:%M')
                                check_time = check_time.time()
                                if session.time.minute - check_time.minute == 0 and session.time.hour - check_time.hour == 0:
                                    if session.is_booked:
                                        return HttpResponseRedirect(reverse('session:is_booked'))

                if range_start != sessioncategory_instance.range_start_day:
                    session_category_1 = SessionCategoryModel.objects.create(salon=sessioncategory_instance.salon,
                                            range_start_day = sessioncategory_instance.range_start_day,
                                            range_end_day = range_start+timedelta(days=-1))
                    session_category_1.save()
                if range_end != sessioncategory_instance.range_end_day:
                    session_category_2 = SessionCategoryModel.objects.create(salon=sessioncategory_instance.salon,
                                            range_start_day = range_end+timedelta(days=1),
                                            range_end_day = sessioncategory_instance.range_end_day)
                    session_category_2.save()
                session_category_3 = SessionCategoryModel.objects.create(salon=sessioncategory_instance.salon,
                                        range_start_day = range_start,
                                        range_end_day = range_end)
                session_category_3.save()
                session_category_4 = SessionCategoryModel.objects.create(salon=sessioncategory_instance.salon,
                                        range_start_day = range_start,
                                        range_end_day = range_end)
                session_category_4.save()
                ###########
                for session in sessions:
                    x1 = session.day - range_start
                    x2 = session.day - range_end
                    x3 = session.day - sessioncategory_instance.range_start_day
                    x4 = session.day - sessioncategory_instance.range_end_day
                    if int(x3.days) >= 0 and int(x1.days) < 0 :
                        if session.day.weekday() == 0:
                            session_category_1.saturdays = True
                            session_category_1.save()
                        if session.day.weekday() == 1:
                            session_category_1.sundays = True
                            session_category_1.save()
                        if session.day.weekday() == 2:
                            session_category_1.mondays = True
                            session_category_1.save()
                        if session.day.weekday() == 3:
                            session_category_1.tuesdays = True
                            session_category_1.save()
                        if session.day.weekday() == 4:
                            session_category_1.wednesdays = True
                            session_category_1.save()
                        if session.day.weekday() == 5:
                            session_category_1.thursdays = True
                            session_category_1.save()
                        if session.day.weekday() == 6:
                            session_category_1.fridays = True
                            session_category_1.save()
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
                        if session.day.weekday() == 0:
                            session_category_2.saturdays = True
                            session_category_2.save()
                        if session.day.weekday() == 1:
                            session_category_2.sundays = True
                            session_category_2.save()
                        if session.day.weekday() == 2:
                            session_category_2.mondays = True
                            session_category_2.save()
                        if session.day.weekday() == 3:
                            session_category_2.tuesdays = True
                            session_category_2.save()
                        if session.day.weekday() == 4:
                            session_category_2.wednesdays = True
                            session_category_2.save()
                        if session.day.weekday() == 5:
                            session_category_2.thursdays = True
                            session_category_2.save()
                        if session.day.weekday() == 6:
                            session_category_2.fridays = True
                            session_category_2.save()
                        session.session_category = session_category_2
                        session.save()

                for session_1 in sessioncategory_instance.sessions.all():
                    if str(session_1.day.weekday()) in days:
                        if session_1.day.weekday() == 0:
                            session_category_3.saturdays = True
                            session_category_3.save()
                        if session_1.day.weekday() == 1:
                            session_category_3.sundays = True
                            session_category_3.save()
                        if session_1.day.weekday() == 2:
                            session_category_3.mondays = True
                            session_category_3.save()
                        if session_1.day.weekday() == 3:
                            session_category_3.tuesdays = True
                            session_category_3.save()
                        if session_1.day.weekday() == 4:
                            session_category_3.wednesdays = True
                            session_category_3.save()
                        if session_1.day.weekday() == 5:
                            session_category_3.thursdays = True
                            session_category_3.save()
                        if session_1.day.weekday() == 6:
                            session_category_3.fridays = True
                            session_category_3.save()
                        session_1.session_category = session_category_3
                        session_1.save()
                    else:
                        if session_1.day.weekday() == 0:
                            session_category_4.saturdays = True
                            session_category_4.save()
                        if session_1.day.weekday() == 1:
                            session_category_4.sundays = True
                            session_category_4.save()
                        if session_1.day.weekday() == 2:
                            session_category_4.mondays = True
                            session_category_4.save()
                        if session_1.day.weekday() == 3:
                            session_category_4.tuesdays = True
                            session_category_4.save()
                        if session_1.day.weekday() == 4:
                            session_category_4.wednesdays = True
                            session_category_4.save()
                        if session_1.day.weekday() == 5:
                            session_category_4.thursdays = True
                            session_category_4.save()
                        if session_1.day.weekday() == 6:
                            session_category_4.fridays = True
                            session_category_4.save()
                        session_1.session_category = session_category_4
                        session_1.save()
                if len(session_category_3.sessions.all()) == 0:
                    session_category_3.delete()
                if len(session_category_4.sessions.all()) == 0:
                    session_category_4.delete()

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
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@sportclub_required
def SessionCreateView_2(request,pk):
    salon_instance = get_object_or_404(SalonModel, pk = pk)
    last_data_instance = get_object_or_404(LastDataModel,salon = salon_instance)
    if salon_instance.sportclub.user == request.user:

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


                start_time = times_form.cleaned_data['start_time']
                duration = times_form.cleaned_data['duration']
                stop_time = times_form.cleaned_data['stop_time']

                jstart_time = JDATETIMETOOL.strptime(str(start_time),'%H:%M')
                jstop_time = JDATETIMETOOL.strptime(str(stop_time),'%H:%M')

                stop_2 = JDATETIMETOOL.strptime(str(duration),'%H:%M') +  timedelta(hours=jstart_time.hour, minutes = jstart_time.minute)
                if first_day > last_day or last_data_instance.first_day_2 <= last_day or jstop_time < stop_2 :
                    return HttpResponseRedirect(reverse('session:logicalerror'))

                length_2 = last_day - first_day
                length_2 = length_2.days
                if length_2 < 6 :
                    return HttpResponseRedirect(reverse('session:lengtherror'))
                last_data_instance = salon_instance.lastdatas.all()
                if not last_data_instance[0].first_day_2:
                    return HttpResponseRedirect(reverse('session:boundaryerror'))
                if last_day >= last_data_instance[0].first_day_2:
                    return HttpResponseRedirect(reverse('session:boundaryerror'))

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

                if str(0) in selected_days:
                    session_category.saturdays = True
                    session_category.save()
                if str(1) in selected_days:
                    session_category.sundays = True
                    session_category.save()
                if str(2) in selected_days:
                    session_category.mondays = True
                    session_category.save()
                if str(3) in selected_days:
                    session_category.tuesdays = True
                    session_category.save()
                if str(4) in selected_days:
                    session_category.wednesdays = True
                    session_category.save()
                if str(5) in selected_days:
                    session_category.thursdays = True
                    session_category.save()
                if str(6) in selected_days:
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

                return HttpResponseRedirect(reverse('session:workspace',
                                                kwargs={'pk':pk}))
            else:
                print(times_form.errors)
                return HttpResponseRedirect(reverse('salon:salondetail',
                                                kwargs={'pk':pk}))
        else:
            days_form_2 = DaysForm_2
            times_form = TimesForm()
            return render(request,'session/sessioncreate_2.html',
                                  {'times_form':times_form,
                                  'last_data':last_data_instance,'days_form':days_form_2})
    else:
        return HttpResponseRedirect(reverse('login'))


def InterferenceErrorView(request,pk):
    session_instance = get_object_or_404(SessionModel,pk = pk)
    return render(request,'session/interferenceerror.html',{'session':session_instance})


class BoundaryErrorView(TemplateView):
    template_name = 'session/boundaryerror.html'


class NoInputErrorView(TemplateView):
    template_name = 'session/noinputerror.html'


@login_required
@sportclub_required
def SessionCreateView(request, pk):
    salon_instance = get_object_or_404(SalonModel, pk = pk)
    if salon_instance.sportclub.user == request.user:
        try:
            lastdata_instance = get_object_or_404(LastDataModel, salon = salon_instance)
        except:
            lastdata_instance = LastDataModel.objects.create(salon=salon_instance)
        if request.method == 'POST':
            is_closed = request.POST.get('is_closed')
            selected_days = request.POST.getlist('selected_days')
            days_form = DaysForm(data = request.POST )
            times_form = TimesForm(data = request.POST )
            if times_form.is_valid() and days_form.is_valid():

                start_time = times_form.cleaned_data['start_time']
                duration = times_form.cleaned_data['duration']
                stop_time = times_form.cleaned_data['stop_time']

                if not start_time and not duration and not stop_time and not is_closed:
                    return HttpResponseRedirect(reverse('session:noinputerror'))

                if lastdata_instance.last_length:
                    length = lastdata_instance.last_length
                    first_day = lastdata_instance.first_day
                    last_day = lastdata_instance.last_day
                else:
                    if lastdata_instance.first_day_2:
                        first_day = lastdata_instance.first_day_2
                    else:
                        first_day = jdatetime.datetime.now().date()
                    last_day_str = days_form.cleaned_data['last_day']
                    last_day_list = last_day_str.split('-')
                    last_day = jdatetime.date(int(last_day_list[0]),int(last_day_list[1]),int(last_day_list[2]))
                    length = last_day - first_day
                    length = length.days

                if length < 6 :
                    return HttpResponseRedirect(reverse('session:lengtherror'))
                try: # be aware of this try structure before adding any other logical errors
                    jstart_time = JDATETIMETOOL.strptime(str(start_time),'%H:%M')
                    jstop_time = JDATETIMETOOL.strptime(str(stop_time),'%H:%M')
                    stop_2 = JDATETIMETOOL.strptime(str(duration),'%H:%M') +  timedelta(hours=jstart_time.hour, minutes = jstart_time.minute)
                    if first_day > last_day or jstop_time < stop_2 :
                        return HttpResponseRedirect(reverse('session:logicalerror'))
                except:
                    pass
                #Creating the SessionCategory Instance
                session_category = SessionCategoryModel.objects.create(salon=salon_instance,
                                        range_start_day = first_day, range_end_day = last_day)

                lastdata_instance.first_day = first_day
                lastdata_instance.last_day = last_day
                lastdata_instance.last_length = length
                lastdata_instance.save()

                if str(0) in selected_days:
                    session_category.saturdays = True
                    session_category.save()
                    lastdata_instance.last_saturday = True
                    lastdata_instance.save()
                if str(1) in selected_days:
                    session_category.sundays = True
                    session_category.save()
                    lastdata_instance.last_sunday = True
                    lastdata_instance.save()
                if str(2) in selected_days:
                    session_category.mondays = True
                    session_category.save()
                    lastdata_instance.last_monday = True
                    lastdata_instance.save()
                if str(3) in selected_days:
                    session_category.tuesdays = True
                    session_category.save()
                    lastdata_instance.last_tuesday = True
                    lastdata_instance.save()
                if str(4) in selected_days:
                    session_category.wednesdays = True
                    session_category.save()
                    lastdata_instance.last_wednesday = True
                    lastdata_instance.save()
                if str(5) in selected_days:
                    session_category.thursdays = True
                    session_category.save()
                    lastdata_instance.last_thursday = True
                    lastdata_instance.save()
                if str(6) in selected_days:
                    session_category.fridays = True
                    session_category.save()
                    lastdata_instance.last_friday = True
                    lastdata_instance.save()

                if is_closed == 'closed':
                    session_category.is_closed = True
                    session_category.save()
                    return HttpResponseRedirect(reverse('salon:salondetail',
                                                    kwargs={'pk':pk}))


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
    else:
        return HttpResponseRedirect(reverse('login'))


def LastDataSetView(request, pk):
    salon_instance = get_object_or_404(SalonModel, pk = pk)
    lastdata_instance = get_object_or_404(LastDataModel, salon = salon_instance)
    if salon_instance.sportclub.user == request.user or request.user.is_superuser or request.user.is_masteruser:
        if request.method == 'POST':
            lastdatasetform = LastDataSetForm(data = request.POST )
            if lastdatasetform.is_valid():
                first_day_str = lastdatasetform.cleaned_data['first_day']
                first_day_list = first_day_str.split('-')
                first_day = jdatetime.date(int(first_day_list[0]),int(first_day_list[1]),int(first_day_list[2]))
                lastdata_instance.first_day_2 = first_day
                lastdata_instance.first_day = None
                lastdata_instance.last_day = None
                lastdata_instance.last_length = None
                lastdata_instance.last_saturday = False
                lastdata_instance.last_sunday = False
                lastdata_instance.last_monday = False
                lastdata_instance.last_tuesday = False
                lastdata_instance.last_wednesday = False
                lastdata_instance.last_thursday = False
                lastdata_instance.last_friday = False
                lastdata_instance.save()
                if request.user.is_masteruser:
                    return HttpResponseRedirect(reverse('salon:detail',
                                                    kwargs={'pk':pk}))
                return HttpResponseRedirect(reverse('salon:salondetail',
                                                kwargs={'pk':pk}))
            else:
                print(lastdatasetform.errors)
                return HttpResponseRedirect(reverse('salon:salondetail',
                                                kwargs={'pk':pk}))

        else:
            lastdatasetform = LastDataSetForm()
            return render(request,'session/lastdataset.html',{'form':lastdatasetform})
    else:
        return HttpResponseRedirect(reverse('login'))


class LogicalErrorView(TemplateView):
    template_name = 'session/logicalerror.html'


class IsBookedErrorView(TemplateView):
    template_name = 'session/isbooked.html'


@method_decorator(login_required, name='dispatch')
class AllSessionListView(ListView):
    model = SessionModel
    template_name = 'session/allsessionslist.html'
    context_object_name = 'sessions'

    def get_queryset(self):
        queryset = SessionModel.objects.filter( salon__is_confirmed = True ).order_by('day')
        return queryset


@login_required
@sportclub_required
def DayListView(request,pk,str):
    # if request.user == # XXX:
    salon = get_object_or_404(SalonModel,pk = pk)
    sessionlist = get_list_or_404(SessionModel,day = str, salon=salon)
    return render(request,'session/daylist.html',{'sessions':sessionlist})
