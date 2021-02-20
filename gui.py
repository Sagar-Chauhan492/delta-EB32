from tkinter import *
s_root = Tk()

s_root.geometry('1000x600')
s_root.minsize(400,400)
s_root.maxsize(1350,705)
s_root.title('AI PEDESTRAIN AND CAR TRACKER')

# defining functions
im_cnt = 1
def onclick1():
    global im_cnt
    if im_cnt == 1:
        l1 = Label(f4, text = 'Please provide the path of image file.', fg = 'red', font = ' "" 10 "italic"')
        l1.pack()
        im_cnt = im_cnt + 1
        print(im_cnt)
    elif im_cnt >= 2:
        pass
        
vd_cnt = 1
def onclick2():
    global vd_cnt
    if vd_cnt == 1:
        Label(f4, text = 'Please provide the path of video file.', fg = 'red', font = ' "" 10 "italic"').pack()
        vd_cnt = vd_cnt + 1
        print(vd_cnt)

def onclick3():
    print('review')

def onclick4():
    print('car')

def onclick5():
    print('face')

def onclick6():
    print('go')

# using label 

lb = Label(text = 'AI PEDESTRAIN AND CAR TRACKER', fg = 'white', bg = 'black', padx = 10, pady = 20, font = ' "" 15 ""')
lb.pack(fill = X)

Label(text = 'Description: This GUI is used to take input from user and show output as per the selected feilds.', fg = 'white', bg = 'black', padx = 20, font = ' "" 8 "italic"').pack(fill = X, side = BOTTOM)

# frame 1 
f1 = Frame(s_root, bg = 'grey', padx = 5)
f1.pack(side = LEFT, fill = Y)
b1 = Button(f1, text = 'IMAGES', padx = 40, command = onclick1)
b1.pack(pady = 5)
b2 = Button(f1, text = 'VIDEOS', padx = 41, command = onclick2)
b2.pack()
b3 = Button(f1, text = 'REVIEW', padx = 41, command = onclick3)
b3.pack(pady = 5)

# frame 2
f2 = Frame(s_root, bg = 'light green')
f2.pack(fill = X)
b4 = Radiobutton(f2, text = 'CAR AND PEDESTRAIN DETECTOR', padx = 100, pady = 8, value = 1, command = onclick4)
b4.pack(side = LEFT, pady = 2, padx = 2, fill = BOTH, expand = TRUE)
b5 = Radiobutton(f2, text = 'FACE AND SMILE DETECTOR', padx = 100, pady = 8, value = 2, command = onclick5)
b5.pack(side = LEFT ,pady = 2, padx = 2, fill = BOTH, expand = TRUE)

 # frame 4
f4 = Frame(s_root)
f4.pack(fill = X, pady = 20)


# frame 3
f3 = Frame(s_root)
f3.pack(pady = 20, padx = 70)

inpt = Label(f3, text = 'INPUT : ', font = ' "" 10 ""', bg = 'grey', padx = 10, pady = 9)
inpt.pack(side = LEFT, padx = 20)
inp = StringVar()
inp_ent = Entry(f3, textvariable = inp, bg = 'grey', font = 10)
inp_ent.pack(side = LEFT, ipady = 8, ipadx = 30)
 
b6 = Button(f3, text = '|  GO  |', padx = 10, pady = 8, bg = 'light green', command = onclick6)
b6.pack(side = LEFT ,pady = 5, padx = 5)


s_root.mainloop()
