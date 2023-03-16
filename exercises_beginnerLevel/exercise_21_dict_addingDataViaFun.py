#AUTHOR   :  JUNA TERES MARTIN
#PROGRAM  :  Write a program that adds a dictionary to a list by calling a function
#DATE     :  16-03-2023

#travel_log is a list with data as dictionaries
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country_name,no_of_visits,cities_visited):
    new_country={} #create an empty list
    new_country["country"]=country_name
    new_country["visits"]=no_of_visits
    new_country["cities"]=cities_visited
    travel_log.append(new_country) #append dict to the list

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"]) #this data should be added
print(travel_log)
