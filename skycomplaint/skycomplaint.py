from haversine import haversine
from FlightRadar24.api import FlightRadar24API


def skycomplaint():
    haversine((0, 0), (1, 1))
    api = FlightRadar24API()
    api.get_flights()

