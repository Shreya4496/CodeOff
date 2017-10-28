from django.shortcuts import render
import urllib
import requests
from django import forms
from rest_framework.response import Response
from django.http import JsonResponse
import json
from django.template import Context, loader
from bs4 import BeautifulSoup

from django.http import HttpResponse
from django.template import Context, loader
from RegistrationForm.form import UserForm
from django.http import HttpResponseRedirect
# Create your views here.


def Dashboard(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            job = form.cleaned_data['job']
            job_t = form.cleaned_data['job_time']
            print("*******" + job + "******" + job_t)

            job_desc = {
                "desk_job_normal": ["Muscular Skeletal Disorders", "Diabetes", "Cancer", "Cardiovascular Disease",
                                    "Obesity",
                                    "Poor Posture", "Aches and Pains", "Neck Issues"],
                "desk_job_comp": ["Muscular Skeletal Disorders", "Diabetes", "Cancer", "Cardiovascular Disease",
                                  "Obesity",
                                  "Poor Posture", "Aches and Pains", "Neck Issues", "Eyestrain", "Aggression",
                                  "Mental stress"],

            }
            job_time = {
                "day_job": [],
                "night_job": []
            }

            if(job=='desk_job'):
                arr = []
                arr2= []

                for textToSearch in job_desc['desk_job_comp']:
                    textToSearch += " exercises"
                    url = "https://www.youtube.com/results?search_query=" + textToSearch
                    response = urllib.urlopen(url)
                    html = response.read()

                    soup = BeautifulSoup(html)



                    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                        s = str(vid['href'])
                        l = len(s)
                        ns = str(s[9:l])
                        # arr.append(ns)
                        arr.append('https://www.youtube.com/embed/' + ns)
                        break
                for textToSearch1 in job_desc['desk_job_comp']:
                    textToSearch1 += " recipes"
                    url = "https://www.youtube.com/results?search_query=" + textToSearch1
                    response = urllib.urlopen(url)
                    html = response.read()

                    soup = BeautifulSoup(html)



                    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                        s = str(vid['href'])
                        l = len(s)
                        ns = str(s[9:l])
                        # arr.append(ns)
                        arr2.append('https://www.youtube.com/embed/' + ns)
                        break
            else:
                arr = []
                arr2=[]
                for textToSearch in job_desc['desk_job_normal']:
                    textToSearch += " exercises"
                    url = "https://www.youtube.com/results?search_query=" + textToSearch
                    response = urllib.urlopen(url)
                    html = response.read()

                    soup = BeautifulSoup(html)


                    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                        s = str(vid['href'])
                        l = len(s)
                        ns = str(s[9:l])
                        # arr.append(ns)
                        arr.append('https://www.youtube.com/embed/' + ns)
                        break
                for textToSearch1 in job_desc['desk_job_normal']:
                    textToSearch1 += " recipes"
                    url = "https://www.youtube.com/results?search_query=" + textToSearch1
                    response = urllib.urlopen(url)
                    html = response.read()

                    soup = BeautifulSoup(html)

                    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                        s = str(vid['href'])
                        l = len(s)
                        ns = str(s[9:l])
                        # arr.append(ns)
                        arr2.append('https://www.youtube.com/embed/' + ns)
                        break

            myList = []
            response = requests.get("https://www.eventbriteapi.com/v3/events/search/",
                                    headers={"Authorization": "Bearer CEIOE6PUYBL5MI2BJCW4", },
                                    params={"q": "Health", "location.address": "Delhi"},
                                    verify=True, )
            for i in range(0, 6):
                event = str(response.json()['events'][i]['name']['text'].encode('utf8'))
                myList.append(event)
            context = {
                'posts': arr,
                'recipes': arr2,
                'myList': myList,

            }
            return render(request, 'dashboard.html', context)
                    # process the data in form.cleaned_data as required
                    # ...
                    # redirect to a new URL:
                    #return HttpResponseRedirect('/thanks/')

            # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    #return render(request, 'name.html', {'form': form})


    return render(request, 'name1.html', {'form': form})
        # print('https://www.youtube.com' + vid['href'])"""

def choices(request):
    return render(request, 'choices.html')
