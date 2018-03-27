#la_Weather.py - warming up exercise

#FUNCTIONS
def weather_counts( a ):
    weather_counts = {}
    for item in a:
        if item in weather_counts:
            weather_counts[item] += 1
        else:
            weather_counts[item] = 1
    return weather_counts



weather_data = []
f = open("la_weather.csv", 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_row = row.split(",")
    weather_data.append( split_row[1] )
weather_data = weather_data[1:]

print( weather_counts( weather_data ) )



    
