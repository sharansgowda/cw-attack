import time

t = time.localtime()
curr = int(time.strftime("%H",t))


if(4 < curr < 12):
    print("Good Morning")

elif(curr == 12):
    print("Good Noon")

elif(12 < curr < 16):
    print("Good Afternoon")

elif(16 <= curr < 22):
    print("Good Evening")
else:
    print("Good Night")