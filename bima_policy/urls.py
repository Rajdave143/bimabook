from django.urls import path

from bima_policy.models import bima_user
from .views import *
app_name='bima_policy'
urlpatterns = [
    path('login/dashboard/', Dashboard, name='dashboard'),
    path('profile/',Profile,name='Profile'),
    path('profile/bank_details/',bank_det,name='bank_det'),
    path('user/',staff, name='staff'),
    path('agent/',agent, name='agent'),
    path('agent/add_agent/',add, name='add_agent'),
    path('service_provider/', service_p, name='service_p'),
    path('service_provider/add_sp/', add_sp, name='add_sp'),
    path('vehicle/',vehicle.as_view(), name='vehi'),
    path('insurance_comp/', ins_comp, name="ins_comp"),
    path('RTO/', rto_conv, name="rto_conv"),
    path('slab/', slab, name="slab"),
    path('slab/slab_payoutlist/', slab_payout, name="slab_payout"),
    path('slab/slab_payoutform/',slab_payoutform, name="slab_payoutform"),
    path('policy/',create_policy, name="create_policy"),
    path('policy/entry',policy_entry, name="policy_entry"),
    path('policy/import',policy_import, name="policy_import"),
    path('upcomingRenewal/',upcoming_renewal, name="upcoming_renewal"),

]