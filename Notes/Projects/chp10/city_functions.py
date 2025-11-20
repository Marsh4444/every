def Country_Details(city, country, population = ''):
    """Tells us about a country"""
    if population:
        country_details = f"{city}, {country}- population={population}"
    else:
        country_details = f"{city}, {country}"
    return country_details.title()

name = Country_Details('london', 'england', 3000000)
print(name)
