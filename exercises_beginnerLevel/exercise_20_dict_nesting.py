#nesting
capitals={
    "India":"Delhi",
    "France":"Paris",
    "Germany":"Berlin",
}

#nesting a list in a dictionary
travel_visited_places={
    'France':['Paris','Lille'],
    'India':['Kerala','TN'],
}
print("nesting a list in a dictionary:")
print(travel_visited_places)
travel_visited_places['France']='Dijon'
print(travel_visited_places)


#nesting a dictionary in a dictionary
travel_visited_places={
    'France':{'Cities_visited':['Paris','Lille'], 'total_visits':12},
    'India':{'cities_visited':['Kerala','TN']},'total_visited':22,
}
print()
print("nesting a dictionary in a dictionary:")
print(travel_visited_places)

#list of dictionaries
travel_visited_places=[
    {
        'country':'France',
        'Cities_visited':['Paris','Lille'],
        'total_visits':12
    },

    {
        'county':'India',
        'cities_visited':['Kerala','TN'],
        'total_visited':22
    },
]
print(travel_visited_places)