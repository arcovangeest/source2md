#!/usr/bin/env python3
## @file
##
## @brief MD filter
##

##
## @author Arco van Geest <d.a.c.vangeest@tudelft.nl>
##
## 
## @date 20190906 first version
##
## grab marked MD lines from source and output md to stdout
##
## 
import sys
import re

functionheader="# "

def get_filter(extension):
  """function to get the right filter function
  """
  ## Depending on the extention a filter is used:
  functionswitch = {
    ## ```
    ## @verbatim
    'php': filter_shell,
    'cfg': filter_cfg,
    'cmd': filter_cmd,
    'Dockerfile': filter_cfg,
    'sh': filter_shell,
    'awk': filter_cfg,
    'add': filter_cfg,
    'conf': filter_cfg,
    'dox': filter_default,
    'ps1': filter_cfg,
    'pl': filter_cfg,
    'xml': filter_xml,
    'xslt': filter_xml,
    'html': filter_xml,
    'ini': filter_ini,
    'pp': filter_cfg,
    'sql': filter_sql,
    'c': filter_default,
    'h': filter_default,
    'cpp': filter_default,
    'md': filter_default,
    'py': filter_shell,
    'yaml': filter_cfg,
    'yml': filter_cfg,
    'au3': filter_cfg,
    'ipxe': filter_cfg
    ## @endverbatim
    ## ```
  }
  func = functionswitch.get(extension, filter_default)
  return func

def doxygen_filter(filename):
  """doxygen_filter
    
    filters non native doxygen-fileformats into md streams

    @param filename 

    @returns none
  """

  #sys.stderr.write("filename = ") 
  #sys.stderr.write("filename = ",filename) 
  #sys.stderr.write(("extension = "+ str(filename.rpartition('.')[-1]) )
  extension = str(filename.rpartition('.')[-1])
  func = get_filter(extension)
  #sys.stderr.write(("used function: "+ str(func.__name__))
  length = func(filename)
  # if no length after filter, hide page in GrpDummyPages
#  if length==0:
#    print('\ingroup GrpDummyPages')
      
  return


def filter_shell(filename):
  """filter shell to md
     
   lines starting with the magic '##' will be shown.
   lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.
   lines between the magics '## SKIP_START' and '## SKIP_END' will be skipped.
  
  """
  ##
  ## #### filter_shell
  ## filter shell to md
  ##
  ## lines starting with the magic '##' will be shown.
  ##
  ## lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.
  ##
  ## lines between the magics '## SKIP_START' and '## SKIP_END' will be skipped.
  ##
  l = 0
  with open(filename, 'r') as fp:
    line = fp.readline()
    verbatim=0
    blok=0
    skip=0
    while line:
      show=0
      if re.match(r'^\s*##',line):
        show=1
      if re.match(r'^\s*##\s*\@verbatim',line):
        show=0
        verbatim=1
        line=""
      if re.match(r'^\s*##\s*\@endverbatim',line):
        show=1
        verbatim=0
        line=""
      if re.match(r'^\s*##\s*SKIP_START',line):
        show=0
        skip=1
      if re.match(r'^\s*##\s*SKIP_END',line):
        show=0
        skip=0
      if (show==1 or verbatim==1 or blok==1) and skip==0:  
        line = re.sub(r'^\s*##','',line)
        line = re.sub(r'^\s*##','##',line)
        line = re.sub(r'^\s*--','--',line)
        line = re.sub(r'^\s*==','==',line)
        print(line.rstrip()) 
        l += len(line.rstrip()) 
      line = fp.readline()
  fp.close()
  return l
  # /filter_shell

def filter_cmd(filename):
  """filter cmd to md
     
   lines starting with the magic '::!' will be shown.
   lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.
   lines between the magics '::! SKIP_START' and '::! SKIP_END' will be skipped.
  
  """
  ##
  ## #### filter_cmd
  ## filter cmd to md
  ##
  ## lines starting with the magic '::!' will be shown.
  ##
  ## lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.
  ##
  ## lines between the magics '::! SKIP_START' and '::! SKIP_END' will be skipped.
  ##
  l = 0
  with open(filename, 'r') as fp:
    line = fp.readline()
    verbatim=0
    blok=0
    skip=0
    magic='(::!)'
    while line:
      show=0
      if re.match(r'^\s*'+magic,line):
        show=1
      if re.match(r'^\s*'+magic+r'\s*\@verbatim',line):
        show=0
        verbatim=1
        line=""
      if re.match(r'^\s*'+magic+r'\s*\@endverbatim',line):
        show=1
        verbatim=0
        line=""
      if re.match(r'^\s*'+magic+r'\s*SKIP_START',line):
        show=0
        skip=1
      if re.match(r'^\s*'+magic+r'\s*SKIP_END',line):
        show=0
        skip=0
      if (show==1 or verbatim==1 or blok==1) and skip==0:  
        line = re.sub(r'^\s*'+magic,'',line)
        line = re.sub(r'^\s*##','##',line)
        line = re.sub(r'^\s*--','--',line)
        line = re.sub(r'^\s*==','==',line)
        print(line.rstrip()) 
        l += len(line.rstrip()) 
      line = fp.readline()
  fp.close()
  return l
  # /filter_cmd

def filter_cfg(filename):
  """filter cfg to md
     
   lines starting with the magic '##' will be shown.
   lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.
   lines between the magics '## SKIP_START' and '## SKIP_END' will be skipped.
  
  """
  ##
  ## #### filter_cfg
  ## filter cfg to md
  ##
  ## lines starting with the magic '##' will be shown.
  ##
  ## lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.
  ##
  ## lines between the magics '## SKIP_START' and '## SKIP_END' will be skipped.
  ##
  l = 0
  with open(filename, 'r') as fp:
    line = fp.readline()
    verbatim=0
    blok=0
    skip=0
    magic='(##|!!)'
    while line:
      show=0
      if re.match(r'^\s*'+magic,line):
        show=1
      if re.match(r'^\s*'+magic+r'\s*\@verbatim',line):
        show=0
        verbatim=1
        line=""
      if re.match(r'^\s*'+magic+r'\s*\@endverbatim',line):
        show=1
        verbatim=0
        line=""
      if re.match(r'^\s*'+magic+r'\s*SKIP_START',line):
        show=0
        skip=1
      if re.match(r'^\s*'+magic+r'\s*SKIP_END',line):
        show=0
        skip=0
      if (show==1 or verbatim==1 or blok==1) and skip==0:  
        line = re.sub(r'^\s*'+magic,'',line)
        line = re.sub(r'^\s*##','##',line)
        line = re.sub(r'^\s*--','--',line)
        line = re.sub(r'^\s*==','==',line)
        print(line.rstrip()) 
        l += len(line.rstrip()) 
      line = fp.readline()
  fp.close()
  return l
  # /filter_cfg

def filter_xml(filename):
  """filter xml to md
     
   lines starting with the magic '<!---' will be shown until the first '-->'.
   lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.
   lines between the magics '<!--- SKIP_START' and '<!--- SKIP_END' will be skipped.
  
  """
  ##
  ## #### filter_xml
  ## filter xml to md
  ##
  ## lines starting with the magic '<!---' will be shown until the first '-->'.
  ##
  ## lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.
  ##
  ## lines between the magics '<!--- SKIP_START' and '<!--- SKIP_END' will be skipped.
  ##
  l = 0
  with open(filename, 'r') as fp:
    line = fp.readline()
    verbatim=0
    blok=0
    skip=0
    while line:
      show=0
      if re.match(r'^\s*<!---',line):
        show=1
        blok=1
      if re.match(r'-->\s*$',line):
        show=blok
        blok=0
      if re.search(r'\@verbatim',line):

        show=0
        verbatim=1
        line=""
      if re.search(r'\@endverbatim',line):

        show=0
        verbatim=0
        blok=0
      if re.search(r'SKIP_START',line):
        show=0
        skip=1
      if re.search(r'SKIP_END',line):
        show=0
        skip=0
      if (show==1 or verbatim==1 or blok==1) and skip==0:  
        line = re.sub(r'^\s*<!---' ,'',line)
        line = re.sub(r'-->\W*$' ,'\n',line)
        print(line.rstrip() )
        l += len(line.rstrip()) 
      line = fp.readline()
  fp.close()
  return l
  # /filter_xml
def filter_ini(filename):
  """filter ini to md
    
   lines starting with the magic ';;' will be shown.\n
   lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.\n
   lines between the magics ';; SKIP_START' and ';; SKIP_END' will be skipped.\n
   section headers [name] wil result in a section header 
  """ 
  ##
  ## #### filter_ini
  ## filter ini to md
  ##   
 
  ## lines starting with the magic ';;' will be shown.\n
  ##
  ## lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.\n
  ##
  ## lines between the magics ';; SKIP_START' and ';; SKIP_END' will be skipped.\n
  ##
  ## section headers [name] wil result in a section header 
  ##

  l = 0
  with open(filename, 'r') as fp:
    line = fp.readline()
    verbatim=0
    blok=0
    skip=0
    while line:
      show=0
      if re.match(r'^\s*\[',line):
        show=0
        ## section name s
        section = re.sub( r'[\[\]]' , '' , line)
        print()
        print("@section "+section +"[]"+section+"]")
        print()
      if re.match(r'^\s*;;',line):
        show=1
      if re.match(r'^\s*;;\s*\@verbatim',line):
        show=0
        verbatim=1
        line=""
      if re.match(r'^\s*;;\s*\@endverbatim',line):
        show=1
        verbatim=0
        line=""
      if re.match(r'^\s*;;\s*SKIP_START',line):
        show=0
        skip=1
      if re.match(r'^\s*;;\s*SKIP_END',line):
        show=0
        skip=0
      if (show==1 or verbatim==1 or blok==1) and skip==0:  
        line = re.sub(r'^\s*;;','',line)
        line = re.sub(r'^\s*##','##',line)
        line = re.sub(r'^\s*--','--',line)
        line = re.sub(r'^\s*==','==',line)
        print(line.rstrip()) 
        l += len(line.rstrip()) 
      line = fp.readline()
  fp.close()
  return l
  # /filter_ini

def filter_sql(filename):
  """filter sql to md
     
   lines starting with the magic '--!' will be shown.
   lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.
   lines between the magics '--! SKIP_START' and '--! SKIP_END' will be skipped.
  
  """
  ##
  ## #### filter_sql
  ## filter sql to md
  ##   
  ## lines starting with the magic '--!' will be shown.
  ##
  ## lines between the magics '(at)verbatim' and '(at)endverbatim' will be shown.
  ##
  ## lines between the magics '--! SKIP_START' and '--! SKIP_END' will be skipped.
  l = 0
  with open(filename, 'r') as fp:
    line = fp.readline()
    verbatim=0
    blok=0
    skip=0
    magic='(--!)'
    while line:
      show=0
      if re.match(r'^\s*'+magic,line):
        show=1
      if re.match(r'^\s*/\*\*',line):
        show=1
        blok=1
      if re.match(r'[*][/]\s*$',line):
        show=blok
        blok=0
        
      if re.match(r'^\s*'+magic+r'\s*\@verbatim',line):
        show=0
        verbatim=1
        line=""
      if re.match(r'^\s*'+magic+r'\s*\@endverbatim',line):
        show=1
        verbatim=0
        line=""
      if re.match(r'^\s*'+magic+r'\s*SKIP_START',line):
        show=0
        skip=1
      if re.match(r'^\s*'+magic+r'\s*SKIP_END',line):
        show=0
        skip=0
      if re.match(r'^\s*CREATE PROCEDURE',line):
        show=0
        sfunction=re.sub(r'^\s*CREATE PROCEDURE\s*','',line)
        sfunction=re.sub(r'\s*$','',sfunction)
        if skip==0:
          print()
          print(functionheader + ' Procedure ' + sfunction)
          print()
      if (show==1 or verbatim==1 or blok==1) and skip==0:  
        line = re.sub(r'^\s*'+magic,'',line)
        line = re.sub(r'^\s*\/[*][*]','',line)
        line = re.sub(r'[*][/]\s*$','',line)
        line = re.sub(r'^\s*##','##',line)
        line = re.sub(r'^\s*--','--',line)
        line = re.sub(r'^\s*==','==',line)
        print(line.rstrip()) 
        l += len(line.rstrip()) 
      line = fp.readline()
  fp.close()
  return l
  # /filter_sql

def filter_default(filename):
  """pass though filter
        just read and output data
  """
##
## #### filter_default
## pass though filter
##
## just read and output data
##
  l = 0
  with open(filename, 'r') as fp:
   line = fp.readline()
   while line:
       print(line.strip())
       l += len(line.strip()) 
       line = fp.readline()
   fp.close()
  return l
  # /filter_default

if __name__== "__main__":
  # script name 
  program_name=sys.argv[0]
  # command line args
  arguments = sys.argv[1:]
  # amount of command line options
  argcount = len(arguments) 
  # file name
  filename = arguments[0]
  doxygen_filter(filename)
