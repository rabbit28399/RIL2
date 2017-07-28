import xml.etree.ElementTree as ET
import os

rootdir = 'InScript/corpus'
myList = []
thefile = open('xmlresult.txt', 'w')

for folder, subs, files in os.walk(rootdir):
    for filename in files:
        if filename.endswith('.xml'):
                tree = ET.parse(os.path.join(folder, filename))
                root = tree.getroot()
                for content in root.iter('content'):
                    myList.append(content.text)
for item in myList:
    thefile.write(item + '\n\n')