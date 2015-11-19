#!/usr/bin/env python

import os
import fontforge

for type in os.listdir("."):
    if type.startswith(".") or not os.path.isdir(type):
        continue
    for filename in os.listdir(type):
        font, extension = os.path.splitext(filename)
        if extension in (".sfd", ".sfdir"):
            print("Generating %s %s" % (type, font))
            fontforge.open(os.path.join(type, filename)).generate(
                "%s %s.otf" % (type, font))
