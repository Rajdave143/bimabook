from djongo import models
# from django import forms
# Create your models here.

# class bima_user(models.Model):
#     sr_no = models.IntegerField
#     login_id = models.CharField(max_length=50)
#     staffname = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=20)
#     cnfmpwd= models.CharField(max_length=20)
#     status= models.TextField   
#     # class Meta:
#     #     abstract = True
        
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
    mob_no = models.IntegerField
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    cnfmpassword= models.CharField(max_length=20)
    beneficiary_name=models.CharField(max_length=50)
    acc_no = models.IntegerField
    bank_name= models.CharField(max_length=50)
    
    def __str__(self):
        return self.full_name