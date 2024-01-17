import requests

print('---Welcome to the SoftUni Weather Forecast---')
print('Just Enter the City you want the weather report for and click on the button!')
city_name = input('Enter the name of the city: ')
print('\n\n')

url = f'https://wttr.in{city_name}'

try:
    data = requests.get(url)
    result = data.text
except:
    result = 'Error Occurred'

print(result)
