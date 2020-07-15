# Laboratorio 2 Tests.py

#Import our gl library
import math
from gl import Render,colorScale
mainGl=Render(800,600)
mainGl.glViewPort(200,100,400,400)

#Cuadrante 1
# mainGl.glLine(0,0,0.707,0.707)
# mainGl.glLine(0,0,0.86,0.5)
# mainGl.glLine(0,0,0,1)
# mainGl.glLine(0,0,0.5,0.86)
# mainGl.glLine(0,0,1,0)
# mainGl.glLine(0,0,0.9659,0.2588)
# mainGl.glLine(0,0,0.2588,0.9659)


# #Cuadrante 2
# mainGl.glLine(0,0,-0.707,0.707)
# mainGl.glLine(0,0,-0.86,0.5)
# mainGl.glLine(0,0,0,1)
# mainGl.glLine(0,0,-0.5,0.86)
# mainGl.glLine(0,0,-1,0)
# mainGl.glLine(0,0,-0.9659,0.2588)
# mainGl.glLine(0,0,-0.2588,0.9659)


# #Cuadrante 3
# mainGl.glLine(0,0,-0.707,-0.707)
# mainGl.glLine(0,0,-0.86,-0.5)
# mainGl.glLine(0,0,0,-1)
# mainGl.glLine(0,0,-0.5,-0.86)
# mainGl.glLine(0,0,-1,0)
# mainGl.glLine(0,0,-0.9659,-0.2588)
# mainGl.glLine(0,0,-0.2588,-0.9659)


# #Cuadrante 4
# mainGl.glLine(0,0,0.707,-0.707)
# mainGl.glLine(0,0,0.86,-0.5)
# mainGl.glLine(0,0,0,-1)
# mainGl.glLine(0,0,0.5,-0.86)
# mainGl.glLine(0,0,1,0)
# mainGl.glLine(0,0,0.9659,-0.2588)
# mainGl.glLine(0,0,0.2588,-0.9659)

for x in range(0,360):
    angle=math.radians(x)
    mainGl.glVertexColorRelative(math.cos(angle),math.sin(angle))
    print(angle)

# mainGl.glLine(-1,-1,1,1)
# mainGl.glLine(-1,1,1,-1)

mainGl.glFinish("graphicCir.bmp")


