from django.shortcuts import render
from .models import Profile
import pdfkit

from django.http import HttpResponse
from django.template import loader
import io
from easy_pdf.views import PDFTemplateResponseMixin
from django.views.generic import DetailView,TemplateView

# Create your views here.
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previous_role = request.POST.get("previous_work","")
        skills = request.POST.get("skills","")

        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_role,skills=skills)
        profile.save()

    return render(request,'pdf/accept.html') 

# def resume(request,id):
#     user_profile = Profile.objects.get(pk=id)
#     template = loader.get_template('pdf/resume.html')
#     html = template.render({'user_profile':user_profile})
#     options = {
#         'page-size':'Letter',
#         'encoding':"UTF-8",

#     }
#     pdf = pdfkit.from_string(html,False,options)
#     response = HttpResponse(pdf,content_type='application/pdf')
#     response['Content-Disposition']='attachment'
#     filename="resume.pdf"

#     return response

class PdfDetail(PDFTemplateResponseMixin,DetailView):
    template_name = 'pdf/resume.html'
    context_object_name = 'user_profile'
    model = Profile

def list(request):
    profiles = Profile.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})

