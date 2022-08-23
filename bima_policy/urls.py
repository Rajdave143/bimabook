from django.urls import path

from bima_policy.models import *
from .views import *
app_name='bima_policy'
urlpatterns = [
    path('login/', loginView, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/',Profile,name='profile'),
    path('profile/bank_details/',bank_details,name='bank_det'),  
    path('profile/bank_details/<str:id>',delete_bank_details,name='del_bank'),
    path('user/',staffmanage.as_view(), name='staff'),
    path('agent/',agent, name='agent'),
    path('agent/add_agent/',add, name='add_agent'),
    path('service_provider/', service_p, name='service_p'),
    path('service_provider/add_sp/', add_sp, name='add_sp'),
    path('vehicle/',vehicleView, name='vehi'),
    path('insurance_comp/', ins_comp, name="ins_comp"),
    path('RTO/', RTOconversion.as_view(), name="rto_conv"),
    path('slab/', slab, name="slab"),
    path('slab/slab_payoutlist/', slab_payout, name="slab_payout"),
    path('slab/slab_payoutform/',slab_payoutform, name="slab_payoutform"),
    path('policy/',create_policy, name="create_policy"),
    path('policy/entry',policy_entry, name="policy_entry"),
    path('policy/import',policy_import, name="policy_import"),
    path('upcomingRenewal/',upcoming_renewal, name="upcoming_renewal"),
    path('agent_payable/',agentpayable, name="agentpayable"),
    path('agent_statement/',agent_statement, name="agent_statement"),
    path('SP_receive/',sp_receivable, name="sp_receivable"),
    path('SP_statement/',sp_statement, name="sp_statement"),
    path('report_agent/',report_agent, name="report_agent"),
    path('report_PP/',report_policyprovider, name="report_policyprovider"),
    path('report_Vcat/',report_vehicleCategory, name="report_vehicleCategory"),
    path('report_broker/',report_brokercode, name="report_brokercode"),
    path('report_insurance/',report_insurance_comp, name="report_insurance_comp"),
    path('subscription/',subscription, name="subscription"),
    path('delete/<int:id>', RtoRemove, name='RtoRemove'),
]