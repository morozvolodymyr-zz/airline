import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from airline_app.models import Flights, Team, Users


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


@api_view(['GET'])
def create_team(request):
    if request.session.get('user_e_mail') is not None and request.session.get('user_role') == 2:
        pilots = Users.objects.filter(id_role=3)
        navigators = Users.objects.filter(id_role=4)
        stewardess = Users.objects.filter(id_role=5)
        radiomen = Users.objects.filter(id_role=6)
        json_personal = {'pilots': [], 'navigators': [], 'radiomen': [], 'stewardess': []}
        for pilot in pilots:
            temp = {'id': pilot.id, 'name': pilot.name, 'surname': pilot.surname}
            json_personal['pilots'].append(temp)
        for navigator in navigators:
            temp = {'id': navigator.id, 'name': navigator.name, 'surname': navigator.surname}
            json_personal['navigators'].append(temp)
        for radioman in radiomen:
            temp = {'id': radioman.id, 'name': radioman.name, 'surname': radioman.surname}
            json_personal['radiomen'].append(temp)
        for st in stewardess:
            temp = {'id': st.id, 'name': st.name, 'surname': st.surname}
            json_personal['stewardess'].append(temp)
        return HttpResponse(json.dumps(json_personal), content_type='application/json',
                            status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)


@csrf_exempt
@api_view(['GET', 'POST'])
def save_team(request, f_id):
    if request.session.get('user_e_mail') is not None and request.session.get('user_role') == 2:
        json_data = JSONParser().parse(request)
        pilot1 = Users.objects.filter(id=json_data['pilot1']).first()
        pilot2 = Users.objects.filter(id=json_data['pilot2']).first()
        navigator = Users.objects.filter(id=json_data['navigator']).first()
        radioman = Users.objects.filter(id=json_data['radioman']).first()
        stewardess1 = Users.objects.filter(id=json_data['stewardess1']).first()
        stewardess2 = Users.objects.filter(id=json_data['stewardess2']).first()
        t = Team(id_pilot1=pilot1, id_pilot2=pilot2, id_navigator=navigator, id_radioman=radioman,
                 id_stewardess1=stewardess1, id_stewardess2=stewardess2)
        t.save()
        flight = Flights.objects.filter(id=f_id).first()
        flight.id_team = t
        flight.save()
        return HttpResponse('ok', status=status.HTTP_200_OK)
    else:
        return HttpResponse('error login', status=status.HTTP_401_UNAUTHORIZED)
