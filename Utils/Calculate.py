def calculate_result(letters_dictionary):
    routes = 0
    for item in letters_dictionary:
        routes += (letters_dictionary[item][-1:][0])
    return routes
