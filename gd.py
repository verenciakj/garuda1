from turtle import speed, forward, backward, left, right, teleport, setposition, mainloop, circle, fillcolor, begin_fill, end_fill, color

speed(5000)

color('red')
#lambang
forward(64)
right(90)
forward(46)
circle(-32,180)
forward(46)

fillcolor('yellow')
begin_fill()
#sayap kanan
teleport(0,5)
left(40)
forward(20)
left(40)
forward(20)
left(1)
circle(-50, 100)
right(180)
forward(1)
right(45)
circle(83, 159)
left(18)
forward(34)
end_fill()


begin_fill()
#kaki kanan
right(180)
circle(20,100)
right(60)
forward(22)
right(45)
forward(10)
circle(3,180)
right(30)
forward(10)
left(120)
circle(-5,170)
left(150)
forward(8)
right(20)
forward(15)
right(60)
circle(14,100)
end_fill()

begin_fill()
#ekor
left(170)
circle(50,48)
left(70)
circle(50,48)
end_fill()

begin_fill()
#kaki kiri
right(190)
circle(14,100)
right(60)
forward(15)
right(20)
forward(8)
left(150)
circle(-5,170)
left(120)
forward(10)
right(30)
circle(3,180)
forward(10)
right(45)
forward(22)
right(60)
circle(20,100)
right(180)
end_fill()

begin_fill()
#sayap kiri
teleport(60,5)
left(75)
forward(20)
right(40)
forward(20)
left(1)
circle(50, 100)
right(180)
forward(1)
left(45)
circle(-83, 159)
right(18)
forward(34)
end_fill()

begin_fill()
#kepala
teleport(0,5)
right(165)
forward(7)
left(80)
forward(25)
right(20)
forward(10)
left(160)
forward(1)
circle(-12,100)
right(160)
circle(12,100)
left(80)
circle(14,100)
right(140)
circle(-10,100)

left(60)
forward(10)
right(160)
forward(5)
left(120)
forward(5)
right(20)
forward(15)
right(10)
forward(15)
left(25)
forward(20)
right(160)
forward(20)

left(65)
forward(20)
left(7)
forward(22)
left(75)
forward(5)

right(90)
forward(6)
right(90)
forward(60)
right(90)
forward(6)
end_fill()

begin_fill()
#sambunganekor
teleport(14,-74)
right(180)
forward(25)
right(20)
forward(25)
right(20)
forward(20)
left(132)
forward(88)
left(130)
forward(20)
right(20)
forward(25)
right(10)
forward(25)
end_fill()

fillcolor('red')

#lambang
teleport(0,0)
right(101)
forward(64)
right(90)
forward(46)
circle(-32,180)
forward(46)
right(90)

begin_fill()
forward(32)
right(90)
forward(38)
right(90)
forward(32)
end_fill()

begin_fill()
teleport(30,-35)
backward(34)
left(90)
forward(14)
circle(-30,90)
right(90)
forward(42)
end_fill()

fillcolor('black')
begin_fill()
teleport(35,-23)
right(90)
forward(15)
right(90)
forward(20)
circle(-15,180)
forward(20)
end_fill()





mainloop()
