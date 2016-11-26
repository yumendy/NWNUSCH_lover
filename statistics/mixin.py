from statistics.models import Info


class InfoStateMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(InfoStateMixin, self).get_context_data(*args, **kwargs)
        context['people_number'] = Info.objects.count()
        context['male_number'] = Info.objects.filter(sex='M').count()
        context['female_number'] = context['people_number'] - context['male_number']
        return context
