import os
import subprocess
import uuid

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage



class HomeView(TemplateView):
    template_name = 'base.html'

    def post(self, request, *args, **kwargs):
        file_1 = request.FILES['file_1']
        file_2 = request.FILES['file_2']
        
        os.remove('../media/img/file_1.jpg') 
        os.remove('../media/img/file_2.jpg') 
    
        default_storage.save('img/file_1.jpg', ContentFile(file_1.read()))
        default_storage.save('img/file_2.jpg', ContentFile(file_2.read()))
        result = str(uuid.uuid4())
        com = 'python main.py --src ../media/img/file_1.jpg --dst ../media/img/file_2.jpg --out ../media/result/' + result + '.jpg --correct_color'
        subprocess.run(com, shell=True, check=True)
        context = {
            'img_name': result
        }
        return render(request, 'base.html', context=context)
