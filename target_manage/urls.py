"""
URL configuration for target_manage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from apps.LV_info.views import lv_order_info
from apps.LV_info.views import lv_order_add
from apps.LV_info.views import lv_order_edit
from apps.LV_info.views import lv_order_detail
from apps.IQC_info.views import iqc_order_info
from apps.IQC_info.views import iqc_order_detail
from apps.IQC_info.views import iqc_order_edit
from apps.TechSupport_info.views import support_lv_info
from apps.TechSupport_info.views import support_lv_info_edit
from apps.TechSupport_info.views import support_lv_info_add
from apps.TechSupport_info.views import support_lv_info_detail
from apps.OQC_info.views import grid_view
from apps.OQC_info.views import oqc_order_info
from apps.OQC_info.views import oqc_lv_info_detail
from apps.OQC_info.views import download_json

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('lv/order/list/', lv_order_info),
    path('lv/order/add/', lv_order_add),
    path('lv/order/<int:nid>/edit/', lv_order_edit),
    path('lv/order/<int:nid>/detail/', lv_order_detail),
    path('iqc/order/list/', iqc_order_info),
    path('iqc/order/<int:nid>/detail/', iqc_order_detail),
    path('iqc/order/<int:nid>/edit/', iqc_order_edit),
    path('support/lv_order/list/', support_lv_info),
    path('support/lv_order/<int:nid>/edit/', support_lv_info_edit),
    path('support/lv_order/add/', support_lv_info_add),
    path('support/lv_order/<int:nid>/detail/', support_lv_info_detail),
    path('grid/', grid_view),
    path('oqc/lv_order/list/', oqc_order_info),
    path('oqc/lv_order/<int:nid>/detail/', oqc_lv_info_detail),
    path('oqc/lv_order/<int:nid>/download_json/', download_json)
]
