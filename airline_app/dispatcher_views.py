import json
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from airline_app.models import Flights


@api_view(['GET'])
def get_dispatcher(request):
    if request.session.get('user_e_mail') is not None and request.session.get('user_role') == 2:
        flights = Flights.objects.all()
        json_flights = {'flights': []}
        for flight in flights:
            is_team = 'N'
            if flight.id_team is not None:
                is_team = 'Y'
            temp = {'id': flight.id, 'from': flight.from_city, 'to': flight.to_city, 'is_team': is_team,
                    'team': flight.id_team_id}
            json_flights['flights'].append(temp)
        return HttpResponse(json.dumps(json_flights), content_type='application/json',
                            status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def view_team(request, f_id):
    if request.session.get('user_e_mail') is not None and request.session.get('user_role') == 2:
        flight = Flights.objects.filter(id=f_id).first()
        team = flight.id_team
        json_team = {'team': []}
        temp = {'pilot1': team.id_pilot1__name + ' ' + team.id_pilot1__surname,
                'pilot2': team.id_pilot2__name + ' ' + team.id_pilot3__surname,
                'dispatcher': team.id_dispatcher__name + ' ' + team.id_dispatcher__surname,
                'stewardess1': team.id_stewardess1__name + ' ' + team.id_stewardess1__surname,
                'stewardess2': team.id_stewardess2__name + ' ' + team.id_stewardess2__surname,
                'radioman': team.id_radioman__name + ' ' + team.id_radioman__surname}
        json_team['team'].append(temp)
        return HttpResponse(json.dumps(json_team), content_type='application/json',
                            status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)
