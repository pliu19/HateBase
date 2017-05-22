Python HateBase Wrapper
===========

Simple Python HateBase v3.0 wrapper for [http://hatebase.org API](http://www.hatebase.org/connect_api)

Clone From https://github.com/andreyferriyan/HateBase, which supports Python 2. This repository supports Python 3. 

# How to use

1. Obtain a [hatebase API key](http://www.hatebase.org/request_api)
2. Go ahead and try it out. The following python script or command can be used as an example
3. In order to get all the vocabulary, simply chage 'page' in 'filters' dict. 

```
>>> from HateBase import HateBaseAPI
>>> hba = HateBaseAPI('--your-api-key-from-hatebase--')
>>> filters = { 'about_language' : '1', 'language' : 'eng', 'page': '1'}
>>> hba.requests(filters, query_type='vocabulary', output='json')
'http://api.hatebase.org/v3-0/--you-api-key-from-hatebase--/vocabulary/json/a
bout_language%3D1%7Clanguage%3D1'
>>> req = hba.requests(filters, query_type='vocabulary', output='json')
>>> from urllib.request import urlopen
>>> fhandle = urlopen(req)
>>> fhandle.read()
```


