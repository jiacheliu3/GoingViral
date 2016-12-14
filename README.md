**Url**

Base url: /sim


Create a country:

add_country?name=...&population=...

*Population is at the unit of one person*


Add an airport:

add_airport?city_name=...&country_name=...&latitude=...&longitude=...


Add an airline:

add_airline?name=...&departure_time=...&from_city=...&from_country=...


Add the location to a country:

add_location_to_country?name=...&latitude=...&longitude=...

**Notes:**
Latitude is within range [-90.0, 90.0]

Longitude is within range [-180.0, 180.0]

On input error, response code will be 406
