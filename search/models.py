from django.db import models
import requests


class links(models.Model):
    searched_word = models.CharField(max_length=100)
    link = models.SlugField()
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.link
    # name = models.CharField(max_length=100)

    # def find_title(self):
    #     return requests.head(self.link)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.name =  find_title()
