#!/usr/bin/env python
# encoding: utf-8
"""
vone.py

Created by Ben Lacker on 2009-06-19.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import sys
import os

from echonest import audio, video

usage = """
Usage: 
    python one.py <input_filename> <output_filename>

Example:
    python one.py EverythingIsOnTheOne.mpg EverythingIsReallyOnTheOne.mpg
"""


def main(input_filename, output_filename):
    av = video.loadav(input_filename)
    collect = audio.AudioQuantumList()
    for bar in av.audio.analysis.bars:
        collect.append(bar.children()[0])
    out = video.getpieces(av, collect)
    out.save(output_filename)


if __name__ == '__main__':
    import sys
    try:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
    except:
        print usage
        sys.exit(-1)
    main(input_filename, output_filename)