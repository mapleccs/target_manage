from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.utils.safestring import mark_safe

from apps.OQC_info import models
import json
import math


# Create your views here.

class OQC_LvOrderModalForm(forms.ModelForm):
    class Meta:
        model = models.OQC_database
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", 'disabled': True}


def oqc_order_info(request):
    form = OQC_LvOrderModalForm()
    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['order__contains'] = search_data
    # 删除重复提交信息的数据
    for row in models.OQC_database.objects.all():
        if models.OQC_database.objects.filter(order=row.order, lot=row.lot).count() > 1:
            row.delete()

    # 计算分页
    page = int(request.GET.get('page', 1))
    page_size = 10  # 每页显示10条数据
    start = (page - 1) * page_size
    end = page * page_size

    # data_count: 数据库总条数
    data_count = models.OQC_database.objects.filter(**data_dict).order_by("-id").count()

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

    queryset = models.OQC_database.objects.filter(**data_dict).order_by('-id')[start:end]
    return render(request, 'templates/oqc_lv_order_info.html',
                  {
                      'queryset': queryset,
                      'form': form,
                      'search_data': search_data,
                      'page_str': page_str,
                      'page_end': page_count
                  }
                  )


def oqc_lv_info_edit(request, nid):
    row_object = models.OQC_database.objects.filter(id=nid).first()
    if request.method == "GET":
        form = OQC_LvOrderModalForm(instance=row_object)
        return render(request, '../TechSupport_info/templates/support_lv_order_edit.html', {'form': form})
    form = OQC_LvOrderModalForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/support/lv_order/list/')
    return render(request, '../TechSupport_info/templates/support_lv_order_edit.html', {'form': form})


def oqc_lv_info_detail(request, nid):
    # 查看订单详细信息
    row_object = models.OQC_database.objects.filter(id=nid).first()
    if request.method == "GET":
        form = OQC_LvOrderModalForm(instance=row_object)
        return render(request, '../TechSupport_info/templates/support_lv_order_detail.html', {'form': form})
    form = OQC_LvOrderModalForm(data=request.POST, instance=row_object)
    return render(request, '../TechSupport_info/templates/support_lv_order_detail.html', {'form': form})


def grid_view(request):
    # 创建横行的数字
    numbers = list(range(1, 11))

    # 创建竖列的字母
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    # 创建方格数据
    grid = []
    for i in range(10):
        row = []
        for j in range(10):
            cell_value = ''  # 初始化单元格的值
            row.append({'value': cell_value})
        grid.append(row)

    return render(request, 'templates/方格.html', {'numbers': numbers, 'letters': letters, 'grid': grid})


def download_json(request, nid):
    data = models.OQC_database.objects.filter(id=nid).values('order', 'gene_name', 'vector_name', 'lot', 'titer_result',
                                                             'report_date', 'report_date', 'check_date', 'checker')
    file_name = data[0]['order']
    json_data = json.dumps(list(data), ensure_ascii=False)

    # 创建HttpResponse对象，将JSON数据返回给客户端
    response = HttpResponse(json.dumps(json_data), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="{0}.json"'.format(file_name)
    return response
