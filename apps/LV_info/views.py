from django.shortcuts import render, redirect
from django.http import JsonResponse
from apps.LV_info import models
from django import forms
from django.utils.safestring import mark_safe
import math


# Create your views here.

class OrderAddModelForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = models.LV_database
        # fields = ['order', 'order_type', 'gene_name', 'gene_num', 'vector_name',
        #           'titer_requirement', 'dispatch', 'pipe_num', 'vector_type',
        #           'plasmid_ReceiptDate', 'transfection_date', 'hours24_state',
        #           'lv_CollectDate', 'lv_RurificationDate', 'lv_DeliveryDate',
        #           'current_state']
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.required:
                field.label = field.label + '*'
            field.widget.attrs.update({"class": "form-control"})

    def clean(self):
        cleaned_data = super().clean()
        current_state = cleaned_data.get('current_state')
        plasmid_ReceiptDate = cleaned_data.get('plasmid_ReceiptDate')
        transfection_date = cleaned_data.get('transfection_date')
        hours24_state = cleaned_data.get('hour24_state')
        lv_CollectDate = cleaned_data.get('lv_CollectDate')
        lv_RurificationDate = cleaned_data.get('lv_RurificationDate')
        lv_DeliveryDate = cleaned_data.get('lv_DeliveryDate')

        if current_state == 2:
            if not plasmid_ReceiptDate:
                self.add_error('plasmid_ReceiptDate', '质粒接受日期不能为空')
            if not transfection_date:
                self.add_error('transfection_date', '转染完成日期不能为空')

        if current_state == 3:
            if not plasmid_ReceiptDate:
                self.add_error('plasmid_ReceiptDate', '质粒接受日期不能为空')
            if not transfection_date:
                self.add_error('transfection_date', '转染完成日期不能为空')
            if hours24_state == 1:
                self.add_error('hours24_state', '24小时订单状态不能为待定状态')

        if current_state == 4:
            if not plasmid_ReceiptDate:
                self.add_error('plasmid_ReceiptDate', '质粒接受日期不能为空')
            if not transfection_date:
                self.add_error('transfection_date', '转染完成日期不能为空')
            if hours24_state == 1:
                self.add_error('hours24_state', '24小时订单状态不能为待定状态')
            if not lv_CollectDate:
                self.add_error('lv_CollectDate', '收毒日期不能为空')

        if current_state == 5:
            if not plasmid_ReceiptDate:
                self.add_error('plasmid_ReceiptDate', '质粒接受日期不能为空')
            if not transfection_date:
                self.add_error('transfection_date', '转染完成日期不能为空')
            if hours24_state == 1:
                self.add_error('hours24_state', '24小时订单状态不能为待定状态')
            if not lv_CollectDate:
                self.add_error('lv_CollectDate', '收毒日期不能为空')
            if not lv_RurificationDate:
                self.add_error('lv_RurificationDate', '纯化日期不能为空')

        if current_state == 6:
            if not plasmid_ReceiptDate:
                self.add_error('plasmid_ReceiptDate', '质粒接受日期不能为空')
            if not transfection_date:
                self.add_error('transfection_date', '转染完成日期不能为空')
            if hours24_state == 1:
                self.add_error('hours24_state', '24小时订单状态不能为待定状态')
            if not lv_CollectDate:
                self.add_error('lv_CollectDate', '收毒日期不能为空')
            if not lv_RurificationDate:
                self.add_error('lv_RurificationDate', '纯化日期不能为空')
            if not lv_DeliveryDate:
                self.add_error('lv_DeliveryDate', '送检日期不能为空')


class OrderEditModelForm(forms.ModelForm):
    class Meta:
        model = models.LV_database
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}
        self.fields['order'].widget.attrs.update({'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})
        self.fields['order_date'].widget.attrs.update({'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})
        self.fields['order_type'].widget.attrs.update({'style': 'background-color: #f2f2f2; pointer-events: none'})
        self.fields['gene_name'].widget.attrs.update({'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})
        self.fields['gene_num'].widget.attrs.update({'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})
        self.fields['vector_name'].widget.attrs.update({'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})
        self.fields['titer_requirement'].widget.attrs.update(
            {'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})
        self.fields['dispatch'].widget.attrs.update({'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})
        self.fields['pipe_num'].widget.attrs.update({'readonly': 'readonly', 'style': 'background-color: #f2f2f2;'})

    def clean(self):
        cleaned_data = super().clean()
        current_state = cleaned_data.get('current_state')
        plasmid_ReceiptDate = cleaned_data.get('plasmid_ReceiptDate')
        transfection_date = cleaned_data.get('transfection_date')
        hours24_state = cleaned_data.get('hour24_state')
        lv_CollectDate = cleaned_data.get('lv_CollectDate')
        lv_RurificationDate = cleaned_data.get('lv_RurificationDate')
        lv_DeliveryDate = cleaned_data.get('lv_DeliveryDate')

        if current_state == 2:
            if not plasmid_ReceiptDate:
                self.add_error('plasmid_ReceiptDate', '质粒接受日期不能为空')
            if not transfection_date:
                self.add_error('transfection_date', '转染完成日期不能为空')

        if current_state == 3:
            if not plasmid_ReceiptDate:
                self.add_error('plasmid_ReceiptDate', '质粒接受日期不能为空')
            if not transfection_date:
                self.add_error('transfection_date', '转染完成日期不能为空')
            if hours24_state == 1:
                self.add_error('hours24_state', '24小时订单状态不能为待定状态')

        if current_state == 4:
            if not plasmid_ReceiptDate:
                self.add_error('plasmid_ReceiptDate', '质粒接受日期不能为空')
            if not transfection_date:
                self.add_error('transfection_date', '转染完成日期不能为空')
            if hours24_state == 1:
                self.add_error('hours24_state', '24小时订单状态不能为待定状态')
            if not lv_CollectDate:
                self.add_error('lv_CollectDate', '收毒日期不能为空')

        if current_state == 5:
            if not plasmid_ReceiptDate:
                self.add_error('plasmid_ReceiptDate', '质粒接受日期不能为空')
            if not transfection_date:
                self.add_error('transfection_date', '转染完成日期不能为空')
            if hours24_state == 1:
                self.add_error('hours24_state', '24小时订单状态不能为待定状态')
            if not lv_CollectDate:
                self.add_error('lv_CollectDate', '收毒日期不能为空')
            if not lv_RurificationDate:
                self.add_error('lv_RurificationDate', '纯化日期不能为空')

        if current_state == 6:
            if not plasmid_ReceiptDate:
                self.add_error('plasmid_ReceiptDate', '质粒接受日期不能为空')
            if not transfection_date:
                self.add_error('transfection_date', '转染完成日期不能为空')
            if hours24_state == 1:
                self.add_error('hours24_state', '24小时订单状态不能为待定状态')
            if not lv_CollectDate:
                self.add_error('lv_CollectDate', '收毒日期不能为空')
            if not lv_RurificationDate:
                self.add_error('lv_RurificationDate', '纯化日期不能为空')
            if not lv_DeliveryDate:
                self.add_error('lv_DeliveryDate', '送检日期不能为空')


class OrderDetailModelForm(forms.ModelForm):
    class Meta:
        model = models.LV_database
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", 'disabled': True}


def lv_order_info(request):
    """ 组别列表 """
    form = OrderAddModelForm()
    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['order__contains'] = search_data

    # 删除重复提交信息的数据
    for row in models.LV_database.objects.all():
        if models.LV_database.objects.filter(order=row.order, order_date=row.order_date).count() > 1:
            row.delete()

    # 计算分页
    page = int(request.GET.get('page', 1))
    page_size = 10  # 每页显示10条数据
    start = (page - 1) * page_size
    end = page * page_size

    # data_count: 数据库总条数
    data_count = models.LV_database.objects.filter(**data_dict).order_by("-id").count()

    # 计算总页数
    page_count = math.ceil(data_count / page_size)

    # 计算当前页的前五页和后五页
    before_page = page - 5
    if before_page < 1:
        before_page = 1
    after_page = page + 6
    if after_page > page_count:
        after_page = page_count

    # 页码显示
    page_str_list = []
    for i in range(before_page, after_page):
        if i == page:
            ele = '<li class="page-item active"><a class="page-link" href="?page={0}">{1}</a></li>'.format(i, i)
        else:
            ele = '<li class="page-item"><a class="page-link" href="?page={0}">{1}</a></li>'.format(i, i)
        page_str_list.append(ele)
    page_str = mark_safe("".join(page_str_list))

    # order_by("-id")表示根据id的倒序进行排序
    queryset = models.LV_database.objects.filter(**data_dict).order_by("-id")[start:end]
    return render(request, 'templates/lv_order_info.html', {
        'queryset': queryset,
        'search_data': search_data,
        'form': form,
        'page_str': page_str,
        'page_end': page_count
    })


def lv_order_add(request):
    """添加订单信息"""
    form = OrderAddModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})


def lv_order_edit(request, nid):
    """修改订单"""
    row_object = models.LV_database.objects.filter(id=nid).first()
    if request.method == "GET":
        form = OrderEditModelForm(instance=row_object)
        return render(request, 'templates/lv_order_edit.html', {'form': form})
    form = OrderEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/lv/order/list/')
    return render(request, 'templates/lv_order_edit.html', {'form': form})


def lv_order_detail(request, nid):
    # 查看订单详细信息
    row_object = models.LV_database.objects.filter(id=nid).first()
    if request.method == "GET":
        form = OrderDetailModelForm(instance=row_object)
        return render(request, 'templates/lv_order_detail.html', {'form': form})
    form = OrderDetailModelForm(data=request.POST, instance=row_object)
    return render(request, 'templates/lv_order_detail.html', {'form': form})
