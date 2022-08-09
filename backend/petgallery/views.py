import requests
from cache_memoize import cache_memoize
from django.conf import settings
from django.shortcuts import render


@cache_memoize(settings.CACHES['default']['TIMEOUT'])
def get_access_token(url, client_id, client_secret):
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    )
    return response.json()["access_token"]

@cache_memoize(settings.CACHES['default']['TIMEOUT'])
def make_request():
    client_id = 'XXX'
    client_secret = 'YYY'
    url = 'https://api.petfinder.com/v2/oauth2/token'

    token = get_access_token(url, client_id, client_secret)

    endpoint = "https://api.petfinder.com/v2/animals?type=dog&page=1"
    headers = {"Authorization": f"Bearer {token}"}
    data = requests.get(endpoint,
                        headers=headers
                        ).json()
    return data


def home(request):
    pets = make_request()
    return render(request,
                  template_name='gallery_home.html',
                  context={'pets': pets['animals']})
