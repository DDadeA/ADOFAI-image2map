# sourcse
# https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python
# https://stackoverflow.com/questions/10607468/how-to-reduce-the-image-file-size-using-pil
# https://cjsal95.tistory.com/35

# 영감을 받은 곳: https://www.youtube.com/watch?v=YeJHNLg92Qs
# 제작자: 정연호 (DDadeA)

from PIL import Image
import math

import tkinter
from tkinter import filedialog
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()
dir_path = filedialog.askopenfilename(parent=root,initialdir="/",title='이미지를 선택해주세요(*.jpg, *.png)')
print("\ndir_path : ", dir_path)
imagesrc = dir_path

x = 0
y = 0

#print("이미지 경로를 확장자를 포함하여 작성해주세요.")
#imagesrc = input()
#imagesrc = '3.jpg'
print("축척을 작성해주세요. (원본=1)")
scale = float(input())
#scale = 0.05

im = Image.open(imagesrc) # Can be many different formats.
osize = im.size 

print("맵이 %f, %f 크기로 제작됩니다. 계속 진행하시겠습니까? (y/n)" % (math.floor(osize[0]*scale),math.floor(osize[1]*scale)))
answer = input()
if answer != "y" and answer != "Y":
    quit()

#im = im.resize((math.floor(osize[0]*scale),math.floor(osize[1]*scale)),Image.ANTIALIAS) #이미지 크기 변경 내림
#im = im.resize((math.round(osize[0]*scale),math.round(osize[1]*scale)),Image.ANTIALIAS) #반올림
im = im.resize((math.ceil(osize[0]*scale),math.ceil(osize[1]*scale)),Image.ANTIALIAS) #올림
size = im.size #수정 후 크기 다시 불러오기
pix = im.load()

f = open("gen.adofai", 'w')
#맵 정보 생성 부분 v
f.write("{\n	\"pathData\": \""+'R' * (size[0]*size[1]+2)+"\", ")
f.write("\n	\"settings\":\n { \n \"version\": 2, \n \"artist\": \"\", \n \"specialArtistType\": \"None\", \n \"artistPermission\": \"\", \n \"song\": \"\", \n \"author\": \"generated by ado gen\", \n \"separateCountdownTime\": \"Enabled\", \n \"previewImage\": \"\", \n \"previewIcon\": \"\", \n \"previewIconColor\": \"003f52\", \n \"previewSongStart\": 0, \n \"previewSongDuration\": 10, \n \"seizureWarning\": \"Disabled\", \n \"levelDesc\": \"none!\", \n \"levelTags\": \"\", \n \"artistLinks\": \"\", \n \"difficulty\": 1, \n \"songFilename\": \"\", \n \"bpm\": 50, \n \"volume\": 100, \n \"offset\": 0, \n \"pitch\": 100, \n \"hitsound\": \"Kick\", \n \"hitsoundVolume\": 100, \n \"countdownTicks\": 4, \n \"trackColorType\": \"Single\", \n \"trackColor\": \"ca4c63\", \n \"secondaryTrackColor\": \"ffffff\", \n \"trackColorAnimDuration\": 2, \n \"trackColorPulse\": \"None\", \n \"trackPulseLength\": 10, \n \"trackStyle\": \"Standard\", \n \"trackAnimation\": \"None\", \n \"beatsAhead\": 3, \n \"trackDisappearAnimation\": \"None\", \n \"beatsBehind\": 4, \n \"backgroundColor\": \"000000\", \n \"bgImage\": \"\", \n \"bgImageColor\": \"ffffff\", \n \"parallax\": [100, 100], \n \"bgDisplayMode\": \"FitToScreen\", \n \"lockRot\": \"Disabled\", \n \"loopBG\": \"Disabled\", \n \"unscaledSize\": 100, \n \"relativeTo\": \"Tile\", \n \"position\": [%f, -%f], \n \"rotation\": 0, \n \"zoom\": 1000, \n \"bgVideo\": \"\", \n \"loopVideo\": \"Disabled\", \n \"vidOffset\": 0, \n \"floorIconOutlines\": \"Disabled\", \n \"stickToFloors\": \"Enabled\", \n \"planetEase\": \"Linear\", \n \"planetEaseParts\": 1 \n }," % (size[0]/2,size[1]/2))
f.write("\n	\"actions\":\n	[")
f.write(" { \"floor\": 1, \"eventType\": \"MoveTrack\", \"startTile\": [0, \"Start\"], \"endTile\": [0, \"End\"], \"duration\": 0, \"positionOffset\": [0, 0], \"rotationOffset\": 0, \"scale\": 200, \"opacity\": 100, \"angleOffset\": 0, \"ease\": \"Linear\", \"eventTag\": \"\" }, \n		 { \"floor\": 1, \"eventType\": \"AddDecoration\", \"decorationImage\": \"%s\", \"position\": [%f, -%f], \"relativeTo\": \"Tile\", \"pivotOffset\": [0, 0], \"rotation\": 0, \"scale\": %f, \"depth\": 0, \"tag\": \"\" }, \n		 { \"floor\": 1, \"eventType\": \"SetSpeed\", \"speedType\": \"Multiplier\", \"beatsPerMinute\": 100, \"bpmMultiplier\": 4 }, \n" % (imagesrc,size[0]/2,size[1]/2,size[0]/scale/100))

print("%d, %d" % (size[0],size[1]))

while y < size[1]:
    while x < size[0]:
        print("x: %d | y: %d\n%s\n" % (x,y,pix[x,y]))
        f.write("		{ \"floor\": %d, \"eventType\": \"ColorTrack\", \"trackColorType\": \"Single\", \"trackColor\": \"%s\", \"secondaryTrackColor\": \"ffffff\", \"trackColorAnimDuration\": 2, \"trackColorPulse\": \"None\", \"trackPulseLength\": 10, \"trackStyle\": \"Standard\" },\n" % (((y)*(size[0])+(x)+1),format(pix[x,y][0],'x')+format(pix[x,y][1],'x')+format(pix[x,y][2],'x')))
        print("%f || %s\n" % (((y)*(size[0]+1)+(x)+1),(format(pix[x,y][0],'x')+format(pix[x,y][1],'x')+format(pix[x,y][2],'x'))))
        x = x + 1
    f.write("		{ \"floor\": %d, \"eventType\": \"PositionTrack\", \"positionOffset\": [-%d, -1], \"editorOnly\": \"Disabled\" },\n" % (size[0]*(y+1)+1,size[0]))
    x = 0
    y = y + 1
f.write('	]\n}\n')
f.close

messagebox.showinfo("들으라","맵이 완성되었습니다. gen.adofai 파일입니다.")
