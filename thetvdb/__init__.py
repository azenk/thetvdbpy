#!/usr/bin/env python
from xml.etree.ElementTree import ElementTree
import httplib

class thetvdb:

	def __init__(self,apikey):
		"""
		Creates an instance of the TVDB python interface using your api key.
		"""
		self.apikey = apikey
		self.mirrors = self.___getmirrors()
		print self.mirrors

	def ___getmirrors(self):
		"""
		Returns a list of mirrors
		"""
		mirrordict = {"xmlmirrors":[],"bannermirrors":[],"zipmirrors":[]}
		conn = httplib.HTTPConnection("www.thetvdb.com")
		conn.request("GET","/api/%s/mirrors.xml" % self.apikey)
		r1 = conn.getresponse()
		if r1.status != 200:
			# TODO: throw useful exception
			pass
		#document = r1.read()
		#print document
		tree = ElementTree()
		tree.parse(r1)
		mirrors = tree.find("Mirrors")
		for mirror in list(mirrors.iter("Mirror")):
			id = mirror.find("id").text
			url = mirror.find("mirrorpath").text
			typemask = int(mirror.find("typemask").text)
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
