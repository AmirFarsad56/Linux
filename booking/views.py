from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

#handmade
from booking.models import ProfitPercentageModel
from commonuser.decorators import commonuser_required
from accounts.decorators import superuser_required
from session.models import SessionModel



@method_decorator([login_required, superuser_required], name='dispatch')
class CreateProfitPercentageView(CreateView):
    model = ProfitPercentageModel
    fields = ('profit_percentage',)
    template_name = 'booking/createprofitpercentage.html'

    def get_success_url(self):
        return reverse('accounts:profile',kwargs={'slug':self.request.user.slug})


@method_decorator([login_required, superuser_required], name='dispatch')
class UpdateProfitPercentageView(UpdateView):
    model = ProfitPercentageModel
    fields = ('profit_percentage',)
    template_name = 'booking/updateprofitpercentage.html'

    def get_success_url(self):
        return reverse('accounts:profile',kwargs={'slug':self.request.user.slug})


@login_required
@commonuser_required
def BookingView(request,pk):
    session = get_object_or_404(SessionModel, pk = pk)
    session.is_booked = True
    session.booker = request.user
    session.save()
    return HttpResponseRedirect(reverse('session:all_sessions_list'))
