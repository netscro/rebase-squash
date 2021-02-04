from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class MainPage(View):

    def get(self, request):
        context = {'name': 'Jeka', 'surname': 'Kovalev'}
        return render(request, 'home.html', context=context)


class AboutPage(View):

    def get(self, request):
        return HttpResponse('About page')


class ContactsPage(View):

    def get(self, request):
        return HttpResponse('Contacts')
