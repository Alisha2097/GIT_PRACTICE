cities = [["Nepal","Kathmandu"],["USA","New York"],["Australia","Sydney"],["UK","London"]]
# cities = {"Kathmandu","New York"}
# for country, city in cities:
#     print("country is " + country +"and city is " + city)

my_dictionary = dict(cities)
print(my_dictionary)

for country,city in my_dictionary.items():
    print(country,city)
    for s in country:
        print(s)

# for city in cities:
#     print(city)

