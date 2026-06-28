# TODO: Add more country codes
country_codes = {
    "PH": "Philippines",
    "US": "United States",
    "UK": "United Kingdom",
    "JP": "Japan",
}

# TODO: Print the country for the given country code
# TODO: # If the key is not found, print Unknown
print(country_codes.get(input("Enter Code: "), "Not Found"))
