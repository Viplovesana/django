from django.shortcuts import render
from .forms import Studentform , StudentLoginform

from .models import Student

# Create your views here.
def home(req):
      if req.method == "POST":   
            print(req.POST)
            form=Studentform(req.POST,req.FILES)
            if form.is_valid():
                  n = form.cleaned_data['name']
                  e = form.cleaned_data['email']
                  c = form.cleaned_data['contact']
                  i = form.cleaned_data['image']
                  d = form.cleaned_data['document']
                  print(n,e,c,d,i)
                  Student.objects.create(name=n,email=e,contact=c,image=i,document=d)
                  form = StudentLoginform()
                  msg = 'Data Saved........'
                  return render (req,'login.html',{'fm':form,'msg':msg})
            else:
                  msg = 'Please fill valid values....'
                  return render (req,'home.html',{'fm':form,'msg':msg})

      else:
            form = Studentform()
            return render (req,'home.html',{'fm':form})
      

      #........Field -level validation......................


            # n =req.POST.get('x')
            # e =req.POST.get('y')
            # c =req.POST.get('z')
            # i =req.FILES.get('f')
            # d =req.FILES.get('d')
            # data={
            #       'name':{'key1':n},
            #       'email':{'key2':e},
            #       'contact':c,
            #       'image':i,
            #       'document':d
            # }
            # data1 = {'name':'Viplove','email':'viplovesana90@gmail.com','contact':8085212206,'image':True,'document':False}
            # print(n,e,c,i,d) 
            # data2 = {
            #       'key1':data,
            #       'key2':data1
            # }    
            # return render(req,'home.html',{'key1':data})
            # return render(req,'home.html',{'key2':data2})
            # return render(req,'home.html',{'key1':data})
            # return render(req,'home.html',{'key1':data})
            # return render(req,'home.html',{'key2':data2})

#       return render(req,'home.html')

# def data(req):
#       if req.method == "POST":
#             n =req.POST.get('x')
#             e =req.POST.get('y')
#             c =req.POST.get('z')
#             i =req.FILES.get('f')
#             d =req.FILES.get('d')
#             data={
#                   'name':{'key1':n},
#                   'email':{'key2':e},
#                   'contact':c,
#                   'image':i,
#                   'document':d

#             }
#             print(n,e,c,i,d) 
#             return render(req,'home.html',{'key':data})
      # print(req.POST)
      # print(req.FILES)
      # print(req.method)
      