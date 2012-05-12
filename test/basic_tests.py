#!/usr/bin/env python

import sys
sys.path.insert(0,"..")
from optparse import OptionParser
import ConfigParser

import thetvdb

def main():
	p = OptionParser()
	p.add_option("-c","--config",dest="config")
	(options,args) = p.parse_args()

        cp = ConfigParser.ConfigParser()
        cp.read([options.config])

	apikey = cp.get("thetvdb","apikey")

	tvdb = thetvdb.thetvdb(apikey)

	print "Server time: %s" % tvdb.getservertime()
	tvdb.getserieszip(72073,"test.zip")

if __name__ == "__main__":
	main()
	
