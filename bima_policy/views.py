from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views import View

from .models import *
# Create your views here.


def Index(request):
     return render(request, 'index.html')

# def Profile(request):
#     return render(request, 'profile.html')

def Profile(request):
    data = profile.objects.all()
    # print(data)
    return render(request, 'profile.html',{'data':data})

def bank_det(request):
    data = profile.objects.all()
    # print(data)
    return render(request, 'bank_details.html',{'data':data})

def Dashboard(request):
    return render(request,'dashboard.html')


def staff(request):
    data = bima_user.objects.all()
    return render(request, 'user.html',{'data':data})

def agent(request):
    data = Agents.objects.all()
    return render(request, 'agent.html', {'data':data})

def add(request):
    return render(request,'add_agent.html')


def service_p(request):
    data = Service_provider.objects.all()
    return render(request, 'service_provider.html', {'data':data})

def add_sp(request):
    return render(request,'add_sp.html')



def ins_comp(request):
    data =Insurance_company.objects.all()
    return render(request,'insurance_comp.html', {'data':data})

def rto_conv(request):
    data =RTO_conversion.objects.all()
    return render(request,'RTO.html', {'data':data})


def slab(request):
    data =SLAB.objects.all()
    return render(request,'slab.html', {'data':data})

def slab_payout(request):
    data =SLAB.objects.all()
    return render(request,'slab_payoutlist.html', {'data':data})

def slab_payoutform(request):
    data =SLAB.objects.all()
    return render(request,'slab_payoutform.html', {'data':data})

def create_policy(request):
    return render(request,'policy_list.html')
    # data =SLAB.objects.all()
    # return render(request,'slab_payoutform.html', {'data':data})

def policy_entry(request):
    return render(request,'policy_entry_list.html')

def policy_import(request):
    return render(request,'policy_list_import.html')

def upcoming_renewal(request):
    return render(request, 'upcoming_renewal.html')

class login(View):
    
    def get(self,request):
        return render(request,'login.html')
        
    def post(self,request):

        full_name = request.POST['full_name']
        password = request.POST['password']
        error_message=None
        user = profile.objects.get(full_name=full_name,password=password)
        if user is not None:
            return render(request, 'dashboard.html')
        else:
            error_message='full_name or password invalid!' 
            return render(request,'login.html',{'error':error_message})


# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('bima_policy/' + load_template)
#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('bima_policy/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('bima_policy/page-500.html')
#         return HttpResponse(html_template.render(context, request))

class vehicle(View):
    def get(self,request):
        data = VehicleMakeBy.objects.all()
        return render(request,'vehicle.html',{'data':data})

    def post(self,request):
        if 'mb_add' in request.POST:
            vmb=VehicleMakeBy()
            company=request.POST['makeby']
            status=request.POST['mbstatus']
            vmb.company=company
            vmb.status=status
            vmb.save()
            return render(request,'vehicle.html')

        elif 'vm_add' in request.POST:
            model=request.POST['model']
            status=request.POST['vmstatus']
            VehicleModelName.objects.create(model=model,status=status)
            return render(request,'vehicle.html')

        elif 'vc_add' in request.POST:
            category=request.POST['category']
            status=request.POST['vcstatus']
            VehicleCategory.objects.create(category=category,status=status)
            return render(request,'vehicle.html')
        return render(request,'vehicle.html')



