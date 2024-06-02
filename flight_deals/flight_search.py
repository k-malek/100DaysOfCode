import os
from datetime import date,datetime,timedelta
from flight_data import FlightData
from dotenv import load_dotenv
import requests

load_dotenv()

class FlightSearch:

    class EmptyResultsException(Exception):
        pass

    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ['AMADEUS_KEY']
        self._api_secret = os.environ['AMADEUS_SECRET']
        self._api_token = self._get_new_token()
        self.found_flights=[]

    def _get_new_token(self):
        url=os.environ['TOKEN_ENDPOINT']
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=url,headers=header,data=body,timeout=5)
        response.raise_for_status()
        return response.json()['access_token']

    def get_city_iata(self,city):
        url=os.environ['BASE_ENDPOINT_V1']+r'/reference-data/locations/cities'
        header = {'Authorization': f'Bearer {self._api_token}'}
        body = {'keyword':city.upper()}

        response = requests.get(url=url,headers=header,params=body,timeout=5)
        response.raise_for_status()
        try:
            return response.json()['data'][0]['iataCode']
        except KeyError:
            return 'NOT_FOUND'

    def get_all_flights(self,
                        destination,
                        origin='KRK',
                        start_day=date.today(),
                        how_many_days=1,
                        currency='PLN',
                        present=False,
                        limit=250,
                        refresh_data=True):
        if refresh_data:
            self.found_flights=[]
        if isinstance(start_day,str):
            start_day = datetime.strptime(start_day, '%Y-%m-%d').date()
        url=os.environ['BASE_ENDPOINT_V2']+r'/shopping/flight-offers'
        header = {'Authorization': f'Bearer {self._api_token}'}
        body = {
            'originLocationCode':origin,
            'destinationLocationCode':destination,
            'adults': 1,
            'currencyCode': currency,
            'max':limit
            }

        for i in range(how_many_days):
            body['departureDate']=start_day+timedelta(days=i)

            print(f"hledam den {body['departureDate']}...")

            response = requests.get(url=url,headers=header,params=body,timeout=5)
            response.raise_for_status()
            for flight in response.json()['data']:
                self.found_flights.append(FlightData(
                    origin,
                    destination,
                    flight['price']['grandTotal'],
                    flight['itineraries'][0]['segments'],
                    currency
                    ))

            if present:
                self.show_results()

    def show_results(self):
        for i,flight in enumerate(self.found_flights):
            print(f'{i+1}.')
            print('='*20)
            print(flight)
            print()

    def get_cheapest_flight(self):
        if not self.found_flights:
            raise self.EmptyResultsException('Search engine has no flights')
        else:
            return min(self.found_flights, key=lambda x: x.price_nr)

    def get_shortest_flight(self):
        if not self.found_flights:
            raise self.EmptyResultsException('Search engine has no flights')
        else:
            return min(self.found_flights, key=lambda x: x.arrival-x.departure)

    def get_fastest_flight(self):
        if not self.found_flights:
            raise self.EmptyResultsException('Search engine has no flights')
        else:
            return min(self.found_flights, key=lambda x: x.arrival)
