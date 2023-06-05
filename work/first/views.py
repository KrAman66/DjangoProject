from django.shortcuts import render

def home(request):
   return render(request,'index.html')

def about(request):
   info ={
      "address":"am bypass",
      "email":"xyz@gmail.com"
   }
   return render(request,'about.html', context=info)
     