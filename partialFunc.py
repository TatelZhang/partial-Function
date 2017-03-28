from functools import partial
from tkinter import Tk, Button, X, messagebox




WARN = "warn"
CRIT = "crit"
REGU = "regu"

SIGNS = {
    "don't enter": CRIT,
    "railroad crossing": WARN,
    "55\nspeed limit": REGU,
    "wrong way": CRIT,
    "merging traffic": WARN,
    "onr way": REGU,
}

critCB = lambda: messagebox.showerror('Error', 'Error Button Pressed')
warnCB = lambda: messagebox.showwarning('Warning', "Warning Button Pressed!")
infoCB = lambda: messagebox.showinfo('Info', 'Info Button Pressed!')


top = Tk()
top.title("road signs")
Button(top, text="QUIT", command=top.quit, bg="red", fg='white').pack()


MyButton = partial(Button, top)
CritButton = partial(MyButton, command=critCB, bg='white', fg="red")
WarnButton = partial(MyButton, command=warnCB, bg="goldenrod1")
ReguButton = partial(MyButton,command =infoCB, bg ='white')

buttons =[CritButton, WarnButton, ReguButton]

'''
for button in buttons:
    button.__call__()
'''
'''
for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=True)' % (signType.title(), eachSign, '.upper()'if signType = CRIT else'.title()')
    
    eval(cmd)
'''
top.mainloop()