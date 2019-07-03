from django.shortcuts import render
import requests

def dog(request):
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    image = response.json()['message']
    print(image)

    return render(request, 'eggs/dog.html', {'image':image})

def get_dog():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    if(response.json()['status'] == 'success'):
        image = response.json()['message']
        return image
    else:
        return None
