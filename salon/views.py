from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django.forms import modelformset_factory
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import jdatetime

#handmade
from accounts.models import UserModel
from sportclub.models import SportClubModel
from salon.forms import SalonForm, SalonPictureForm, SalonProfitForm
from salon.models import SalonModel, SalonPictureModel
from sportclub.decorators import sportclub_required
from accounts.decorators import superuser_required
from masteruser.decorators import masteruser_required
from booking.models import ProfitPercentageModel


#recaptcha
import json
import urllib
from django.conf import settings
from django.contrib import messages




@login_required
@sportclub_required
def SalonCreateView(request,slug):
    user = get_object_or_404(UserModel, slug=slug)
    sportclub = get_object_or_404(SportClubModel, user = user)
    if sportclub == request.user.sportclubs:

        imageformset = modelformset_factory(SalonPictureModel,
                                            form=SalonPictureForm, extra=4)
        if request.method == 'POST':
            salon_form = SalonForm(data = request.POST)
            formsets = imageformset(request.POST or None, request.FILES or None)
            if salon_form.is_valid() and formsets.is_valid():

                salon = salon_form.save(commit=False)
                #sportclub = get_object_or_404(SportClubModel, slug=slug)
                salon.sportclub = sportclub
                profit_percentage = ProfitPercentageModel.objects.get()
                salon.profit_percentage = profit_percentage.profit_percentage
                salon.save()
                for formset in formsets.cleaned_data:
                    if formset:
                        picture = formset['picture']
                        photo = SalonPictureModel(salon = salon, picture = picture)
                        photo.save()
                return HttpResponseRedirect(reverse('sportclub:workspace',
                                            kwargs={'slug':user.slug}))
            else:
                print(salon_form.errors)
        else:
            salon_form = SalonForm()
            formsets = imageformset(queryset=SalonPictureModel.objects.none())
    else:
        return HttpResponseRedirect(reverse('login'))
    return render(request,'salon/createsalon.html',
                  {'salon_form':salon_form,
                  'formsets':formsets})


@login_required
@superuser_required
def SalonSetProfitPercentage(request,pk):
    salon = get_object_or_404(SalonModel, pk = pk)
    if request.user.is_superuser:
        set_profit_form = SalonProfitForm(request.POST or None, instance = salon)
        if set_profit_form.is_valid():
            set_profit_form.save()
            salon.save()
            return HttpResponseRedirect(reverse('sportclub:detailforsuperuser',
                                                kwargs={'slug':salon.sportclub.user.slug}))
        return render(request,'salon/setprofitpercentage.html',
                              {'form':set_profit_form,})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@sportclub_required
def SalonUpdateView(request,slug,pk):
    sportclub_user = get_object_or_404(UserModel, slug = slug)
    sportclub = get_object_or_404(SportClubModel, user = sportclub_user)
    salon = get_object_or_404(SalonModel, pk = pk)
    if salon.sportclub == sportclub:

        salon_update_form = SalonForm(request.POST or None, instance = salon)
        if salon_update_form.is_valid():
            salon_update_form.save()
            salon.is_confirmed = False
            salon.save()
            return HttpResponseRedirect(reverse('sportclub:workspace',
                                        kwargs={'slug':slug,}))
        return render(request,'salon/updatesalon.html',
                              {'form':salon_update_form,})
    else:
        return HttpResponseRedirect(reverse('login'))




@method_decorator([login_required, sportclub_required], name='dispatch')
class SalonDetailView(DetailView):
    model = SalonModel
    context_object_name = 'salon_detail'
    template_name = 'salon/salondetail.html'

    def get_queryset(self):
        return SalonModel.objects.filter(sportclub = self.request.user.sportclubs)


@method_decorator([login_required, masteruser_required], name='dispatch')
class ConfirmedSalonListView(ListView):
    model = SalonModel
    context_object_name = 'salons'
    template_name = 'salon/confirmedsalonlist.html'


@method_decorator([login_required, masteruser_required], name='dispatch')
class UnConfirmedSalonListView(ListView):
    model = SalonModel
    context_object_name = 'salons'
    template_name = 'salon/unconfirmedsalonlist.html'


@login_required
@masteruser_required
def SalonDeleteView(request,pk):
    if request.user.is_masteruser:
        salon = get_object_or_404(SalonModel,pk = pk)
        masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
        masteruser_instance_logs = masteruser_instance.user_logs
        now = jdatetime.datetime.now()
        dtime = str(now.year)+'-'+str(now.month)+'-'+ str(now.day)+'  '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        new_log = '''{previous_logs}\n
On {date_time}:\n
Deleted Salon: {salon}
Related to Sport Club: {sportclub}
-------------------------------------------------------
        '''.format(previous_logs = masteruser_instance_logs,
                   date_time = dtime,
                    salon = str(salon),
                    sportclub = str(salon.sportclub.user.username))
        masteruser_instance.user_logs = new_log
        masteruser_instance.save()
        salon.delete()
        return HttpResponseRedirect(reverse('salon:unconfirmedsalonlist'))
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@masteruser_required
def SalonConfirmView(request,pk):
    if request.user.is_masteruser:
        salon = get_object_or_404(SalonModel,pk = pk)
        related_user = salon.sportclub.user
        if salon.sportclub.user.is_active:
            salon.confirm()
            masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
            masteruser_instance_logs = masteruser_instance.user_logs
            now = jdatetime.datetime.now()
            dtime = str(now.year)+'-'+str(now.month)+'-'+ str(now.day)+'  '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
            new_log = '''{previous_logs}\n
On {date_time}:\n
Confirmed Salon: {salon}
Related to Sport Club: {sportclub}
-------------------------------------------------------
            '''.format(previous_logs = masteruser_instance_logs,
                       date_time = dtime,
                        salon = str(salon),
                        sportclub = str(salon.sportclub.user.username))
            masteruser_instance.user_logs = new_log
            masteruser_instance.save()
            return HttpResponseRedirect(reverse('sportclub:detail',
                                                kwargs={'slug':salon.sportclub.user.slug}))
        else:
            return HttpResponseRedirect(reverse('sportclub:bannedsportclubexception',
                                                kwargs={'slug':related_user.username}))

    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@masteruser_required
def SalonConfirmView_2(request,pk):
    if request.user.is_masteruser:
        salon = get_object_or_404(SalonModel,pk = pk)
        related_user = salon.sportclub.user
        if salon.sportclub.user.is_active:
            salon.confirm()
            masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
            masteruser_instance_logs = masteruser_instance.user_logs
            now = jdatetime.datetime.now()
            dtime = str(now.year)+'-'+str(now.month)+'-'+ str(now.day)+'  '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
            new_log = '''{previous_logs}\n
On {date_time}:\n
Confirmed Salon: {salon}
Related to Sport Club: {sportclub}
-------------------------------------------------------
            '''.format(previous_logs = masteruser_instance_logs,
                       date_time = dtime,
                        salon = str(salon),
                        sportclub = str(salon.sportclub.user.username))
            masteruser_instance.user_logs = new_log
            masteruser_instance.save()
            return HttpResponseRedirect(reverse('salon:unconfirmedsalonlist'))
        else:
            return HttpResponseRedirect(reverse('sportclub:bannedsportclubexception',
                                                kwargs={'slug':related_user.username}))

    else:
        return HttpResponseRedirect(reverse('login'))



@login_required
@masteruser_required
def SalonBanView(request,pk):
    if request.user.is_masteruser:
        salon = get_object_or_404(SalonModel,pk = pk)
        salon.ban()
        masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
        masteruser_instance_logs = masteruser_instance.user_logs
        now = jdatetime.datetime.now()
        dtime = str(now.year)+'-'+str(now.month)+'-'+ str(now.day)+'  '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        new_log = '''{previous_logs}\n
On {date_time}:\n
Banned Salon: {salon}
Related to Sport Club: {sportclub}
-------------------------------------------------------
        '''.format(previous_logs = masteruser_instance_logs,
                   date_time = dtime,
                    salon = str(salon),
                    sportclub = str(salon.sportclub.user.username))
        masteruser_instance.user_logs = new_log
        masteruser_instance.save()
        return HttpResponseRedirect(reverse('sportclub:detail',
                                            kwargs={'slug':salon.sportclub.user.slug}))
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@masteruser_required
def SalonBanView_2(request,pk):
    if request.user.is_masteruser:
        salon = get_object_or_404(SalonModel,pk = pk)
        salon.ban()
        masteruser_instance = get_object_or_404(UserModel, slug = request.user.slug)
        masteruser_instance_logs = masteruser_instance.user_logs
        now = jdatetime.datetime.now()
        dtime = str(now.year)+'-'+str(now.month)+'-'+ str(now.day)+'  '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
        new_log = '''{previous_logs}\n
On {date_time}:\n
Banned Salon: {salon}
Related to Sport Club: {sportclub}
-------------------------------------------------------
        '''.format(previous_logs = masteruser_instance_logs,
                   date_time = dtime,
                    salon = str(salon),
                    sportclub = str(salon.sportclub.user.username))
        masteruser_instance.user_logs = new_log
        masteruser_instance.save()
        return HttpResponseRedirect(reverse('salon:confirmedsalonlist'))
    else:
        return HttpResponseRedirect(reverse('login'))



@login_required
@masteruser_required
def SalonDetailViewMasterUser(request,pk):
    if request.user.is_masteruser:
        salon = get_object_or_404(SalonModel,pk = pk)
        return render(request,'salon/salondetail_masteruser.html',
                          {'salon_detail':salon})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@masteruser_required
def BanModalView(request,pk):
    if request.user.is_masteruser:
        salon = get_object_or_404(SalonModel,pk = pk)
        return render(request,'salon/banmodal.html',
                          {'salon':salon})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@masteruser_required
def BanModalView_2(request,pk):
    if request.user.is_masteruser:
        salon = get_object_or_404(SalonModel,pk = pk)
        return render(request,'salon/banmodal2.html',
                          {'salon':salon})
    else:
        return HttpResponseRedirect(reverse('login'))


@login_required
@masteruser_required
def ConfirmModalView(request,pk):
    if request.user.is_masteruser:
        salon = get_object_or_404(SalonModel,pk = pk)
        return render(request,'salon/confirmmodal.html',
                          {'salon':salon})
    else:
        return HttpResponseRedirect(reverse('login'))

@login_required
@masteruser_required
def ConfirmModalView_2(request,pk):
    if request.user.is_masteruser:
        salon = get_object_or_404(SalonModel,pk = pk)
        return render(request,'salon/confirmmodal2.html',
                          {'salon':salon})
    else:
        return HttpResponseRedirect(reverse('login'))
