from django.shortcuts import render

# Create your views here.
def home(req):
      if req.method == "POST":
            n =req.POST.get('x')
            e =req.POST.get('y')
            c =req.POST.get('z')
            i =req.FILES.get('f')
            d =req.FILES.get('d')
            data={
                  'name':{'key1':n},
                  'email':{'key2':e},
                  'contact':c,
                  'image':i,
                  'document':d
            }
            data1 = {'name':'Neeraj','email':'neeraj@gmail.com','contact':9424444348,'image':True,'document':False}
            print(n,e,c,i,d) 
            data2 = {
                  'key1':data,
                  'key2':data1
            }    
            # return render(req,'home.html',{'key1':data})
            return render(req,'home.html',{'key2':data2})
            # return render(req,'home.html',{'key1':data})
            # return render(req,'home.html',{'key1':data})
            # return render(req,'home.html',{'key2':data2})

      return render(req,'home.html')

def data(req):
      if req.method == "POST":
            n =req.POST.get('x')
            e =req.POST.get('y')
            c =req.POST.get('z')
            i =req.FILES.get('f')
            d =req.FILES.get('d')
            data={
                  'name':{'key1':n},
                  'email':{'key2':e},
                  'contact':c,
                  'image':i,
                  'document':d

            }
            print(n,e,c,i,d) 
            return render(req,'home.html',{'key':data})
      # print(req.POST)
      # print(req.FILES)
      # print(req.method)
      