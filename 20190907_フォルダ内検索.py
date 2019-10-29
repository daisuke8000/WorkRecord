import os

dock = r"ここにファイルフルパスを貼る"    

for folder,subfolders,files in os.walk(dock):
    print('folder: {}'.format(folder))
    print('subfolders: {}'.format(subfolders))
    print('files: {}'.format(files))