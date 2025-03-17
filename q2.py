import requests


def ge(ttf):
    geoas = 'http://geocode-maps.yandex.ru/1.x/'
    geopar = {
        'apikey': '8013b162-6b42-4997-9691-77b7074026e0',
        'geocode': ttf,
        'format': 'json'
    }
    resp = requests.get(geoas, params=geopar)
    if not resp:
        pass
    jsr = resp.json()
    t = jsr["response"]["GeoObjectCollection"]["featureMember"][0]['GeoObject']
    return t if t else None


def get_coordinates(ttf):
    t = ge(ttf)
    if not t:
        return None, None
    t_c = t['Point']['pos']
    toponym_longiture, toponym_lattitude = t_c.split(' ')
    toponym_longiture, toponym_lattitude = float(toponym_longiture), float(toponym_lattitude)


def get_ll_span(ttf):
    t = ge(ttf)
    if not t:
        return None, None
    t_c = t['Point']['pos']
    toponym_longiture, toponym_lattitude = t_c.split(' ')

    ll = ','.join([toponym_longiture, toponym_lattitude])
    left, bottom = t['boundedBy']['Envelope']['lowerCorner'].split(' ')
    right, top = t['boundedBy']['Envelope']['lowerCorner'].split(' ')

    dx = abs(float(left) - float(right)) / 2
    dy = abs(float(top) - float(bottom)) / 2
    span = f"{dx}{dy}"
    return ll, span
