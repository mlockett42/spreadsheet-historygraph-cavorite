# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

class LandingPageView(LoginRequiredMixin, TemplateView):

    template_name = "landingpage.html"

    def get_context_data(self, **kwargs):
        context = super(LandingPageView, self).get_context_data(**kwargs)
        context['boot_file'] = 'boot_spreadsheet.py'
        context['current_user_public_key'] = self.request.user.public_key
        return context


