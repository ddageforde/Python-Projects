import random
from tkinter import *
from PIL import ImageTk ,Image
import numpy
from tkinter.messagebox import showinfo

window = Tk()
window.title('Dan\'s Furniture Store')
window.configure(width=9000,height=9000,bg='BLACK')

furniture = {'end table':25.99,'side table':29.99, 'coffee table':79.99,'drink table':74.99, 'console table':99.99,'rocking chair':129.99, 'recliner':99.99, 'office chair':39.99, 'bar stool':55.99, 'folding chair':9.99, 'deck chair':49.99,'sleeper ottoman':549.99, 'tufted ottoman':195.99, 'pouf ottoman':44.99, 'storage ottoman':122.99,'air mattress':39.99, 'memory foam mattress':399.99, 'water bed mattress':1099.99, 'futons':119.99,'latex mattress': 699.99,'twin mattress':99.99,'queen mattress': 199.99, 'king mattress': 349.99, 'single bed':119.99,'twin bed':238.99,'twin xl bed':279.99, 'double bed':189.99, 'full bed':449.99 , 'queen bed':299.99, 'king bed':409.99,'california king bed':599.99, 'sectional sofa':359.99, 'sleeper sofa':399.99, 'loveseat sofa': 214.99, 'traditional sofa':289.99, 'chaise sofa':429.99, 'open shelving tv stand':159.99, 'console tv stand':129.99, 'hutch tv stand':199.99, 'cabinet tv stand':175.99, 'swivel tv stand':35.99, 'floating tv stand':41.99}

currentorder = []

currentqty = []

price = []

totalprice = []

def addtoorder():

    currentorder.append(v.get())
    currentqty.append(qty.get())
    currorder = {currentorder[i]:currentqty[i] for i in range(len(currentorder))}
    price.append(furniture[v.get().lower()])
    totalprice.append(qty.get() * furniture[v.get().lower()])

def tables():

        top = Toplevel()
        top.geometry("600x800")
        top.title('Order Tables')

        L = Label(top, bg='orange', width=500,
                 text='Choose a table type and the quantity you would like to order:')
        L.pack()

        global v

        v = StringVar(top, 0)

        values = {"END TABLE  $25.99": "END TABLE",
              "SIDE TABLE  $29.99": "SIDE TABLE",
              "COFFEE TABLE  $79.99": "COFFEE TABLE",
              "DRINK TABLE  $74.99": "DRINK TABLE",
              "CONSOLE TABLE  $99.99": "CONSOLE TABLE"}

        for (text, value) in values.items():
            Radiobutton(top, text=text, variable=v,
                    value=value).pack(side=TOP, ipady=5)

        L1 = Label(top, text  = 'QUANTITY:')
        L1.place(x=430,y=30)

        global qty

        qty = IntVar()
        qty.set(1)

        opt = OptionMenu(top,qty,1, 2, 3, 4, 5)
        opt.place(x=500,y=25)

        button1 = Button(top, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12), command=lambda: (top.destroy(),addtoorder()))
        button1.pack()

        top.mainloop()

def chairs():

    top = Toplevel()
    top.geometry("600x800")
    top.title('Order Chairs')

    L = Label(top, bg='orange', width=500,
              text='Choose a chair type and the quantity you would like to order:')
    L.pack()

    global v

    v = StringVar(top, 0)

    values = {"ROCKING CHAIR  $129.99": "ROCKING CHAIR",
              "RECLINER  $99.99": "RECLINER",
              "OFFICE CHAIR  $39.99": "OFFICE CHAIR",
              "BAR STOOL  $55.99": "BAR STOOL",
              "FOLDING CHAIR  $9.99": "FOLDING CHAIR","DECK CHAIR  $49.99":"DECK CHAIR"}

    for (text, value) in values.items():
        Radiobutton(top, text=text, variable=v,
                    value=value).pack(side=TOP, ipady=5)

    L1 = Label(top, text='QUANTITY:')
    L1.place(x=430, y=30)

    global qty

    qty = IntVar()
    qty.set(1)

    opt = OptionMenu(top, qty, 1, 2, 3, 4, 5)
    opt.place(x=500, y=25)

    button1 = Button(top, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12),
                     command=lambda: (top.destroy(), addtoorder()))
    button1.pack()

    top.mainloop()

def ottomans():

    top = Toplevel()
    top.geometry("600x800")
    top.title('Order Ottomans')

    L = Label(top, bg='orange', width=500,
              text='Choose an ottoman type and the quantity you would like to order:')
    L.pack()

    global v

    v = StringVar(top, 0)

    values = {"SLEEPER  $549.99": "SLEEPER OTTOMAN",
              "TUFTED  $195.99": "TUFTED OTTOMAN",
              "POUF  $44.99": "POUF OTTOMAN",
              "STORAGE  $122.99": "STORAGE OTTOMAN"
              }

    for (text, value) in values.items():
        Radiobutton(top, text=text, variable=v,
                    value=value).pack(side=TOP, ipady=5)

    L1 = Label(top, text='QUANTITY:')
    L1.place(x=430, y=30)

    global qty

    qty = IntVar()
    qty.set(1)

    opt = OptionMenu(top, qty, 1, 2, 3, 4, 5)
    opt.place(x=500, y=25)

    button1 = Button(top, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12),
                     command=lambda: (top.destroy(), addtoorder()))
    button1.pack()

    top.mainloop()

def mattresses():

    top = Toplevel()
    top.geometry("600x800")
    top.title('Order Mattresses')

    L = Label(top, bg='orange', width=500,
              text='Choose a mattress type and the quantity you would like to order:')
    L.pack()

    global v

    v = StringVar(top, 0)

    values = {"AIR MATTRESS  $39.99": "AIR MATTRESS",
              "MEMORY FOAM  $399.99": "MEMORY FOAM MATTRESS",
              "WATER BED  $1099.99": "WATER BED MATTRESS",
              "FUTONS  $119.99": "FUTONS",
              "LATEX  $699.99": "LATEX MATTRESS","TWIN  $99.99":"TWIN MATTRESS",
              "QUEEN  $199.99": "QUEEN MATTRESS", "KING  $349.99": "KING MATTRESS"}

    for (text, value) in values.items():
        Radiobutton(top, text=text, variable=v,
                    value=value).pack(side=TOP, ipady=5)

    L1 = Label(top, text='QUANTITY:')
    L1.place(x=430, y=30)

    global qty

    qty = IntVar()
    qty.set(1)

    opt = OptionMenu(top, qty, 1, 2, 3, 4, 5)
    opt.place(x=500, y=25)

    button1 = Button(top, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12),
                     command=lambda: (top.destroy(), addtoorder()))
    button1.pack()

    top.mainloop()

def beds():

    top = Toplevel()
    top.geometry("600x800")
    top.title('Order Beds')

    L = Label(top, bg='orange', width=500,
              text='Choose a bed type and the quantity you would like to order:')
    L.pack()

    global v

    v = StringVar(top, 0)

    values = {"SINGLE  $119.99": "SINGLE BED",
              "TWIN  $238.99": "TWIN BED",
              "TWIN XL  $279.99": "TWIN XL BED",
              "DOUBLE  $189.99": "DOUBLE BED",
              "FULL  $449.99": "FULL BED", "QUEEN  $299.99": "QUEEN BED","KING  $409.99": "KING BED","CALIFORNIA KING  $599.99": "CALIFORNIA KING BED"}

    for (text, value) in values.items():
        Radiobutton(top, text=text, variable=v,
                    value=value).pack(side=TOP, ipady=5)

    L1 = Label(top, text='QUANTITY:')
    L1.place(x=430, y=30)

    global qty

    qty = IntVar()
    qty.set(1)

    opt = OptionMenu(top, qty, 1, 2, 3, 4, 5)
    opt.place(x=500, y=25)

    button1 = Button(top, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12),
                     command=lambda: (top.destroy(), addtoorder()))
    button1.pack()

    top.mainloop()

def sofa():

    top = Toplevel()
    top.geometry("600x800")
    top.title('Order Sofas')

    L = Label(top, bg='orange', width=500,
              text='Choose a sofa type and the quantity you would like to order:')
    L.pack()

    global v

    v = StringVar(top, 0)

    values = {"SECTIONAL  $359.99": "SECTIONAL SOFA",
              "SLEEPER  $399.99": "SLEEPER SOFA",
              "LOVESEAT  $214.99": "LOVESEAT SOFA",
              "TRADITIONAL  $289.99": "TRADITIONAL SOFA",
              "CHAISE  $429.99": "CHAISE SOFA"}

    for (text, value) in values.items():
        Radiobutton(top, text=text, variable=v,
                    value=value).pack(side=TOP, ipady=5)

    L1 = Label(top, text='QUANTITY:')
    L1.place(x=430, y=30)

    global qty

    qty = IntVar()
    qty.set(1)

    opt = OptionMenu(top, qty, 1, 2, 3, 4, 5)
    opt.place(x=500, y=25)

    button1 = Button(top, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12),
                     command=lambda: (top.destroy(), addtoorder()))
    button1.pack()

    top.mainloop()

def tvstand():

    top = Toplevel()
    top.geometry("600x800")
    top.title('Order TV Stands')

    L = Label(top, bg='orange', width=500,
              text='Choose a tv stand and the quantity you would like to order:')
    L.pack()

    global v

    v = StringVar(top, 0)

    values = {"OPEN SHELVING  $159.99": "OPEN SHELVING TV STAND",
              "CONSOLE  $129.99": "CONSOLE TV STAND",
              "HUTCH  $199.99": "HUTCH TV STAND",
              "CABINET  $175.99": "CABINET TV STAND",
              "SWIVEL  $35.99": "SWIVEL TV STAND", "FLOATING  $41.99": "FLOATING TV STAND"}

    for (text, value) in values.items():
        Radiobutton(top, text=text, variable=v,
                    value=value).pack(side=TOP, ipady=5)

    L1 = Label(top, text='QUANTITY:')
    L1.place(x=430, y=30)

    global qty

    qty = IntVar()
    qty.set(1)

    opt = OptionMenu(top, qty, 1, 2, 3, 4, 5)
    opt.place(x=500, y=25)

    button1 = Button(top, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12),
                     command=lambda: (top.destroy(), addtoorder()))
    button1.pack()

    top.mainloop()

def currorder():

    top2 = Toplevel()
    top2.geometry("800x800")
    top2.title('Current Order Summary')

    L = Label(top2, bg='orange', width=500,
              text='CURRENT ORDER SUMMARY:')
    L.pack()

    for i in range(len(currentorder)):
            Label(top2, text=currentorder[i] + '   QTY:' + str(currentqty[i]) + '   ITEM TOTAL:$' + str(round(totalprice[i],2))).pack(ipady=5)

    #Gives the customer a 15% discount if the order is $5000 or more
    #Gives the customer a 25% discount if 15 or more items are purchased

    stotalprice = sum(totalprice)

    discount = stotalprice - (stotalprice * .15)

    qtydiscount = stotalprice - (stotalprice * .25)

    bulkexp = stotalprice - (stotalprice * .4)

    tax = stotalprice * .053

    if stotalprice < 5000 and sum(currentqty) < 15:

        L2 = Label(top2, text='TAX:$' + str(round(tax,2)) +'\nCURRENT ORDER TOTAL:$' + str(round(stotalprice + tax,2)))
        L2.pack()

    elif stotalprice >= 5000 and sum(currentqty) < 15:

        L2 = Label(top2, text='EXPENSIVE ORDER 15% DISCOUNT:$' + str(round(stotalprice * .15,2)) +  '\nTAX:$' + str(round(discount * .053,2)) + '\nCURRENT ORDER TOTAL:$' + str(round(discount + (discount * .053),2)))
        L2.pack()

    elif stotalprice < 5000 and sum(currentqty) >= 15:

        L2 = Label(top2, text='BULK ORDER 25% DISCOUNT:$' + str(round(stotalprice * .25, 2)) +  '\nTAX:$' + str(round(qtydiscount * .053,2)) + '\nCURRENT ORDER TOTAL:$' + str(round(qtydiscount + (qtydiscount * .053),2)))
        L2.pack()

    elif stotalprice >= 5000 and sum(currentqty) >= 15:

        L2 = Label(top2, text='BULK ORDER 25% DISCOUNT:$' + str(round(stotalprice * .25, 2)) + '\nEXPENSIVE ORDER 15% DISCOUNT:$' + str(round(stotalprice * .15,2)) + '\nTAX:$' + str(round(bulkexp * .053,2)) +'\nCURRENT ORDER TOTAL:$' + str(round(bulkexp + (bulkexp * .053),2)))
        L2.pack()

    top2.mainloop()

def removefromorder():

    del totalprice[currentorder.index(v.get())]
    del currentqty[currentorder.index(v.get())]
    currentorder.remove(v.get())

def removeitem():
    top4 = Toplevel()
    top4.geometry("500x500")
    top4.title("Remove Item From Order")

    L = Label(top4, bg='orange', width=500,
              text='Choose the item that you would like to remove from your order:')
    L.pack()

    global v

    v = StringVar(top4, 0)

    for text in currentorder:
        Radiobutton(top4, text=text,variable=v,value=text).pack()

    button1 = Button(top4, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12),
                     command=lambda: (top4.destroy(), removefromorder()))
    button1.pack()

    top4.mainloop()

def changeqty():

    currentqty[currentorder.index(v.get())] = qty.get()
    totalprice[currentorder.index(v.get())] = qty.get() * furniture[v.get().lower()]

def chgqty():
    top5 = Toplevel()
    top5.geometry("500x500")
    top5.title("Change Quantity")

    L = Label(top5, bg='orange', width=500,
              text='Choose an item and change the quantity to the amount you would like to be ordered:')
    L.pack()

    global v

    v = StringVar(top5, 0)

    for i in range(len(currentorder)):
        Radiobutton(top5, text=currentorder[i] + '   QTY:' + str(currentqty[i]),variable = v,value =currentorder[i]).pack(ipady=5)

    L1 = Label(top5, text='QUANTITY:')
    L1.place(x=360, y=30)

    global qty

    qty = IntVar()
    qty.set(1)

    opt = OptionMenu(top5, qty, 1, 2, 3, 4, 5)
    opt.place(x=430, y=25)

    button1 = Button(top5, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12),
                     command=lambda: (top5.destroy(), changeqty()))

    button1.pack()

    top5.mainloop()

def checkout():
    top6 = Toplevel()
    top6.geometry("525x500")
    top6.title("Place Order")

    stotalprice = sum(totalprice)

    discount = stotalprice - (stotalprice * .15)

    qtydiscount = stotalprice - (stotalprice * .25)

    bulkexp = stotalprice - (stotalprice * .4)

    tax = stotalprice * .053

    if stotalprice < 5000 and sum(currentqty) < 15:
            currordertotal = str(round(stotalprice + tax, 2))

    elif stotalprice >= 5000 and sum(currentqty) < 15:
            currordertotal =  str(round(discount + (discount * .053),2))

    elif stotalprice < 5000 and sum(currentqty) >= 15:
            currordertotal = str(round(qtydiscount + (qtydiscount * .053),2))


    elif stotalprice >= 5000 and sum(currentqty) >= 15:
            currordertotal = str(round(bulkexp + (bulkexp * .053),2))

    methodpayment = {'CHECK':1,'CREDIT CARD':2}

    L = Label(top6, bg='orange', width=500,
              text=f'Your current order total is ${currordertotal} \nPlease choose which method you would like to pay with:')
    L.pack()

    global v

    v = IntVar(top6, 0)

    for (text, value) in methodpayment.items():
        Radiobutton(top6, text=text, variable=v,
                    value=value).pack(side=TOP, ipady=5)

    button1 = Button(top6, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12),
                     command=lambda: (top6.destroy(), checkorcredit()))
    button1.pack()

    top6.mainloop()

def checkorcredit():
    if v.get() == 1:
            check()
    if v.get() == 2:
            creditcard()

def check():
    top7 = Toplevel()
    top7.geometry("500x500")
    top7.title("Pay With Check")

    Label1 = Label(top7,text='Enter the 12 digit account number:', width=50)
    Label1.place(x=10,y=80)

    global v

    v = StringVar(top7)

    v.set('')

    entry1 = Entry(top7, textvariable=v)
    entry1.place(x=300,y=80)

    Label2 = Label(top7, text='Enter the 4 digit check number:', width = 50)
    Label2.place(x=10,y=250)

    global v2

    v2 = StringVar(top7)
    v2.set('')

    entry2 = Entry(top7, textvariable = v2)
    entry2.place(x=300, y=250)

    button1 = Button(top7, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12),
                     command= checkcredentials)
    button1.place(x = 250, y=350)

    top7.mainloop()

def checkcredentials():

    if len(v.get()) == 12 and v.get().isnumeric() and len(v2.get()) == 4 and v2.get().isnumeric():
        showinfo(f'THANKS', 'Thank you for submitting your order! Your order has been placed and you should receive your furniture within the next 5-7 business days.')
        exit()
    else:
        showinfo('INCORRECT CREDENTIALS',
                 'Please enter a 12 digit account number and a 4 digit check number.')

def creditcard():

    top8 = Toplevel()
    top8.geometry("500x500")
    top8.title("Pay With Credit Card")

    Label1 = Label(top8, text='Enter the 16 digit credit card number:', width=50)
    Label1.place(x=10, y=80)

    global v

    v = StringVar(top8)

    v.set('')

    entry1 = Entry(top8, textvariable=v)
    entry1.place(x=300, y=80)

    Label2 = Label(top8, text='Enter the 4 digit expiration date:', width=50)
    Label2.place(x=10, y=250)

    global v2

    v2 = StringVar(top8)
    v2.set('')

    entry2 = Entry(top8, textvariable=v2)
    entry2.place(x=300, y=250)

    button1 = Button(top8, text="SUBMIT", bg="white", fg="black", width=20, font=("Times", 12),
                     command=cccredentials)
    button1.place(x=250, y=350)

    top8.mainloop()

def cccredentials():
    if len(str(v.get())) == 16 and v.get().isnumeric() and len(v2.get()) == 4 and v2.get().isnumeric():
        showinfo('THANKS',
                 'Thank you for submitting your order! Your order has been placed and you should receive your furniture within the next 5-7 business days.')
        exit()
    else:
        showinfo('INCORRECT CREDENTIALS',
                 'Please enter a 16 digit account number and a 4 digit check number.')


label1 = Label(window, text= 'PLEASE CHOOSE A CATEGORY THAT YOU WOULD LIKE TO ORDER FROM:', bg = 'red').grid(row=1, column = 5)

button1 = Button(window, text="TABLES", bg="white", fg="black", width=20, font=("Times", 12), command=tables)
button2 = Button(window, text="CHAIRS", bg="white", fg="black", width=20, font=("Times", 12), command=chairs)
button3 = Button(window, text="OTTOMANS", bg="white", fg="black", width=20, font=("Times", 12), command=ottomans)
button4 = Button(window, text = "MATTRESSES",  bg="white", fg="black", width=20, font=("Times", 12), command=mattresses)
button5 = Button(window, text = "BEDS",  bg="white", fg="black", width=20, font=("Times", 12), command=beds)
button6 = Button(window, text = "SOFAS",  bg="white", fg="black", width=20, font=("Times", 12), command=sofa)
button7 = Button(window, text = "TV STANDS",  bg="white", fg="black", width=20, font=("Times", 12), command=tvstand)
button8 = Button(window, text = "VIEW CURRENT ORDER TOTAL", bg= 'white', fg= 'black', width=35, font=("Times", 12), command = currorder)
button9 = Button(window, text = "REMOVE ITEM FROM ORDER", bg = 'white', fg='black',width=30,font=("Times",12), command = removeitem)
button10 = Button(window, text = "CHANGE QUANTITY OF AN ITEM ORDERED", bg = 'white', fg='black',width=50,font=("Times",12), command = chgqty)
button11 = Button(window, text = "CHECKOUT", bg = 'white', fg='black',width=20,font=("Times",12), command = checkout)

button1.grid(row=4, column=4, padx=40, pady=10)
button2.grid(row=4, column=5, padx=40, pady=10)
button3.grid(row=4, column=6, padx=40, pady=10)
button4.grid(row=5, column=4, padx=40, pady=10)
button5.grid(row=5, column=5, padx=40, pady=10)
button6.grid(row=5, column=6, padx=40, pady=10)
button7.grid(row=6, column=4, padx=40, pady=10)
button8.grid(row=6, column=5, padx=40, pady=10)
button9.grid(row=6, column=6, padx=40, pady=10)
button10.grid(row=7,column=4, padx=40,pady=10)
button11.grid(row=7,column=5, padx=40,pady=10)

window.mainloop()
