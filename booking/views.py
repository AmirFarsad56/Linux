from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, TemplateView
from django.urls import reverse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect
import jdatetime
from jdatetime import timedelta as jtimedelta
from datetime import timedelta
from jdatetime import date as jdate
from django.core.paginator import Paginator
import datetime
import random

#handmade
from booking.forms import NumberForm
from booking.filters import ContractFilter
from booking.models import ProfitPercentageModel
from commonuser.decorators import commonuser_required
from accounts.decorators import superuser_required
from session.models import SessionModel
from booking.models import BookingModel, ContractModel
from salon.models import SalonModel



@method_decorator([login_required, superuser_required], name='dispatch')
class CreateProfitPercentageView(CreateView):
    model = ProfitPercentageModel
    fields = ('profit_percentage',)
    template_name = 'booking/createprofitpercentage.html'

    def get_success_url(self):
        return reverse('accounts:workspace',kwargs={'slug':self.request.user.slug})


@method_decorator([login_required, superuser_required], name='dispatch')
class UpdateProfitPercentageView(UpdateView):
    model = ProfitPercentageModel
    fields = ('profit_percentage',)
    template_name = 'booking/updateprofitpercentage.html'

    def get_success_url(self):
        return reverse('accounts:workspace',kwargs={'slug':self.request.user.slug})


@login_required
@commonuser_required
def BookingView(request,pk):
    today = jdatetime.datetime.now().date()
    session = get_object_or_404(SessionModel, pk = pk)
    if session.day >= today and session.is_ready and session.salon.is_confirmed:

        #session adjustment
        session.is_booked = True
        session.booker = request.user

        var = 'abcdefghijklmnopqrstuvwxyzABCDEFIJKLMNOPQRSTUVWXYZ1234567890'
        random_code=''
        for i in range(0,random.randrange(10,13,1)):
            c = random.choice(var)
            random_code += c

        #booking_object
        price = session.price
        final_price = (((100-session.discount_percentage)/100) * price ) * ((100 - session.salon.company_discount_percentage)/100)
        sportclub_portion = ((100-session.discount_percentage-session.salon.profit_percantage)/100) * price
        company_portion = final_price - sportclub_portion
        booked_at_time = datetime.datetime.now().time()
        booked_at_date = jdatetime.datetime.now().date()
        booking_object  = BookingModel.objects.create(session=session, booked_at_time=booked_at_time, booked_at_date = booked_at_date,
                                    booker = request.user.commonusers, raw_price = session.price, final_price = final_price,
                                     company_discount_percentage = session.salon.company_discount_percentage,
                                     discount_percentage = session.discount_percentage,
                                     code = random_code, profit_percantage = session.salon.profit_percentage,
                                     sportclub_portion = sportclub_portion, company_portion = company_portion)
        booking_object.save()
        session.save()

        return HttpResponseRedirect(reverse('commonuser:dashboard'))


@login_required
@commonuser_required
def CancellingView(request,pk):
    today = jdatetime.datetime.now().date()
    now_time = datetime.datetime.now().time()

    booking_object = get_object_or_404(BookingModel, pk = pk)
    session = booking_object.session
    ceil_date = jdate(today.year,today.month,today.day)+jtimedelta(days=2)
    ceil_time = (datetime.datetime.combine(datetime.date(1,1,1),now_time) + timedelta(hours = 5)).time()
    if booking_object.session.day >= ceil_date:
        if not booking_object.is_contract:
            session.is_booked = False
            session.booker = None
            contract_discount = booking_object.contract_discount
            booking_object.pay_back = (booking_object.final_price * (100-contract_discount))/100
            booking_object.cancelled = True
            booking_object.cancelled_at_date = today
            booking_object.cancelled_at_time = now_time
        else:
            session.is_booked = False
            session.booker = None
            booking_object.pay_back = booking_object.final_price
            booking_object.cancelled = True
            booking_object.cancelled_at_date = today
            booking_object.cancelled_at_time = now_time
    elif booking_object.session.day == today and  booking_object.session.time < ceil_time:
        return HttpResponseRedirect(reverse('booking:cantcancell'))
    elif booking_object.session.day < today:
        return HttpResponseRedirect(reverse('booking:cancellingerror'))
    else:
        if not booking_object.is_contract:
            session.is_booked = False
            session.booker = None
            booking_object.pay_back = (booking_object.final_price * 85)/100
            booking_object.cancelled = True
            booking_object.cancelled_at_date = today
        else:
            session.is_booked = False
            session.booker = None
            contract_discount = booking_object.contract_discount
            booking_object.pay_back = (booking_object.final_price * (85-contract_discount))/100
            booking_object.cancelled = True
            booking_object.cancelled_at_date = today
    booking_object.cancelled_at_time = now_time
    booking_object.save()
    session.save()
    return HttpResponseRedirect(reverse('booking:cancelsuccess'))



class CantCancellView(TemplateView):
    template_name = 'booking/cantcancell.html'


class CancellingErrorView(TemplateView):
    template_name = 'booking/cancellingerror.html'


@login_required
@commonuser_required
def SignContractView(request,pk):
    initilized = False
    salon_instance = get_object_or_404(SalonModel,pk = pk)
    if request.method == 'POST':
        if 'submit1' in request.POST:

            form = NumberForm(data = request.POST)
            checks = request.POST.getlist('checks') #session pk
            days = request.POST.getlist('days')
            if form.is_valid():
                numbers = form.cleaned_data['numbers']
                range_start_str = form.cleaned_data['range_start']
                range_start_list = range_start_str.split('-')
                range_start = jdatetime.date(int(range_start_list[0]),int(range_start_list[1]),int(range_start_list[2]))
                range_end_str = form.cleaned_data['range_end']
                range_end_list = range_end_str.split('-')
                range_end = jdatetime.date(int(range_end_list[0]),int(range_end_list[1]),int(range_end_list[2]))
                today = jdatetime.datetime.now().date()
                session = get_object_or_404(SessionModel,pk = checks[0])
                session_time = session.time
                sessioncategory_instance = session.session_category
                if numbers < 2 or today > range_start or len(checks) != 1 or len(days) != 1 or sessioncategory_instance.range_start_day > range_start or range_start > range_end or sessioncategory_instance.range_end_day < range_end :
                    return HttpResponseRedirect(reverse('session:logicalerror'))

                sessions = sessioncategory_instance.sessions.all()
                for session in sessions:
                    x1 = session.day - range_start
                    x2 = session.day - range_end
                    if int(x1.days) >= 0 and int(x2.days) <= 0 :

                        if str(session.day.weekday()) in days:
                            #if  str(session.time) == str(session_time) and session.day >= today and session.is_ready and session.salon.is_confirmed:
                            if  str(session.time) == str(session_time) and session.day >= today and session.is_ready and session.salon.is_confirmed:
                                session_instance = session

                                break
                sum_price = 0
                try:
                    if (session_instance.day + jdatetime.timedelta(days = (numbers-1)*7)) > range_end:
                        return HttpResponseRedirect(reverse('booking:notavailablesessions'))
                except:
                    return HttpResponseRedirect(reverse('booking:notavailablesessions'))
                for i in range(numbers):
                    day = session_instance.day + jdatetime.timedelta(days = i*7)
                    if day <= range_end:
                        wanted_session = get_object_or_404(SessionModel,session_category = sessioncategory_instance,
                                                            day = day, time = session_instance.time)
                        wanted_session.is_booked = True
                        wanted_session.booker = request.user

                        var = 'abcdefghijklmnopqrstuvwxyzABCDEFIJKLMNOPQRSTUVWXYZ1234567890'
                        random_code=''
                        for i in range(0,random.randrange(10,13,1)):
                            c = random.choice(var)
                            random_code += c


                        #calculating price:
                        price = wanted_session.price

                        if numbers >= 6 and numbers < 12:
                            six_to_twelve_sessions_discount = wanted_session.salon.six_to_twelve_sessions_discount
                            final_price = (((100-wanted_session.discount_percentage-six_to_twelve_sessions_discount)/100) * price ) * ((100-wanted_session.salon.company_discount_percentage)/100)
                            sportclub_portion = ((100-wanted_session.discount_percentage-six_to_twelve_sessions_discount-wanted_session.salon.company_discount_percentage)/100) * price
                            company_portion = final_price - sportclub_portion
                            sum_price += final_price
                            discount_for_multiple_sessions = six_to_twelve_sessions_discount
                        elif numbers < 6:

                            final_price = (((100-wanted_session.discount_percentage)/100) * price ) * ((100 - wanted_session.salon.company_discount_percentage)/100)
                            sum_price += final_price
                            discount_for_multiple_sessions = 0
                        elif numbers > 12:
                            more_than_twelve_sessions_discount = wanted_session.salon.more_than_twelve_sessions_discount
                            final_price = (((100-wanted_session.discount_percentage-more_than_twelve_sessions_discount)/100) * price ) * ((100-wanted_session.salon.company_discount_percentage)/100)
                            sportclub_portion = ((100-wanted_session.discount_percentage-wanted_session.salon.company_discount_percentage-more_than_twelve_sessions_discount)/100) * price
                            company_portion = final_price - sportclub_portion
                            sum_price += final_price
                            discount_for_multiple_sessions = more_than_twelve_sessions_discount
                        #booking_object

                        booked_at_time = datetime.datetime.now().time()
                        booked_at_date = jdatetime.datetime.now().date()
                        booking_object  = BookingModel.objects.create(session=wanted_session, booked_at_time=booked_at_time, booked_at_date = booked_at_date,
                                                    booker = request.user.commonusers, raw_price = wanted_session.price, final_price = final_price,
                                                     company_discount_percentage = wanted_session.salon.company_discount_percentage,
                                                     discount_percentage = wanted_session.discount_percentage, is_contract = True,
                                                     code = random_code, profit_percantage = wanted_session.salon.profit_percentage,
                                                     contract_discount = discount_for_multiple_sessions,sportclub_portion = sportclub_portion,
                                                     company_portion = company_portion,)
                        booking_object.save()

                        wanted_session.save()
                created_at_time = datetime.datetime.now().time()
                created_at_date = jdatetime.datetime.now().date()
                contract_object = ContractModel.objects.create(salon = session_instance.salon, booker = request.user.commonusers,
                                                                total_price = sum_price, created_at_date = created_at_date,
                                                                created_at_time = created_at_time, numbers = numbers)
                #contract_object.save()
                initilized = True
                return HttpResponseRedirect(reverse('booking:contractsuccess'))


            else:
                print(form.errors)
    else:
        try:
            l = 0
            for category in salon_instance.sessioncategories.all():
                if not category.is_closed:
                    list = category.sessions.all()
                    obj = list[0]
                    session_instances = get_list_or_404(SessionModel,day = obj.day,
                                                        session_category = category)
                    dictionary = {'category':category,'sessions':session_instances}
                    if l == 0:
                        list = [dictionary,]
                        l += 1
                    else:
                        list.append(dictionary)
                else:
                    pass

            form = NumberForm()
            today = jdatetime.datetime.now().date()
            return render(request,'booking/signcontract.html',{'form':form,'salon':salon_instance,'list':list,
                                                            'today':today,'initilized':initilized})
        except:
            return HttpResponseRedirect(reverse('booking:nosessionerror'))



class NotAvailableSessionsView(TemplateView):
    template_name = 'booking/notavailablesessions.html'

class NoSessionErrorView(TemplateView):
    #has not sessions (this salon)
    template_name = 'booking/nosessionerror.html'

class ContractSuccessView(TemplateView):
    template_name = 'booking/contractsuccess.html'

class CancelSuccessView(TemplateView):
    template_name = 'booking/cancelsuccess.html'


def ContractListView(request,pk):
    salon = get_object_or_404(SalonModel,pk = pk)
    if request.user == salon.sportclub.user:

        contract_list = ContractModel.objects.filter(salon = salon )
        contract_filter = ContractFilter(request.GET,queryset = contract_list)
        paginator = Paginator(contract_filter.qs, 20)
        page = request.GET.get('page')
        contracts = paginator.get_page(page)
        return render(request,'booking/contractlist.html',{'contracts':contracts,'filter':contract_filter})
    else:
        return HttpResponseRedirect(reverse('login'))


def BookedSessionListView(request,pk):
    salon = get_object_or_404(SalonModel,pk = pk)
    if request.user == salon.sportclub.user:

        sessions = get_list_or_404(BookingModel, salon = salon)
        return render(request,'booking/bookedsessionlist.html',{'sessions':sessions})
    else:
        return HttpResponseRedirect(reverse('login'))
