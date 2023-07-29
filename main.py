'''
SOURCES
    https://stackoverflow.com/questions/138250/how-to-read-the-rgb-value-of-a-given-pixel-in-python
    https://stackoverflow.com/questions/10607468/how-to-reduce-the-image-file-size-using-pil
    https://cjsal95.tistory.com/35

INSPIRATION
    https://www.youtube.com/watch?v=YeJHNLg92Qs
'''

# Load libs
from PIL import Image
from math import ceil
from tkinter import filedialog, messagebox, Tk, Label, Entry, Button, mainloop, Scale

def make_map(pix, image_path:str, scale:float=1, width:int=0, height:int=0, file_path:str='./gen.adofai'):
    '''
    pix: Pixel color data. Instance of PixelAccess Class.
    image_path: image path
    scale: (size of map)/(size of image)
    width: Width
    height: Height
    '''
    
    
    f = open(file_path, 'w')
    
    f.write("{\n	\"pathData\": \""+'R' * (width*height+2)+"\", ")
    f.write("\n	\"settings\":\n { \n \"version\": 2, \n \"artist\": \"\", \n \"specialArtistType\": \"None\", \n \"artistPermission\": \"\", \n \"song\": \"\", \n \"author\": \"https://github.com/DDadeA/ADOFAI-image2map\", \n \"separateCountdownTime\": \"Enabled\", \n \"previewImage\": \"\", \n \"previewIcon\": \"\", \n \"previewIconColor\": \"003f52\", \n \"previewSongStart\": 0, \n \"previewSongDuration\": 10, \n \"seizureWarning\": \"Disabled\", \n \"levelDesc\": \"none!\", \n \"levelTags\": \"\", \n \"artistLinks\": \"\", \n \"difficulty\": 1, \n \"songFilename\": \"\", \n \"bpm\": 50, \n \"volume\": 100, \n \"offset\": 0, \n \"pitch\": 100, \n \"hitsound\": \"Kick\", \n \"hitsoundVolume\": 100, \n \"countdownTicks\": 4, \n \"trackColorType\": \"Single\", \n \"trackColor\": \"ca4c63\", \n \"secondaryTrackColor\": \"ffffff\", \n \"trackColorAnimDuration\": 2, \n \"trackColorPulse\": \"None\", \n \"trackPulseLength\": 10, \n \"trackStyle\": \"Standard\", \n \"trackAnimation\": \"None\", \n \"beatsAhead\": 3, \n \"trackDisappearAnimation\": \"None\", \n \"beatsBehind\": 4, \n \"backgroundColor\": \"000000\", \n \"bgImage\": \"\", \n \"bgImageColor\": \"ffffff\", \n \"parallax\": [100, 100], \n \"bgDisplayMode\": \"FitToScreen\", \n \"lockRot\": \"Disabled\", \n \"loopBG\": \"Disabled\", \n \"unscaledSize\": 100, \n \"relativeTo\": \"Tile\", \n \"position\": [%f, -%f], \n \"rotation\": 0, \n \"zoom\": 1000, \n \"bgVideo\": \"\", \n \"loopVideo\": \"Disabled\", \n \"vidOffset\": 0, \n \"floorIconOutlines\": \"Disabled\", \n \"stickToFloors\": \"Enabled\", \n \"planetEase\": \"Linear\", \n \"planetEaseParts\": 1 \n }," % (width/2,height/2))
    f.write("\n	\"actions\":\n	[")
    f.write(" { \"floor\": 1, \"eventType\": \"MoveTrack\", \"startTile\": [0, \"Start\"], \"endTile\": [0, \"End\"], \"duration\": 0, \"positionOffset\": [0, 0], \"rotationOffset\": 0, \"scale\": 200, \"opacity\": 100, \"angleOffset\": 0, \"ease\": \"Linear\", \"eventTag\": \"\" }, \n		 { \"floor\": 1, \"eventType\": \"AddDecoration\", \"decorationImage\": \"%s\", \"position\": [%f, -%f], \"relativeTo\": \"Tile\", \"pivotOffset\": [0, 0], \"rotation\": 0, \"scale\": %f, \"depth\": 0, \"tag\": \"\" }, \n		 { \"floor\": 1, \"eventType\": \"SetSpeed\", \"speedType\": \"Multiplier\", \"beatsPerMinute\": 100, \"bpmMultiplier\": 4 }, \n" % (image_path,width/2,height/2,width/scale/100))

    print("%d, %d" % (width, height))

    x, y = 0, 0
    while y < height:
        while x < width:
            # print("x: %d | y: %d\n%s\n" % (x,y,pix[x,y]))
            f.write("		{ \"floor\": %d, \"eventType\": \"ColorTrack\", \"trackColorType\": \"Single\", \"trackColor\": \"%s\", \"secondaryTrackColor\": \"ffffff\", \"trackColorAnimDuration\": 2, \"trackColorPulse\": \"None\", \"trackPulseLength\": 10, \"trackStyle\": \"Standard\" },\n" % (((y)*(width)+(x)+1),format(pix[x,y][0],'x')+format(pix[x,y][1],'x')+format(pix[x,y][2],'x')))
            # print("%f || %s\n" % (((y)*(width+1)+(x)+1),(format(pix[x,y][0],'x')+format(pix[x,y][1],'x')+format(pix[x,y][2],'x'))))
            x = x + 1
        f.write("		{ \"floor\": %d, \"eventType\": \"PositionTrack\", \"positionOffset\": [-%d, -1], \"editorOnly\": \"Disabled\" },\n" % (width*(y+1)+1,width))
        x = 0
        y = y + 1
    f.write('	]\n}\n')

    f.close()

    return file_path
    

if __name__ == "__main__":    
    
    image_path = ''
    def get_img_path():
        global image_path, e1
        image_path = filedialog.askopenfilename(parent=root,initialdir="/", title='Select a image.(*.jpg, *.png)')
        e1.insert(0, image_path)
        
    file_path = './'
    def get_file_path():
        global file_path, e2
        file_path = filedialog.askdirectory(parent=root,initialdir="/", title='Select the directory.')
        e2.insert(0, file_path)
    
    def update_size(*args):
        global image_path
        if (image_path==''):
            text = 'Select image path first!'
        else:
            image = Image.open(image_path)
            scale = float(e3.get())
            x, y = ceil(image.size[0]*scale), ceil(image.size[1]*scale)
            text = f'({x} X {y})'
            
        Label(root, text=text).grid(row=3, column=1)
        
    
    def main():
        # Open file
        image = Image.open(image_path)

        # Determine map scale (map/image pixel)
        scale = float(e3.get())     #scale = float(input('Resize scale. (Original = 1) : '))
                        
        x, y = ceil(image.size[0]*scale), ceil(image.size[1]*scale)
        
        print(f"Map will be generated in size of ({x} x {y}).")

        # Resize the image
        image = image.resize((x, y), Image.Resampling.LANCZOS)
        
        # Make the map
        pix = image.load()
        gen_path = make_map(pix, image_path, scale, x, y, file_path+'gen.adofai')
        
        if not (gen_path == None):
            messagebox.showinfo(f"Listen","Map is generated. ({gen_path})")
            quit()
        else:
            messagebox.showinfo("ERROR","Error Occurred")
            quit()
    
     # UI
    root = Tk(className='Image to Map Generator')
    
    Label(root, text='Image path').grid(row=0)
    Label(root, text='Save path').grid(row=1)
    Label(root, text='Resize scale (defalut 1)').grid(row=2)

    Label(root, text='').grid(row=3, column=1)
    
    e1 = Entry(root)
    e2 = Entry(root)
    e2.insert(0, './')
    e3 = Scale(root, from_=0, to=1, resolution=0.01, orient='horizontal')
    e3.set(1)
    e3.bind("<ButtonRelease-1>", update_size)
    
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    
    Button(root, text='Select image path', command=get_img_path).grid(row=0, column=2)
    Button(root, text='Select Map path', command=get_file_path).grid(row=1, column=2)
    
    Button(root, text='Generate the map', command=main).grid(row=3)
    
    mainloop()