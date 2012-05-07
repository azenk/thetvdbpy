#!/usr/bin/env python
from xml.dom.minidom import parse, parseString
import urllib2

import datetime
import random
import inspect

class thetvdb:

	def __init__(self,apikey):
		"""
		Creates an instance of the TVDB python interface using your api key.
		"""
		self.apikey = apikey
		self.mirrors = self.___getmirrors()
		random.seed()

	def ___choosemirror(self,mirrortype):
		"""Choose a mirror at random"""
		if mirrortype == "xml":
			index = random.randint(0,len(self.mirrors["xmlmirrors"])-1)	
			return self.mirrors["xmlmirrors"][index]
		elif mirrortype == "banner":
			index = random.randint(0,len(self.mirrors["bannersmirrors"])-1)	
			return self.mirrors["bannersmirrors"][index]
		elif mirrortype == "zip":
			index = random.randint(0,len(self.mirrors["zipmirrors"])-1)	
			return self.mirrors["zipmirrors"][index]

	def ___geturl(self,url):
		f = urllib2.urlopen(url)
		document = f.read()
		return document

	def ___getmirrors(self):
		"""
		Returns a list of mirrors
		"""
		mirrordict = {"xmlmirrors":[],"bannermirrors":[],"zipmirrors":[]}
		url = "http://www.thetvdb.com/api/%s/mirrors.xml" % self.apikey
		document = self.___geturl(url)
		#print document
		dom = parseString(document)
		mirrors = dom.getElementsByTagName("Mirror")
		for mirror in mirrors:
			id = mirror.getElementsByTagName("id")[0].firstChild.nodeValue
			url = mirror.getElementsByTagName("mirrorpath")[0].firstChild.nodeValue
			typemask = int(mirror.getElementsByTagName("typemask")[0].firstChild.nodeValue)
			if (typemask & 1 != 0):
				# This is a xml mirror
				mirrordict["xmlmirrors"].append(url)

			if (typemask & 2 != 0):
				# This is a banner mirror
				mirrordict["bannermirrors"].append(url)

			if (typemask & 4 != 0):
				# This is a zip mirror
				mirrordict["zipmirrors"].append(url)

		return mirrordict

	def getservertime(self):
		"""Gets the current server time, returns as a datetime.datetime object"""
		url = "http://www.thetvdb.com/api/Updates.php?type=none"
		dom = parseString(self.___geturl(url))
		time = dom.getElementsByTagName("Time")[0].firstChild.nodeValue
		return datetime.datetime.fromtimestamp(float(time))

	def getserieszip(self,seriesid,filename):
		"""Download zipfile for series"""
		url = "%s/api/%s/series/%i/all/en.zip" % (self.___choosemirror("zip"),self.apikey,seriesid)
		z = self.___geturl(url)
		f = open(filename,"w")
		f.write(z)
		
