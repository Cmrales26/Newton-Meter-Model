# import dependencies
from vpython import *
import math
import numpy as np

# vpython canvas size
canvas(width=1320,height=680)

# create static objects
ring(pos=vector(0,8.3,0),axis=vector(1,0,0),radius=1,thickness=0.2,texture=textures.metal,color=color.white)
cylinder(length=2.3,radius=.8,pos=vector(0,5,0),axis=vector(0,1,0),texture=textures.metal,color=color.white)
cylinder(length=2,radius=.5,pos=vector(0,4.8,0),axis=vector(0,1,0),texture=textures.metal,color=color.white)

box(length=1.8,width=2.2,height=.1,pos=vector(0,4.95,0),color=color.black)
box(length=.1,width=.9,height=10,pos=vector(.95,0,.6),color=color.black)
box(length=.1,width=.9,height=10,pos=vector(.95,0,-.7),color=color.black)
box(length=.1,width=.9,height=10,pos=vector(-.95,0,.6),color=color.black)
box(length=.1,width=.9,height=10,pos=vector(-.95,0,-.7),color=color.black)
box(length=1.8,width=2.2,height=.1,pos=vector(0,-4.95,0),color=color.black)
box(length=4,width=.2,height=12,pos=vector(0,0,1.2),color=color.black)
box(length=.8,width=.1,height=10,pos=vector(.6,0,-1.15),color=color.black)
box(length=.8,width=.1,height=10,pos=vector(-.6,0,-1.15),color=color.black)

box(length=5,width=.1,height=13,pos=vector(0,0,1.3),texture=textures.metal,color=color.yellow)
cylinder(length=.1,radius=.4,pos=vector(2.1,6.5,1.25),axis=vector(0,0,1),texture=textures.metal,color=color.yellow)
cylinder(length=.1,radius=.4,pos=vector(2.1,-6.5,1.25),axis=vector(0,0,1),texture=textures.metal,color=color.yellow)
cylinder(length=.1,radius=.4,pos=vector(-2.1,6.5,1.25),axis=vector(0,0,1),texture=textures.metal,color=color.yellow)
cylinder(length=.1,radius=.4,pos=vector(-2.1,-6.5,1.25),axis=vector(0,0,1),texture=textures.metal,color=color.yellow)
box(length=3.4,width=.1,height=14.6,pos=vector(0,0,1.3),texture=textures.metal,color=color.yellow)
cylinder(length=.1,radius=.4,pos=vector(1.7,6.9,1.25),axis=vector(0,0,1),texture=textures.metal,color=color.yellow)
cylinder(length=.1,radius=.4,pos=vector(1.7,-6.9,1.25),axis=vector(0,0,1),texture=textures.metal,color=color.yellow)
cylinder(length=.1,radius=.4,pos=vector(-1.7,6.9,1.25),axis=vector(0,0,1),texture=textures.metal,color=color.yellow)
cylinder(length=.1,radius=.4,pos=vector(-1.7,-6.9,1.25),axis=vector(0,0,1),texture=textures.metal,color=color.yellow)

box(length=.4,width=.5,height=9,pos=vector(0,0,1.2),color=color.black,opacity=0.4)

newton=text(text='Newton',align='center',pos=vector(0,6.4,1.3),color=color.black)
newton.height=.5
newton.length=2
newton.depth=.06
meter=text(text='Meter',align='center',pos=vector(0,5.6,1.3),color=color.black)
meter.height=.5
meter.length=1.6
meter.depth=.06

x=-.8
y=4.4
a=.2
for j in range(2):
    for i in range(11):
        box(length=.8,width=.02,height=.05,pos=vector(x,y,1.4),color=color.black)
        box(length=.4,width=.02,height=.05,pos=vector(x+a,y-.45,1.4),color=color.black)
        y=y-.88
    a=a-.4
    y=4.4
    x=.8

newton=text(text='Newtons',align='center',pos=vector(-1.4,4.8,1.3),color=color.black)
newton.height=.4
newton.length=1.4
newton.depth=.06

y=4.25
num=0
for i in range(0,110,10):
    numstring=str(num)
    cNum=text(text=numstring,align='center',pos=vector(-1.8,y,1.4),color=color.black)
    cNum.height=.3
    cNum.length=.3
    cNum.depth=.02
    y=y-.88
    num+=1

grams=text(text='grams',align='center',pos=vector(1.35,4.88,1.3),color=color.black)
grams.height=.3
grams.length=1.2
grams.depth=.06

y=4.25
num=0

# render the text objects
for i in range(0,110,10):
    numstring=str(num)
    cNum=text(text=numstring,align='center',pos=vector(1.8,y,1.4),color=color.black)
    cNum.height=.3
    cNum.length=.3
    cNum.depth=.02
    y=y-.88
    num=num+100

pointer=box(length=1,width=.4,height=.1,pos=vector(0,4.3,1.8),texture=textures.metal)
pointer_bar=box(length=.3,width=2.4,height=.2,pos=vector(0,4.3,.5),texture=textures.metal)
top_disc=cylinder(length=.4,radius=.8,pos=vector(0,4.2,0),axis=vector(0,1,0),texture=textures.metal)
internal_rod=cylinder(length=10,radius=.1,pos=vector(0,4.2,0),axis=vector(0,-1,0),texture=textures.metal)
top_spring=helix(pos=vector(0,4.3,0),axis=vector(0,-1,0),radius=0.8,thickness=.1,length=.3,coils=3)
main_spring=helix(pos=vector(0,4.4,0),axis=vector(0,-1,0),radius=.8,thickness=.1,length=9,coils=10)
bottom_spring=helix(pos=vector(0,-4.9,0),axis=vector(0,1,0),radius=0.8,thickness=.1,length=.3,coils=3)
external_rod=cylinder(length=2.3,radius=.4,pos=vector(0,-5,0),axis=vector(0,-1,0),texture=textures.metal)
lowest_ring=ring(pos=vector(0,-7.8,0),axis=vector(0,0,1),radius=1,thickness=.1,texture=textures.metal)
key_ring=helix(pos=vector(-.1,-9.7,0),axis=vector(1,0,0),radius=1,thickness=.1,length=.2,coils=2)
holder_ring=ring(pos=vector(-.1,-11.2,0),axis=vector(0,0,1),radius=.6,thickness=.1,texture=textures.metal)
mass=box(pos=vector(-.1,-13,0),color=color.white,texture=textures.wood,size=vector(3,3,3))

# program loop
while True:
    # animate position in downward direction
    for movement in np.linspace(0,8.5,100):
        rate(60)
        pointer.pos=vector(0,4.3-movement,1.8)
        pointer_bar.pos=vector(0,4.2-movement,.5)
        top_disc.pos=vector(0,4.2-movement,0)
        internal_rod.pos=vector(0,4.2-movement,0)
        top_spring.pos=vector(0,4.3-movement,0)
        main_spring.pos=vector(0,4.4-movement,0)
        main_spring.length=9-movement
        external_rod.pos=vector(0,-5-movement,0)
        lowest_ring.pos=vector(0,-7.8-movement,0)
        key_ring.pos=vector(-.1,-9.7-movement,0)
        holder_ring.pos=vector(-.1,-11.2-movement,0)
        mass.pos=vector(-.1,-13-movement,0)
    
    # animate position in upward direction
    for movement in np.linspace(8.5,0,100):
        rate(60)
        pointer.pos=vector(0,4.3-movement,1.8)
        pointer_bar.pos=vector(0,4.2-movement,.5)
        top_disc.pos=vector(0,4.2-movement,0)
        internal_rod.pos=vector(0,4.2-movement,0)
        top_spring.pos=vector(0,4.3-movement,0)
        main_spring.pos=vector(0,4.4-movement,0)
        main_spring.length=9-movement
        external_rod.pos=vector(0,-5-movement,0)
        lowest_ring.pos=vector(0,-7.8-movement,0)
        key_ring.pos=vector(-.1,-9.7-movement,0)
        holder_ring.pos=vector(-.1,-11.2-movement,0)
        mass.pos=vector(-.1,-13-movement,0)
