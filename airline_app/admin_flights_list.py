import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from airline_app.models import Flights


@api_view(['GET'])
def get_flights(request):
    if request.session.get('user_e_mail') is not None and request.session.get('user_role') == 1:
        flights = Flights.objects.all()
        json_flights = {'flights': []}
        for flight in flights:
            temp = {'id': flight.id, 'from': flight.from_city, 'to': flight.to_city}
            json_flights['flights'].append(temp)
        return HttpResponse(json.dumps(json_flights), content_type='application/json',
                            status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@api_view(['GET', 'POST'])
def add_flight(request):
    if request.session.get('user_e_mail') is not None and request.session.get('user_role') == 1:
        json_data = JSONParser().parse(request)
        from_city = json_data['from']
        to_city = json_data['to']
        f = Flights(from_city=from_city, to_city=to_city)
        f.save()
        return HttpResponse('ok', status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@api_view(['DELETE'])
def delete_flight(request, f_id):
    if request.session.get('user_e_mail') is not None and request.session.get('user_role') == 1:
        flight = Flights.objects.filter(id=f_id).first()
        flight.delete()
        return HttpResponse('ok', status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)