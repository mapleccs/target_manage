from django.shortcuts import render, redirect
from django.http import JsonResponse
from apps.TechSupport_info import models
from django import forms
from django.utils.safestring import mark_safe
import math


# Create your views here.
class Support_LvOrderModelForm(forms.ModelForm):
    class Meta:
        model = models.TechSupport_database
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control"}


class Support_LvOrderDetailModelForm(forms.ModelForm):
    class Meta:
        model = models.TechSupport_database
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", 'disabled': True}


def support_lv_info(request):
    form = Support_LvOrderModelForm()
    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['order__contains'] = search_data

    # 计算分页
    page = int(request.GET.get('page', 1))
    page_size = 10  # 每页显示10条数据
    start = (page - 1) * page_size
    end = page * page_size

    # data_count: 数据库总条数
    data_count = models.TechSupport_database.objects.filter(**data_dict).order_by("-id").count()

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

    queryset = models.TechSupport_database.objects.filter(**data_dict).order_by('-id')[start:end]
    return render(request, '../templates/support_lv_order_info.html',
                  {
                      'queryset': queryset,
                      'form': form,
                      'search_data': search_data,
                      'page_str': page_str,
                      'page_end': page_count
                  }
                  )


def support_lv_info_add(request):
    """添加订单信息"""
    form = Support_LvOrderModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})


def support_lv_info_edit(request, nid):
    row_object = models.TechSupport_database.objects.filter(id=nid).first()
    if request.method == "GET":
        form = Support_LvOrderModelForm(instance=row_object)
        return render(request, '../templates/support_lv_order_edit.html', {'form': form})
    form = Support_LvOrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/support/lv_order/list/')
    return render(request, '../templates/support_lv_order_edit.html', {'form': form})


def support_lv_info_detail(request, nid):
    # 查看订单详细信息
    row_object = models.TechSupport_database.objects.filter(id=nid).first()
    if request.method == "GET":
        form = Support_LvOrderDetailModelForm(instance=row_object)
        return render(request, '../templates/support_lv_order_detail.html', {'form': form})
    form = Support_LvOrderDetailModelForm(data=request.POST, instance=row_object)
    return render(request, '../templates/support_lv_order_detail.html', {'form': form})


def support_lv_info_delete(request, nid):
    pass
