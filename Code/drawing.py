from turtle import *
from Face import Face

# sets the animation speed: can be 'slow'
speed("slow")

# uncomment for instanteneous drawing - no animation
# tracer(0)

panda1 = Face(-600, 0, "black") #第三個參數為設定眼睛顏色
panda1.setSize(200) # 設定臉大小
panda1.setEarColour("black") # 設定耳朵顏色
panda1.setNoseSize("large") # 設定鼻子大小
panda1.draw()

panda2 = Face(0, 0, "blue") # 耳朵顏色預設白色，鼻子大小預設正常
panda2.setSize(250)
panda2.draw()

panda3 = Face(600, 0, "red")
panda3.setSize(170)
panda3.setEarColour("blue")
panda3.setNoseSize("small")
panda3.draw()

showturtle()
done()
