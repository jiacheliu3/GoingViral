from django.shortcuts import render
import tools
import dao
from models import Country, Airline, Airport
from django.http import HttpResponse
import toolbox

'''
    CRUD actions
'''


# Country
def add_country(request):
    name = request.GET['name']
    population = request.GET['population']
    if not population.isdigit():
        print 'Error: Population ', population, ' is not an int'
        return HttpResponse(content_type="application/json", status_code=406)

    # Create the area
    area = Country(name=name, population=int(population))
    if dao.save_area(area) is False:
        return HttpResponse(content_type="application/json", status_code=406)

    return HttpResponse(content_type="application/json", status_code=200)


# Add location to an existing country by name
def add_location_to_country(request):
    name = request.GET['name']

    # Input validation
    latitude_raw = toolbox.try_parse_float(request.GET['latitude'])
    if latitude_raw is False:
        print 'Error: Latitude ', request.GET['latitude'], ' is not a number'
        return HttpResponse(content_type="application/json", status_code=406)
    elif latitude_raw > 90.0 or latitude_raw < -90.0:
        print 'Error: Latitude ', latitude_raw, ' out of range -90~90'
        return HttpResponse(content_type="application/json", status_code=406)

    longitude_raw = toolbox.try_parse_float(request.GET['longitude'])
    if longitude_raw is False:
        print 'Error: Longitude ', request.GET['longitude'], ' is not a number'
        return HttpResponse(content_type="application/json", status_code=406)
    elif longitude_raw > 180.0 or longitude_raw < -180.0:
        print 'Error: Longitude ', longitude_raw, ' out of range -180~180'
        return HttpResponse(content_type="application/json", status_code=406)

    # Find the country first
    country = dao.find_country_by_name(name)
    if country is None:
        print 'Error: Cannot add location to country ', name
        return HttpResponse(content_type="application/json", status_code=406)

    # Add the location to the country
    country.update(latitude=float(latitude_raw), longitude=float(longitude_raw))
    return HttpResponse(content_type="application/json", status_code=200)


# Add an airport
def add_airport(request):
    city_name = request.GET['city_name']
    country_name = request.GET['country_name']
    latitude_raw = request.GET['latitude']
    longitude_raw = request.GET['longitude']

    # Input validation
    latitude = toolbox.try_parse_float(latitude_raw)
    if latitude is False:
        print 'Error: Latitude ', request.GET['latitude'], ' is not a number'
        return HttpResponse(content_type="application/json", status_code=406)
    longitude = toolbox.try_parse_float(longitude_raw)
    if longitude is False:
        print 'Error: Longitude ', request.GET['longitude'], ' is not a number'
        return HttpResponse(content_type="application/json", status_code=406)

    # Find country
    country = dao.find_country_by_name(country_name)
    if country is None:
        print 'Error: the country ', country_name, ' of airport ', city_name, ' cannot be found'
        return HttpResponse(content_type="application/json", status_code=406)

    # Add airport
    airport = Airport(city_name=city_name, country=country, latitude=latitude, longitude=longitude)
    if dao.save_airport(airport) is False:
        return HttpResponse(content_type="application/json", status_code=406)

    return HttpResponse(content_type="application/json", status_code=200)


# Airline
def add_airline(request):
    print "Add airline"
    name = request.GET['name']
    departure = tools.parse_date(request.GET['departure'])
    arrival = tools.parse_date(request.GET['arrival'])

    from_city = request.GET['from_city']
    from_country = request.GET['from_country']
    to_city = request.GET['to_city']
    to_country = request.GET['to_country']
    from_area = dao.find_area_by_name(from_country)
    to_area = dao.find_area_by_name(to_country)

    # Create the airline
    airline = Airline(name=name, departure=departure, arrival=arrival, from_area=from_area, to_area=to_area)
    if dao.save_airline(airline) is False:
        return HttpResponse(content_type="application/json", status_code=406)

    return HttpResponse(content_type="application/json", status_code=200)
