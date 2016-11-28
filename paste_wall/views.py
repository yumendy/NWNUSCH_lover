# coding=utf-8
from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.template import loader, Context
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic import TemplateView

from paste_wall.models import Paste
from website.mixin import FrontMixin
import logging

logger = logging.getLogger(__name__)


class PasteCreateView(FrontMixin, CreateView):
    model = Paste
    fields = ['content', 'name', 'grade', 'class_num', 'email', 'author', 'is_anonymous']
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('paste-success')

    def form_valid(self, form):
        form.instance.author_ip = self.request.META.get('REMOTE_ADDR', '0.0.0.0')
        return super(PasteCreateView, self).form_valid(form)


class UncheckedPasteView(UserPassesTestMixin, ListView):
    login_url = reverse_lazy('user-login')
    paginate_by = 20
    template_name = 'paste_wall/unchecked_paste_list.html'
    context_object_name = 'paste_list'
    model = Paste

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        return Paste.objects.filter(is_checked=False)


class PassCheckView(UserPassesTestMixin, FormView):
    login_url = reverse_lazy('user-login')

    def test_func(self):
        return self.request.user.is_staff

    def post(self, request, *args, **kwargs):
        paste = Paste.objects.get(pk=kwargs['pk'])
        paste.is_checked = True
        paste.save()
        email_content = loader.get_template('paste_wall/email_template.html').render(Context({'paste': paste}))
        result = None
        if paste.email:
            try:
                result = send_mail(
                    u'%s,[附中人社][十日CP活动]有人向你表白啦！' % paste.name,
                    email_content,
                    settings.EMAIL_HOST_USER,
                    [paste.email],
                    fail_silently=False,
                    html_message=email_content
                )
            except Exception as e:
                logger.error('[EMAIL ERROR]: ' + unicode(e))
        return JsonResponse({'state': 'success', 'email_result': result})


class PasteListView(UserPassesTestMixin, ListView):
    login_url = reverse_lazy('user-login')
    paginate_by = 20
    template_name = 'paste_wall/paste_list.html'
    context_object_name = 'paste_list'
    model = Paste

    def test_func(self):
        return self.request.user.is_staff


class PasteTimeLineView(FrontMixin, ListView):
    model = Paste
    paginate_by = 30
    template_name = 'paste_wall/paste_time_line.html'
    context_object_name = 'paste_list'

    def get_queryset(self):
        return Paste.objects.filter(is_checked=True)


class PasteSuccessView(FrontMixin, TemplateView):
    template_name = 'utils/success_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PasteSuccessView, self).get_context_data(*args, **kwargs)
        context['message'] = '发表成功，待管理员审核后展示。'
        return context
