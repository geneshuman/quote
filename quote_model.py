#!/usr/bin/env python

"""quote
   a utility for producing quotes for laser cutting 2d shapes

   usage - ./quote_model [file]
"""
import sys, getopt, json

from model.util import *

def main():
    # validate args
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)

    for o, a in opts:
        if o in ("-h", "--help"):
            print __doc__
            sys.exit(0)

    if len(sys.argv) != 2:
        print __doc__
        sys.exit(0)

    # quote model
    filename = sys.argv[1]
    try:
        f = open(filename)
    except IOError:
        print "File or path not found - %s" % filename
        sys.exit(0)

    try:
        data = json.load(f)
    except ValueError:
        print "Decoding JSON has failed"
        f.close()
        sys.exit(0)

    try:
        model = parse_json(data)
    except ValueError as e:
        print str(e)
        f.close()
        sys.exit(0)

    f.close()

    # validate(model) - might be overkill for this project

    print '%.2f dollars' % quote(model)


if __name__ == "__main__":
    main()
