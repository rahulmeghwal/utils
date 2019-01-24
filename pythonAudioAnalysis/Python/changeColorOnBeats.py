import pyaudio
import numpy as np
import cv2

def create_blank(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image


CHUNK = 2**11
RATE = 22050*4;
screenSize = 8;
maxX = 160*screenSize ;
maxY = 120*screenSize ;
a = 1;
OffsetR = 0;
OffsetG = 0;
OffsetB = 0;


p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

#for i in range(int(10*44100/1024)): #go for a few seconds
while ( 1 ) :
   
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    #peak=np.amax(np.abs(data))
    peak=np.amax(data)
    #bars="#"*int(50*peak/2**16)
    #print("%04d %05d %s"%(i,peak,bars))
    #print(bars)
    originalIntensity = int(100*peak/2**15)
    bars="#"*originalIntensity
    #print('peak',peak)
    #print(bars)
    #print(intensity)
    # map intensity to colors
    intensity = 0;
    #print(originalIntensity)
                
    if( originalIntensity > 8) : 
        intensity = originalIntensity;
        
    #if ( intensity > 255 ):
    #    intensity = 255 ;
    
    if (originalIntensity > 20 ) :
        a = a + 1;
        a = a % 7;
    #print(a);
    
    if ( intensity > 255 ):
        intensity = 255 ;
    
    R = OffsetR + ( a&0b1 )*intensity;
    G = OffsetG + ( a&0b10 )*intensity;
    B = OffsetB + ( a&0b100 )*intensity;

    img = create_blank(maxX,maxY,( B , G , R ))
    cv2.imshow('Color to Display',img)
    key = cv2.waitKey(2) & 0xFF
    if key == ord("q"):
       break

stream.stop_stream()
stream.close()
p.terminate()