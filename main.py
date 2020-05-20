import turtle, time

t = turtle.Turtle()
t.speed(0)

def init():
  t.ht()
  t.up()

def half_background(loc_x,loc_y,color):
  t.up()
  t.goto(loc_x,loc_y)
  t.down()
  t.color(color)
  t.begin_fill()
  for _ in range(2):
    t.fd(750)
    t.rt(90)
    t.fd(220)
    t.rt(90)
  t.end_fill()

def third_background(loc_x,loc_y,color):
  t.up()
  t.goto(loc_x,loc_y)
  t.down()
  t.color(color)
  t.begin_fill()
  for _ in range(2):
    t.fd(750)
    t.rt(90)
    t.fd(440/3)
    t.rt(90)
  t.end_fill()

def third_vert_background(loc_x,loc_y,color):
  t.up()
  t.goto(loc_x,loc_y)
  t.down()
  t.color(color)
  t.begin_fill()
  for _ in range(2):
    t.fd(750/3)
    t.rt(90)
    t.fd(440)
    t.rt(90)
  t.end_fill()

def fifth_background(loc_x,loc_y,color):
  t.up()
  t.goto(loc_x,loc_y)
  t.down()
  t.color(color)
  t.begin_fill()
  for _ in range(2):
    t.fd(750)
    t.rt(90)
    t.fd(440/5)
    t.rt(90)
  t.end_fill()

def outline():
  t.up()
  t.goto(-375,200)
  t.down()
  t.color('black')
  for _ in range(2):
    t.fd(750)
    t.rt(90)
    t.fd(440)
    t.rt(90)
  t.color('white')
  t.up()
  t.goto(10000,10000)
  print("Task Complete\n")

def moon(loc_x,loc_y,color,bgcolor,size,bg_size,bgdist,angle):
  t.up()
  t.goto(loc_x,loc_y)
  t.down()
  t.right(angle)
  t.color(color)
  t.begin_fill()
  t.circle(size)
  t.end_fill()
  t.up()
  t.goto(loc_x+bgdist,loc_y)
  t.down()
  t.color(bgcolor)
  t.begin_fill()
  t.circle(bg_size)
  t.end_fill()
  t.up()
  t.left(angle)

def circle(loc_x,loc_y,size,color):
  t.up()
  t.goto(loc_x,loc_y)
  t.down()
  t.color(color)
  t.begin_fill()
  t.circle(size)
  t.end_fill()
  t.up()

def five_star(size,loc_x,loc_y,color,angle):
  t.up()
  t.goto(loc_x,loc_y)
  t.right(angle)
  t.down()
  t.color(color)
  t.begin_fill()
  for side in range(5):
      t.fd(size)
      t.rt(145)
      t.fd(size)
      t.rt(72 - 145)
  t.end_fill()
  t.up()
  t.left(angle)

def nside_star(loc_x,loc_y,length,color,side,angle):
  t.up()
  t.goto(loc_x,loc_y)
  t.right(angle)
  t.down()
  t.color(color)
  t.begin_fill()
  interior_angle_total = 180 * (side-2)
  turn_angle = interior_angle_total / side
  for _ in range(side):
    t.fd(length)
    t.lt(turn_angle)
  t.end_fill()
  t.left(angle)
  t.up()

def canton(loc_x,loc_y,width,height,color):
  t.up()
  t.goto(loc_x,loc_y)
  t.down()
  t.color(color)
  t.begin_fill()
  for _ in range(2):
    t.fd(width)
    t.rt(90)
    t.fd(height)
    t.rt(90)
  t.end_fill()
  t.up()


def draw_stripes_even(loc_x,loc_y,color1,color2,count):
  actual_count = (count)/2
  for stripe in range(actual_count):
    for color in [color1,color2]:
      t.up()
      t.goto(loc_x,loc_y)
      t.down()
      t.color(color)
      t.begin_fill()
      for _ in range(2):
        t.fd(750)
        t.rt(90)
        t.fd(220/actual_count)
        t.rt(90)
      t.end_fill()
      loc_y -= (220/actual_count)
  t.up()
  t.goto(loc_x,loc_y)
  t.down()
  t.color(color1)
  t.begin_fill()
  for _ in range(2):
    t.fd(750)
    t.rt(90)
    t.fd(220/actual_count)
    t.rt(90)
  t.end_fill()
  loc_y -= (220/actual_count)

def reset():
  t.up()
  t.goto(-380,205)
  t.down()
  t.color('white')
  t.begin_fill()
  for _ in range(2):
    t.fd(760)
    t.rt(90)
    t.fd(450)
    t.rt(90)
  t.end_fill()
  t.up()
  t.goto(10000,10000)

if __name__ == "__main__":
  print("To exit this program, type 'exit'\n")
  print("Countries that are currently available:")
  print("Singapore, Taiwan, Indonesia, Japan, China, Bangladesh, Vietnam, Libya, Ukraine, and Myanmar.")
  while True:
    country = str(input("\nChoose a country:"))
    reset()
    if country.lower() == "singapore" or country.lower() == "sg":
      print("Country Selected: Singapore")
      init()
      half_background(-375,200,'red')
      moon(-250,20,'white','red',75,75,35,0)
      star1x =-190
      star1y = 145
      five_star(12,star1x,star1y,'white',0)
      five_star(12,star1x-45,star1y-35,'white',0)
      five_star(12,star1x+43,star1y-35,'white',0)
      five_star(12,star1x-25,star1y-85,'white',0)
      five_star(12,star1x+25,star1y-85,'white',0)
      outline()
      continue
    if country.lower() == "indonesia" or country.lower() == "id":
      print("Country Selected: Indonesia")
      init()
      half_background(-375,200,'red')
      outline()
      continue
    if country.lower() == "china" or country.lower() == "cn" or country.lower() == "prc" or country.lower() == "people's republic of china": #TBD
      print("Country Selected: China / PRC")
      init()
      half_background(-375,200,'red')
      half_background(-375,-20,'red')
      five_star(50,-240,105,'yellow',0)
      five_star(15,-100,55,'yellow',0)
      five_star(15,-95,110,'yellow',45)
      five_star(15,-145,160,'yellow',-45)
      five_star(15,-145,0,'yellow',-45)
      outline()
      continue
    if country.lower() == "japan" or country.lower() == "jp":
      print("Country Selected: Japan")
      init()
      circle(0,-120,100,'red')
      outline()
      continue
    if country.lower() == "bangladesh" or country.lower() == "bd":
      print("Country Selected: Bangladesh")
      init()
      half_background(-375,200,'dark green')
      half_background(-375,-20,'dark green')
      circle(-60,-120,100,'red')
      outline()
      continue
    if country.lower() == "vietnam" or country.lower() == "vn":
      print("Country Selected: Vietnam")
      init()
      half_background(-375,200,'red')
      half_background(-375,-20,'red')
      five_star(110,10,20,'yellow',0)
      outline()
      continue
    if country.lower() == "myanmar" or country.lower() == "mm":
      print("Country Selected: Myanmar")
      init()
      third_background(-375,200,'yellow')
      third_background(-375,200-(440/3),'green')
      third_background(-375,200-(2*(440/3)),'red')
      five_star(110,10,20,'white',0)
      outline()
      continue
    if country.lower() == "taiwan" or country.lower() == "tw" or country.lower() == "roc" or country.lower() == "republic of china":
      print("Country Selected: Taiwan / ROC")
      init()
      half_background(-375,200,'red')
      half_background(-375,-20,'red')
      canton(-375,200,340,220,'blue')
      nside_star(-287,92,150,'white',12,15)
      circle(-210,45,45,'blue')
      circle(-210,50,40,'white')
      outline()
      continue
    if country.lower() == "malaysia" or country.lower() == "my":
      print("Country Selected: Malaysia")
      init()
      draw_stripes_even(-375,200,'red','white',14)
      canton(-375,200,370,215.5,'dark blue')
      moon(-150,85,'yellow','dark blue',85,78,15,275)
      nside_star(-215,95,120,'yellow',12,15)
      outline()
      continue
    if country.lower() == "ukraine" or country.lower() == "ua":
      print("Country Selected: Ukraine")
      init()
      half_background(-375,200,(0, 91, 187))
      half_background(-375,-20,'yellow')
      outline()
      continue
    if country.lower() == "libya" or country.lower() == "ly":
      print("Country Selected: Libya")
      init()
      half_background(-375,200,'red')
      half_background(-375,-20,'green')
      half_background(-375,90,'black')
      moon(35,-20,'white','black',60,52,5,270)
      five_star(30,65,-7,'white',-15)
      outline()
      continue
    if country.lower() == "france" or country.lower() == "fr":
      print("Country Selected: France")
      init()
      third_vert_background(-375,200,"blue")
      third_vert_background(-125,200,"white")
      third_vert_background(125,200,"red")
      outline()
      continue
    if country.lower() == "italy" or country.lower() == "it":
      print("Country Selected: Italy")
      init()
      third_vert_background(-375,200,"green")
      third_vert_background(-125,200,"white")
      third_vert_background(125,200,"red")
      outline()
      continue
    if country.lower() == "belgium" or country.lower() == "be":
      print("Country Selected: Belgium")
      init()
      third_vert_background(-375,200,"black")
      third_vert_background(-125,200,"yellow")
      third_vert_background(125,200,"red")
      outline()
      continue
    if country.lower() == "turkey" or country.lower() == "tr":
      print("Country Selected: Turkey")
      init()
      half_background(-375,200,'red')
      half_background(-375,-20,'red')
      moon(-10,-20,'white','red',110,87,5,270)
      five_star(40,40,0,'white',-15)
      outline()
      continue
    if country.lower() == "austria" or country.lower() == "at":
      print("Country Selected: Austria")
      init()
      third_background(-375,200,'red')
      third_background(-375,200-(440/3),'white')
      third_background(-375,200-(2*(440/3)),'red')
      outline()
      continue
    if country.lower() == "hungary" or country.lower() == "hu":
      print("Country Selected: Hungary")
      init()
      third_background(-375,200,'red')
      third_background(-375,200-(440/3),'white')
      third_background(-375,200-(2*(440/3)),(67,111,77))
      outline()
      continue
    if country.lower() == "poland" or country.lower() == "pl":
      print("Country Selected: Poland")
      init()
      half_background(-375,-20,'red')
      outline()
      continue
    if country.lower() == "exit" or country.lower() == "quit" or country.lower() == "close":
      print("\nClosing program...\n")
      time.sleep(2)
      break
    else:
      print("\nError: Invalid Country\n")
      continue