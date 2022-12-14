from django.shortcuts import render,redirect
from shortener.models import Users
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    user = Users.objects.filter(username="admin").first()
    email = user.email if user else "Anonymous User!"
    return render(request, "base.html",{"welcome_msg":"Hello FastCampus!"})

@csrf_exempt
def get_user(request, user_id):
    print(user_id)
    if request.method == "GET":
        abc = request.GET.get("abc")
        xyz = request.GET.get("xyz")
        user = Users.objects.filter(pk=user_id).first()
        return render(request,"base.html",{"user": user ,"params":[abc,xyz]})
    elif request.method == "POST":
        username = request.GET.get("username")
        if username:
            user = Users.objects.filter(pk=user_id).update(username=username)
        return JsonResponse(status=201, data = dict(msg="You just reached with Post Method!"))

# def redirect_test(request):
#     print("Go Redirect")
#     return redirect("index")