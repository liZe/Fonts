#!/usr/bin/env python2

import os
import fontforge

for filename in os.listdir("."):
    font, extension = os.path.splitext(filename)
    if extension == ".sfd":
        print("Generating %s" % font)
        fontforge.open("%s.sfd" % font).generate("%s.otf" % font)
