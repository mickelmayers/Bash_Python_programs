import os
 
startDir = '.'
for file_list in os.listdir(startDir):
    print('\t%s' % file_list)
    if file_list.split('.')[-1] == 'jpg':
            os.rename(file_list, file_list.replace('jpg','png'))