#!/usr/bin/env python

"""quote
"""
import sys
import getopt

from model.util import *

def main():
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

    model = load(None)
    # validate(model) - might be overkill for this project
    # compute quote
    print '%.2f' % quote(model)

if __name__ == "__main__":
    main()
