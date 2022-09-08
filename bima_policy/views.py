import profile
from django.http import HttpResponse, HttpResponseServerError
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.template.loader import render_to_string
from django.shortcuts import redirect,render
from django.http import JsonResponse
from django.contrib import messages
from django.views import View
from .models import *
from .forms import *

def get_id_from_session(request):
    id=request.session['id']
    return id
def Index(request):
     return render(request, 'index.html')


# DashBoard
def dashboard(request):
    agentcount=Agents.objects.filter(profile_id=get_id_from_session(request)).count()
    staffcount=StaffModel.objects.filter(profile_id=get_id_from_session(request)).count()
    spcount=ServiceProvider.objects.filter(profile_id=get_id_from_session(request)).count()
    policycount=Agents.objects.filter(profile_id=get_id_from_session(request)).count()
    print('total agents are:',agentcount)
    return render(request,'dashboard.html',{'agentcount':agentcount,'staffcount':staffcount,'spcount':spcount,'totalpolicy':policycount})






# LoginView
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
                    return redirect('bima_policy:dashboard')
            except ProfileModel.DoesNotExist:
                error_message='Invalid ID or Password!'
                return render(request,'login.html',{'error_message':error_message})
        except TypeError:
            return redirect('bima_policy:dashboard')

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




# ProfileView
def Profile(request):
    if request.method=="GET":
        try:
            data = ProfileModel.objects.filter(id=get_id_from_session(request))
            return render(request, 'profile/profile.html',{'data':data})
        except ProfileModel.DoesNotExist:
            return HttpResponse('Profile does not exist.')

    elif request.method=='POST' and 'updpassword' in request.POST:
        try:
            profile=ProfileModel.objects.filter(id=get_id_from_session(request))
            password=request.POST['password']
            profile.update(password=password)
            return render(request,'login.html',{'success_message':'Password update successfully!'})
        except ProfileModel.DoesNotExist:
            return HttpResponse('Profile does not exist.')



# UserView
def staffmanage(request):
    if request.method=='GET':
        try:
            data = StaffModel.objects.filter(profile_id=get_id_from_session(request))
            return render(request, 'user/user.html',{'data':data})
        except StaffModel.DoesNotExist:
            return render(request, 'user/user.html')
    else:
        if 'staff_add' in request.POST:
            data = ProfileModel.objects.get(id=get_id_from_session(request))
            staffname=request.POST['staffname']
            password=request.POST['password']
            StaffModel.objects.create(staffname=staffname,password=password,profile_id=data)
            return HttpResponseRedirect(request.path,('staff'))


def staff_edit(request,id):
    if request.method=='GET':
        try:
            data = StaffModel.objects.filter(login_id=id)
            return render(request, 'user/user_edit.html',{'data':data})
        except StaffModel.DoesNotExist:
            return render(request, 'user/user_edit.html')
    else:
        if 'profile' in request.POST:
            StaffModel.objects.filter(login_id=id).update(staffname=request.POST['full_name'],status=request.POST['status'])
        return redirect('bima_policy:staff')




# ProfileView
def bank_details(request):
    if request.method=="GET":
        try:
            data={}
            pdata = ProfileModel.objects.filter(id=get_id_from_session(request))
            bdata = BankDetail.objects.filter(profile_id_id=get_id_from_session(request))
            return render(request, 'profile/bank_details.html' , {'pdata':pdata,'bdata':bdata})
        except BankDetail.DoesNotExist:
            return render(request, 'profile/bank_details.html')
    else:
        try:
            if "bankadd" in request.POST:
                data = ProfileModel.objects.get(id=get_id_from_session(request))
                beneficiary_name=request.POST['beneficiary_name']
                acc_no=request.POST['account_number']
                bank_name=request.POST['bank_name']
                BankDetail.objects.create(beneficiary_name=beneficiary_name, acc_no=acc_no,bank_name=bank_name, profile_id=data)
                return HttpResponseRedirect(request.path,('bank_det'))
        except ProfileModel.DoesNotExist:
            return HttpResponse('error')
    return HttpResponseRedirect(request.path,('bank_det'))  



def delete_bank_details(request,id):
    if request.method=="GET":
        return redirect('bima_policy:bank_det')
    else:
        if "delete" in request.POST:
            # obj=BankDetail.objects.filter(id=id)
            #obj.delete()
            get_object_or_404(BankDetail, id=id).delete()
            return redirect('bima_policy:bank_det')



def change_password(request):
    if request.method=='POST' and 'updpassword' in request.POST:
        profile=ProfileModel.objects.filter(id=get_id_from_session(request))
        password=request.POST['password']
        profile.update(password=password)



# RTOView
def rto_list(request):
    if request.method=="GET":
        data=RtoConversionModel.objects.filter(profile_id_id=get_id_from_session(request))
        return render(request, 'rto/RTO.html', {'data': data})
    if request.method=="POST" and 'rto_add' in request.POST:
        data = ProfileModel.objects.get(id=get_id_from_session(request))
        rtoseries=request.POST['rtoseries']
        rtoreturn=request.POST['rtoreturn']
        RtoConversionModel.objects.create(rto_series=rtoseries,rto_return=rtoreturn,profile_id=data)
        return redirect('bima_policy:rto')

def update_rto(request,id):
    data={}
    if request.method=="GET":
        data = RtoConversionModel.objects.filter(profile_id_id=get_id_from_session(request))
        udata=RtoConversionModel.objects.filter(id=id)
        return render(request, 'RTO.html',{'data':data,'udata':udata})
    if request.method=='POST':
        if "delete" in request.POST:
            item = get_object_or_404(RtoConversionModel, id=id)
            item.delete()
            return redirect('bima_policy:rto')
        # if "rto_update" in request.POST:
        #     item = get_object_or_404(RtoConversionModel, id=id)
        #     RtoConversionModel.objects.filter(id=id).update(rto_series=request.POST['ertoseries'],rto_return=request.POST['ertoreturn'])
        #     return redirect('bima_policy:rto')

# InsuranceView
def ins_comp(request):
    if request.method=="GET":
        try:
            data=InsuranceCompany.objects.filter(profile_id=get_id_from_session(request))
            return render(request,'insurancecompany/insurance_comp.html', {'data':data})
        except ProfileModel.DoesNotExist:
            return render(request,'insurancecompany/insurance_comp.html')
    elif 'company_add' in request.POST:
        try:
            data=ProfileModel.objects.get(id=get_id_from_session(request))
            ins_name=request.POST['inscomp_name']
            status=request.POST['status']
            InsuranceCompany.objects.create(comp_name=ins_name,status=status,profile_id=data)
            return redirect('bima_policy:ins_comp')
        except ProfileModel.DoesNotExist:
            return HttpResponseRedirect(request.path,('bank_det'))

def ins_del(request,id):
    if request.method=='POST' and 'delete' in request.POST:
        data=InsuranceCompany.objects.filter(id=id)
        data.delete()
        return redirect('bima_policy:ins_comp')

# VehicleView
def vehicle_view(request):
    if request.method=="GET":
        try:
            data=VehicleMakeBy.objects.filter(profile_id_id=get_id_from_session(request))
            datamn=VehicleModelName.objects.filter(profile_id_id=get_id_from_session(request))
            datavc=VehicleCategory.objects.filter(profile_id_id=get_id_from_session(request))
            mylist=zip(datamn,data)
            return render(request,'vehicle/vehicle.html',{'list':mylist, 'datavc':datavc, 'data':data,'datamn':datamn})
        except(VehicleMakeBy.DoesNotExist,VehicleModelName.DoesNotExist,VehicleCategory.DoesNotExist):
            return render(request,'vehicle/vehicle.html')
    else:
        p= ProfileModel.objects.get(id=get_id_from_session(request))
        if 'mb_add' in request.POST:
            VehicleMakeBy.objects.create(company=request.POST['makeby'],status = request.POST['mbstatus'],profile_id=p)
            return redirect('bima_policy:vehi')
        elif 'vm_add' in request.POST:
            VehicleModelName.objects.create(model=request.POST['model'],status = request.POST['vmstatus'],profile_id=p)
            return redirect('bima_policy:vehi')
        elif 'vc_add' in request.POST:
            VehicleCategory.objects.create(category=request.POST['category'],status = request.POST['vcstatus'],profile_id=p)
            return redirect('bima_policy:vehi')
        return redirect('bima_policy:vehi')

def delete_vehicle(request,id):
    if request.method=="POST" and 'delete' in request.POST:
        data1=VehicleCategory.objects.filter(id=id)
        data2=VehicleMakeBy.objects.filter(id=id)
        data3=VehicleModelName.objects.filter(id=id)
        if data1:
            data1.delete()
        elif data2:
            data2.delete()
        elif data3:
            data3.delete()
        return redirect('bima_policy:vehi')
    elif request.method=="POST" and 'edit' in request.POST:
        return edit_vehicle(request,id)

def edit_vehicle(request,id):
    data={}
    vcd=VehicleCategory.objects.filter(id=id)
    vmbd=VehicleMakeBy.objects.filter(id=id)
    vmd=VehicleModelName.objects.filter(id=id)
    if request.method=="GET" :
        if vcd:
            data['vcd']=VehicleCategory.objects.filter(id=id)
        elif vmbd:
            data['vmbd']=VehicleMakeBy.objects.filter(id=id)
        elif vmd:
            data['vmd']=VehicleModelName.objects.filter(id=id)
        return render(request,'vehicle/vehicle_edit.html',{'data':data})
    # elif request.method=="POST" and 'edit' in request.POST:
    #     vcd=VehicleCategory.objects.filter(id=id)
    #     vmbd=VehicleMakeBy.objects.filter(id=id)
    #     vmd=VehicleModelName.objects.filter(id=id)
    #     if data1:



# ServiceProviderView
def service_provider(request):
    if request.method=="GET":
        try:
            brokerdata = BrokerCode.objects.filter(profile_id_id = get_id_from_session(request))
            data = ServiceProvider.objects.filter(profile_id_id = get_id_from_session(request))
            return render(request,'serviceprovider/service_provider.html',{'data':data, 'brokerdata':brokerdata})  
        except (ServiceProvider.DoesNotExist , BrokerCode.DoesNotExist):
            return render(request,'serviceprovider/service_provider.html') 
    else:
        if 'code_add' in request.POST: 
            data =ProfileModel.objects.get(id = get_id_from_session(request))
            code=request.POST['code']
            status=request.POST['status']
            BrokerCode.objects.create(code=code,status=status,profile_id=data)
            return redirect('bima_policy:service_p')


def add_sp(request):
    if request.method=="GET":
        data =ServiceProvider.objects.all()
        return render(request,'serviceprovider/add_sp.html', {'data':data})
    else:
       if 'subbtn' in request.POST: 
            p=ProfileModel.objects.get(id=get_id_from_session(request))
            data =ServiceProvider.objects.filter(profile_id_id=get_id_from_session(request))
            full_name=request.POST['full_name']
            email_id=request.POST['email_id']
            phone=request.POST['phone']
            address=request.POST['address']
            state=request.POST['state']
            city=request.POST['city']
            gstin=request.POST['gstin']
            pan=request.POST['pan']
            ServiceProvider.objects.create(full_name=full_name, email_id=email_id, mob_no=phone, address=address, state= state, city=city, GSTIN=gstin,PAN=pan,profile_id=p)
            return render(request,'serviceprovider/service_provider.html')



# def save_product_form(request, form, template_name):
#     data = dict()
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             data['form_is_valid'] = True
#             products = RtoConversionModel.objects.filter(profile_id_id=get_id_from_session(request))
#             data['html_product_list'] = render_to_string('includes/partial_product_list.html', {
#                 'products' : products
#             })
#         else:
#             data['form_is_valid'] = False
#     context = {'form' : form}
#     data['html_form'] = render_to_string(template_name, context, request=request)
#     return JsonResponse(data)

 
# def product_create(request):
#     if request.method == 'POST':
#         form = RtoForm(request.POST)
#     else:
#         form = RtoForm()
#     return save_product_form(request, form, 'includes/partial_product_create.html')

# def product_update(request, pk):
#     product = get_object_or_404(RtoConversionModel, id=pk)
#     if request.method == 'POST':
#         form = RtoForm(request.POST, instance=product)
#     else:
#         form = RtoForm(instance=product)
#     return save_product_form(request, form, 'includes/partial_product_update.html')
 
 
# def product_delete(request, pk):
#     product = get_object_or_404(RtoConversionModel, id=pk)
#     data = dict()
#     if request.method == 'POST':
#         product.delete()
#         data['form_is_valid'] = True
#         products = RtoConversionModel.objects.filter(profile_id_id=get_id_from_session(request))
#         data['html_product_list'] = render_to_string('includes/partial_product_list.html', {
#             'products': products
#         })
#     else:
#         context = {'product': product}
#         data['html_form'] = render_to_string('includes/partial_product_delete.html', context, request=request)
#     return JsonResponse(data)







    # if request.method=="GET":
    #     try:
    #         data = RtoConversionModel.objects.filter(profile_id_id=get_id_from_session(request))
    #         return render(request, 'RTO.html',{'data':data})
    #     except BankDetail.DoesNotExist:
    #         return render(request, 'RTO.html')
    # if request.method=="POST" and 'rto_add' in request.POST:
    #     data = ProfileModel.objects.get(id=get_id_from_session(request))
    #     if form.
    #     RtoConversionModel.objects.create(rto_series=rtoseries,rto_return=rtoreturn,profile_id=data)
    # return redirect('bima_policy:rto_conv')
    


class create_policy(View):
    def get(self,request):
        data=InsuranceCompany.objects.filter(profile_id=get_id_from_session(request))
        datasp=ServiceProvider.objects.filter(profile_id=get_id_from_session(request))
        databc=BrokerCode.objects.filter(profile_id=get_id_from_session(request))
        datamb=VehicleMakeBy.objects.filter(profile_id=get_id_from_session(request))
        datavm=VehicleModelName.objects.filter(profile_id=get_id_from_session(request))
        datavc=VehicleCategory.objects.filter(profile_id=get_id_from_session(request))
        datag=Agents.objects.filter(profile_id=get_id_from_session(request))
        # mylist=zip(datamn,data)
        # return render(request,'vehicle.html',{'listt':mylist, 'datavc':datavc, 'data':data})
        return render(request,'policylist/policy_list.html',{'data':data,'datasp':datasp,'databc':databc,'datamb':datamb, 'datavm':datavm, 'datavc':datavc,'datag':datag})
    def post(self,request):
            policy_no=request.POST['policy_no']
            registration=request.POST['registration']
            case_type=request.POST['case_type']
            ins_company=request.POST['ins_company']
            service_provider=request.POST['service_provider']
            code=request.POST['code']
            issue_date=request.POST['issue_date']
            risk_date=request.POST['risk_date']
            cpa=request.POST['cpa']
            document=request.FILES['document']
            fs=FileSystemStorage()
            fs.save(document.name, document)
            previous_policy=request.FILES.get('previous_policy')
            fs1=FileSystemStorage()
            fs1.save(previous_policy.name, previous_policy)
            vehicle_rc=request.FILES.get('vehicle_rc')
            fs2=FileSystemStorage()
            fs2.save(vehicle_rc.name, vehicle_rc)
            vehicle_makeby=request.POST['vehicle_makeby']
            vehicle_model=request.POST['vehicle_model']
            vehicle_category=request.POST['vehicle_category']
            vehicle_other_info=request.POST['vehicle_other_info']
            fuel_type=request.POST['fuel_type']
            manu_year=request.POST['manu_year']
            engine_no=request.POST['engine_no']
            chasis_no=request.POST['chasis_no']
            agent=request.POST['agent']
            cust_name=request.POST['cust_name']
            remarks=request.POST['remarks']
            od=request.POST['od']
            tp=request.POST['tp']
            gst=request.POST['gst']
            net=request.POST['total']
            payment_mode=request.POST['payment_mode']
            total=request.POST['total']
            policy_type=request.POST.get('policy_type')
            Policy.objects.create(policy_no=policy_no, registration_no=registration, casetype=case_type, insurance_comp=ins_company, sp_name=service_provider, sp_brokercode=code, issueDate=issue_date,riskDate=risk_date,
            CPA=cpa,insurance=document, previous_policy=previous_policy,vehicle_rc=vehicle_rc,vehicle_makeby=vehicle_makeby,vehicle_model=vehicle_model, vehicle_category=vehicle_category,other_info=vehicle_other_info,
            vehicle_fuel_type=fuel_type,manufature_year=manu_year,engine_no= engine_no,chasis_no=chasis_no,agent_name=agent,customer_name=cust_name,remark=remarks,OD_premium=od,
            TP_premium=tp,GST=gst,net=net,payment_mode=payment_mode,total=total,policy_type=policy_type)
            return HttpResponseRedirect(request.path,('policy_list'))
# mydata = Members.objects.all().order_by('lastname', '-id').values()
# mydata = Members.objects.all().order_by('-firstname').values()
def policy_entry(request):
    data = Policy.objects.all().order_by('-policyid').values()
    datag=Agents.objects.all()
    return render(request, 'policy_entry_list.html',{'data':data ,'datag':datag})

def policy_delete(request, id):
    if request.method=='post' and 'Remove' in request.POST:
        Policy.objects.filter(policyid=id).delete()
    return redirect('bima_policy:policy_entry')


def logout(request):
    request.session.clear()
    return render(request,'login.html')




def agent(request):
    data = Agents.objects.filter(profile_id=get_id_from_session(request))
    return render(request, 'agents/agent.html', {'data':data})



def add_agent(request):
    try:
        if request.method=="GET":
            Adata=Slab.objects.filter(profile_id=get_id_from_session(request))
            data =Agents.objects.filter(profile_id=get_id_from_session(request))
            return render(request,'agents/add_agent.html', {'data':data,'Adata':Adata})
    except Agents.DoesNotExist:
        return render(request, 'agents/add_agent.html')
    else:
        if 'subagent' in request.POST: 
            data =ProfileModel.objects.get(id=get_id_from_session(request))
            full_name=request.POST['full_name']
            email_id=request.POST['email_id']
            phone=request.POST['phone']
            address=request.POST['address']
            state=request.POST['state']
            city=request.POST['city']
            agent_slab=request.POST['agent_slab']
            gstin=request.POST['gstin']
            pan=request.POST['pan']
            docs=request.POST.get('docs')
            password=request.POST['password']
            # a=Agents.objects.get(full_name=full_name)
            # if full_name==Agents.objects.get(full_name=a.full_name):
            #     error_message="Full Name already exist! Please enter unique name to continue..."
            #     return redirect('bima_policy:add_agent',{'error_message':error_message})
            # else:
            Agents.objects.create(full_name=full_name, email_id=email_id, mob_no=phone, address=address, state= state, city=city,slab=agent_slab, GSTIN=gstin,PAN=pan,document=docs,password=password ,profile_id=data)
            # return render(request,'agent.html',{'data':data})
            messages.success(request, 'Successfully added agent!')
            return redirect('bima_policy:agent')









# PayoutView
def slab(request):
    if request.method=="GET":
        try:
            data =Slab.objects.filter(profile_id=get_id_from_session(request))
            return render(request,'payout/slab.html', {'data':data})
        except Slab.DoesNotExist:
            return render(request,'payout/slab.html')
    else :
        try:
            if 'slab_add' in request.POST:
                profile=ProfileModel.objects.get(id=get_id_from_session(request))
                slab_name=request.POST['slab']
                Slab.objects.create(slab_name=slab_name,profile_id=profile)
                return redirect('bima_policy:slab')
            # if 'slab_remove' in request.POST:

        except ProfileModel.DoesNotExist:
            return redirect('bima_policy:slab')

def slab_delete(request,id):
    data=Slab.objects.filter(slab_name=id)
    data.delete()
    return redirect('bima_policy:slab')
def slab_edit(request,id):
    data=Slab.objects.filter(slab_name=id)
    if request.method=='GET':
        return render(request,'payout/payoutname_edit.html',{'data':data})
    else:
        slab_name=request.POST['slab_name']
        status=request.POST['stauts']
        Slab.objects.filter(slab_name=id).update(slab_name=slab_name,status=status)
        return redirect('bima_policy:slab') 

def slab_payout(request,id):
    if request.method=='GET':
        try:
            data=Payout.objects.filter(profile_id=get_id_from_session(request))
            data1=data.filter(slab_name=id)
            print(data1)
            return render(request,'payout/slab_payoutlist.html', {'data1':data1})
        except Payout.DoesNotExist:
            return render(request,'payout/slab_payoutlist.html')


def slab_payoutform(request):
    if request.method=="GET":
        pol_provider=ServiceProvider.objects.filter(profile_id=get_id_from_session(request))
        ins_comp=InsuranceCompany.objects.filter(profile_id=get_id_from_session(request))
        vcat=VehicleCategory.objects.filter(profile_id=get_id_from_session(request))
        vmb=VehicleMakeBy.objects.filter(profile_id=get_id_from_session(request))
        vmodel=VehicleModelName.objects.filter(profile_id=get_id_from_session(request))
        slab = Slab.objects.filter(profile_id=get_id_from_session(request))
        return render(request,'payout/slab_payoutform.html', {'slab': slab,'vcat':vcat,'vmb':vmb,'vmodel':vmodel,'ins_comp':ins_comp,'pol_provider':pol_provider})

    if request.method=='POST' and 'savepayout' in request.POST:
        data=ProfileModel.objects.get(id=get_id_from_session(request))
        payoutName=request.POST['payout_name']
        slab=request.POST['slab']
        s=Slab.objects.get(slab_name=slab)
        status=request.POST['status']
        vehicle_category=request.POST['vehicle_category']
        Insurance_company=request.POST['ins_com']
        policy_provider=request.POST['policy_provider']
        vehicle_make_by=request.POST['vehicle_make_by']
        rtos=request.POST['rtos']
        casetype=request.POST['casetype']
        coverage=request.POST['coverage']
        fueltype=request.POST['fueltype']
        cpa=request.POST['cpa']
        rewards_on=request.POST['areward_on']
        rewards_age=request.POST['areward_pct']
        self_rewards_on=request.POST['sreward_on']
        self_rewards_age=request.POST['sreward_pct']
        Payout.objects.create(payout_name=payoutName,slab_name=s,status=status,vehicle_category=vehicle_category,Insurance_company=Insurance_company,policy_provider=policy_provider,vehicle_make_by=vehicle_make_by,rto=rtos,case_type=casetype,coverage=coverage,fuel_type=fueltype,cpa=cpa,rewards_on=rewards_on,rewards_age=rewards_age,self_rewards_on=self_rewards_on,self_rewards_age=self_rewards_age,profile_id=data)
        return redirect('bima_policy:slab')






def policy_entry(request):
    data = Policy.objects.all()
    datag=Agents.objects.all()
    return render(request, 'policylist/policy_entry_list.html',{'data':data ,'datag':datag})



def policy_import(request):
    if request.method=='GET':
        return render(request,'policylist/policy_list_import.html')
    else:
        if 'submitup' in request.POST:
            fcsv=request.FILES.get('fcsv')
            fs=FileSystemStorage()
            fs.save(fcsv.name, fcsv)
            InsuranceUpload.objects.create(ins_upload=fcsv)
            messages.success(request, 'Insurance upload succefully......')
            return HttpResponseRedirect(request.path,('policy_list/policy_list_import'))




def upcoming_renewal(request):
    return render(request, 'upcomingrenewal/upcoming_renewal.html')




def agentpayable(request):
    return render(request, 'ledger/agent_payable.html')




def agent_statement(request):
    return render(request, 'ledger/agent_statement.html')




def sp_receivable(request):
    return render(request, 'ledger/SP_recevaible.html')




def sp_statement(request):
    return render(request, 'ledger/SP_statement.html')




def report_agent(request):
    return render(request, 'reports/report_agent.html')




def report_policyprovider(request):
    return render(request, 'reports/report_Policyprovider.html')




def report_vehicleCategory(request):
    return render(request, 'reports/report_vehicalCategory.html')




def report_brokercode(request):
    return render(request, 'reports/report_brokerCode.html')




def report_insurance_comp(request):
    return render(request, 'reports/report_insurance_company.html')
    



def subscription(request):
    return render(request, 'subscription.html')


def agent_profile(request):
    return render(request,'agents/agent_particular.html')

