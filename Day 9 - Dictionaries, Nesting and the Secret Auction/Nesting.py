""" Nested dictionary
{
    Key1: [List],
    Key2: {Dict},

}
"""
## Nesting
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

## Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

## Nesting Dictionary in a dictionary
travel_log = {
    "France": {"cities_visited" :  ["Paris", "Lille", "Dijon"], "total_visites" : 12},
   
    "Germany": {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visites" : 13},
}


## Nesting a dictionary in a list
travel_log = [
    {
        "country" : "France" , 
        "cities_visited" :  ["Paris", "Lille", "Dijon"], 
        "total_visites" : 12
    },
   
    { 
        "country" : "Germany",
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
        "total_visites" : 13
    },
]