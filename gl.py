# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 10/07/2020
# Laboratorio 1 gl.py

#Import struct to have c# alike structures with memory defined
import struct

#char 1 byte
def char(var):
    return struct.pack('=c',var.encode('ascii'))

#word 2 bytes
def word(var):
    return struct.pack('=h',var)

#double word 4 bytes
def dword(var):
    return struct.pack('=l',var)

#double double word 8 bytes
def ddword(var):
    return struct.pack('=q',var)

#color function ro return rgb in bytes
def color(r,g,b):
    return bytes([b,g,r])

#color function ro return rgb in bytes
def colorScale(r,g,b):
    return bytes([int(b*255),int(g*255),int(r*255)])

#class Render for library of gl
class Render(object):
    #Inititalize function glInit
    #Takes width and height to initialize, also the color
    def __init__(self,width,height,color=None):
        self.glInit(width,height,color)

    def glInit(self,width,height,color=None):
        self.glCreateWindow(width,height)
        self.currentColor = colorScale(1,1,1) if color==None else color
        self.glClear()
        self.glViewPort(0,0,width-1,height-1)
  
    #Size of image result
    def glCreateWindow(self,width,height):
        self.width = width
        self.height = height
    
    #Change Viewport position
    def glViewPort(self,x, y, width, height):
        if(x>=self.width or y>=self.height):
            return False
        if(x+width>=self.width or y+height>=self.height):
            return False
        #We save the data necessary for the viewPort
        self.viewPortWidth= width
        self.viewPortHeight = height
        self.viewPortX = x
        self.viewPortY = y
        return True

    #Clear to set bitmap of one color default black
    def glClear(self):
        #Set to black
        self.glClearColorScaleRGB(0,0,0)

    #Set bitmap to specif color
    def glClearColorScaleRGB(self,r,g,b):
        self.backgroundColor = colorScale(r,g,b)
        #Basically painting background
        # for x in range(self.width):
        #     for y in range(self.height):
        #         self.pixels[x][y]=colorPixels
        # Easier to use nested list comprenhension
        #https://www.geeksforgeeks.org/nested-list-comprehensions-in-python/
        self.pixels= [[self.backgroundColor for x in range(self.width)] for y in range(self.height)]

    #Functions to create points as absolute position
    def glVertexRGBAbsolute(self,x,y,r,g,b):
        self.pixels[y][x]=colorScale(r,g,b)

    def glVertexColorAbsolute(self,x,y,color=None):
        self.pixels[y][x]=self.currentColor if color == None else color
    
    #Functions to create points as relative position of ViewPort
    def glVertexRGBRelative(self,x,y,r,g,b):
        xAbs =int(((x+1)*(self.viewPortWidth/2))+ self.viewPortX)
        yAbs =int(((y+1)*(self.viewPortHeight/2))+ self.viewPortY)
        self.pixels[yAbs][xAbs]=colorScale(r,g,b)

    def glVertexColorRelative(self,x,y,color=None):
        xAbs =int(((x+1)*(self.viewPortWidth/2))+ self.viewPortX)
        yAbs =int(((y+1)*(self.viewPortHeight/2))+ self.viewPortY)
        self.pixels[yAbs][xAbs]=self.currentColor if color == None else color
    
    #Change current vertex color
    def glColor(self,color):
        self.currentColor=color;

    def glColorRGB(self,r,g,b):
        self.currentColor=colorScale(r,g,b)
    
    #Function to write image in file
    def glFinish(self,filename):
        file = open(filename,'wb')
        #https://itnext.io/bits-to-bitmaps-a-simple-walkthrough-of-bmp-image-format-765dc6857393
        #Reference to construct BMP

        #File Type Data BMP Header 14 Bytes
        file.write(char('B'))
        file.write(char('M'))
        file.write(dword(14+40+self.width*self.height*3))
        file.write(dword(0))
        file.write(dword(14+40))

        #File Image Header 40 Bytes
        file.write(dword(40))
        file.write(dword(self.width))
        file.write(dword(self.height))
        file.write(word(1))
        file.write(word(24))
        file.write(dword(0))
        file.write(dword(self.width*self.height*3))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))
        file.write(dword(0))

        #Pixels 3 Bytes each
        for x in range(self.height):
            for y in range(self.width):
                 file.write(self.pixels[x][y])
        file.close()


    #Function for a line
    def glLine(self,x0,y0,x1,y1,color=None):
        #Convert to absolute coordinates
        x0Abs =int(((x0+1)*(self.viewPortWidth/2))+ self.viewPortX)
        y0Abs =int(((y0+1)*(self.viewPortHeight/2))+ self.viewPortY)
        x1Abs =int(((x1+1)*(self.viewPortWidth/2))+ self.viewPortX)
        y1Abs =int(((y1+1)*(self.viewPortHeight/2))+ self.viewPortY)
        dy=y1Abs-y0Abs
        dx=x1Abs-x0Abs
        #Graphic a point if is the same
        if(x0Abs==x1Abs and y0Abs==y1Abs):
             self.glVertexColorAbsolute(int(x0Abs),int(y0Abs))
        
        #If vertical line
        if(dx==0):
            #Vertical Line
            step= +1 if (y1Abs>y0Abs) else -1;
            
            for y in range(y0Abs,y1Abs,step):
                x=x0Abs
                self.glVertexColorAbsolute(int(x),int(y))
        #Any other line
        else:
           #Use mx+b=y if m<=1 else my+b=x m>1
           #This is better for points by set rather tan using just mx+b=y
            m=dy/dx
            if(abs(m)<=1 or dy==0):
                b=y0Abs-(m*x0Abs)
                step = 1 if (dx>0) else -1
                if(m>0 and dy<=0 and dx<=0):
                    step=-1
                elif(m>0 and dy>=0 and dx>=0):
                    step=+1
                
                for x in range(x0Abs,x1Abs,step):
                    y=m*x+b
                    self.glVertexColorAbsolute(int(x),int(y))
            else:
                m=dx/dy
                b=x0Abs-(m*y0Abs)
                step = 1 if (dy>0) else -1
                if(m>0 and dy<=0 and dx<=0):
                    step=-1
                elif(m>0 and dy>=0 and dx>=0):
                    step=+1
                
                for y in range(y0Abs,y1Abs,step):
                    x=m*y+b
                    self.glVertexColorAbsolute(int(x),int(y))
            
            


      

