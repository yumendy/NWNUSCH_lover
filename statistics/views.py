# coding=utf-8
import csv

from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader, Context
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, View
from django.utils import timezone

from statistics.models import Info
from website.mixin import FrontMixin


class InfoCreateView(FrontMixin, CreateView):
    model = Info
    fields = ['name', 'sex', 'birthday', 'grade', 'class_num', 'teacher_name', 'college', 'major', 'city', 'qq_num',
              'wx_num', 'can_long_distance_relationship', 'remarks']
    success_url = reverse_lazy('signup-success')
    template_name_suffix = '_create_form'


class SignupSuccessView(FrontMixin, TemplateView):
    template_name = 'utils/success_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SignupSuccessView, self).get_context_data(*args, **kwargs)
        context['message'] = '报名成功，清耐心等待消息。'
        return context


class InfoListView(UserPassesTestMixin, ListView):
    model = Info
    paginate_by = 30
    template_name = 'statistics/info_list.html'

    def test_func(self):
        return self.request.user.is_staff


class GenCSVView(UserPassesTestMixin, TemplateView):
    login_url = reverse_lazy('user-login')

    def test_func(self):
        return self.request.user.is_staff

    def get(self, request, *args, **kwargs):
        info_list = Info.objects.all()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="名单.csv"'

        writer = csv.writer(response)
        writer.writerow(map(lambda item: item.encode('gbk'),
                            [u'姓名', u'性别', u'届别', u'班级', u'班主任', u'现读学校', u'专业', u'所在城市', u'QQ号', u'微信号', u'是否接受异地恋',
                             u'报名时间', u'其他要求']))

        for info in info_list:
            content = [
                info.name,
                u'男' if info.sex == 'M' else u'女',
                info.grade,
                info.class_num,
                info.teacher_name,
                info.college,
                info.major,
                info.city,
                info.qq_num,
                info.wx_num,
                info.can_long_distance_relationship,
                timezone.make_naive(info.create_time, timezone.get_current_timezone()).strftime('%Y-%m-%d %H:%M:%S'),
                info.remarks
            ]
            writer.writerow(map(lambda x: unicode(x.strip()).encode('gbk'), content))

        return response
