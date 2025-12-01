from django.shortcuts import render
import json
from .models import Register
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def reg(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        Fname = data.get("Fname")
        Lname = data.get("Lname")
        Phone = data.get("Phone")
        Email = data.get("Email")
        Password = data.get("Password")

        Register.objects.create(
            Fname=Fname,
            Lname=Lname,
            Phone=Phone,
            Email=Email,
            Password=Password
        )

        return JsonResponse({"message": "Registration successfull"}, status=201)

    return JsonResponse({"Error": "Post Method only"}, status=405)


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))

        # ✅ corrected here
        email = data.get("email")
        password = data.get("password")

        user = Register.objects.filter(Email=email, Password=password)

        if user:
            return JsonResponse({"message": "Login Successfully"})
        else:
            return JsonResponse({"message": "Invalid Email or Password"})

    return JsonResponse({"Error": "Post Method only"})


@csrf_exempt
def get_data(request):
    if request.method == "GET":
        data = Register.objects.all()
        sample = []
        for users in data:
            sample.append({
                "Firstname": users.Fname,
                "Lastname": users.Lname,
                "Phone": users.Phone,
                "Email": users.Email,
                "Password": users.Password
            })
        return JsonResponse({"Details": sample})
    
    return JsonResponse({"Error": "GET Method only"})


@csrf_exempt
def delete_data(request):
    if request.method == "DELETE":
        data = json.loads(request.body.decode("utf-8"))
        Id=data.get("Id")
        remove=Register.objects.filter(id=Id)
        if remove.exists():
            remove.delete()
            return JsonResponse({"message":"Deleted Successfully"})
        else:
            return JsonResponse({"message":"Deleted unsuccessfully"})
    return JsonResponse({"Error":"Delete Method only"})


@csrf_exempt
def update_data(request):
    if request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        Id = data.get("id")
        if not Register.objects.filter(id=Id).exists():
            return JsonResponse({"message": "data not found"})
        Register.objects.filter(id=Id).update(
            Fname=data.get("Fname"),
            Lname=data.get("Lname"),
            Phone=data.get("Phone"),
            Email=data.get("Email"),
            Password=data.get("Password")
        )
        return JsonResponse({"message": "Updated Successfully"})
    return JsonResponse({"Error": "PUT Method only"})
