import requests


# If you wanna use a txt file instead of hard pasting it (if you can figure it out) use:#-> open('api_key.txt', 'r').read()
api_key = ('6d298b4853f93b0b36e9ece168ddb665')

while True:
    location = input('Where In the World? :')

    result = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={api_key}')
    if result.json()['cod'] == '404':
        print('Invalid Location!')
        continue
    break

description = result.json()['weather'][0]['description']
temp = round(result.json()['main']['temp'])
feels_like = round(result.json()['main']['feels_like'])
high = round(result.json()['main']['temp_max'])
low = round(result.json()['main']['temp_min'])

print(f'The Temperature in {location[0].upper()}{location[1:]} is {temp}°F with {description}, while it feels like {feels_like}°F. The high is {high}F° while the low is going to be {low}F°.')
