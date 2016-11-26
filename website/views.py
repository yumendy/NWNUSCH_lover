from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from website.mixin import FrontMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy


class HomepageView(FrontMixin, TemplateView):
    template_name = 'website/frontend/homepage.html'


class DashboardOverviewView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('user-login')
    template_name = 'website/backend/overview.html'
