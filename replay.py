#!/usr/bin/python

from subprocess import call
from optparse import OptionParser
from urlparse import urlparse
from cgi import parse_qs
from os import path, getcwd, chdir

oparser = OptionParser()
oparser.add_option("-u", action="store", dest="url")
options, _args = oparser.parse_args()

adstring = "Hosted by Intelligent Computing Solutions (ics-il.com)"

url_parts = urlparse(options.url)
replay_name = url_parts[4]
if replay_name:
    try:
        cwd = path.join("/var/www/ttybin/", "replays", replay_name)
        if path.exists(cwd):
            chdir(cwd)
            if path.isfile(replay_name + ".rti"):
                print adstring
                call(["scriptreplay", replay_name + ".rti"])
            elif path.isfile("ttyrecord"):
                print adstring
                call(["ttyplay", "ttyrecord"])
            else:
                print "There is no \"%s\" recording." % replay_name
        else:
            print "There is no \"%s\" recording." % replay_name
    except KeyboardInterrupt:
        print "\n"*200, "*****CARRIER LOST"
    else:
        print "\n"*200, adstring
