from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import datetime
from .models import Movies


def show(request):
    # find out fav color of client by taking color cookie's value
    cookies = request.COOKIES
    if 'color' in cookies:
        color = cookies['color']
    else:
        return HttpResponseRedirect("/demo/selectcolor/")

    # print(cookies)
    return HttpResponse("Your fav color is : " + color)


def selectcolor(request):
    if request.method == "GET":
        return render(request, 'demo/selectcolor.html')
    else:  # POST
        color = request.POST['color']
        # create a cookie with name color and value of color variable
        response = HttpResponseRedirect("/demo/show")
        response.set_cookie("color", color,
                            expires=datetime.datetime.now() + datetime.timedelta(days=10))
        return response


def selectcity(request):
    if request.method == "GET":
        return render(request, 'demo/selectcity.html',
                      {'cities': Movies.get_cities()})
    else:  # POST
        city = request.POST['city']
        # create a cookie with name color and value of color variable
        response = HttpResponseRedirect("/demo/showmovies")
        response.set_cookie("city", city,
          expires=datetime.datetime.now() + datetime.timedelta(days=10))
        return response


def showmovies(request):
    # find out city of client by taking city cookie's value
    cookies = request.COOKIES
    if 'city' in cookies:
        city = cookies['city']
    else:
        return HttpResponseRedirect("/demo/selectcity/")

    # print all movies
    return render(request, 'demo/showmovies.html',
                  {'city': city, 'movies': Movies.get_movies(city)})
