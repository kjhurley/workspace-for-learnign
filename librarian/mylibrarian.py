#!/usr/local/bin/python2.7
# encoding: utf-8
'''
mylibrarian -- tool for library taks

mylibrarian is a command line tool for finding new recordings of tv shows and 
movies and putting them in suitable locations with names that xbmc can match


@author:     Kevin Hurley
        
@copyright:  2014 Kevin Hurley.
        
@license:    free for all

'''

import sys
import os

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

import librarian
import glob

__all__ = []
__version__ = 0.1
__date__ = '2014-08-29'
__updated__ = '2014-08-29'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''
    
    print "hello"
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = """ %s is a tool for detecting and processing new recordings 
    """%program_name

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-n", "--newfiles", dest="new_files", action="store_true", help="list new files")
        
        # Process arguments
        args = parser.parse_args()
        
        new_files = args.new_files
        
        print "ready?"
        a_librarian = librarian.Librarian()
        
        for a_file in glob.glob("/srv/media/IPlayer/log_*.out"):
            with open(a_file) as a_log:
                a_librarian.look_for_new_files(a_log)
        
        
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0

   # except Exception, e:
   #     if DEBUG or TESTRUN:
   #         raise(e)
   #     else:
   #         raise(e)
   #     indent = len(program_name) * " "
   #     sys.stderr.write(program_name + ": " + repr(e) + "\n")
   #     sys.stderr.write(indent + "  for help use --help")
   #     return 2

if __name__ == "__main__":
    sys.exit(main())