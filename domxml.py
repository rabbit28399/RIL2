from xml.dom import minidom
import os

rootdir = 'DeScript_LREC2016/esds/second_esd'
myList = []
thefile = open('descript.txt', 'w')

for folder, subs, files in os.walk(rootdir):
    for filename in files:
        if filename.endswith('.xml'):
            myList.append('Title : ' + filename)
            doc = minidom.parse(os.path.join(folder, filename))
            script = doc.getElementsByTagName("script")
            for scr in script:
                items = scr.getElementsByTagName("item")
                for it in items:
                    itori = it.getAttribute("original")
                    print ('%s' % itori)
                    myList.append(itori)
                myList.append('\n')
for item in myList:
    thefile.write(item + '\n')