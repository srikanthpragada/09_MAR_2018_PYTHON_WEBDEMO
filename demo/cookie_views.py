from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import datetime


def show(request):
    # find out fav color of client by taking color cookie's value
    cookies = request.COOKIES
    if 'color' in cookies:
        color = cookies['color']
    else:
        return HttpResponseRedirect("/demo/selectcolor/")

    print(cookies)
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
