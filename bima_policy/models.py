from djongo import models
# from django import forms
# Create your models here.

class bima_user(models.Model):
    sr_no = models.IntegerField
    login_id = models.CharField(max_length=50)
    staffname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    cnfmpwd= models.CharField(max_length=20)
    status= models.CharField(default='active', max_length=20)
    # class Meta:
    #     abstract = True
        
# # class Bima_Form(forms.ModelForm):
# #     class Meta:
# #         model = bima_user
# #         fields = (
# #             'sr_no', 'login_id','staffname','username','password','cnfmpassword',''
# #         )
class profile(models.Model):
    _id = models.ObjectIdField()
    full_name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=30)
    mob_no = models.IntegerField()
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    cnfmpassword= models.CharField(max_length=20)
    beneficiary_name=models.CharField(max_length=50)
    acc_no = models.IntegerField()
    bank_name= models.CharField(max_length=50)
    package_GB=models.CharField(max_length=10)
    package_MB=models.CharField(max_length=10)
    package_duration=models.CharField(max_length=10)
    
    def __str__(self):
        return self.full_name
    
    def get_user(self):
        if profile.objects.filter(full_name=self.full_name,password=self.password):
            return True
        else:
            return False

class Agents(models.Model):
    sr_no = models.IntegerField()
    login_id = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    cnfmpwd= models.CharField(max_length=20)
    mob_no = models.IntegerField()
    email_id = models.EmailField(max_length=30)
    address=models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    slab=models.CharField(max_length=100)
    GSTIN=models.CharField(max_length=100)
    PAN=models.CharField(max_length=100)
    document=models.FileField()
    status= models.CharField(default='active', max_length=20)

class Service_provider(models.Model):
    # sr_no = models.IntegerField()
    # login_id = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    # password = models.CharField(max_length=20)
    # cnfmpwd= models.CharField(max_length=20)
    mob_no = models.IntegerField()
    email_id = models.EmailField(max_length=30)
    address=models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    GSTIN=models.CharField(max_length=100)
    PAN=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    status= models.CharField(default='active', max_length=20)

class Vehicle(models.Model):
    # sr_no = models.IntegerField()
    category = models.CharField(max_length=100)
    status= models.CharField(default='active', max_length=20)
    veh_model = models.CharField(max_length=100)
    company= models.CharField(max_length=100)


class Insurance_company(models.Model):
    comp_name= models.CharField(max_length=100)
    status= models.CharField(default='active', max_length=20)

class RTO_conversion(models.Model):
    # _id=models.ForeignKey("profile", on_delete=models.CASCADE)
    rto_series=models.CharField(max_length=10)
    rto_return=models.CharField(max_length=10)
    status= models.CharField(default='active', max_length=20)
    pan=models.CharField(max_length=15)

class SLAB(models.Model):
    _id = models.ObjectIdField()
    slab_name=models.CharField(max_length=50)
    payout_name=models.CharField(max_length=100)
    case_type=models.CharField(max_length=100)
    coverage=models.CharField(max_length=100)
    fuel_type=models.CharField(max_length=50)
    CPA=models.CharField(max_length=50)
    rewards_on=models.CharField(max_length=50)
    rewards_age=models.IntegerField()
    self_rewards_on=models.CharField(max_length=50)
    self_rewards_age=models.IntegerField()
    status=models.CharField(default='ACTIVE',max_length=10)
    def __str__(self):
        return self.slab_name

class Policy(models.Model):
    policy_no = models.IntegerField()
    registration_no = models.CharField(max_length=50)
    casetype = models.CharField(max_length=100)
    insurance_comp = models.CharField(max_length=100)
    sp_name= models.CharField(max_length=100)
    sp_brokercode = models.CharField(max_length=100)
    issueDate= models.DateField()
    riskDate= models.DateField()
    CPA=models.CharField(max_length=100)
    insurance=models.FileField()
    previous_policy=models.FileField()
    vehicle_rc=models.FileField()
    vehicle_makeby=models.CharField(max_length=100)
    vehicle_category=models.CharField(max_length=100)
    other_info=models.CharField(max_length=100)
    engine_no=models.IntegerField()
    chasis_no=models.IntegerField()
    agent_name=models.CharField(max_length=100)
    customer_name=models.CharField(max_length=100)
    remark=models.CharField(max_length=100)
    OD_premium=models.IntegerField()
    TP_premium=models.IntegerField()
    net=models.IntegerField()
    GST=models.IntegerField()
    total=models.IntegerField()
    payment_mode=models.CharField(max_length=100)
    policy_type=models.CharField(max_length=100)
    insurance_upload=models.FileField()
    # status= models.CharField(default='active', max_length=20)

# class UpcomingRenewal(models.Model):
#     _id = models.ObjectIdField()
#     policy_no=models.IntegerField()
#     riskDate= models.DateField()
#     slab_name=models.CharField(max_length=50)
#     payout_name=models.CharField(max_length=100)
#     case_type=models.CharField(max_length=100)
#     coverage=models.CharField(max_length=100)
#     fuel_type=models.CharField(max_length=50)
#     CPA=models.CharField(max_length=50)
#     rewards_on=models.CharField(max_length=50)
#     rewards_age=models.IntegerField()
#     self_rewards_on=models.CharField(max_length=50)
#     self_rewards_age=models.IntegerField()
#     status=models.CharField(default='ACTIVE',max_length=10)

class VehicleCategory(models.Model):
    category = models.CharField(max_length=100)
    status= models.CharField(default='active', max_length=20)
    def __str__(self):
        return self.category

class VehicleModelName(models.Model):
    model = models.CharField(max_length=100)
    status= models.CharField(default='active', max_length=20)
    def __str__(self):
        return self.model
class VehicleMakeBy(models.Model):
    company= models.CharField(max_length=100)
    status= models.CharField(default='active', max_length=20)
    def __str__(self):
        return self.company