import json
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view

from airline_app.models import Team, Flights


@api_view(['GET'])
def user_flights(request, u_id):
    if request.session.get('user_e_mail') is not None and request.session.get('user_role') != 1 and request.session.get(
            'user_role') != 2:
        teams = Team.objects.filter(id_pilot1=u_id) | Team.objects.filter(id_pilot2=u_id) | Team.objects.filter(
            id_navigator=u_id) | Team.objects.filter(id_radioman=u_id) | Team.objects.filter(
            id_stewardess1=u_id) | Team.objects.filter(id_stewardess2=u_id)
        json_flights = {'flights': []}
        flights = Flights.objects.all()
        for team in teams:
            for flight in flights:
                if team.id == flight.id_team_id:
                    temp = {'id': flight.id, 'from': flight.from_city, 'to': flight.to_city, 'team': flight.id_team_id}
                    json_flights['flights'].append(temp)
        return HttpResponse(json.dumps(json_flights), content_type='application/json',
                            status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def user_team(request, f_id):
    if request.session.get('user_e_mail') is not None and request.session.get('user_role') != 1 and request.session.get(
            'user_role') != 2:
        flight = Flights.objects.filter(id=f_id).first()
        team = flight.id_team
        json_team = {'team': []}
        temp = {'pilot1': team.id_pilot1.name + ' ' + team.id_pilot1.surname,
                'pilot2': team.id_pilot2.name + ' ' + team.id_pilot2.surname,
                'navigat': team.id_navigator.name + ' ' + team.id_navigator.surname,
                'stewardess1': team.id_stewardess1.name + ' ' + team.id_stewardess1.surname,
                'stewardess2': team.id_stewardess2.name + ' ' + team.id_stewardess2.surname,
                'radioman': team.id_radioman.name + ' ' + team.id_radioman.surname}
        json_team['team'].append(temp)
        return HttpResponse(json.dumps(json_team), content_type='application/json',
                            status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)
