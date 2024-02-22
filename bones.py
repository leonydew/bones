from tkinter import *
import random, time

def sesh():
	x = random.choice(['images for game/b1.png',\
		'images for game/b2.png','images for game/b3.png','images for game/b4.png',\
		'images for game/b5.png','images for game/b6.png',])
	return x

def img(event):
	global b1, b2
	for i in range(18):
		b1 = PhotoImage(file = (sesh()))
		b2 = PhotoImage(file = (sesh()))
		label_1['image'] = b1
		label_2['image'] = b2
		time.sleep(0.12)
		root.update()

root = Tk()#window
root.geometry('400x200')#window_size
root.title('Bones...sesh...')#title
root.resizable(height = False, width = False)#cant change window
root.iconphoto(True, PhotoImage(file = ('images for game/iconka.png'))) # icon, but only for Windows/MacOS
bg = PhotoImage(file = ('images for game/holst.png'))
Label(root, image = bg).pack() #label for bg

#labels for cubes
label_1 = Label(root)
label_1.place(relx = 0.3, rely = 0.5, anchor = CENTER) # anchor it center of label
label_2 = Label(root)
label_2.place(relx = 0.7, rely = 0.5, anchor = CENTER)

root.bind('<1>', img)# start on left button of mouse
#Button(root, text = "Sesh", command = img).pack()
img('event')

root.mainloop()