from django.http import HttpResponse

# Create Your Views 

def homePageView(request):
    return HttpResponse('<h2>Hello...<br><br> My Name Is Abhishek Thakare and My PRN is 1841053</h2>')
    