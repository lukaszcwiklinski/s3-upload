from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Upload


class UploadCreateView(CreateView):
    model = Upload
    fields = ['upload', ]
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uploads = Upload.objects.all()
        context['uploads'] = uploads
        return context