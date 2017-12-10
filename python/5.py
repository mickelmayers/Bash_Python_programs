import os
 
startDir = '.'
for Name, subdirs_list, file_list in os.walk(startDir):
    print('Directory: %s' % Name)
    for file in file_list:
        print('\t%s' % file)