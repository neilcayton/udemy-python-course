# nesting dictionary in a dictionary
travel_vlog = {
    'France': {"cities_visited": ['Paris', 'Lille', 'Dijon'], "total_visits": 12},
    'Germany': {"cities_visited": ['Hamburg', 'Berlin', 'Stuttgart'], "total_visits": 5}
}

# nesting dictionary into a lists

travel_log = [{
    {"country": 'France',
     "cities_visited": ['Paris', 'Lille', 'Dijon'],
     "total_visits": 12},

    {"country": 'Germany',
     "cities_visited": ['Hamburg', 'Berlin', 'Stuttgart'],
     "total_visits": 5}
}]
