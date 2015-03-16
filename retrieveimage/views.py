from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def hello_world(request):
	if request.method=="GET":
#		form=HashtagForm()
		return render(request,'image.html')
	else:
		return HttpResponse("Complete")
