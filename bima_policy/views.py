from urllib import request
from django.http import HttpResponse, HttpResponseServerError
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.template.loader import render_to_string
from django.shortcuts import redirect,render
from django.http import JsonResponse
from django.contrib import messages
from .models import *
from .forms import *


#LoginView
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

def get_id_from_session(request):
    id=request.session['id']
    return id

def Index(request):
     return render(request, 'index.html')



#ProfileView
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



#UserView
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




#ProfileView
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




#RTOView
def rto_list(request):
    if request.method=="GET":
        data=RtoConversionModel.objects.filter(profile_id_id=get_id_from_session(request))
        return render(request, 'rto/RTO.html', {'data': data})




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



def vehicle_view(request):
    if request.method=="GET":
        try:
            data=VehicleMakeBy.objects.filter(profile_id_id=get_id_from_session(request))
            datamn=VehicleModelName.objects.filter(profile_id_id=get_id_from_session(request))
            datavc=VehicleCategory.objects.filter(profile_id_id=get_id_from_session(request))
            mylist=zip(datamn,data)
            return render(request,'vehicle/vehicle.html',{'list':mylist, 'datavc':datavc, 'data':data})
        except(VehicleMakeBy.DoesNotExist,VehicleModelName.DoesNotExist,VehicleCategory.DoesNotExist):
            return render(request,'vehicle/vehicle.html')
    else:
        p= ProfileModel.objects.get(id=get_id_from_session(request))
        if 'mb_add' in request.POST:
            VehicleMakeBy.objects.create(company=request.POST['makeby'],status=request.POST['mbstatus'],profile_id=p)
            return redirect('bima_policy:vehi')
        elif 'vm_add' in request.POST:
            VehicleModelName.objects.create(model=request.POST['model'],status=request.POST['vmstatus'],profile_id=p)
            return redirect('bima_policy:vehi')
        elif 'vc_add' in request.POST:
            VehicleCategory.objects.create(category=request.POST['category'],status=request.POST['vcstatus'],profile_id=p)
            return redirect('bima_policy:vehi')
        return redirect('bima_policy:vehi')


#ServiceProviderView
def service_provider(request):
    if request.method=="GET":
        try:
            data = ServiceProvider.objects.filter(profile_id_id = get_id_from_session(request))
            datab = BrokerCode.objects.filter(profile_id_id = get_id_from_session(request))
            return render(request,'serviceprovider/service_provider.html',{'data':data, 'datab':datab})  
        except (ServiceProvider.DoesNotExist , BrokerCode.DoesNotExist):
            return render(request,'serviceprovider/service_provider.html') 
    else:
        if 'code_add' in request.POST: 
            data =BrokerCode.objects.filter()
            code=request.POST['code']
            status=request.POST['status']
            BrokerCode.objects.create(code=code,status=status)
            return redirect('service_provider')

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
    
# def update_rto(request,id):
#     data={}
#     if request.method=="GET":
#         data = RtoConversionModel.objects.filter(profile_id_id=get_id_from_session(request))
#         udata=RtoConversionModel.objects.filter(id=id)
#         return render(request, 'RTO.html',{'data':data,'udata':udata})
#     if request.method=='POST':
#         if "delete" in request.POST:
#             item = get_object_or_404(RtoConversionModel, id=id)
#             item.delete()
#             return redirect('bima_policy:rto_conv')
#         if "rto_update" in request.POST:
#             item = get_object_or_404(RtoConversionModel, id=id)
#             RtoConversionModel.objects.filter(id=id).update(rto_series=request.POST['ertoseries'],rto_return=request.POST['ertoreturn'])
#             return redirect('bima_policy:rto_conv')

def create_policy(request):
    if request.method== "GET":
        data=InsuranceCompany.objects.all()
        datasp=ServiceProvider.objects.all()
        databc=BrokerCode.objects.all()
        datamb=VehicleMakeBy.objects.all()
        datavm=VehicleModelName.objects.all()
        datavc=VehicleCategory.objects.all()
        datag=Agents.objects.all()
        # mylist=zip(datamn,data)
        # return render(request,'vehicle.html',{'listt':mylist, 'datavc':datavc, 'data':data})
        return render(request,'policylist/policy_list.html',{'data':data,'datasp':datasp,'databc':databc,'datamb':datamb, 'datavm':datavm, 'datavc':datavc,'datag':datag})   
    else:
            policy_no=request.POST['policy_no']
            registration=request.POST['registration']
            case_type=request.POST['case_type']
            ins_company=request.POST['ins_company']
            service_provider=request.POST['service_provider']
            code=request.POST['code']
            issue_date=request.POST['issue_date']
            risk_date=request.POST['risk_date']
            cpa=request.POST['cpa']
            document=request.FILES.get('document')
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
            policy_type=request.POST['policy_type']
            Policy.objects.create(policy_no=policy_no, registration_no=registration, casetype=case_type, insurance_comp=ins_company, sp_name=service_provider, sp_brokercode=code, issueDate=issue_date,riskDate=risk_date,
            CPA=cpa,insurance=document, previous_policy=previous_policy,vehicle_rc=vehicle_rc,vehicle_makeby=vehicle_makeby,vehicle_model=vehicle_model, vehicle_category=vehicle_category,other_info=vehicle_other_info,
            vehicle_fuel_type=fuel_type,manufature_year=manu_year,engine_no= engine_no,chasis_no=chasis_no,agent_name=agent,customer_name=cust_name,remark=remarks,OD_premium=od,
            TP_premium=tp,GST=gst,net=net,payment_mode=payment_mode,total=total,policy_type=policy_type)
            return HttpResponseRedirect(request.path,('policy_list'))


def logout(request):
    request.session.clear()
    return render(request,'login.html')




def agent(request):
    data = Agents.objects.all()
    return render(request, 'agents/agent.html', {'data':data})



def add_agent(request):
    try:
        if request.method=="GET":
            data =Agents.objects.filter(profile_id=get_id_from_session(request))
            return render(request,'agents/add_agent.html', {'data':data})
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
            Agents.objects.create(full_name=full_name, email_id=email_id, mob_no=phone, address=address, state= state, city=city,slab=agent_slab, GSTIN=gstin,PAN=pan,document=docs,password=password ,profile_id=data)
            # return render(request,'agent.html',{'data':data})
            messages.success(request, 'Successfully added agent!')
            return redirect('bima_policy:agent')










def slab(request):
    data =SLAB.objects.all()
    return render(request,'payout/slab.html', {'data':data})



def slab_payout(request):
    data =SLAB.objects.all()
    return render(request,'payout/slab_payoutlist.html', {'data':data})




def slab_payoutform(request):
    data =SLAB.objects.all()
    return render(request,'payout/slab_payoutform.html', {'data':data})






def policy_entry(request):
    return render(request,'policylist/policy_entry_list.html')




def policy_import(request):
    return render(request,'policylist/policy_list_import.html')




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




# def vehicleView(request):
#     if request.method=='GET':
#         vmb=VehicleMakeBy.objects.all()
#         vmn=VehicleModelName.objects.all()
#         vc=VehicleCategory.objects.all()
#         data ={'vmb':vmb,'vmn':vmn,'vc':vc}
#         return render(request,'vehicle.html',{'data':data}) 
#     else:
#         if 'mb_add' in request.POST:
#             vehiclemb=VehicleMakeBy.objects.create(company=request.POST['makeby'])
#             vehiclemb.save()
#             return render(request,'vehicle.html')

#         elif 'vm_add' in request.POST:
#             Model=VehicleModelName.objects.create(model=request.POST['model'])
#             Model.save()
#             return render(request,'vehicle.html')

#         elif 'vc_add' in request.POST:
#             VehicleCategory.objects.create(category=request.POST['category'])
#             return render(request,'vehicle.html')
#         return render(request,'vehicle.html')
