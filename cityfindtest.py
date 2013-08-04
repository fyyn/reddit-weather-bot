import pywapi

cities = ["Vienna", "Madrid", "Munich"]

sentence = "Forecast please. City: Vienna"
for city in cities:
    if city in sentence:
        print(city)

new_sentence = sentence.replace("Forecast please. City: ", "")

print new_sentence

names = pywapi.get_location_ids("Chicago")

print """Which location did you mean? Please find the location in the
    following list, and reformulate your request with the correct city code:"""

for thing in names:
    print "City: " + names[thing] + " Code: " + thing


