#!/usr/bin/env python

print ("Choose file: (use 'filename')'")
file_to_search  = input( "> " )

to_remove = ['sie', 'i', 'oraz', 'nigdy', 'dlaczego']

lines = []
with open(file_to_search) as infile:
    for line in infile:
        for src in to_remove:
            line = line.replace(src, "")
        lines.append(line)
with open(file_to_search, 'w') as outfile:
    for line in lines:
        outfile.write(line)
