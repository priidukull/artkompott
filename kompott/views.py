import os

from django.shortcuts import render
from sqlalchemy import create_engine

if os.environ.get('ENVIRONMENT') == 'legal_webapp':
    db_conn_string = 'postgresql://artkompott@localhost:5432/kompott'
else:
    db_conn_string = 'postgresql://priidukull@localhost:5432/kompott'
engine = create_engine(db_conn_string)


def index(request):
    artists = engine.execute('SELECT * FROM artist')
    image_data = []
    secondary_image_data = []
    for artist in artists:
        image_data.append(('%s-1' % artist.prefix, artist))
        if artist.prefix != 'liisi':
            secondary_image_data.append(('%s-2' % artist.prefix, artist))
    image_data += secondary_image_data
    context = dict(image_data=image_data)
    return render(request, 'index.html', context=context)

def category(request, cat):
    artists = engine.execute("SELECT * FROM artist WHERE category='%s'" % cat)
    image_data = []
    secondary_image_data = []
    for artist in artists:
        image_data.append(('%s-1' % artist.prefix, artist))
        if artist.prefix == 'liisi':
            continue
        secondary_image_data.append(('%s-2' % artist.prefix, artist))
        if artist.prefix in ('ene', 'mirgoods'):
            continue
        secondary_image_data.append(('%s-3' % artist.prefix, artist))
        if artist.prefix in ('aleksandra', 'sofia'):
            continue
        secondary_image_data.append(('%s-4' % artist.prefix, artist))
    image_data += secondary_image_data
    context = dict(image_data=image_data)
    return render(request, 'index.html', context=context)


