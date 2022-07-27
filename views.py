 from django.http import HttpResponse
 from django.shortcuts import Redirect 


 def index(request):
     return HttpResponse('index')

 def login(request):
     return Redirect('/index')
