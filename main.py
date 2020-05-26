import turtle, time

t = turtle.Turtle()
t.speed(0)

def init():
  t.ht()
  t.up()

def draw_rectangle_filled(loc_x,loc_y,height,width,color):
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

def draw_rectangle(loc_x,loc_y,height,width,color):
  t.up()
  t.goto(loc_x,loc_y)
  t.down()
  t.color(color)
  for _ in range(2):
    t.fd(width)
    t.rt(90)
    t.fd(height)
    t.rt(90)

def outline():
  draw_rectangle(-375,200,440,750,'black')
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

def full_background(loc_x,loc_y,color):
  draw_rectangle_filled(loc_x,loc_y,440,750,color)

def half_background(loc_x,loc_y,color):
  draw_rectangle_filled(loc_x,loc_y,440/2,750,color)

def third_background(loc_x,loc_y,color):
  draw_rectangle_filled(loc_x,loc_y,440/3,750,color)

def fourth_background(loc_x,loc_y,color):
  draw_rectangle_filled(loc_x,loc_y,440/4,750,color)

def fifth_background(loc_x,loc_y,color):
  draw_rectangle_filled(loc_x,loc_y,440/5,750,color)

def half_vert_background(loc_x,loc_y,color):
  draw_rectangle_filled(loc_x,loc_y,440,750/2,color)

def third_vert_background(loc_x,loc_y,color):
  draw_rectangle_filled(loc_x,loc_y,440,750/3,color)

def fourth_vert_background(loc_x,loc_y,color):
  draw_rectangle_filled(loc_x,loc_y,440,750/4,color)

def fifth_vert_background(loc_x,loc_y,color):
  draw_rectangle_filled(loc_x,loc_y,440,750/5,color)

def canton(loc_x,loc_y,width,height,color):
  draw_rectangle_filled(loc_x,loc_y,height,width,color)

def stgeorge_cross(loc_x,loc_y,width,height,color):
  t.up()
  t.goto(loc_x,loc_y)
  t.fd((750-width)/2)
  t.rt(90)
  t.down()
  t.color(color)
  t.begin_fill()
  t.fd((440-height)/2)
  t.rt(90)
  t.fd((750-width)/2)
  t.lt(90)
  t.fd(height)
  t.lt(90)
  t.fd((750-width)/2)
  t.rt(90)
  t.fd((440-height)/2)
  t.lt(90)
  t.fd(width)
  t.lt(90)
  t.fd((440-height)/2)
  t.rt(90)
  t.fd((750-width)/2)
  t.lt(90)
  t.fd(height)
  t.lt(90)
  t.fd((750-width)/2)
  t.rt(90)
  t.fd((440-height)/2)
  t.lt(90)
  t.fd(width)
  t.end_fill()

def nordic_cross(loc_x,loc_y,width,height,color,left_align):
  t.up()
  t.goto(loc_x,loc_y)
  t.fd(((750-width)/2)-left_align)
  t.rt(90)
  t.down()
  t.color(color)
  t.begin_fill()
  t.fd((440-height)/2)
  t.rt(90)
  t.fd(((750-width)/2)-left_align)
  t.lt(90)
  t.fd(height)
  t.lt(90)
  t.fd(((750-width)/2)-left_align)
  t.rt(90)
  t.fd((440-height)/2)
  t.lt(90)
  t.fd(width)
  t.lt(90)
  t.fd((440-height)/2)
  t.rt(90)
  t.fd(((750-width)/2)+left_align)
  t.lt(90)
  t.fd(height)
  t.lt(90)
  t.fd(((750-width)/2)+left_align)
  t.rt(90)
  t.fd((440-height)/2)
  t.lt(90)
  t.fd(width)
  t.end_fill()

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
  print("Singapore, Indonesia, China, Japan, Bangladesh, Vietnam, Myanmar, Taiwan, Malaysia, Ukraine, Libya, France, Italy, Belgium, Turkey, Austria, Hungary, Poland, Russia, the Netherlands, Germany, Thailand, Yemen, Laos, Armenia, Bulgaria, Somalia, Mauritius, Chad, Romania, Columbia, England, Gabon, Guinea, Denmark, Sweden, Norway, Finland and Iceland.")
  while True:
    country = str(input("\nChoose a country:"))
    reset()
    if country.lower() == "singapore" or country.lower() == "sg":
      print("Country Selected: Singapore")
      init()
      half_background(-375,200,(237, 41, 57))
      moon(-250,20,(255, 255, 255),(237, 41, 57),75,75,35,0)
      star1x =-190
      star1y = 145
      five_star(12,star1x,star1y,(255, 255, 255),0)
      five_star(12,star1x-45,star1y-35,(255, 255, 255),0)
      five_star(12,star1x+43,star1y-35,(255, 255, 255),0)
      five_star(12,star1x-25,star1y-85,(255, 255, 255),0)
      five_star(12,star1x+25,star1y-85,(255, 255, 255),0)
      outline()
      continue
    if country.lower() == "indonesia" or country.lower() == "id":
      print("Country Selected: Indonesia")
      init()
      half_background(-375,200,(255, 0, 0))
      outline()
      continue
    if country.lower() == "china" or country.lower() == "cn" or country.lower() == "prc" or country.lower() == "people's republic of china":
      print("Country Selected: China / PRC")
      init()
      full_background(-375,200,(222, 41, 16))
      five_star(50,-240,105,(255, 222, 0),0)
      five_star(15,-100,50,(255, 222, 0),0)
      five_star(15,-95,110,(255, 222, 0),45)
      five_star(15,-145,160,(255, 222, 0),-45)
      five_star(15,-145,0,(255, 222, 0),-45)
      outline()
      continue
    if country.lower() == "japan" or country.lower() == "jp":
      print("Country Selected: Japan")
      init()
      circle(0,-120,100,(188, 0, 45))
      outline()
      continue
    if country.lower() == "bangladesh" or country.lower() == "bd":
      print("Country Selected: Bangladesh")
      init()
      full_background(-375,200,(0, 106, 78))
      circle(-60,-120,100,(244, 42, 65))
      outline()
      continue
    if country.lower() == "vietnam" or country.lower() == "vn":
      print("Country Selected: Vietnam")
      init()
      full_background(-375,200,(218, 37, 29))
      five_star(110,10,20,(255, 255, 0),0)
      outline()
      continue
    if country.lower() == "myanmar" or country.lower() == "mm":
      print("Country Selected: Myanmar")
      init()
      third_background(-375,200,(254, 203, 0))
      third_background(-375,200-(440/3),(52, 178, 51))
      third_background(-375,200-(2*(440/3)),(234, 40, 57))
      five_star(110,10,20,(255, 255, 255),0)
      outline()
      continue
    if country.lower() == "taiwan" or country.lower() == "tw" or country.lower() == "roc" or country.lower() == "republic of china":
      print("Country Selected: Taiwan / ROC")
      init()
      full_background(-375,200,(254, 0, 0))
      canton(-375,200,340,220,(0, 0, 149))
      nside_star(-287,92,150,(255, 255, 255),12,15)
      circle(-210,45,45,(0, 0, 149))
      circle(-210,50,40,(255, 255, 255))
      outline()
      continue
    if country.lower() == "malaysia" or country.lower() == "my":
      print("Country Selected: Malaysia")
      init()
      draw_stripes_even(-375,200,(204, 0, 0),(255, 255, 255),14)
      canton(-375,200,370,215.5,(0, 0, 102))
      moon(-150,85,(255, 204, 0),(0, 0, 102),85,78,15,275)
      nside_star(-215,95,120,(255, 204, 0),12,15)
      outline()
      continue
    if country.lower() == "ukraine" or country.lower() == "ua":
      print("Country Selected: Ukraine")
      init()
      half_background(-375,200,(0, 91, 187))
      half_background(-375,-20,(255, 213, 0))
      outline()
      continue
    if country.lower() == "libya" or country.lower() == "ly":
      print("Country Selected: Libya")
      init()
      half_background(-375,200,(231, 0, 19))
      half_background(-375,-20,(35, 158, 70))
      half_background(-375,90,(0, 0, 0))
      moon(35,-20,(255, 255, 255),(0, 0, 0),60,52,5,270)
      five_star(30,65,-7,(255, 255, 255),-15)
      outline()
      continue
    if country.lower() == "france" or country.lower() == "fr":
      print("Country Selected: France")
      init()
      third_vert_background(-375,200,(0, 85, 164))
      third_vert_background(-125,200,(255, 255, 255))
      third_vert_background(125,200,(239, 65, 53))
      outline()
      continue
    if country.lower() == "italy" or country.lower() == "it":
      print("Country Selected: Italy")
      init()
      third_vert_background(-375,200,(0, 146, 70))
      third_vert_background(-125,200,(255, 255, 255))
      third_vert_background(125,200,(206, 43, 55))
      outline()
      continue
    if country.lower() == "belgium" or country.lower() == "be":
      print("Country Selected: Belgium")
      init()
      third_vert_background(-375,200,(255, 255, 255))
      third_vert_background(-125,200,(250, 224, 66))
      third_vert_background(125,200,(237, 41, 57))
      outline()
      continue
    if country.lower() == "turkey" or country.lower() == "tr":
      print("Country Selected: Turkey")
      init()
      full_background(-375,200,'red')
      moon(-10,-20,'white','red',110,87,5,270)
      five_star(40,40,0,'white',-15)
      outline()
      continue
    if country.lower() == "austria" or country.lower() == "at":
      print("Country Selected: Austria")
      init()
      third_background(-375,200,(237, 41, 57))
      third_background(-375,200-(440/3),(255, 255, 255))
      third_background(-375,200-(2*(440/3)),(237, 41, 57))
      outline()
      continue
    if country.lower() == "hungary" or country.lower() == "hu":
      print("Country Selected: Hungary")
      init()
      third_background(-375,200,(205, 42, 62))
      third_background(-375,200-(440/3),(255, 255, 255))
      third_background(-375,200-(2*(440/3)),(67, 111, 77))
      outline()
      continue
    if country.lower() == "poland" or country.lower() == "pl":
      print("Country Selected: Poland")
      init()
      half_background(-375,-20,(220, 20, 60))
      outline()
      continue
    if country.lower() == "russia" or country.lower() == "ru":
      print("Country Selected: Russia")
      init()
      third_background(-375,200,"white")
      third_background(-375,200-(440/3),"blue")
      third_background(-375,200-(2*(440/3)),"red")
      outline()
      continue
    if country.lower() == "netherlands" or country.lower() == "nl" or country.lower() == "the netherlands":
      print("Country Selected: The Netherlands")
      init()
      third_background(-375,200,(174, 28, 40))
      third_background(-375,200-(440/3),(255, 255, 255))
      third_background(-375,200-(2*(440/3)),(33, 70, 139))
      outline()
      continue
    if country.lower() == "germany" or country.lower() == "de":
      print("Country Selected: Germany")
      init()
      third_background(-375,200,(0, 0, 0))
      third_background(-375,200-(440/3),(221, 0, 0))
      third_background(-375,200-(2*(440/3)),(255, 206, 0))
      outline()
      continue
    if country.lower() == "thailand" or country.lower() == "th":
      print("Country Selected: Thailand")
      init()
      third_background(-375,200-(2*(440/3)),(165, 25, 49))
      third_background(-375,200-((440/3)*1.5),(244, 245, 248))
      third_background(-375,200,(165, 25, 49))
      third_background(-375,200-((440/3)*0.5),(244, 245, 248))
      third_background(-375,200-(440/3),(45, 42, 74))
      outline()
      continue
    if country.lower() == "yemen" or country.lower() == "ye":
      print("Country Selected: Yemen")
      init()
      third_background(-375,200,(206, 17, 38))
      third_background(-375,200-(440/3),(255, 255, 255))
      third_background(-375,200-(2*(440/3)),(0, 0, 0))
      outline()
      continue
    if country.lower() == "laos" or country.lower() == "la":
      print("Country Selected: Laos")
      init()
      third_background(-375,200,(206, 17, 38))
      third_background(-375,200-(2*(440/3)),(206, 17, 38))
      half_background(-375,90,(0, 40, 104))
      circle(0,-105,85,(255,255,255))
      outline()
      continue
    if country.lower() == "armenia" or country.lower() == "am":
      print("Country Selected: Armenia")
      init()
      third_background(-375,200,(217, 0, 18))
      third_background(-375,200-(440/3),(0, 51, 160))
      third_background(-375,200-(2*(440/3)),(242, 168, 0))
      outline()
      continue
    if country.lower() == "bulgaria" or country.lower() == "bg":
      print("Country Selected: Bulgaria")
      init()
      third_background(-375,200,(255, 255, 255))
      third_background(-375,200-(440/3),(0, 150, 110))
      third_background(-375,200-(2*(440/3)),(214, 38, 18))
      outline()
      continue
    if country.lower() == "somalia" or country.lower() == "so":
      print("Country Selected: Somalia")
      init()
      half_background(-375,200,(65,137,221))
      half_background(-375,-20,(65,137,221))
      five_star(85,10,10,(255,255,255),0)
      outline()
      continue
    if country.lower() == "mauritius" or country.lower() == "mu":
      print("Country Selected: Mauritius")
      init()
      fourth_background(-375,200,(234, 40, 57))
      fourth_background(-375,200-(440/4),(26, 32, 109))
      fourth_background(-375,200-(2*(440/4)),(255, 213, 0))
      fourth_background(-375,200-(3*(440/4)),(0, 165, 81))
      outline()
      continue
    if country.lower() == "chad" or country.lower() == "td":
      print("Country Selected: Chad")
      init()
      third_vert_background(-375,200,(0, 38, 100))
      third_vert_background(-125,200,(254, 203, 0))
      third_vert_background(125,200,(198, 12, 48))
      outline()
      continue
    if country.lower() == "romania" or country.lower() == "ro":
      print("Country Selected: Romania")
      init()
      third_vert_background(-375,200,(0, 43, 127))
      third_vert_background(-125,200,(252, 209, 22))
      third_vert_background(125,200,(206, 17, 38))
      outline()
      continue
    if country.lower() == "england":
      print("Country Selected: England")
      init()
      stgeorge_cross(-375,200,80,80,(206, 17, 36))
      t.rt(180)
      outline()
      continue
    if country.lower() == "colombia" or country.lower() == "co":
      print("Country Selected: Colombia")
      init()
      half_background(-375,200,(252,209,22))
      fourth_background(-375,200-(2*(440/4)),(0, 56, 147))
      fourth_background(-375,200-(3*(440/4)),(206, 17, 38))
      outline()
      continue
    if country.lower() == "gabon" or country.lower() == "ga":
      print("Country Selected: Gabon")
      init()
      third_background(-375,200,(0,158,96))
      third_background(-375,200-(440/3),(252, 209, 22))
      third_background(-375,200-(2*(440/3)),(58, 117, 196))
      outline()
      continue
    if country.lower() == "guinea" or country.lower() == "gn":
      print("Country Selected: Guinea")
      init()
      third_vert_background(-375,200,(206, 17, 38))
      third_vert_background(-125,200,(252, 209 ,22))
      third_vert_background(125,200,(0, 148, 96))
      outline()
      continue
    if country.lower() == "denmark" or country.lower() == "dk":
      print("Country Selected: Denmark")
      init()
      full_background(-375,200,(198, 12, 48))
      nordic_cross(-375,200,75,75,(255, 255, 255),90)
      t.rt(180)
      outline()
      continue
    if country.lower() == "sweden" or country.lower() == "se":
      print("Country Selected: Sweden")
      init()
      full_background(-375,200,(0, 106, 167))
      nordic_cross(-375,200,75,75,(254, 204, 0),90)
      t.rt(180)
      outline()
      continue
    if country.lower() == "norway" or country.lower() == "no":
      print("Country Selected: Norway")
      init()
      full_background(-375,200,(198, 12, 48))
      nordic_cross(-375,200,75,75,(255, 255, 255),90)
      t.rt(180)
      nordic_cross(-375,200,35,35,(0, 40, 104),90)
      t.rt(180)
      outline()
      continue
    if country.lower() == "finland" or country.lower() == "fi":
      print("Country Selected: Finland")
      init()
      full_background(-375,200,(255, 255, 255))
      nordic_cross(-375,200,90,90,(0, 53, 128),90)
      t.rt(180)
      outline()
      continue
    if country.lower() == "iceland" or country.lower() == "is":
      print("Country Selected: Norway")
      init()
      full_background(-375,200,(2, 82, 156))
      nordic_cross(-375,200,75,75,(255, 255, 255),90)
      t.rt(180)
      nordic_cross(-375,200,35,35,(220, 30, 53),90)
      t.rt(180)
      outline()
      continue
    if country.lower() == "exit" or country.lower() == "quit" or country.lower() == "close":
      print("\nClosing program...\n")
      time.sleep(2)
      break
    else:
      print("\nError: Invalid Country\n")
      continue