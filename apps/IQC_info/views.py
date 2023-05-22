from django.shortcuts import render, redirect
from apps.IQC_info import models
from django import forms


# Create your views here.
class IQC_OrderEditModelForm(forms.ModelForm):
    class Meta:
        model = models.IQC_database
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}
        self.fields['order'].widget.attrs.update({'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})
        self.fields['gene_name'].widget.attrs.update({'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})
        self.fields['vector_name'].widget.attrs.update({'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})
        self.fields['titer_requirement'].widget.attrs.update(
            {'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})
        self.fields['lv_DeliveryDate'].widget.attrs.update(
            {'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})
        self.fields['Lot'].widget.attrs.update({'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})


class IQC_OrderDetailModelForm(forms.ModelForm):
    class Meta:
        model = models.IQC_database
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", 'disabled': True}


def iqc_order_info(request):
    # 进行搜索查询功能
    data_dict = {}
    search_data = request.GET.get('q', '')
    print(search_data)
    if search_data:
        data_dict['order__contains'] = search_data

    # 删除重复提交信息的数据
    for row in models.IQC_database.objects.all():
        if models.IQC_database.objects.filter(order=row.order, lv_DeliveryDate=row.lv_DeliveryDate).count() > 1:
            row.delete()
    queryset = models.IQC_database.objects.all().order_by('-id')
    return render(request, 'templates/iqc_order_info.html',
                  {
                      'queryset': queryset,
                      'search_data': search_data,
                  })


def iqc_order_detail(request, nid):
    # 查看订单详细信息
    row_object = models.IQC_database.objects.filter(id=nid).first()
    if request.method == "GET":
        form = IQC_OrderDetailModelForm(instance=row_object)
        return render(request, 'templates/iqc_order_detail.html', {'form': form})
    form = IQC_OrderDetailModelForm(data=request.POST, instance=row_object)
    return render(request, 'templates/iqc_order_detail.html', {'form': form})


def iqc_order_edit(request, nid):
    """修改订单"""
    row_object = models.IQC_database.objects.filter(id=nid).first()
    if request.method == "GET":
        form = IQC_OrderEditModelForm(instance=row_object)
        return render(request, 'templates/iqc_order_edit.html', {'form': form})
    form = IQC_OrderEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # print(form.data)
        form.save()
        return redirect('/iqc/order/list/')
    return render(request, 'templates/iqc_order_edit.html', {'form': form})
