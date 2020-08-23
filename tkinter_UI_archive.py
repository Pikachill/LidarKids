from tkinter import *
from tkinter import filedialog

# Main GUI window
root = Tk()

udid = StringVar(None, ' ')
mode = StringVar(None, ' ')
#threshold = IntVar()

# Title
Label(root,text= 'Aggregated Data Report').grid(row=0,column=0,columnspan=3,sticky='w')
Label(text='').grid(row=1,column=0)

# UDID selection
uLabel = Label(root, text='Choose Intersection:')
uLabel.grid(row=2, column=0, sticky='w')
u1 = Radiobutton(root, text='Bernard Ave. & Pandosy St.', variable=udid, value='BCT_3D_5G_0101001')
u1.grid(row=3, column=0, sticky='w',padx=10)
u2 = Radiobutton(root, text='Bernard Ave. & Water St.', variable=udid, value='BCT_3D_5G_0101002')
u2.grid(row=4, column=0, sticky='w',padx=10)

# Mode Selection
Label(root, text='Mode Selection:').grid(row=5,column=0,sticky='w')
m1 = Radiobutton(root, text='Simplified', variable=mode, value='simplified')
m1.grid(row=6,column=0,padx=10, sticky='w')
m2 = Radiobutton(root, text='Custom', variable=mode, value='custom')
m2.grid(row=7,column=0,padx=10, sticky='w')


# Date range input

Label(root, text='Enter start and end date').grid(row=8,column=0,sticky='w')
d1 = Entry(root)
d1.grid(row=9,column=0,pady=10, sticky='ew')
d2 = Entry(root)
d2.grid(row=10,column=0,pady=10, sticky='ew')

confirmButton = Button(root, text='Confirm', command=query).grid(row=11,column=0,sticky='w')

root.mainloop()