from announcement.mixin import LeastAnnouncementMixin
from paste_wall.mixin import PasteStateMixin
from statistics.mixin import InfoStateMixin


class FrontMixin(LeastAnnouncementMixin, PasteStateMixin, InfoStateMixin):
    def get_context_data(self, *args, **kwargs):
        return super(FrontMixin, self).get_context_data(*args, **kwargs)
