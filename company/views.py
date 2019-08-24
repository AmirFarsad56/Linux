from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from django.urls import reverse

#handmade
from company.models import TermsModel
from company.forms import TermsForm
from accounts.decorators import superuser_required



@method_decorator([login_required, superuser_required], name='dispatch')
class CreateTermsView(CreateView):
    model = TermsModel
    form_class = TermsForm
    template_name = 'company/createterms.html'

    def get_success_url(self):
        return reverse('accounts:workspace',kwargs={'slug':self.request.user.slug})


@method_decorator([login_required, superuser_required], name='dispatch')
class UpdateTermsView(UpdateView):
    model = TermsModel
    form_class = TermsForm
    template_name = 'company/updateterms.html'

    def get_success_url(self):
        return reverse('accounts:workspace',kwargs={'slug':self.request.user.slug})
