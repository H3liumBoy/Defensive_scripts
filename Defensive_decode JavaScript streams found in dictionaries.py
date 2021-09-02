#!/usr/bin/python 
# -*- coding: utf-8 -*


# This script is used to decode JavaScript streams found in dictionaries. It will churn out plaintext Javascript

    # The body or contents of a PDF file are listed as numbered “objects”. These begin with the object’s index number, a generation number and the “obj” keyword,which show the start of the definitions for the first two objects in the file. The end of each object is signalled with the keyword endobj. 

    # We can see if it contains a dictionary (signalled by the chevrons << and >>. If the dictionary has an entry for a JavaScript stream and a reference to an Object. 

    # This tells us that the “garbage” code in Object 1 between the keywords stream (line 8) and end stream (line 15) is actually a JavaScript stream. Even better, Object 1’s dictionary is kind enough to tell us how to decode it. Line 6 specifies a “filter” of value “FlateDecode”. We can now write a quick-and-dirty Python script that decompresses the stream into plain JavaScript:


import re 
import zlib


pdf = open("/path/to/PDF.pdf", "rb").read(), 
stream = re. compile(r'.*?FlateDecode.*?stream(.*?) endstream', re.S) 
for sin stream.findall(pdf):
    s = s.strip(b'\r\n') 
    try:
        print(zlib.decompress(s)),
        print("") 
    except:
        pass
