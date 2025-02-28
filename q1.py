from io import BytesIO
from q2 import *
import requests
from PIL import Image

toponym_to_find = "г. Моска, ул. Профсоюзная 156 к6"
toponym_longiture, toponym_lattitude = get_coordinates(toponym_to_find)
ll, span = get_ll_span(toponym_to_find)

map_params = {
    "ll": ll,
    "spn": span,
    "l": "map",
    "pt": ll
}

map_api_server = "https://static-maps.yandex.ru/v1"
response = requests.get(map_api_server, params=map_params)
Image.open(BytesIO(response.content)).show()
