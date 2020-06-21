from __future__ import print_function

import sys
from os.path import basename
from classes.Utils import *
from classes.Compiler import *

if (__name__ == "__main__"):
    argv = sys.argv[1:]
    length = len(argv)
    if length != 0:
        input_file = argv[0]
    else:
        print("Error: not enough argument supplied:")
        print("carbon-compiler.py <i")
        exit(0)


def render_content_with_text(key, value):
    if (FILL_WITH_RANDOM_TEXT):
        if (key.find("button") != -1):
            value = value.replace(TEXT_PLACE_HOLDER, Utils.get_random_text())
        
        elif (key.find("CodeSnippet") != -1):
            value = value.replace(TEXT_PLACE_HOLDER,
                                  Utils.get_random_text(length_text=30, space_number=7, with_upper_case=False))
            
        elif (key.find("Search") != -1):
            value = value.replace(TEXT_PLACE_HOLDER,
                                  Utils.get_random_text(length_text=35, space_number=7, with_upper_case=False))
    return value
    

dsl_path = "assets/carbon-dsl-mapping.json"
compiler = Compiler(dsl_path)
FILL_WITH_RANDOM_TEXT = True
TEXT_PLACE_HOLDER = "[]"
file_uid = basename(input_file)[:basename(input_file).find(".")]
path = input_file[:input_file.find(file_uid)]
input_file_path = "{}{}.gui".format(path, file_uid)
output_file_path = "{}{}.xml".format(path, file_uid)
#compiler.compile("[ 'text-input-basic', ',', ',', 'text-input-basic', '}', 'text-input-basic', 'text-input-basic', 'text-input-basic', 'text-input-basic', ", output_file_path)
compiler.compile("  text-input-basic  , text-input-basic , text-input-basic , text-input-basic   ", output_file_path)