from django.shortcuts import render
from django.http import HttpResponseRedirect

def main_view(request):
    return render(request, "index.html")



def search_amazon(request):
    if request.method=='POST':
        data=request.POST.get('content')
        data_1=data.split()
        data_2="+".join(data_1)
        url = f"https://www.amazon.in/s?k={data_2}&ref=nb_sb_noss_2"
        return render(request, "index.html",{"URL":url})







# Create your views here.
