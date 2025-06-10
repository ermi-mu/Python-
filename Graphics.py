from cs1graphics import*
from time import sleep
paper = Canvas(1250, 650, 'skyblue', 'paper')
####wellcome
ee=Layer()
e2=Layer()
r1=Rectangle(800,800,Point(100,300))
r1.setFillColor(("lightsalmon"))
r1.setDepth(1)
ee.add(r1)
r2=Rectangle(800,800,Point(1200,300))
r2.setFillColor(("lightsalmon"))
r2.setDepth(1)
e2.add(r2)
paper.add(ee)
paper.add(e2)
for i in range(500):
    ee.move(-1,0)
    e2.move(1,0)
r3=Rectangle(1000,700,Point(625,325))
r3.setFillColor("peru")
r3.setDepth(2)
paper.add(r3)
r4=Text("--------WELLCOME--------",20,Point(625,325))
r4.setFontColor("black")
r4.setDepth(1)
paper.add(r4)
for i in range(500):
    r3.move(0,-2)
    r4.move(0,-1)
#creating_railway
Runway = Layer()

Runway1 = Polygon(Point(150, 649), Point(350, 649), Point(150, 120))
Runway1.setFillColor('black')
Runway.add(Runway1)

whiteline1 = Polygon(Point(255, 648), Point(150, 122), Point(245, 648))
whiteline1.setBorderColor('white')
whiteline1.setFillColor('white')
Runway.add(whiteline1)

Runway2 = Polygon(Point(150, 120), Point(-50, 649), Point(150, 649))
Runway2.setFillColor('black')
Runway.add(Runway2)

whiteline2 = Polygon(Point(45, 648), Point(150, 122), Point(55, 648))
whiteline2.setBorderColor('white')
whiteline2.setFillColor('white')
whiteline2.setDepth(49)
Runway.add(whiteline2)
paper.add(Runway)


#bridge_formation
RoadBridge = Layer()

road1 = Polygon(Point(180, 200), Point(199, 250), Point(1300, 250), Point(1300,200))
road1.setFillColor('black')
road1.setDepth(60)
RoadBridge.add(road1)

coverup1 = Path(Point(180, 201), Point(199, 249))
coverup1.setBorderColor('darkgrey')
coverup1.setBorderWidth(5)
RoadBridge.add(coverup1)

riverboundery1 = Path(Point(150, 120), Point(1100, 649))
riverboundery1.setDepth(90)
RoadBridge.add(riverboundery1)

riverboundery2 = Path(Point(150, 120), Point(5500, 649))
riverboundery2.setDepth(80)
RoadBridge.add(riverboundery2)

def bridge_steel(A, B, C, D, E, F, G, H, I, J = 50):
    bridge_steel = Polygon(Point(A, B), Point(C, D), Point(E, F), Point(G, H))
    bridge_steel.setFillColor(I)
    bridge_steel.setDepth(J)
    RoadBridge.add(bridge_steel)

bridge_steel(635, 300, 585, 300, 585, 225, 635, 225, "steelblue")
bridge_steel(785, 300, 735, 300, 735, 175, 785, 175, "steelblue")
bridge_steel(1050, 300, 1000, 300, 1000, 175, 1050, 175, "steelblue")
bridge_steel(1200, 300, 1150, 300, 1150, 225, 1200, 225, "steelblue")
bridge_steel(522, 225, 495, 225, 495, 152, 522, 152, "steelblue", 70)
bridge_steel(700, 225, 670, 225, 670, 152, 700, 152, "steelblue", 80)
bridge_steel(825, 212, 795, 212, 795, 175, 825, 175, "steelblue", 80)

whitelineroad = Path(Point(189, 225), Point(1300, 225))
whitelineroad.setBorderColor('white')
whitelineroad.setBorderWidth(3)
whitelineroad.setDepth(60)
RoadBridge.add(whitelineroad)

def wire(A, B, C, D, E = 3, F = 50):
    wire = Path(Point(A, B), Point(C, D))
    wire.setBorderWidth(E)
    wire.setDepth(F)
    RoadBridge.add(wire)

wire(635, 225, 735, 200)
wire(585, 225, 735, 175)
wire(785, 175, 1000, 175)
wire(785, 200, 1000, 200)
wire(785, 225, 1000, 225)
wire(1050, 175, 1200, 225)
wire(1050, 200, 1150, 225)
wire(825, 175, 700, 152)
wire(815, 175, 700, 168)
wire(670, 152, 522, 152)
wire(670, 168, 522, 168)
wire(670, 183, 522, 183)
paper.add(RoadBridge)
#ship_creating
Ship = Layer()

shipbody1 = Polygon(Point(910, 400), Point(850, 390), Point(720, 340), Point(778, 324), Point(920, 370))
shipbody1.setFillColor('black')
Ship.add(shipbody1)

def ship_body(A, B, C, D, E, F, G, H, I, J = 50):
    ship_body = Polygon(Point(A, B), Point(C, D), Point(E, F), Point(G, H))
    ship_body.setFillColor(I)
    ship_body.setDepth(J)
    Ship.add(ship_body)
    
ship_body(910, 400, 870, 440, 720, 374, 720, 340, "blue", 70)
ship_body(850, 360, 820, 370, 820, 330, 850, 320, "blue")

shipbody4 = Polygon(Point(820, 370), Point(820, 330), Point(740, 305), Point(740, 340))
shipbody4.setFillColor('blue')
Ship.add(shipbody4)

ship_body(850, 320, 820, 330, 740, 305, 770, 296, "powderblue")
ship_body(740, 305, 740, 280, 770, 271, 770, 296, "lightblue")
ship_body(870, 325, 850, 290, 820, 302, 840, 335, "lightblue", 45)
ship_body(840, 335, 820, 302, 740, 280, 740, 305, "lightblue", 45)
ship_body(820, 302, 740, 280, 770, 271, 850, 290, "black")

Ship.setDepth(64)
Ship.scale(.1)
Ship.moveTo(100, 90)
paper.add(Ship)
#sun
sun = Circle(25,Point(590, 50))
sun.setDepth(120)
sun.setFillColor("yellow")
sun.setBorderColor("yellow")
paper.add(sun)
#sky
sky = Rectangle(2500, 120, Point(0,180))
sky.setFillColor('skyblue')
sky.setDepth(75)
sky.setBorderColor('skyblue')
paper.add(sky)
#mountain

Mountain = Layer()
Mountain.setDepth(80)

def mountcir(A, B, C, D, E, F):
    mount = Circle(A, Point(B, C))
    mount.setDepth(D)
    mount.setFillColor(E)
    mount.setBorderColor(F)
    Mountain.add(mount)

mountcir(60, 30, 100, 100, 'darkgreen', 'darkgreen')
mountcir(100, 210, 100, 100, 'darkgreen', 'darkgreen')
mountcir(60, 320, 100, 100, 'darkgreen', 'darkgreen')
mountcir(60, 100, 100, 100, 'darkgreen', 'darkgreen')
mountcir(80, 430, 100, 100, 'darkgreen', 'darkgreen')
mountcir(60, 540, 100, 100, 'darkgreen', 'darkgreen')
mountcir(60, 650, 100, 100, 'darkgreen', 'darkgreen')
mountcir(60, 760, 100, 100, 'darkgreen', 'darkgreen')
mountcir(60, 870, 100, 100, 'darkgreen', 'darkgreen')
mountcir(100, 980, 100, 100, 'darkgreen', 'darkgreen')
mountcir(60, 1090, 100, 100, 'darkgreen', 'darkgreen')
mountcir(60, 1200, 100, 100, 'darkgreen', 'darkgreen')

paper.add(Mountain)
#airplane
Airplane = Layer()

def plane_body(A, B, C, D, E, F, G, H, I, J = 50):
    plane_body = Polygon(Point(A, B), Point(C, D), Point(E, F), Point(G, H))
    plane_body.setFillColor(I)
    plane_body.setDepth(J)
    Airplane.add(plane_body)

planebody1 = Polygon(Point(50, 500), Point(100, 500), Point(100, 465), Point(50, 465))
planebody1.setFillColor('lightblue')
Airplane.add(planebody1)

plane_body(100, 465, 50, 465, 75, 380, 105, 380, "mintcream")
plane_body(75, 380, 105, 380, 100, 320, 85, 320, "mintcream")

planebody3 = Polygon(Point(50, 500), Point(100, 500), Point(85, 530))
planebody3.setFillColor('mintcream')
Airplane.add(planebody3)

planebody5 = Polygon(Point(100, 320), Point(85, 320), Point(97, 310))
planebody5.setFillColor('mintcream')
Airplane.add(planebody5)

planebody6 = Polygon(Point(85, 530), Point(110, 495), Point(111, 377), Point(98, 310), Point(105, 380), Point(100, 465), Point(100, 500))
planebody6.setFillColor('mintcream')
Airplane.add(planebody6)

plane_body(105, 460, 107, 410, 157, 410, 157, 430, "mintcream")
plane_body(30, 410, 80, 410, 80, 460, 25, 430, "mintcream", 70)

Airplane.scale(0.1)
Airplane.moveTo(125, -55)
Airplane.setDepth(45)
paper.add(Airplane)
#coloring
river = Polygon(Point(150, 120), Point(1100, 649), Point(5500, 649))
river.setDepth(70)
river.setFillColor((127, 200, 212))
paper.add(river)

grass1 = Polygon(Point(350, 649), Point(1100, 649), Point(150, 120))
grass1.setDepth(75)
grass1.setFillColor('forestgreen')
paper.add(grass1)

grass2 = Polygon(Point(150, 120), Point(0, 120), Point(-50, 649))
grass2.setFillColor('forestgreen')
grass2.setBorderColor('forestgreen')
grass2.setDepth(60)
paper.add(grass2)

grass3 = Polygon(Point(150, 120), Point(1300, 120), Point(5500, 649))
grass3.setFillColor('forestgreen')
grass3.setBorderColor('forestgreen')
grass3.setDepth(66)
paper.add(grass3)
#road lamp
lamp = Layer()

lam = Path(Point(79,280),Point(79,200))
lam.setBorderWidth(10)
lam.setBorderColor("brown")
lamp.add(lam)

lam1=Path(Point(69,280),Point(89,280))
lam1.setBorderWidth(5)
lam1.setBorderColor("brown")
lamp.add(lam1)

lam2=Path(Point(74,200),Point(94,200))
lam2.setBorderWidth(5)
lam2.setBorderColor("brown")
lamp.add(lam2)

lamcir = Circle(10, Point(104, 200))
lamcir.setFillColor('white')
lamp.add(lamcir)

lamp.moveTo(-60, 157)
paper.add(lamp)

def new_lamp(A, B, C, D = 50):
    new_lamp = lamp.clone()
    new_lamp.scale(A)
    new_lamp.move(B, C)
    new_lamp.setDepth(D)
    paper.add(new_lamp)

new_lamp(0.75, 65, -40)
new_lamp(0.6, 110, -80)
new_lamp(0.45, 145, -100)
new_lamp(0.3, 175, -100)



###############################
#station
ControlCenter = Layer()

def rec_port(A, B, C, D, E, F, G, H, I, J = 50):
    recport = Polygon(Point(A, B), Point(C, D), Point(E, F), Point(G, H))
    recport.setFillColor(I)
    recport.setDepth(J)
    ControlCenter.add(recport)

recport1 = Polygon(Point(345, 569), Point(545, 569), Point(545, 489), Point(345, 489))
recport1.setFillColor('gray')
ControlCenter.add(recport1)

rec_port(300, 519, 324, 519, 324, 448, 300, 448, "gray")
rec_port(345, 569, 345, 489, 239, 288, 239, 324, "gray", 70)
rec_port(249, 334, 262, 334, 262, 380, 249, 380, "gray")
rec_port(324, 448, 300, 448, 249, 334, 263, 334, "lightgray")
rec_port(545, 489, 345, 489, 239, 288, 330, 288, "lightgray")
rec_port(355, 449, 465, 449, 465, 249, 355, 249, "gray")
rec_port(355, 449, 355, 249, 282, 203, 282, 300, 'gray')

recport8 = Polygon(Point(355, 449), Point(355, 249), Point(282, 203), Point(282, 330))
recport8.setFillColor('gray')
ControlCenter.add(recport8)

rec_port(465, 249, 355, 249, 282, 203, 351, 203, "gray")
Winwtxt = Layer()
paper.add(Winwtxt)
Winwtxt.setDepth(20)
ControlCenter.setDepth(30)
paper.add(ControlCenter)
Prec = Rectangle(110, 50, Point(410, 300))
Prec.setDepth(21)
Prec.setFillColor("white")
Winwtxt.add(Prec)
Winw1 = Rectangle(90, 70, Point(410, 385))
Winw1.setFillColor("lightblue")
Winwtxt.add(Winw1)

Winw2 = Polygon(Point(355, 449), Point(355, 249), Point(282, 193), Point(282, 330))
Winw2.scale(0.65)
Winw2.setFillColor("lightblue")
Winwtxt.add(Winw2)
Winw2.move(-15, -50)

Winw3 = recport1.clone()
Winw3.scale(0.65)
Winw3.setFillColor("lightblue")
Winw3.move(35, -15)
Winwtxt.add(Winw3)

Winw4 = shipbody4.clone()
Winw4.scale(0.65)
Winw4.move(-15, -12)
Winw4.setFillColor("lightblue")
Ship.add(Winw4)

P = Text(" TICKET \n OFFICE", 18)
P.setFontColor("black")
P.moveTo(410, 300)
P.setDepth(20)
Winwtxt.add(P)



#movement code
sleep(2)

global x
global y
x = 0.00001
y = 0.0000001
for i in range(432):
    Ship.move(x,y)
    Ship.scale(1.004)
    sleep(0.03)
    x+= 0.004
    y+= 0.0000001
Ship.setDepth(40)
for i in range(60):
    Ship.move(x,y)
    Ship.scale(1.004)
    sleep(0.03)
    x+= 0.001
    y+= 0.0000001

global m
global n
n = -0.001
m = 0.001
for i in range(800):
    Airplane.move(n,m)
    Airplane.scale(1.0012)
    sleep(0.01)
    n-= 0.00005
    m+= 0.0005
for i in range(70):
    Airplane.move(n,m)
    Airplane.scale(1.005)
    sleep(0.04)
    n-= 0.0069
    m+= 0.00008
for i in range(80):
    Airplane.move(n,m)
    Airplane.scale(1.007)
    sleep(0.05)
    n-= 0.00099
    m+= 0.009

sleep(2)
from math import*
from time import sleep
def animate_sunrise(sun):
	w = paper.getWidth()
	h = paper.getHeight()
	r = sun.getRadius()
	x0 = 6500
	y0 = 500
	max_x = w / 2.0 - r
	max_y = h
	for angel in range(230):
		rad = (angel/180.0) * pi
		x = (x0 - max_x * cos(rad))*0.1
		y = (y0 - max_y * sin(rad))*0.1
		sun.moveTo(x, y)
		sleep(0.03)
		
animate_sunrise(sun)
#night time
NightTime = Layer()
NightTime.setDepth(120)
NightTime.move(300, -60)
NightTime.scale(0.7)
paper.add(NightTime)

blacknight = Rectangle(600,100, Point(500, 115))
blacknight.setFillColor("black")
NightTime.add(blacknight)

moon = Circle(30, Point(750, 120))
NightTime.add(moon)
moon.setFillColor("grey")
moon.setBorderColor("grey")

m1 = Circle(30, Point(735,118))
m1.setFillColor("black")
m1.setBorderColor("black")
NightTime.add(m1)

m2 = Circle(3, Point(550,120))
m2.setFillColor("grey")
m2.setBorderColor("grey")
NightTime.add(m2)

m3 = Circle(3,Point(450,150))
m3.setFillColor("grey")
m3.setBorderColor("grey")
NightTime.add(m3)

m4=Circle(3, Point(245,115))
m4.setFillColor("grey")
m4.setBorderColor("grey")
NightTime.add(m4)

m5=Circle(3, Point(399,113))
m5.setFillColor("dark grey")
m5.setBorderColor("dark grey")
NightTime.add(m5)
 
m6=Circle(3, Point(347,110))
NightTime.add(m6)
m6.setFillColor("grey")
m6.setBorderColor("grey")

m7=Circle(3, Point(700, 140))
m7.setFillColor("grey")
m7.setBorderColor("grey")
NightTime.add(m7)
paper.setBackgroundColor("black")
sleep(1)
lamcir.setFillColor("yellow")

lightcir = Circle(20, Point(120, 280))
lightcir.setFillColor("yellow")
lightcir.setBorderColor("yellow")
lamp.add(lightcir)

lightray = Polygon(Point(114, 200), Point(94, 200), Point(100, 280), Point(141, 280))
lightray.setFillColor("yellow")
lightray.setBorderColor("yellow")
lightray.setDepth(51)
lamp.add(lightray)

new_lamp(0.75, 65, -40)
new_lamp(0.6, 110, -80)
new_lamp(0.45, 145, -100)
new_lamp(0.3, 175, -100)

sleep(2)


#group name
group=Layer()
hh=Rectangle(500,300,Point(700,1300))
hh.setFillColor("blue")
hh.setBorderColor("red")
group.add(hh)
gr2=Text('DISIGNED BY SECTION 21',16,Point(700,1185))
gr2.setFontColor("white")
group.add(gr2)
gr3=Text('No    ---- NAME     --------     --------   --------       ID No',15,
         Point(675,1208))
gr3.setFontColor("white")
group.add(gr3)
paper.add(group)
sif=Text('1 -SIFEN FISEHA------------ugr/35408/16',16,Point(680,1225))
sif.setFontColor("white")
group.add(sif)
sem=Text('2 -SEM ARAYA---------------ugr/35385/16',16,Point(680,1250))
sem.setFontColor("white")
group.add(sem)
mul=Text('3 -SEM ARAYA---------------ugr/35385/16',16,Point(680,1275))
mul.setFontColor("white")
group.add(mul)
yis=Text('4 -SIFEN FISEHA------------ugr/35408/16',16,Point(680,1300))
yis.setFontColor("white")
group.add(yis)
mul=Text('5 -SEM ARAYA---------------ugr/35385/16',16,Point(680,1325))
mul.setFontColor("white")
group.add(mul)
mul=Text('6 -SEM ARAYA---------------ugr/35385/16',16,Point(680,1350))
mul.setFontColor("white")
group.add(mul)
date=Text('Submitted date: march 18,2024 G.C.',16,
         Point(780,1395))
date.setFontColor("white")
group.add(date)
astu=Text('Project for freshman',18,Point(680,1425))
astu.setFontColor("white")
group.setDepth(-110)
group.add(astu)


for i in range(500):
     group.move(0,-2)
     








