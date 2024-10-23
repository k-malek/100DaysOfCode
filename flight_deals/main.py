# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

sheet_prices=DataManager.get_prices()
flight_search=FlightSearch()

for row,content in sheet_prices.iterrows():
    if not content['IATA Code']:
        sheet_prices.at[row,'IATA Code']=flight_search.get_city_iata(content['City'])

DataManager.set_prices(sheet_prices)

flight_search.get_all_flights('ROM',origin='PRG',how_many_days=30,start_day='2024-11-01')

print(flight_search.get_cheapest_flight())
print(flight_search.get_shortest_flight())
print(flight_search.get_fastest_flight())
