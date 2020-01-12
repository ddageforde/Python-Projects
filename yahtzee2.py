import random
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.messagebox import showinfo
import tkinter.font as font
from collections import defaultdict

import io
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

one = []
two = []
three = []
four = []
five = []
six = []
threeofakind = []
fourofakind = []
smstraight = []
lgstraight = []
fullhouse = []
yaht = []
bonus = []
chance = []
totalscore = []
upperbonus = []
lowtotal = []

btnclick1 = 0
btnclick2 = 0
btnclick3 = 0
btnclick4 = 0
btnclick5 = 0

diceclicked1 = []
diceclicked2 = []
diceclicked3 = []
diceclicked4 = []
diceclicked5 = []

class updatescore():

    def __init__(self):
        master = Toplevel()
        master.title('SCORECARD')

        w = self.w = Canvas(master, width=500, height=1000)
        w.pack()

        w.create_text(200, 40, text='UPPER SECTION SCORING')
        w.create_text(200, 41, text='_____________________________')
        w.create_text(55, 80, text='ONES:')
        w.create_text(55, 105, text='TWOS:')
        w.create_text(55, 130, text='THREES:')
        w.create_text(55, 155, text='FOURS:')
        w.create_text(55, 180, text='FIVES:')
        w.create_text(55, 205, text='SIXES:')
        w.create_text(55, 230, text='TOTAL SCORE:')
        w.create_text(55, 255, text='BONUS:')
        w.create_text(65, 280, text='TOTAL UPPER SECTION:')
        w.create_text(200, 355, text='LOWER SECTION SCORING')
        w.create_text(200, 356, text='____________________________')

        w.create_text(55, 415, text='THREE OF A KIND:')
        w.create_text(55, 440, text='FOUR OF A KIND:')
        w.create_text(55, 465, text='FULL HOUSE:')
        w.create_text(55, 490, text='SMALL STRAIGHT:')
        w.create_text(55, 515, text='LARGE STRAIGHT:')
        w.create_text(55, 540, text='YAHTZEE:')
        w.create_text(55, 565, text='YAHTZEE BONUS:')
        w.create_text(55, 590, text='CHANCE:')
        w.create_text(70, 615, text='LOWER SECTION TOTAL:')
        w.create_text(55, 640, text='GRAND TOTAL:')

        w.create_text(160, 80,text=one)
        w.create_text(160, 105, text=two)
        w.create_text(160, 130, text=three)
        w.create_text(160, 155, text=four)
        w.create_text(160, 180, text=five)
        w.create_text(160, 205, text=six)
        w.create_text(160, 415, text=threeofakind)
        w.create_text(160, 440, text=fourofakind)
        w.create_text(160, 465, text=fullhouse)
        w.create_text(160, 490, text=smstraight)
        w.create_text(160, 515, text=lgstraight)
        w.create_text(160, 540, text=yaht)
        w.create_text(160, 565, text=bonus)
        w.create_text(160, 590, text=chance)

class Score():

    def __init__(self):
        master = Toplevel()
        master.title('SCORECARD')

        w = self.w= Canvas(master, width=500, height=1000)
        w.pack()

        w.create_text(200, 40, text='UPPER SECTION SCORING')
        w.create_text(200, 41, text='_____________________________')
        w.create_text(55, 80, text='ONES:')
        w.create_text(55, 105, text='TWOS:')
        w.create_text(55, 130, text='THREES:')
        w.create_text(55, 155, text='FOURS:')
        w.create_text(55, 180, text='FIVES:')
        w.create_text(55, 205, text='SIXES:')
        w.create_text(55, 230, text='TOTAL SCORE:')
        w.create_text(55, 255, text='BONUS:')
        w.create_text(65, 280, text='TOTAL UPPER SECTION:')
        w.create_text(200, 355, text='LOWER SECTION SCORING')
        w.create_text(200, 356, text='____________________________')

        w.create_text(55, 415, text='THREE OF A KIND:')
        w.create_text(55, 440, text='FOUR OF A KIND:')
        w.create_text(55, 465, text='FULL HOUSE:')
        w.create_text(55, 490, text='SMALL STRAIGHT:')
        w.create_text(55, 515, text='LARGE STRAIGHT:')
        w.create_text(55, 540, text='YAHTZEE:')
        w.create_text(55, 565, text='YAHTZEE BONUS:')
        w.create_text(55, 590, text='CHANCE:')
        w.create_text(70, 615, text='LOWER SECTION TOTAL:')
        w.create_text(55, 640, text='GRAND TOTAL:')

        diceclicked = diceclicked1 + diceclicked2 + diceclicked3 + diceclicked4 + diceclicked5


        if  v.get() == '1':
            if not one:
                w.create_text(160,80,text= 1 * diceclicked.count(1))
                one.append(1 * diceclicked.count(1))
            else:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. Please choose another category.')
                chartscore()

        elif v.get() == '2':
            if not two:
                w.create_text(160,105,text=2 * diceclicked.count(2))
                two.append(2 * diceclicked.count(2))
            else:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. Please choose another category.')
                chartscore()

        elif v.get() == '3':
            if not three:
                w.create_text(160,130,text= 3 * diceclicked.count(3))
                three.append(3 * diceclicked.count(3))
            else:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. Please choose another category.')
                chartscore()

        elif v.get() == '4':
            if not four:
                w.create_text(160,155,text= 4 * diceclicked.count(4))
                four.append(4 * diceclicked.count(4))
            else:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. Please choose another category.')
                chartscore()

        elif v.get() == '5':
            if not five:
                w.create_text(160,180,text= 5 * diceclicked.count(5))
                five.append(5 * diceclicked.count(5))
            else:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. Please choose another category.')
                chartscore()

        elif v.get() == '6':
            if not six:
                w.create_text(160,205,text=6 * diceclicked.count(6))
                six.append(6 * diceclicked.count(6))
            else:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. Please choose another category.')
                chartscore()

        elif v.get() == '7':
            if 3 in list(times(diceclicked)) and not threeofakind:
                w.create_text(160,415,text=sum(diceclicked))
                threeofakind.append(sum(diceclicked))
            elif threeofakind:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. Please choose another category.')
                chartscore()
            else:
                w.create_text(160, 415, text=0)
                threeofakind.append(0)

        elif v.get() == '8':
            if 4 in list(times(diceclicked)) and not fourofakind:
                w.create_text(160, 440, text=sum(diceclicked))
                fourofakind.append(sum(diceclicked))
            elif fourofakind:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. Please choose another category.')
                chartscore()
            else:
                w.create_text(160, 440, text=0)
                fourofakind.append(0)

        elif v.get() == '9':
            if 3 in list(times(diceclicked)) and 2 in list(times(diceclicked)) and not fullhouse:
                w.create_text(160,465,text=25)
                fullhouse.append(25)
            elif fullhouse:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. Please choose another category.')
                chartscore()
            else:
                w.create_text(160, 465, text=0)
                fullhouse.append(0)

        elif v.get() == '10':
            if 4 in consnumb(sorted(diceclicked)) and not smstraight:
                w.create_text(160,490,text=30)
                smstraight.append(30)

            elif smstraight:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. Please choose another category.')
                chartscore()
            else:
                w.create_text(160, 490, text=0)
                smstraight.append(0)

        elif v.get() == '11':
            if 5 in consnumb(sorted(diceclicked)) and not lgstraight:
                w.create_text(160,515,text=40)
                lgstraight.append(40)

            elif lgstraight:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. Please choose another category.')
                chartscore()

            else:
                w.create_text(160, 515, text=0)
                lgstraight.append(0)

        elif v.get() == '12':
            if 5 in list(times(diceclicked)) and not yaht:
                w.create_text(160,540,text=50)
                yaht.append(50)
            elif yaht:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. If you have another Yahtzee please submit Yahtzee Bonus.')
                chartscore()
            else:
                w.create_text(160, 540, text=0)
                yaht.append(0)
                bonus.append(0)

        elif v.get() == '13':
            if 5 in list(times(diceclicked)) and yaht:
                w.create_text(160,565,text=100)
                bonus.append(100)
            elif 5 in list(times(diceclicked)) and yaht and bonus:
                bonus.append(100)
                w.create_text(160,565,text=sum(bonus))

            elif 5 in list(times(diceclicked)) and not yaht:
                master.destroy()
                showinfo('WARNING', 'This is your first Yahtzee. You must chart your score as Yahtzee instead of Yahtzee Bonus.')
            else:
                w.create_text(160, 565, text=0)
                bonus.append(0)

        elif v.get() == '14':
            if not chance:
                w.create_text(160,590,text=sum(diceclicked))
                chance.append(sum(diceclicked))
            else:
                master.destroy()
                showinfo('WARNING', 'You have already charted this category. Please choose another category.')
                chartscore()

        w.create_text(160,80,text=one)
        w.create_text(160, 105, text=two)
        w.create_text(160, 130, text=three)
        w.create_text(160, 155, text=four)
        w.create_text(160, 180, text=five)
        w.create_text(160, 205, text=six)
        w.create_text(160, 415, text=threeofakind)
        w.create_text(160, 440, text=fourofakind)
        w.create_text(160, 465, text=fullhouse)
        w.create_text(160, 490, text=smstraight)
        w.create_text(160, 515, text=lgstraight)
        w.create_text(160, 540, text=yaht)
        w.create_text(160, 565, text=bonus)
        w.create_text(160, 590, text=chance)

        nrFont = font.Font(weight='bold')

        nextroll = Button(master, text='NEXT ROLL', width=15, command=lambda: (master.destroy(),rollagain()))
        nextroll['font'] = nrFont
        nextroll.place(x=200, y=750)

        def finalscore():
            if one and two and three and four and five and six and threeofakind and fourofakind and fullhouse and smstraight and lgstraight and yaht and bonus and chance:
                totalscore.append(sum(one) + sum(two) + sum(three) + sum(four) + sum(five) + sum(six))
                lowtotal.append(sum(threeofakind) + sum(fourofakind) + sum(fullhouse) + sum(smstraight) + sum(lgstraight) + sum(yaht) + sum(bonus) + sum(chance))
                w.create_text(160, 230, text=totalscore)
                if sum(totalscore) >= 63:
                    upperbonus.append(35)
                    w.create_text(160, 255, text=upperbonus)
                    w.create_text(160, 280, text=sum(totalscore + upperbonus))
                    w.create_text(160,615,text=lowtotal)
                    w.create_text(160,640,text=sum(totalscore+upperbonus+lowtotal))
                    compscore = random.randint(200, 300)
                    total2 = sum(totalscore + upperbonus + lowtotal)
                    showinfo('GRAND TOTAL', f'Your grand total score is a {total2}.')
                    if compscore > total2:
                        showinfo('SORRY', f'Sorry you lose! You were outscored by the computer {compscore}-{total2}.')
                    elif compscore == total2:
                        showinfo('TIE', f'You tied the computer {compscore}-{total2}.')
                    elif total2 > compscore:
                        showinfo('CONGRATS',
                                 f'Congratulations you win! You outscored the computer {total2}- {compscore}.')
                    master.destroy()
                    root.counter1 = 0
                    one.clear(),two.clear(),three.clear(),four.clear(),five.clear(),six.clear(),threeofakind.clear(),fourofakind.clear(),fullhouse.clear(),smstraight.clear(),lgstraight.clear(),yaht.clear(),bonus.clear(),chance.clear(),totalscore.clear(),lowtotal.clear(),upperbonus.clear()
                else:
                    w.create_text(160, 255, text=0)
                    w.create_text(160, 280, text=totalscore)
                    w.create_text(160,615,text=lowtotal)
                    w.create_text(160,640,text=sum(totalscore+lowtotal))
                    compscore = random.randint(200, 300)
                    total = sum(totalscore + lowtotal)
                    total2 = sum(totalscore + upperbonus + lowtotal)
                    showinfo('GRAND TOTAL', f'Your grand total score is a {total}.')
                    if compscore > total2:
                        showinfo('SORRY', f'Sorry you lose! You were outscored by the computer {compscore}-{total2}.')
                    elif compscore == total2:
                        showinfo('TIE', f'You tied the computer {compscore}-{total2}.')
                    elif total2 > compscore:
                        showinfo('CONGRATS',
                                 f'Congratulations you win! You outscored the computer {total2}- {compscore}.')
                    master.destroy()
                    root.counter1 = 0
                    one.clear(), two.clear(), three.clear(), four.clear(), five.clear(), six.clear(), threeofakind.clear(), fourofakind.clear(), fullhouse.clear(), smstraight.clear(), lgstraight.clear(), yaht.clear(), bonus.clear(), chance.clear(),totalscore.clear(),lowtotal.clear(),upperbonus.clear()
            else:
                showinfo('WARNING','You must chart a score in each category before calculating final score. Please click Next Roll.')

        calcfinalscore = Button(master, text='CALCULATE FINAL SCORE', width=30, command= finalscore)
        calcfinalscore['font'] = nrFont
        calcfinalscore.place(x = 150, y = 850)

        master.mainloop()

root = Tk()
root.title('Yahtzee')
root.configure(width=1500,height=2000,bg='BLACK')
root.counter1 = 0
root.counter2 = 0
root.counter3 = 0
root.counter4 = 0
root.counter5 = 0

global times
def times(diceclicked):
        counted = defaultdict(int)

        for v in diceclicked:
            counted[v] += 1
            yield counted[v]

def consnumb(one):
    consec = [1]
    for x, y in zip(one, one[1:]):
        if x == y - 1:
            consec[-1] += 1
        else:
            consec.append(1)
    return consec

def rollagain():
    global diceclicked1
    diceclicked1.clear()
    global diceclicked2
    diceclicked2.clear()
    global diceclicked3
    diceclicked3.clear()
    global diceclicked4
    diceclicked4.clear()
    global diceclicked5
    diceclicked5.clear()
    root.counter1 = 0
    root.counter2 = 0
    root.counter3 = 0
    root.counter4 = 0
    root.counter5 = 0

    yahtzee()

def on_click6(event):
    global btnclick5
    btnclick5 +=1

    if btnclick5 % 2 == 0:
        event.widget.config(bg='white')
        root.counter5 -= 1
    else:
        event.widget.config(bg='red')
        root.counter5 += 1

def on_click5(event):
    global btnclick4
    btnclick4 +=1

    if btnclick4 % 2 == 0:
        event.widget.config(bg='white')
        root.counter4 -= 1
    else:
        event.widget.config(bg='red')
        root.counter4 += 1

def on_click4(event):
    global btnclick3
    btnclick3 += 1

    if btnclick3 % 2 == 0:
        event.widget.config(bg='white')
        root.counter3 -= 1
    else:
        event.widget.config(bg='red')
        root.counter3 += 1

def on_click3(event):
    global btnclick2
    btnclick2 +=1

    if btnclick2 % 2 == 0:
        event.widget.config(bg='white')
        root.counter2 -= 1
    else:
        event.widget.config(bg='red')
        root.counter2 += 1

def on_click(event):
    global btnclick1
    btnclick1 +=1

    if btnclick1 % 2 == 0:
        event.widget.config(bg='white')
        root.counter1 -= 1
    else:
        event.widget.config(bg='red')
        root.counter1 += 1

def countdice(a):
    global diceclicked1

    if btnclick1 % 2 != 0:
        diceclicked1.append(dicedict[a])

    elif btnclick1 % 2 == 0 and btnclick1 >= 2:
        diceclicked1 = diceclicked1[:-1]


def countdice2(a):
    global diceclicked2

    if btnclick2 % 2 != 0:
        diceclicked2.append(dicedict[a])

    elif btnclick2 % 2 == 0 and btnclick2 >= 2:
        diceclicked2 = diceclicked2[:-1]

def countdice3(a):
    global diceclicked3

    if btnclick3 % 2 != 0:
        diceclicked3.append(dicedict[a])

    elif btnclick3 % 2 == 0 and btnclick3 >= 2:
        diceclicked3 = diceclicked3[:-1]

def countdice4(a):
    global diceclicked4

    if btnclick4 % 2 != 0:
        diceclicked4.append(dicedict[a])

    elif btnclick4 % 2 == 0 and btnclick4 >= 2:
        diceclicked4 = diceclicked4[:-1]

def countdice5(a):
    global diceclicked5

    if btnclick5 % 2 != 0:
        diceclicked5.append(dicedict[a])

    elif btnclick5 % 2 == 0 and btnclick5 >= 2:
        diceclicked5 = diceclicked5[:-1]

def chartscore():

    window = Tk()
    window.geometry("600x800")
    window.title('Chart Score')
    L = Label(window, bg='orange', width=500,
                 text='Please choose the category you would like to chart your score in. If a score is submitted \n in a category that it does not qualify for it will automatically be scored as a zero on the scorecard:')
    L.pack()

    global v

    v = StringVar(window, 0)

    values = {"ONES": "1",
              "TWOS": "2",
              "THREES": "3",
              "FOURS": "4",
              "FIVES": "5",
              "SIXES": "6",
              "THREE OF A KIND": "7",
              "FOUR OF A KIND": "8",
              "FULL HOUSE": "9",
              "SMALL STRAIGHT": "10",
              "LARGE STRAIGHT": "11",
              "YAHTZEE": "12",
              "YAHTZEE BONUS": "13",
              "CHANCE": "14"}

    for (text, value) in values.items():
        Radiobutton(window, text=text, variable=v,
                    value=value).pack(side=TOP, ipady=5)

    button1 = Button(window, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12), command=lambda: (window.destroy(),Score()))
    button1.pack()

    button2 = Button(window, text="VIEW SCORECARD", bg="white",fg="black", width=20, font=("Times",12), command=updatescore)
    button2.pack(side=BOTTOM)
    mainloop()

def thirdroll():

    remdice2 = remdice - root.counter1 - root.counter2 - root.counter3 - root.counter4 - root.counter5

    global btnclick1
    btnclick1 = 0

    global btnclick2
    btnclick2 = 0

    global btnclick3
    btnclick3 = 0

    global btnclick4
    btnclick4 = 0

    global btnclick5
    btnclick5 = 0

    top3 = Toplevel()
    top3.title('Third Roll')

    url = "https://upload.wikimedia.org/wikipedia/commons/2/2c/Alea_1.png"
    imageb = urlopen(url).read()
    data = io.BytesIO(imageb)
    picimage = Image.open(data)
    d, n = picimage.size
    tkimage = ImageTk.PhotoImage(picimage)

    url2 = "https://upload.wikimedia.org/wikipedia/commons/b/b8/Alea_2.png"
    imageb = urlopen(url2).read()
    data = io.BytesIO(imageb)
    picimage = Image.open(data)
    d, n = picimage.size
    tkimage2 = ImageTk.PhotoImage(picimage)

    url3 = "https://upload.wikimedia.org/wikipedia/commons/2/2f/Alea_3.png"
    imageb = urlopen(url3).read()
    data = io.BytesIO(imageb)
    picimage = Image.open(data)
    d, n = picimage.size
    tkimage3 = ImageTk.PhotoImage(picimage)

    url4 = "https://upload.wikimedia.org/wikipedia/commons/8/8d/Alea_4.png"
    imageb = urlopen(url4).read()
    data = io.BytesIO(imageb)
    picimage = Image.open(data)
    d, n = picimage.size
    tkimage4 = ImageTk.PhotoImage(picimage)

    url5 = "https://upload.wikimedia.org/wikipedia/commons/5/55/Alea_5.png"
    imageb = urlopen(url5).read()
    data = io.BytesIO(imageb)
    picimage = Image.open(data)
    d, n = picimage.size
    tkimage5 = ImageTk.PhotoImage(picimage)

    url6 = "https://upload.wikimedia.org/wikipedia/commons/f/f4/Alea_6.png"
    imageb = urlopen(url6).read()
    data = io.BytesIO(imageb)
    picimage = Image.open(data)
    d, n = picimage.size
    tkimage6 = ImageTk.PhotoImage(picimage)

    root.counter1 = 0
    root.counter2 = 0
    root.counter3 = 0
    root.counter4 = 0
    root.counter5 = 0

    global my_img
    global image2
    global image3
    global image4
    global image5
    global image6

    label2 = Label(top3, text="Click on the dice you would like to keep for this round. Then click chart score.").pack()
    label = Label(top3,text="Your third roll is:").pack()

    my_img = tkimage
    image2 = tkimage2
    image3 = tkimage3
    image4 = tkimage4
    image5 = tkimage5
    image6 = tkimage6

    butn2 = Button(top3, text='View Scorecard', width=15, command=updatescore).place(x=20, y=100)
    butn3 = Button(top3, text='Chart Score', width=15, command=lambda: (top3.destroy(),chartscore())).place(x=20, y=50)

    dice = [my_img, image2, image3, image4, image5, image6]

    global rdice
    global rdice2
    global rdice3
    global rdice4
    global rdice5

    rdice = random.choice(dice)
    rdice2 = random.choice(dice)
    rdice3 = random.choice(dice)
    rdice4 = random.choice(dice)
    rdice5 = random.choice(dice)

    global dicedict

    dicedict = {my_img: 1, image2: 2, image3: 3, image4: 4, image5: 5, image6: 6}

    if remdice2 == 1:
          btn1 = Button(top3, image=rdice, command=lambda a =rdice:countdice(a))
          btn1.pack()
          btn1.bind('<Button-1>', on_click)

    if remdice2 == 2:
          btn1 = Button(top3, image=rdice, command=lambda a =rdice:countdice(a))
          btn1.pack()
          btn1.bind('<Button-1>', on_click)
          btn2 = Button(top3, image=rdice2,  command=lambda a =rdice2:countdice2(a))
          btn2.pack()
          btn2.bind('<Button-1>', on_click3)

    if remdice2 == 3:
          btn1 = Button(top3, image=rdice,command=lambda a =rdice:countdice(a))
          btn1.pack()
          btn1.bind('<Button-1>', on_click)
          btn2 = Button(top3, image=rdice2,  command=lambda a =rdice2:countdice2(a))
          btn2.pack()
          btn2.bind('<Button-1>', on_click3)
          btn3 = Button(top3, image=rdice3, command=lambda a =rdice3:countdice3(a))
          btn3.pack()
          btn3.bind('<Button-1>', on_click4)

    if remdice2 == 4:
          btn1 = Button(top3, image=rdice, command=lambda a =rdice:countdice(a))
          btn1.pack()
          btn1.bind('<Button-1>', on_click)
          btn2 = Button(top3, image=rdice2, command=lambda a =rdice2:countdice2(a))
          btn2.pack()
          btn2.bind('<Button-1>', on_click3)
          btn3 = Button(top3, image=rdice3, command=lambda a =rdice3:countdice3(a))
          btn3.pack()
          btn3.bind('<Button-1>', on_click4)
          btn4 = Button(top3, image=rdice4, command=lambda a =rdice4:countdice4(a))
          btn4.pack()
          btn4.bind('<Button-1>', on_click5)

    if remdice2 == 5:
          btn1 = Button(top3, image=rdice, command=lambda a =rdice:countdice(a))
          btn1.pack()
          btn1.bind('<Button-1>', on_click)
          btn2 = Button(top3, image=rdice2,  command=lambda a =rdice2:countdice2(a))
          btn2.pack()
          btn2.bind('<Button-1>', on_click3)
          btn3 = Button(top3, image=rdice3, command=lambda a =rdice3:countdice3(a))
          btn3.pack()
          btn3.bind('<Button-1>', on_click4)
          btn4 = Button(top3, image=rdice4, command=lambda a =rdice4:countdice4(a))
          btn4.pack()
          btn4.bind('<Button-1>', on_click5)
          btn5 = Button(top3, image=rdice5, command=lambda a =rdice5:countdice5(a))
          btn5.pack()
          btn5.bind('<Button-1>', on_click6)

def secondroll():

    global remdice
    remdice = 5 - root.counter1 - root.counter2 - root.counter3 - root.counter4 - root.counter5

    global btnclick1
    btnclick1 = 0

    global btnclick2
    btnclick2 = 0

    global btnclick3
    btnclick3 = 0

    global btnclick4
    btnclick4 = 0

    global btnclick5
    btnclick5 = 0

    top2 = Toplevel()
    top2.title('Second Roll')

    url = "https://upload.wikimedia.org/wikipedia/commons/2/2c/Alea_1.png"
    imageb = urlopen(url).read()
    data = io.BytesIO(imageb)
    picimage = Image.open(data)
    d, n = picimage.size
    tkimage = ImageTk.PhotoImage(picimage)

    url2 = "https://upload.wikimedia.org/wikipedia/commons/b/b8/Alea_2.png"
    imageb = urlopen(url2).read()
    data = io.BytesIO(imageb)
    picimage = Image.open(data)
    d, n = picimage.size
    tkimage2 = ImageTk.PhotoImage(picimage)

    url3 = "https://upload.wikimedia.org/wikipedia/commons/2/2f/Alea_3.png"
    imageb = urlopen(url3).read()
    data = io.BytesIO(imageb)
    picimage = Image.open(data)
    d, n = picimage.size
    tkimage3 = ImageTk.PhotoImage(picimage)

    url4 = "https://upload.wikimedia.org/wikipedia/commons/8/8d/Alea_4.png"
    imageb = urlopen(url4).read()
    data = io.BytesIO(imageb)
    picimage = Image.open(data)
    d, n = picimage.size
    tkimage4 = ImageTk.PhotoImage(picimage)

    url5 = "https://upload.wikimedia.org/wikipedia/commons/5/55/Alea_5.png"
    imageb = urlopen(url5).read()
    data = io.BytesIO(imageb)
    picimage = Image.open(data)
    d, n = picimage.size
    tkimage5 = ImageTk.PhotoImage(picimage)

    url6 = "https://upload.wikimedia.org/wikipedia/commons/f/f4/Alea_6.png"
    imageb = urlopen(url6).read()
    data = io.BytesIO(imageb)
    picimage = Image.open(data)
    d, n = picimage.size
    tkimage6 = ImageTk.PhotoImage(picimage)

    root.counter1 = 0
    root.counter2 = 0
    root.counter3 = 0
    root.counter4 = 0
    root.counter5 = 0

    global my_img
    global image2
    global image3
    global image4
    global image5
    global image6

    lbl2 = Label(top2,text="Click on the dice you would like to keep for this round. Then click third roll or chart score.").pack()
    label = Label(top2, text="Your second roll is:").pack()

    my_img = tkimage
    image2 = tkimage2
    image3 = tkimage3
    image4 = tkimage4
    image5 = tkimage5
    image6 = tkimage6
    butn = Button(top2, text="Third Roll", width=10, command=lambda: (thirdroll(),top2.destroy())).place(x=370, y=100)
    butn2 = Button(top2, text='View Scorecard', width=15, command=updatescore).place(x=50, y=100)
    butn3 = Button(top2, text='Chart Score', width=15, command=lambda: (top2.destroy(),chartscore())).place(x=50, y=50)

    dice = [my_img, image2, image3, image4, image5, image6]

    global rdice
    global rdice2
    global rdice3
    global rdice4
    global rdice5

    rdice = random.choice(dice)
    rdice2 = random.choice(dice)
    rdice3 = random.choice(dice)
    rdice4 = random.choice(dice)
    rdice5 = random.choice(dice)

    global dicedict

    dicedict = {my_img: 1, image2: 2, image3: 3, image4: 4, image5: 5, image6: 6}

    if remdice == 1:
          btn1 = Button(top2, image=rdice, command=lambda a =rdice:countdice(a))
          btn1.pack()
          btn1.bind('<Button-1>', on_click)

    if remdice == 2:
          btn1 = Button(top2, image=rdice, command=lambda a =rdice:countdice(a))
          btn1.pack()
          btn1.bind('<Button-1>', on_click)
          btn2 = Button(top2, image=rdice2,  command=lambda a =rdice2:countdice2(a))
          btn2.pack()
          btn2.bind('<Button-1>', on_click3)

    if remdice == 3:
          btn1 = Button(top2, image=rdice, command=lambda a =rdice:countdice(a))
          btn1.pack()
          btn1.bind('<Button-1>', on_click)
          btn2 = Button(top2, image=rdice2,  command=lambda a =rdice2:countdice2(a))
          btn2.pack()
          btn2.bind('<Button-1>', on_click3)
          btn3 = Button(top2, image=rdice3, command=lambda a =rdice3:countdice3(a))
          btn3.pack()
          btn3.bind('<Button-1>', on_click4)

    if remdice == 4:
          btn1 = Button(top2, image=rdice, command=lambda a =rdice:countdice(a))
          btn1.pack()
          btn1.bind('<Button-1>', on_click)
          btn2 = Button(top2, image=rdice2,  command=lambda a =rdice2:countdice2(a))
          btn2.pack()
          btn2.bind('<Button-1>', on_click3)
          btn3 = Button(top2, image=rdice3,command=lambda a =rdice3:countdice3(a))
          btn3.pack()
          btn3.bind('<Button-1>', on_click4)
          btn4 = Button(top2, image=rdice4, command=lambda a =rdice4:countdice4(a))
          btn4.pack()
          btn4.bind('<Button-1>', on_click5)

    if remdice == 5:
          btn1 = Button(top2, image=rdice, command=lambda a =rdice:countdice(a))
          btn1.pack()
          btn1.bind('<Button-1>', on_click)
          btn2 = Button(top2, image=rdice2,  command=lambda a =rdice2:countdice2(a))
          btn2.pack()
          btn2.bind('<Button-1>', on_click3)
          btn3 = Button(top2, image=rdice3, command=lambda a =rdice3:countdice3(a))
          btn3.pack()
          btn3.bind('<Button-1>', on_click4)
          btn4 = Button(top2, image=rdice4, command=lambda a =rdice4:countdice4(a))
          btn4.pack()
          btn4.bind('<Button-1>', on_click5)
          btn5 = Button(top2, image=rdice5,command=lambda a =rdice5:countdice5(a))
          btn5.pack()
          btn5.bind('<Button-1>', on_click6)

def yahtzee():

      global btnclick1
      btnclick1 = 0

      global btnclick2
      btnclick2 = 0

      global btnclick3
      btnclick3 = 0

      global btnclick4
      btnclick4 = 0

      global btnclick5
      btnclick5 = 0

      global diceclicked1
      diceclicked1.clear()
      global diceclicked2
      diceclicked2.clear()
      global diceclicked3
      diceclicked3.clear()
      global diceclicked4
      diceclicked4.clear()
      global diceclicked5
      diceclicked5.clear()

      top = Toplevel()
      top.title('First Roll')

      url = "https://upload.wikimedia.org/wikipedia/commons/2/2c/Alea_1.png"
      imageb = urlopen(url).read()
      data = io.BytesIO(imageb)
      picimage = Image.open(data)
      d, n = picimage.size
      tkimage = ImageTk.PhotoImage(picimage)

      url2 = "https://upload.wikimedia.org/wikipedia/commons/b/b8/Alea_2.png"
      imageb = urlopen(url2).read()
      data = io.BytesIO(imageb)
      picimage = Image.open(data)
      d, n = picimage.size
      tkimage2 = ImageTk.PhotoImage(picimage)

      url3 = "https://upload.wikimedia.org/wikipedia/commons/2/2f/Alea_3.png"
      imageb = urlopen(url3).read()
      data = io.BytesIO(imageb)
      picimage = Image.open(data)
      d, n = picimage.size
      tkimage3 = ImageTk.PhotoImage(picimage)

      url4 = "https://upload.wikimedia.org/wikipedia/commons/8/8d/Alea_4.png"
      imageb = urlopen(url4).read()
      data = io.BytesIO(imageb)
      picimage = Image.open(data)
      d, n = picimage.size
      tkimage4 = ImageTk.PhotoImage(picimage)

      url5 = "https://upload.wikimedia.org/wikipedia/commons/5/55/Alea_5.png"
      imageb = urlopen(url5).read()
      data = io.BytesIO(imageb)
      picimage = Image.open(data)
      d, n = picimage.size
      tkimage5 = ImageTk.PhotoImage(picimage)

      url6 = "https://upload.wikimedia.org/wikipedia/commons/f/f4/Alea_6.png"
      imageb = urlopen(url6).read()
      data = io.BytesIO(imageb)
      picimage = Image.open(data)
      d, n = picimage.size
      tkimage6 = ImageTk.PhotoImage(picimage)

      global my_img
      global image2
      global image3
      global image4
      global image5
      global image6

      lbl2 = Label(top, text="Click on the dice you would like to keep for this round. Then click second roll or chart score.").pack()
      lbl = Label(top, text="Your first roll is:").pack()
      my_img = tkimage
      image2 = tkimage2
      image3 = tkimage3
      image4 = tkimage4
      image5 = tkimage5
      image6 = tkimage6
      butn = Button(top, text="Second Roll", width=10, command=lambda: (secondroll(),top.destroy())).place(x=400, y=500)
      butn2 = Button(top, text='View Scorecard', width=15,command=updatescore).place(x=370,y=600)
      butn3 = Button(top, text='Chart Score',width=15,command=lambda: (top.destroy(),chartscore())).place(x=50,y=500)

      dice = [my_img, image2, image3, image4, image5, image6]

      global rdice
      global rdice2
      global rdice3
      global rdice4
      global rdice5

      rdice = random.choice(dice)
      rdice2 = random.choice(dice)
      rdice3 = random.choice(dice)
      rdice4 = random.choice(dice)
      rdice5 = random.choice(dice)

      global dicedict

      dicedict = {my_img:1,image2:2,image3:3,image4:4,image5:5,image6:6}

      btn1 = Button(top, image=rdice, command=lambda a =rdice:countdice(a))
      btn1.pack()
      btn1.bind('<Button-1>', on_click)
      btn2 = Button(top, image=rdice2, command=lambda a =rdice2:countdice2(a))
      btn2.pack()
      btn2.bind('<Button-1>', on_click3)
      btn3 = Button(top, image=rdice3, command=lambda a =rdice3:countdice3(a))
      btn3.pack()
      btn3.bind('<Button-1>', on_click4)
      btn4 = Button(top, image=rdice4,command=lambda a =rdice4:countdice4(a))
      btn4.pack()
      btn4.bind('<Button-1>', on_click5)
      btn5 = Button(top, image=rdice5, command=lambda a =rdice5:countdice5(a))
      btn5.pack()
      btn5.bind('<Button-1>', on_click6)

def quit():
    exit()

def rules():
    showinfo('RULES','The game begins by the player rolling a cup of five dice. The player may roll the 5 dice a total'
          ' of 3 times. After each roll the player may set aside any dice they wish to keep for scoring and place the others'
          ' back in the cup. Then the player must choose a category to score the points. Scoring can be charted at any'
          ' point in the round. The player does not have to roll the dice three times.'
    '\n\nSCORING\n'

    '\nTo chart your score choose one of the categories on the scorecard. Once you place a score in a category \n'
          'it cannot be scored again the rest of the game, except for the Yahtzee Bonus. The player with the most \n'
          'points after all categories have been filled wins the game. Listed below is an explanation of the scoring for each category:\n\n'
          'UPPER SECTION SCORING\n\n'
          'ONES: The sum of all the 1s rolled by the player.\n'
          'TWOS: The sum of all the 2s rolled by the player.\n'
          'THREES: The sum of all the 3s rolled by the player.\n'
          'FOURS: The sum of all the 4s rolled by the player.\n'
          'FIVES: The sum of all the 5s rolled by the player.\n'
          'SIXES: The sum of the 6s rolled by the player.\n'
          'TOTAL SCORE: The sum of the 6 categories above.\n'
          'BONUS: If the total score is 63 or greater a bonus score of 35 is added.\n'
          'TOTAL UPPER SECTION: The total score plus the bonus if one is given.\n\n'

          'LOWER SECTION SCORING\n\n'

          'THREE OF A KIND: Scores the total of all dice and must include 3 of the same number.\n'
          'FOUR OF A KIND: Scores the total of all dice and must include 4 of the same number.\n'
          'FULL HOUSE: Scored as 25 points and must include 3 dice of one number and 2 dice of another number.\n'
          'SMALL STRAIGHT: Scored as 30 points and is a sequence of 4 numbers.\n'
          'LARGE STRAIGHT: Scored as 40 points and is a sequence of 5 numbers.\n'
          'YAHTZEE: Scored as 50 points and is a 5 of a kind.(5 dice of the same number)\n'
          'CHANCE: Total of all 5 dice.\n'
          'YAHTZEE BONUS: Scored as 100 points and this category is charted for each additonal Yahtzee rolled.\n'
          'LOWER SECTION TOTAL: Sum of all categories in the lower section.\n'

          '\nGRAND TOTAL: The sum of the upper section total and the lower section total.\n')

button1= Button(root, text="Quit", bg="white", fg="black", width=20, font=("Times", 12),command=quit)
button2= Button(root, text="Rules", bg="white", fg="black", width=20, font=("Times", 12),command=rules)
button3= Button(root, text="Play A Game Of Yahtzee", bg="white", fg="black", width=20, font=("Times", 12),command=yahtzee)

button1.grid(row=1,column=4, padx=40, pady=10)
button2.grid(row=1,column=5, padx=40, pady=10)
button3.grid(row=1,column=6,padx=40,pady=10)

mainloop()











