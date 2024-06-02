from datetime import datetime

class FlightData:
    class Segment():
        def __init__(self,from_city,departure,to_city,arrival) -> None:
            self.from_city=from_city
            self.departure=departure
            self.to_city=to_city
            self.arrival=arrival

    def __init__(self,origin,destination,price,segments,currency) -> None:
        self.origin=origin
        self.destination=destination
        self.price=f'{price} {currency}'
        self.price_nr=float(price)
        self.departure,self.arrival=self.retrieve_arrival_departure(segments)
        self.roadmap=self.generate_roadmap(segments)
        self.segments=[]
        self.generate_segments_from_json(segments)

    def __repr__(self) -> str:
        return f'''
Origin: {self.origin}
Destination: {self.destination}
Price: {self.price}
Departure: {self.departure}
Arrival: {self.arrival}
Roadmap: {self.roadmap}'''

    @staticmethod
    def retrieve_arrival_departure(segments_json):
        return (datetime.strptime(segments_json[0]['departure']['at'],'%Y-%m-%dT%H:%M:%S'),
                datetime.strptime(segments_json[-1]['arrival']['at'],'%Y-%m-%dT%H:%M:%S'))

    @staticmethod
    def generate_roadmap(segments_json):
        roadmap=segments_json[0]['departure']['iataCode']
        for segment_json in segments_json:
            roadmap+=f"->{segment_json['arrival']['iataCode']}"
        return roadmap

    def generate_segments_from_json(self,segments_json):
        for segment_json in segments_json:
            self.segments.append(self.Segment(
                segment_json['departure']['iataCode'],
                datetime.strptime(segment_json['departure']['at'],'%Y-%m-%dT%H:%M:%S'),
                segment_json['arrival']['iataCode'],
                datetime.strptime(segment_json['arrival']['at'],'%Y-%m-%dT%H:%M:%S'),
            ))
