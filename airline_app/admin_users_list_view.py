import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from airline_app.models import Users


@api_view(['GET'])
def get_users(request):
    if request.session.get('user_e_mail') is not None and request.session.get('user_role') == 1:
        users = Users.objects.all()
        json_users = {'users': []}
        for user in users:
            confirmed = "N"
            if user.confirmed:
                confirmed = "Y"
            temp = {'name': user.name, 'surname': user.surname, 'e_mail': user.e_mail, 'role': user.id_role.role,
                    'id': user.id, 'confirmed': confirmed}
            json_users['users'].append(temp)
        return HttpResponse(json.dumps(json_users), content_type='application/json',
                            status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@api_view(['DELETE'])
def delete_user(request, u_id):
    if request.session.get('user_e_mail') is not None and request.session.get('user_role') == 1:
        user = Users.objects.filter(id=u_id).first()
        user.delete()
        return HttpResponse('ok', status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@api_view(['GET', 'POST'])
def confirm_user(request, u_id):
    if request.session.get('user_e_mail') is not None and request.session.get('user_role') == 1:
        user = Users.objects.filter(id=u_id).first()
        user.confirmed = True
        user.save()
        return HttpResponse('ok', status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)
