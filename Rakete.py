print('Hello, Django girls!')
if 3 > 2:
	print("true")
else:
	print("false")
name = "Steffi"
if name =="Ola":
	print("Hey Ola")	
elif name == "Steffi":
	print("Hey Steffi")
else:
	print("Hey anonymous")
volume = 120
if volume < 20:
	print("its kinda quiet")
elif 20<= volume < 40:
	print("its nice for background")
elif 40<= volume < 60:
	print("perfect")
elif 80<= volume < 100:
	print("loud")
else:
	print ("my ears are hurting!! :(")
def hi():
	print("Hi there!")
	print("How are you")
hi()
def ho():
	print("bububu")
	print("bibibi")
ho()
def hi(name):
	if name == "Ola":
		print("Hi Ola")
	elif name == "Sonja":
		print("Hi Sonja")
	else:
		print("Hi An")
hi("Steff")

def hi(name):
	print("hi " + name + "!")
hi("Steffi")


def hi(name):
	print("Hi " + name + "!")
girls = ["Rachel", "Steffi", "Ola"]	
for name in girls:
	hi(name)
	print("Next girl")

for i in range (1, 6):
	print(i)

for b in range (2,10):
	print(b)

