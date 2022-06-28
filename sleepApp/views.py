from django.http.response import JsonResponse
import json
from datetime import datetime
from sleepApp.models import Account, User
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes

# Create your views here.
@parser_classes((MultiPartParser))
class UserApi(APIView):
    def get(self, request, format=None, Id = None):
        if Id == None or Id == '':
            users = User.objects.values()
            list_user = []
            for user in users:
                list_user.append({"Id":user['Id'],"Name":user['Name'],"Notification": user['Notification']})
            return JsonResponse(list_user,safe=False)
        else:
            user = list(User.objects.filter(Id = Id).values())
            return JsonResponse(user[0],safe=False)

    def post(self, request, format=None):
        try:
            try:
                Avatar = request.FILES['Avatar']
            except:
                Avatar = ''
            
            user = json.loads(request.data['data'])

            if(User.objects.filter(Id = user['Id']).count() == 0):
                User.objects.create(
                    Id = user['Id'],
                    Name = user['Name'],
                    Cmnd = user['Cmnd'],
                    Email = user['Email'],
                    Phone = user['Phone'],
                    Avatar = Avatar,
                    Notification = user['Notification']
                )
                return JsonResponse("Sucess",safe = False)
            else: return JsonResponse("Error",safe = False)
        except:
            return JsonResponse("Error",safe = False)
    
    def put(self, request, format=None):
        try:
            user = json.loads(request.data['data'])

            user_change = User.objects.get(Id = user['Id'])

            try:
                user_change.Name = user['Name']
                user_change.Cmnd = user['Cmnd']
                user_change.Email = user['Email']
                user_change.Phone = user['Phone']
            except:
                pass
            
            try:
                Avatar = request.FILES['Avatar']
                user_change.Avatar = Avatar
            except:
                pass

            try:
                for i in user['Notification']:
                    tmp = {"Time" : datetime.utcnow(),"Text": i['Text']}
                    user_change.Notification.insert(0,tmp)
            except:
                pass

            user_change.save()

            return JsonResponse("Sucess",safe = False)
        except:
            return JsonResponse("Error",safe = False)
    
    def delete(self, request, format=None, Id = None):
        user = User.objects.get(Id = Id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)

class AccountApi(APIView):
    def get(self, request, format=None,username=None,password=None):
        if username != None and password != None:
            accounts = Account.objects.values()
            for account in accounts:
                if (account['Username'] == username and account['Password'] == password):
                    return JsonResponse(account['Role'],safe=False)
        return JsonResponse("Error",safe=False)
    def post(self, request, format=None):
        try:
            if(Account.objects.filter(Id = request.data['Id']).count() == 0):
                Account.objects.create(
                    Id = request.data['Id'],
                    Username = request.data['Username'],
                    Password = request.data['Password'],
                    Role = request.data['Role']
                )
                return JsonResponse("Sucess",safe = False)
            else: return JsonResponse("Error",safe = False)
        except:
            return JsonResponse("Error",safe = False)
