#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def get_special_paths(dir):
  result = []

  if not os.path.exists(dir):
    sys.stderr.write('No se puede abrir el directorio: ' + dir + '(' + os.path.abspath(dir) +')')
    return result

  files = os.listdir(dir)

  for filename in files:
    if re.search('__\w+__',filename):
      result.append(os.path.abspath(os.path.join(dir,filename)))

  return result

def copy_to(paths, dir):
  dir = os.path.abspath(dir)

  if not os.path.exists(dir):
    os.makedirs(dir)

  for path in paths:
    newpath = os.path.abspath( os.path.join(dir, os.path.basename(path) ) )
    shutil.copy(path, newpath)


def zip_to(paths, zippath):
  ret_code = os.system('zip -j ' + zippath + ' ' + ' '.join(paths))
  return ret_code==0


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  for dir in args:
    files = get_special_paths(dir)
    print('\n'.join(files))
    if todir:
      copy_to(files,todir)

    if tozip:
      if not zip_to(files,tozip):
        print "[ERROR] No se ha podido crear el archivo comprimido"

if __name__ == "__main__":
  main()
