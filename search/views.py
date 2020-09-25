from django.shortcuts import render
from django.views import View
from .forms import searchfeild
from .models import search_in_sites

class Search(View):


    def get(self, request):
        context = {
            "form": searchfeild
        }
        return render(request, "search/index.html", context)
    


    def post(self, request):
        form = searchfeild(request.POST)
        if form.is_valid():
            print(form['search'].value())
            result = search_in_sites(form['search'].value())
        context = {
            "form" : searchfeild,
            "results": result,

        }
        return render(request, "search/index.html", context)
