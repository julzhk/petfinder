from dataclasses import dataclass, field
from typing import List

import requests
from cache_memoize import cache_memoize
from dataclasses_json import dataclass_json
from django.conf import settings


@dataclass_json
@dataclass
class AnimalType:
    name: str
    coats: list[str] = field(default_factory=list)
    colors: list[str] = field(default_factory=list)
    genders: list[str] = field(default_factory=list)
    links: dict = field(default_factory=dict)


@dataclass_json
@dataclass
class Animals:
    animals: List[AnimalType] = field(default_factory=list)

    def __post_init__(self):
        data = make_request(path='types')
        self.animals = [AnimalType.from_dict(d) for d in data['types']]


@cache_memoize(settings.CACHES['default']['TIMEOUT'])
def get_access_token(url=settings.CLIENT_URL,
                     client_id=settings.CLIENT_ID,
                     client_secret=settings.CLIENT_SECRET):
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    )
    return response.json()["access_token"]


@cache_memoize(settings.CACHES['default']['TIMEOUT'])
def make_request(path):
    token = get_access_token()
    endpoint = f"https://api.petfinder.com/v2/{path}"
    headers = {"Authorization": f"Bearer {token}"}
    data = requests.get(endpoint,
                        headers=headers
                        ).json()
    return data
