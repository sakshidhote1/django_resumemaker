import os

from django.http import Http404
from django.shortcuts import render,redirect,HttpResponse
from django.views import View

from resumeuploader import settings
from .forms import ResumeForm
from .models import ResumeModel

# Create your views here.

class HomeView(View):
    def get(self,request):
        form=ResumeForm()
        candidates=ResumeModel.objects.all()
        return render(request,'myapp/home.html',{'candidates':candidates,'form':form})

    def post(self,request):
        form=ResumeForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('myapp/home.html')
        return HttpResponse("Invalid")
class CandidateView(View):
    def get(self,request,pk):
        candidate=ResumeModel.objects.get(pk=pk)
        return render(request,'myapp/candidate.html',{'candidate':candidate})

# def download(request,path):
#     file_path=os.path.join(settings.MEDIA_ROOT,path)
#     if os.path.exists(file_path):
#         with open(file_path,'rb')as fh:
#             response=HttpResponse(fh.read(),content_type="application/candidate")
#             response['Content-Disposition']='inline;filename'+os.path.basename(file_path)
#             return response
#     raise Http404