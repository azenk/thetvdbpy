#!/usr/bin/env python

import sys
sys.path.insert(0,"..")
from optparse import OptionParser

import thetvdb

def main():
	p = OptionParser()
	p.add_option("-a","--apikey",dest="apikey")
	(options,args) = p.parse_args()
	tvdb = thetvdb.thetvdb(options.apikey)

	print "Server time: %s" % tvdb.getservertime()
	tvdb.getserieszip(72073,"test.zip")

if __name__ == "__main__":
	main()
	
