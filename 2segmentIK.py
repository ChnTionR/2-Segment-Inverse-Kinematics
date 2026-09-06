import tkinter as tk
import math

class Segment:
    def __init__(self,x1,y1,length,angle):
        self.x1 = x1
        self.y1 = y1
        self.length = length
        self.angle = angle

    def draw(self):#draw segment
        x2 = math.cos(self.angle) * self.length + self.x1
        y2 = -math.sin(self.angle) * self.length + self.y1
        canvas.create_line(self.x1,self.y1,x2,y2,width=5)

origin = (500,500)#base of the arm

def draw():#draw segments on screen
    canvas.delete("all")
    segment1.draw()


def calcArm(event):#calc and draw arm at every mouse movement
    target = (event.x,event.y)
    relativeTarget = (target[0]-origin[0],origin[1]-target[1])
    RelTargetDir = math.atan2(relativeTarget[1],relativeTarget[0])
    segment1.angle = RelTargetDir
    draw()

#window generation and config
root = tk.Tk()
root.geometry("1000x1000")

#canvas config
canvas = tk.Canvas(height=1000,width=1000)
canvas.pack()


#create segment
segment1 = Segment(origin[0],origin[1],300,math.radians(90))

root.bind("<Motion>", calcArm)
draw()


root.mainloop()