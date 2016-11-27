from statistics.models import Info


class InfoStateMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(InfoStateMixin, self).get_context_data(*args, **kwargs)
        context['people_number'] = Info.objects.count()
        context['male_number'] = Info.objects.filter(sex='M').count()
        context['female_number'] = context['people_number'] - context['male_number']
        if context['people_number'] != 0:
            context['female_rate'] = "%.2f%%" % ((context['female_number'] * 1.0 / context['people_number']) * 100)
            context['male_rate'] = "%.2f%%" % ((context['male_number'] * 1.0 / context['people_number']) * 100)
        else:
            context['female_rate'] = "%.2f%%" % 0
            context['male_rate'] = "%.2f%%" % 0
        return context
