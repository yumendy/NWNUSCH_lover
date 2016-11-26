from paste_wall.models import Paste


class PasteStateMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(PasteStateMixin, self).get_context_data(*args, **kwargs)
        context['paste_number'] = Paste.objects.count()
        context['real_name_paste_number'] = Paste.objects.filter(is_anonymous=False).count()
        context['anonymous_name_paste_number'] = Paste.objects.filter(is_anonymous=True).count()
        context['unchecked_paste_number'] = Paste.objects.filter(is_checked=False).count()
        return context