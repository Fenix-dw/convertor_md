#!/usr/bin/env python

import re;
import os
import sys

arguments = sys.argv[1:] 

if len(arguments) > 0 :
  file = arguments[0]
  dirname = os.path.dirname(file)
  dirname = dirname.capitalize() + '\{}'

  with open(file, 'r', encoding='utf-8') as myfile:
    text = myfile.read()

  links =  re.findall(r"\w*\.md", text)
  map_links = map(dirname.format,links)
  str_links = ' '.join(map_links)

  print("start generate")
  os.system("pandoc -s " + str_links + " -o ../result/output.docx  --lua-filter=../docx/luafilters.lua --reference-doc=../docx/custom-reference.docx" )
  print("end generate")