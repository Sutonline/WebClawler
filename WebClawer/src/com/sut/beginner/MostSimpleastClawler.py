#!/bin/env python3
#Usage: most simple web crawler,just for study and have fun.
#Author:sut
#Created at:2016/06/23
#

#Crawler login
# user enters the begining url
# crawler goes in, and goes through the source code, gething all URL's inside
# crawler then visits each url in another for loop, gathering chid url's from the initial parent urls.

import re,urllib.request
textfile = open('depth_1.txt', 'wt');
print("Enter the URL you wish to crawl..")
print('Usage - "Http://phocks.org/stumble/creepy/" <-- With the doulbe quotes')
myurl = input("@>")
#print(re.findall(b'nq-footer', urllib.request.urlopen("http://www.skyon.com.cn").read(), re.I));
for i in re.findall(b'''href=["'](.[^"']+)["']''', urllib.request.urlopen(myurl).read(), re.I):
    print (i);
    for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.request.urlopen(i).read(), re.I):
        print(ee)
        textfile.write(ee+"\n")
#response = urllib.request.urlopen('http://www.so.com');
#html = response.read();
#print(html);
textfile.close()

