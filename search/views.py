from django.shortcuts import render
from django.views import View
from django.contrib.messages import warning
from .forms import searchfeild
from .search import search_in_sites
from .models import links


class Search(View):

    def get(self, request):
        context = {
            "form": searchfeild
        }
        return render(request, "search/index.html", context)

    def post(self, request):
        form = searchfeild(request.POST)
        if form.is_valid():
            word = form.cleaned_data.get('searched_word')
            print(word)
            query = links.objects.filter(searched_word=word)
            if query:
                result = query
            else:
                result = search_in_sites(word)
                for i in result:
                    link = links(searched_word=word, link=i)
                    link.save()
            context = {
                "form": searchfeild,
                "results": result,
            }
            return render(request, "search/index.html", context)
        else:
            warning(request, "input is invalid")
