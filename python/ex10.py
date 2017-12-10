#!/usr/bin/env python

print ("Choose file: (use 'filename')'")
file_to_search  = input( "> " )

replacements = {'i':'oraz', 'oraz':'i', 'nigdy':'prawie nigdy', 'dlaczego':'czemu'}

lines = []
with open(file_to_search) as infile:
    for line in infile:
        for src, target in replacements.iteritems():
            line = line.replace(src, target)
        lines.append(line)
with open(file_to_search, 'w') as outfile:
    for line in lines:
        outfile.write(line)
