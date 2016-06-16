Python HateBase Wrapper
===========

Simple Python HateBase v3.0 wrapper for [http://hatebase.org API](http://www.hatebase.org/connect_api)

# How to use

1. Obtain a [hatebase API key](http://www.hatebase.org/request_api)
2. Go ahead and try it out. The following python script or command can be used as an example

```
>>> from HateBase import HateBaseAPI
>>> hba = HateBaseAPI('--your-api-key-from-hatebase--')
>>> filters = { 'about_language' : '1', 'language' : 'eng' }
>>> hba.requests(filters, query_type='vocabulary', output='json')
'http://api.hatebase.org/v3-0/--you-api-key-from-hatebase--/vocabulary/json/a
bout_language%3D1%7Clanguage%3D1'
>>> req = hba.requests(filters, query_type='vocabulary', output='json')
>>> import urllib2
>>> fhandle = urllib2.urlopen(req)
>>> fhandle.read()
```


