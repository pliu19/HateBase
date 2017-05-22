from HateBase import HateBaseAPI

hba = HateBaseAPI('81a75e1d9a56edad8167ae7cb47b49ec')
filters = { 'about_language' : '1', 'language' : 'eng', 'page': '2'}
hba.requests(filters, query_type='vocabulary', output='json')

req = hba.requests(filters, query_type='vocabulary', output='json')

from urllib.request import urlopen

fhandle = urlopen(req)
print(fhandle.read())