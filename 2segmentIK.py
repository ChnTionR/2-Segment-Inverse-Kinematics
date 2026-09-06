import tkinter as tk
import math

class Segment:
    def __init__(self,x1,y1,length,angle,target=(0,0)):
        self.x1 = x1
        self.y1 = y1
        self.x2 = 0
        self.y2 = 0
        self.length = length
        self.angle = angle
        self.target = target

    def calcPos(self):#calc pos
        x2 = math.cos(self.angle) * self.length + self.x1
        y2 = -math.sin(self.angle) * self.length + self.y1

        self.x2 = x2
        self.y2 = y2

    def draw(self):#draw segment
        canvas.create_line(self.x1,self.y1,self.x2,self.y2,width=5)

origin = (500,500)#base of the arm

def draw():#draw segments on screen
    canvas.delete("all")
    segment1.draw()
    segment2.draw()


def calcArm(event):#calc and draw arm at every mouse movement
    target = (event.x,event.y)
    relativeTarget = (target[0]-origin[0],origin[1]-target[1])
    a = segment1.length
    b = segment2.length
    c = math.sqrt(relativeTarget[0]**2 + relativeTarget[1]**2)
    c = min(a + b, c)
    c = max(abs(a-b), c)
    RelTargetDir = math.atan2(relativeTarget[1],relativeTarget[0])



    elbowAngle = math.acos((a**2 + b**2 - c**2)/(2*a*b))
    baseAngle = math.asin(math.sin(elbowAngle) * b / c)

    
    segment1.angle = baseAngle + RelTargetDir
    segment2.angle = -(math.pi - elbowAngle - segment1.angle)
    segment1.calcPos()
    segment2.x1 = segment1.x2
    segment2.y1 = segment1.y2
    segment2.calcPos()
    draw()

"""
    segment1.angle = RelTargetDir
    segment2.x1 = segment1.x2
    segment2.y1 = segment1.y2
"""

#window generation and config
root = tk.Tk()
root.geometry("1000x1000")

#canvas config
canvas = tk.Canvas(height=1000,width=1000)
canvas.pack()


#create segment
segment1 = Segment(origin[0],origin[1],300,math.radians(90))
segment2 = Segment(origin[0],origin[1],250,math.radians(90))

root.bind("<Motion>", calcArm)
draw()


root.mainloop()