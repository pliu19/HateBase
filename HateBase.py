#!/usr/bin/env python
# -*- coding: ASCII -*-
import urllib2

"""HateBase Wrapper v3.0 for hatebase.org API class

   construct url:
   http://api.hatebase.org/version/key/query-type/output/encoded-filters

   version	v{increment}-{sub-increment}
   key	{32-digit key}
   query type	{query type}	vocabulary; sightings
   output	{output}	xml; json
   (encoded) filters	{key}%3D{value}%7C{key}%3D{value}	(see filter table below)

"""
__author__ = "Andrey Ferriyan"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Andrey Ferriyan"
__email__ = "andrey.silversburg@gmail.com"
__status__ = "Development"


class HateBaseAPI(object):
    """
            The HateBase Class
    """

    def __init__(self, key=""):
        """Initialization of class."""
        self.base_url = "http://api.hatebase.org"
        self.version = "3"
        self.key = key
        self.url = ""

    def encoded_filters(self, parameters=dict()):
        """encoded filters and added to the requests code."""
        primary = "%3D"
        secondary = "%7C"
        pair = []

        for key, value in parameters.iteritems():
            pair.append(key + primary + value)

        return self.url + pair[0] + secondary + pair[1]

    def requests(self, filters=dict(), query_type='vocabulary', output='xml'):
        """return url for opening."""
        self.url = self.base_url + "/v" + self.version + "-0/" + self.key + "/" + \
            query_type + "/" + output + "/" + HateBaseAPI().encoded_filters(filters)
        return self.url
