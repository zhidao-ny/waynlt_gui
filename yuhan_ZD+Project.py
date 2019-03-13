
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

from PIL import Image, ImageTk  


# In[13]:


###create a window titled GUI START
#create instance
ZD = tk.Tk()

#add a title
ZD.title("ZHIDAO CAREER SEARCH")

#fig = plt.figure()

# Add logo
image = Image.open("zhidaopic1.gif")
photo = ImageTk.PhotoImage(image, master = ZD)
label = tk.Label(ZD, image=photo)
label.image = image
label.place(x=50,y=30,relx = 0.45, rely = 0.15 ,anchor = CENTER)



#adding a Lable
#a_label = ttk.Label(ZD, text = "ZHIDAO").pack(side = 'left', anchor = N)#grid(column = 0, row = 0)


##Modified Button Click Function
#def click_me():
#    action.configure(text = "Search" + name.get() + '' + number_chosen.get())
#    
##Changing our Label
#ttk.Label(ZD, text = "Enter Your Search1:").pack(side='left', anchor = CENTER)#grid(column = 0, row = 0,sticky=E+W+N+S, pady=5)
#
## Adding a Textbox Entry widget
#name = tk.StringVar()
#name_entered = ttk.Entry(ZD, width = 12, textvariable = name).pack(side='left', anchor = CENTER)#grid(column = 0, row = 1,sticky=E+W+N+S, pady=5)
#
#
#ttk.Label(ZD, text = "Choose an Industry:").pack(side = 'left', anchor = CENTER)#grid(column = 1, row = 0)
#number = tk.StringVar()
#number_chosen = ttk.Combobox (ZD, width = 12, textvariable = number, state = 'readonly') #??? What readonly 
#number_chosen['values'] = ("Finace","IT","Internet","Manufacturing","Entertainment & Media","Education") # what does [] mean?
#number_chosen.pack(side = 'left')#grid(column = 1, row = 1)
#number_chosen.current(0) #What does chosen.current mean?
#
##Adding a Button
#def printIndustry():
#    print("industry button clicked!!!")
#action = ttk.Button(ZD, text = "Search", command = printIndustry).pack(side = 'left', anchor = CENTER)#grid(column = 2, row = 1)
## ?? What does click_me as a command mean?Is it necessary to take notes in order to remember the functions?


### Adding search for Skills

#Modified Button Click Function
def click_me2():
    action.configure(text = "Search" + name.get() + '' + number_chosen.get())
    
#Changing our Label 2
ttk.Label(ZD, text = "Enter Your Search1:").pack(side = 'left', anchor = CENTER)#grid(column = 0, row = 3)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(ZD, width = 12, textvariable = name).pack(side = 'left', anchor = CENTER)#grid(column = 0, row = 4)

ttk.Label(ZD, text = "Choose an skillset:").pack(side = 'left', anchor = CENTER)#grid(column = 1, row = 3)
number = tk.StringVar()
number_chosen = ttk.Combobox (ZD, width = 12, textvariable = number, state = 'readonly') #??? What readonly 
number_chosen['values'] = ("Skill A","Skill B","Skill C","Skill D","Skill E","Skill F") # what does [] mean?
number_chosen.pack(side = 'left', anchor = CENTER)#grid(column = 1, row = 4)
number_chosen.current(0) #What does chosen.current mean?


#Adding a Button
action = ttk.Button(ZD, text = "Search", command = print("hello Skillset")).pack(side = 'left', anchor = CENTER)#grid(column = 2, row = 4)


## Adding search for Company

#Modified Button Click Function
def click_me3():
    action.configure(text = "Search" + name.get() + '' + number_chosen.get())
    
#Changing our Label 2
ttk.Label(ZD, text = "Enter Your Search2:").pack(side = 'left', anchor = CENTER)#grid(column = 0, row = 5)

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(ZD, width = 12, textvariable = name).pack(side = 'left', anchor = CENTER)#grid(column = 0, row = 6)


ttk.Label(ZD, text = "Choose an company:").pack(side = 'left', anchor = CENTER)#grid(column = 1, row = 5)
number = tk.StringVar()
number_chosen = ttk.Combobox (ZD, width = 12, textvariable = number, state = 'readonly') #??? What readonly 
number_chosen['values'] = ("Comapny A","Company B","Comapany C","Company D","Company E","COmpany F") # what does [] mean?
number_chosen.pack(side = 'left', anchor = CENTER)#grid(column = 1, row = 6)
number_chosen.current(0) #What does chosen.current mean?

#Adding a Button
action = ttk.Button(ZD, text = "Search", command = print("hello company")).pack(side = 'left', anchor = CENTER)#grid(column = 2, row = 6)

ZD.mainloop()




