from django.urls import path
from app.models import *
from app.views import *

urlpatterns = [

    path('register2/', ragistertoken),
    path('login2/', logintoken),
    path('login_A/', login),
    path('ragister/',register),
    path('register_user/',register_user),
    path('ragisterm/',create_register_pagemodel),
    path('login/',create_login_page),
    path('ragister/',create_register_page),
    path('item_search/',item_filters),
    path('studentwithsub/',student_datac),
    path('studentdatacreate/',studentpage_create),
    path('viewbyid/',student_viewid),
    path('student/',student_data),
    path('itemviewbyfilter/',item_view_filter),
    path('date/',item_datefilter1),
    path('datefilter/',item_datefilter),
    path('iteamview/',item_viewall),
    path('iteamcreate1/',item_Create),
    path('viewiteam/',item_view),
    path('createfile/',view_create),
    path('cdelete/',cat_delete),
    path('sudta/',sub_Update),
    path('udata/',Cat_Update),
    path('fdata/',filter_cat),
    path('bdata/',sub_view3,),
    path('adata/',sub_view2,),
    path('ndata/',sub_view1,),
    path('data/',View_catview,),
    path('sdata/',Sub_view,),
    path('create/', view_createc,),
    path('subc/',view_Subcatcreate,name='create')
   

    
]