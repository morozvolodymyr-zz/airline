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
