import subprocess

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


class HomeView(TemplateView):
    template_name = 'base.html'

    def post(self, request, *args, **kwargs):
        # subprocess.run('python main.py --src imgs/test6.jpg --dst imgs/test7.jpg --out ../media/output6_7.jpg --correct_color', shell=True, check=True)
        file_1 = request.FILES['file_1']
        file_2 = request.FILES['file_2']

        default_storage.save('imgs/file_1.jpg', ContentFile(file_1.read()))
        default_storage.save('imgs/file_2.jpg', ContentFile(file_2.read()))
        return HttpResponse('Hello, World!')
