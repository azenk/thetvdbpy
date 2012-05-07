#!/usr/bin/env python
from xml.dom.minidom import parse, parseString
import httplib

import inspect

class thetvdb:

	def __init__(self,apikey):
		"""
		Creates an instance of the TVDB python interface using your api key.
		"""
		self.apikey = apikey
		self.mirrors = self.___getmirrors()
		print self.mirrors

	def ___choosemirror(self,mirrortype):
		"""Choose a mirror at random"""
		pass

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
		document = r1.read()
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
