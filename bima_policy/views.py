from django.shortcuts import get_object_or_404,render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect,render
from .models import *
from django.views import View



#loginview
def login_form(request):
    return render(request,'login.html')
def loginView(request):
    if request.method=='POST':
        try:
            full_name = request.POST['full_name']
            password = request.POST['password']
            try:
                user=ProfileModel.objects.get(full_name=full_name,password=password)
                if user is not None:
                    request.session['id']=user.id
                    request.session['full_name']=user.full_name
                    return render(request,'dashboard.html')
            except ProfileModel.DoesNotExist:
                error_message='Invalid ID or Password!'
                return render(request,'login.html',{'error_message':error_message})
        except TypeError:
            return render(request,'dashboard.html')
        # try:
        #         return render(request, 'Dashboard.html')
            
        #     else:
        #         return(request,'login.html')
        #     # elif:
        #     #     user=StaffModel.objects.get(login_id=full_name,password=password)
        #     #     return render(request, 'staffDashboard.html')
        #     # elif:
        #     #     user=Agents.objects.get(login_id=full_name,password=password)
        #     #     return render(request, 'AgentDashboard.html')
        # except ObjectDoesNotExist:
        #     error_message='User ID or Password Invalid!' 
        #     return render(request,'login.html',{'error':error_message})



def getId_from_session(request):
    id=request.session['id']
    return id

def Index(request):
     return render(request, 'index.html')


class staffmanage(View):
    def get(self , request):
        try:
            data = StaffModel.objects.filter(profile_id_id=getId_from_session(request))
            return render(request, 'user.html',{'data':data})
        except StaffModel.DoesNotExist:
            return render(request, 'user.html')

    def post(self,request):
        staffname=request.POST['staffname']
        password=request.POST['password']
        StaffModel.objects.create(staffname=staffname,password=password,profile_id_id=getId_from_session(request))
        return HttpResponseRedirect(request.path,('staff'))

#BankView

def bank_details(request):
    if request.method=="GET":
        try:
            data = BankDetail.objects.filter(profile_id_id=getId_from_session(request))
            return render(request, 'bank_details.html' , {'bankdata':data})
        except BankDetail.DoesNotExist:
            return render(request, 'bank_details.html')
    else:
        try:
            if "bankadd" in request.POST:
                data = ProfileModel.objects.get(id=getId_from_session(request))
                beneficiary_name=request.POST['beneficiary_name']
                acc_no=request.POST['account_number']
                bank_name=request.POST['bank_name']
                BankDetail.objects.create(beneficiary_name=beneficiary_name,acc_no=acc_no,bank_name=bank_name,profile_id=data)
                return HttpResponseRedirect(request.path,('bank_det'))
        except ProfileModel.DoesNotExist:
            return HttpResponseRedirect('error')
    return HttpResponseRedirect(request.path,('bank_det'))  


def delete_bank_details(request,id):
    
    if request.method=="GET":
            data = get_object_or_404(BankDetail,profile_id_id=getId_from_session(request))
            return render(request, 'bank_details.html' , {'bankdata':data})
    else:
        obj = get_object_or_404(BankDetail, id= id)
        if "delete" in request.POST:
            # obj=BankDetail.objects.filter(id=id)
            obj.delete()
            return redirect('bima_policy:bank_det')


class RTOconversion(View):
    def get(self,request):
        data =RtoConversionModel.objects.all()
        return render(request,'RTO.html', {'data':data})
    def post(self,request):
        data =RtoConversionModel.objects.all()
        rtoseries=request.POST['rtoseries']
        rtoreturn=request.POST['rtoreturn']
        RtoConversionModel.objects.create(rto_series=rtoseries,rto_return=rtoreturn)
        return render(request,'RTO.html',{'data':data})


#@login_required(login_url='login/')
def RtoRemove(request,id):
    item = RtoConversionModel.objects.get(id=id)
    item.delete()
    return render(request,'RTO.html')


#@login_required(login_url='login/')
def Profile(request):
    full_name=request.session['full_name']
    data = ProfileModel.objects.filter(full_name=full_name)
    return render(request, 'profile.html',{'data':data})

def logout(request):
    request.session.clear()
    return render(request,'login.html')
#@login_required(login_url='login/')


#@login_required(login_url='login/')
def agent(request):
    data = Agents.objects.all()
    return render(request, 'agent.html', {'data':data})


#@login_required(login_url='login/')
def add(request):
    return render(request,'add_agent.html')


#@login_required(login_url='login/')
def service_p(request):
    data = Service_provider.objects.all()
    return render(request, 'service_provider.html', {'data':data})


#@login_required(login_url='login/')
def add_sp(request):
    return render(request,'add_sp.html')


#@login_required(login_url='login/')
def ins_comp(request):
    data =Insurance_company.objects.all()
    return render(request,'insurance_comp.html', {'data':data})


#@login_required(login_url='login/')
def slab(request):
    data =SLAB.objects.all()
    return render(request,'slab.html', {'data':data})


#@login_required(login_url='login/')
def slab_payout(request):
    data =SLAB.objects.all()
    return render(request,'slab_payoutlist.html', {'data':data})


#@login_required(login_url='login/')

def slab_payoutform(request):
    data =SLAB.objects.all()
    return render(request,'slab_payoutform.html', {'data':data})


#@login_required(login_url='login/')

def create_policy(request):
    return render(request,'policy_list.html')


#@login_required(login_url='login/')

def policy_entry(request):
    return render(request,'policy_entry_list.html')


#@login_required(login_url='login/')

def policy_import(request):
    return render(request,'policy_list_import.html')


#@login_required(login_url='login/')

def upcoming_renewal(request):
    return render(request, 'upcoming_renewal.html')


#@login_required(login_url='login/')

def agentpayable(request):
    return render(request, 'agent_payable.html')


#@login_required(login_url='login/')

def agent_statement(request):
    return render(request, 'agent_statement.html')


#@login_required(login_url='login/')

def sp_receivable(request):
    return render(request, 'SP_recevaible.html')


#@login_required(login_url='login/')

def sp_statement(request):
    return render(request, 'SP_statement.html')


#@login_required(login_url='login/')

def report_agent(request):
    return render(request, 'report_agent.html')


#@login_required(login_url='login/')

def report_policyprovider(request):
    return render(request, 'report_Policyprovider.html')


#@login_required(login_url='login/')

def report_vehicleCategory(request):
    return render(request, 'report_vehicalCategory.html')


#@login_required(login_url='login/')

def report_brokercode(request):
    return render(request, 'report_brokerCode.html')


#@login_required(login_url='login/')

def report_insurance_comp(request):
    return render(request, 'report_insurance_company.html')
    

#@login_required(login_url='login/')

def subscription(request):
    return render(request, 'subscription.html')











#@login_required(login_url='login/')

def Dashboard(request):
    return render(request,'dashboard.html')



def vehicleView(request):
    if request.method=='GET':
        vmb=VehicleMakeBy.objects.all()
        vmn=VehicleModelName.objects.all()
        vc=VehicleCategory.objects.all()
        data ={'vmb':vmb,'vmn':vmn,'vc':vc}
        return render(request,'vehicle.html',{'data':data}) 
    else:
        if 'mb_add' in request.POST:
            vehiclemb=VehicleMakeBy.objects.create(company=request.POST['makeby'])
            vehiclemb.save()
            return render(request,'vehicle.html')

        elif 'vm_add' in request.POST:
            Model=VehicleModelName.objects.create(model=request.POST['model'])
            Model.save()
            return render(request,'vehicle.html')

        elif 'vc_add' in request.POST:
            VehicleCategory.objects.create(category=request.POST['category'])
            return render(request,'vehicle.html')
        return render(request,'vehicle.html')



