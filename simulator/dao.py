from models import Airport, Airline, Country


def save_country(country):
    try:
        country.save()
        return True
    except Exception as e:
        print 'Error: cannot save Country, ', str(country), e.message
        return False


def save_airport(airport):
    try:
        airport.save()
        return True
    except Exception as e:
        print 'Error: cannot save Airport, ', str(airport), e.message
        return False


def save_airline(airline):
    try:
        airline.save()
        return True
    except Exception as e:
        print 'Error: cannot save Airline, ', str(airline), e.message
        return False


def find_country_by_name(name):
    try:
        country = Country.objects.get(name=name)
        return country
    except Exception as e:
        print "Error: cannot find area by name ", name, e.message
        return None


def save_area(area):
    try:
        area.save()
        return True
    except Exception as e:
        print "Error: cannot save Area ", str(area), e.message
        return False
