from djongo import models
# from django import forms
# Create your models here.

class bima_user(models.Model):
    sr_no = models.IntegerField
    login_id = models.CharField(max_length=50)
    staffname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    cnfmpassword= models.CharField(max_length=20)
    status= models.TextField   
    # class Meta:
    #     abstract = True
        
# class Bima_Form(forms.ModelForm):
#     class Meta:
#         model = bima_user
#         fields = (
#             'sr_no', 'login_id','staffname','username','password','cnfmpassword',''
#         )
