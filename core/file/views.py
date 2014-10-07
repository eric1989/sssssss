from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from file.models import Image
from file.forms  import UploadImgForm, RatingForm
from file.service import Service

fileService = Service()

class File(View):

    def get(self,request):
        form = UploadImgForm()
        return render(request, 'file/index.html',{'form': form})

# def index(request):
#     form = UploadImgForm()
#     return render(request, 'file/index.html',{'form': form})

# class ImageList(View):

#     def get(self,request,*args, **kwargs):
#         imgs = fileService.get_img_list()
#         return render(request, 'file/list.html', {'imgs' : imgs})

# class ImageDetail(View):

#     def get(self,request, imageId, *args, **kwargs):
#         form = RatingForm()
#         image = fileService.get_img_byID(imageId)
#         return render(request,'file/show.html', {'form': form, 'img': image})
        
class ImageView(View):

    def get(self,request, action, imageId=-1):
        if action == 'list':
            return self.getList(request)
        elif action == 'detail':
            return self.getDetail(request,imageId)
        elif action == 'get':
            content  = fileService.get_img_content_byID(imageId)
            return HttpResponse(content.read(), mimetype='image/%s' % content.content_type)
    
    def post(self,request):
        if request.method == 'POST':
            form = UploadImgForm(request.POST, request.FILES)
        if form.is_valid():
            fileService.handle_upload_img(request.POST,request.FILES)
            return HttpResponse('success')
        return redirect('/file')

    def getDetail(self,request, imageId):
        form = RatingForm()
        image = fileService.get_img_byID(imageId)
        return render(request,'file/show.html', {'form': form, 'img': image})

    def getList(self,request):
        imgs = fileService.get_img_list()
        return render(request, 'file/list.html', {'imgs' : imgs})

class RatingView(View):

    def post(self,request):
        if request.method == 'POST':
            imgId =  request.POST.get('imgID')
            form = RatingForm(request.POST)
        if form.is_valid():
            fileService.handle_submit_rating(request.POST, imgId)
            return HttpResponse('success')
        return redirect('/file')

# def upload(request):
#     if request.method == 'POST':
#         form = UploadImgForm(request.POST, request.FILES)
#         if form.is_valid():
#             fileService.handle_upload_img(request.POST,request.FILES)
#             return HttpResponse('success')
#     return redirect('/file')

# def list(request):
#     imgs = fileService.get_img_list()
#     return render(request, 'file/list.html', {'imgs' : imgs})


# def submitRating(request):
#     if request.method == 'POST':
#         imgId =  request.POST.get('imgID')
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             fileService.handle_submit_rating(request.POST, imgId)
#             return HttpResponse('success')
#     return redirect('/file')

# def getImage(request, imageId):
#         content  = fileService.get_img_content_byID(imageId)
#         return HttpResponse(content.read(), mimetype='image/%s' % content.content_type)           

# def showImage(request, imageId):
#     form = RatingForm()
#     image = fileService.get_img_byID(imageId)
#     return render(request,'file/show.html', {'form': form, 'img': image})