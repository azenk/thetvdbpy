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

if __name__ == "__main__":
	main()
	
