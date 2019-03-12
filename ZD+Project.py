
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext


# In[13]:


###create a window titled GUI START
#create instance
ZD = tk.Tk()

#add a title
ZD.title("ZHIDAO CAREER SEARCH")

#adding a Lable
a_label = ttk.Label(ZD, text = "ZHIDAO").grid(column = 0, row = 0)

#Modified Button Click Function
def click_me():
    action.configure(text = "Search" + name.get() + '' + number_chosen.get())
    
#Changing our Label
ttk.Label(ZD, text = "Enter Your Search1:").grid(column = 0, row = 0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(ZD, width = 12, textvariable = name).grid(column = 0, row = 1)

#Adding a Button
def printIndustry():
    print("industry button clicked!!!")
action = ttk.Button(ZD, text = "Search", command = printIndustry).grid(column = 2, row = 1)
# ?? What does click_me as a command mean?Is it necessary to take notes in order to remember the functions?

ttk.Label(ZD, text = "Choose an Industry:").grid(column = 1, row = 0)
number = tk.StringVar()
number_chosen = ttk.Combobox (ZD, width = 12, textvariable = number, state = 'readonly') #??? What readonly 
number_chosen['values'] = ("Finace","IT","Internet","Manufacturing","Entertainment & Media","Education") # what does [] mean?
number_chosen.grid(column = 1, row = 1)
number_chosen.current(0) #What does chosen.current mean?

## Adding search for Skills

#Modified Button Click Function
def click_me2():
    action.configure(text = "Search" + name.get() + '' + number_chosen.get())
    
#Changing our Label 2
ttk.Label(ZD, text = "Enter Your Search2:").grid(column = 0, row = 3)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(ZD, width = 12, textvariable = name).grid(column = 0, row = 4)

#Adding a Button
action = ttk.Button(ZD, text = "Search", command = print("hello Skillset")).grid(column = 2, row = 4)

ttk.Label(ZD, text = "Choose an skillset:").grid(column = 1, row = 3)
number = tk.StringVar()
number_chosen = ttk.Combobox (ZD, width = 12, textvariable = number, state = 'readonly') #??? What readonly 
number_chosen['values'] = ("Skill A","Skill B","Skill C","Skill D","Skill E","Skill F") # what does [] mean?
number_chosen.grid(column = 1, row = 4)
number_chosen.current(0) #What does chosen.current mean?

## Adding search for Company

#Modified Button Click Function
def click_me3():
    action.configure(text = "Search" + name.get() + '' + number_chosen.get())
    
#Changing our Label 2
ttk.Label(ZD, text = "Enter Your Search3:").grid(column = 0, row = 5)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(ZD, width = 12, textvariable = name).grid(column = 0, row = 6)

#Adding a Button
action = ttk.Button(ZD, text = "Search", command = print("hello company")).grid(column = 2, row = 6)

ttk.Label(ZD, text = "Choose an skillset:").grid(column = 1, row = 5)
number = tk.StringVar()
number_chosen = ttk.Combobox (ZD, width = 12, textvariable = number, state = 'readonly') #??? What readonly 
number_chosen['values'] = ("Comapny A","Company B","Comapany C","Company D","Company E","COmpany F") # what does [] mean?
number_chosen.grid(column = 1, row = 6)
number_chosen.current(0) #What does chosen.current mean?

ZD.mainloop()




# In[69]:


###create a window titled GUI START
#create instance
win = tk.Tk()

#add a title
win.title("GUI START")

#adding a Lable
a_label = ttk.Label(win, text = "A LABEL").grid(column = 0, row = 0)

#Modified Button Click Function
def click_me():
    action.configure(text = "Hello" + name.get() + '' + number_chosen.get())

#Changing our Label
ttk.Label(win, text = "Enter Your Search:").grid(column = 0, row = 0)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width = 12, textvariable = name).grid(column = 0, row = 1) #?? what is textvariable? 

#Adding a Button
action = ttk.Button(win, text = "Click Me!", command = print("hello world")).grid(column = 2, row = 1)
# ?? What does click_me as a command mean?Is it necessary to take notes in order to remember the functions?

# Creating 3 Checkbuttons
ttk.Label(win, text = "Choose a number:").grid(column = 1, row = 0)
number = tk.StringVar()
number_chosen = ttk.Combobox (win, width = 12, textvariable = number, state = 'readonly') #??? What readonly 
number_chosen['values'] = (1,2,4,42,100) # what does [] mean?
number_chosen.grid(column = 1, row = 1)
number_chosen.current(0) #What does chosen.current mean?

# what is thissss??
chVarDis = tk.IntVar() # What does this IntVar mean?
check1 = tk.Checkbutton(win, text = "Disabled", variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column = 0, row = 4, sticky = tk.W) #??what does sticky mean??

chVarUn = tk.IntVar() 
check2 = tk.Checkbutton(win, text = "UnChecked", variable = chVarUn)
check2.deselect()
check2.grid(column = 1, row = 4, sticky = tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text = "Enable", variable = chVarEn)
check3.deselect()
check3.grid(column = 2, row = 4, sticky = tk.W)

#GUI Callback function 
def checkCallback(*ignoredArgs): #(?? what is *ignoredArgs?? )
    #only enable one checkbutton
    if chVarUn.get():check3.configure(state = "disabled")
    else: check3.configure(state = 'normal')
    if chVarEn.get(): check2.configure (state = 'disabled')
    else: check2.configure(state = 'normal')
        
# ??trace the state of the 2 checkbuttons  # ?? what issss thissss??
chVarUn.trace('w', lambda unused0, unused1, unused2: checkCallback())
chVarEn.trace('w', lambda unused0, unused1, unused2: checkCallback())

# ??first, we change our Radiobutton global variables into a list # ??? what is this???
colors = ["Blue", "Glod", "Red"]

# ??we have also changed the callback function to be zero-based, using the list 
#instead of module-level global variables
#Radiobutton Callback
def radCall():
    radSel = radVar.get()
    if radSel == 0: win.configure(background = colors[0])  # now zero-based
    elif radSel == 1: win.configure(background = colors[1]) # and using list
    elif radSel == 2: win.configure(background = colors[2])

# ??create 3 Radiobuttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar
radVar.set(99)

#Now we are creating all 3 Radiobutton widgets within one loop

for col in range(3):
    curRad = tk.Radiobutton (win, text = colors[col], variable = radVar, value = col, command = radCall)
    curRad.grid(column = 0, row = 5, sticky = tk.W)

# Using a scrolled Text control
scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width = scrol_w, height = scrol_h, wrap = tk.WORD).grid(column = 0, columnspan =3)



win.mainloop()


# In[36]:





# In[12]:






