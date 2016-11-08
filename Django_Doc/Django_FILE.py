# -*- coding: utf-8 -*-
'''

文件上传¶
当Django在处理文件上传的时候，文件数据被保存在request. FILES
'''


# 基本的文件上传¶
#
# 考虑一个简单的表单，它含有一个FileField：

from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    upload_file = forms.FileField()


# 处理这个表单的视图会在request中接收到上传文件的数据。
# FILES是个字典，它包含每个FileField的键
# （或者ImageField，FileField的子类）。
# 这样的话就可以用request.FILES['file']
# 来存放表单中的这些数据了。
'''
注意request.FILES 只有在请求方法为POST，
并且发送请求的<form>拥有enctype="multipart/form-data" 属性时，
才会包含数据。否则request.FILES 为空。
'''

from django.http import HttpResponseRedirect
from django.shortcuts import render

def  upload_file(request):
    if request.metho == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render('upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# 使用模型处理上传文件¶
#
# 如果你在Model上使用FileField保存文件，
# 使用ModelForm可以让这个操作更加容易。
# 调用form.save()的时候，
# 文件对象会保存在相应的FileField的upload_to参数指定的地方。

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ModelFormWithFileField

def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})

# 如果你手动构造一个对象，你可以简单地把文件对象从request.FILE赋值给模型：

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .models import ModelWithFileField

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            instance = ModelWithFileField(file_field=request.FILES['file'])
            instance.save()

            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


# 上传数据在哪里储存¶
#
# 在你保存上传文件之前，数据需要储存在某个地方。
#
# 通常，如果上传文件小于2.5MB，Django会把整个内容存到内存。
# 这意味着，文件的保存仅仅涉及到从内存读取和写到磁盘，所以非常快。
#
# 但是，如果上传的文件很大，Django会把它写入一个临时文件，储存在你系统的临时目录中。
# 在类Unix的平台下，你可以认为Django生成了一个文件，名称类似于/tmp/tmpzfp6I6.upload。
# 如果上传的文件足够大，你可以观察到文件大小的增长，由于Django向磁盘写入数据。
#
# 这些特定值 – 2.5 MB，/tmp，以及其它 -- 都仅仅是"合理的默认值"，它们可以自定义，
# 这会在下一节中描述。


# 注意
#
# 你只可以在访问request.POST或者request.FILES之前修改上传处理器--
# 在上传处理工作执行之后再修改上传处理就毫无意义了。
# 如果你在读取request.FILES之后尝试修改request.upload_handlers，Django会抛出异常。
#
# 所以，你应该在你的视图中尽早修改上传处理器。
#
# CsrfViewMiddleware 也会访问request.POST，它是默认开启的。
# 这意味着你需要在你的视图中使用csrf_exempt() 来允许你修改上传处理器。
# 然后你需要在真正处理请求的函数上使用csrf_protect()。
# 注意这意味着处理器可能会在CSRF验证完成之前开始接收上传文件。例如：

from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_exempt
def upload_file_view(request):
    request.upload_handlers.insert(0, ProgressBarUploadHandler())
    return _upload_file_view(request)

@csrf_protect
def _upload_file_view(request):
    pass
    # ... # Process request


















































































