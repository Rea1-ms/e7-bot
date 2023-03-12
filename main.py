import json
import tempfile
import os
import re
import time
import xml.etree.cElementTree as ET
import tempfile
from datetime import datetime


def IDX(text,fuc):
    os.system("adb shell uiautomator dump")
    tree = ET.parse('dump.xml')
    root = tree.getroot()
    for node in root.findall('.//node'):
        if node.attrib['text']==text:
            if fuc=="sf":
                return node.attrib['clickable']
            elif fuc=="cc":
                bd = node.attrib['bounds']
                nums = re.findall("\d+",bd)
                x=(int(nums[0])+int(nums[2]))/2
                y=(int(nums[1])+int(nums[3]))/2
                cmd="adb shell input tap "+str(x)+" "+str(y)
                os.system(cmd)
            elif fuc=="swp":

                cmd="adb shell input swipe "+
                os.system(cmd)
            


def get_location():
    os.popen("adb shell uiautomator dump /data/local/tmp/uidump.xml")
    os.popen("adb pull /data/local/tmp/uidump.xml " + temp_path)


day=datetime.now().strftime("%a")
hour=int(datetime.now().strftime("%H"))

temp_path="E:\Python\E7"




#每周第一次启动
if day=="Mon" and 2<=hour<=5 :    #搞   点

