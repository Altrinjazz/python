import tkinter as tk
import sys

class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        toolbar = tk.Frame(self)
        toolbar.pack(side="top", fill="x")
        b1 = tk.Button(self, text="print logo", command=self.print_stdout)
        b1.pack(in_=toolbar, side="left")
        self.text = tk.Text(self, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)
        self.text.tag_configure("stderr", foreground="#b22222")

        sys.stdout = TextRedirector(self.text, "stdout")
        sys.stderr = TextRedirector(self.text, "stderr")

    def print_stdout(self):


        for i in range(20):
            for j in range (26):
                if (i==0 and j==12 or 
                i==1 and j==10 or
                i==1 and j==14 or
                i==2 and j==8 or
                i==2 and j==16 or 
                i==3 and j==6 or 
                i==3 and j==18 or
                i==4 and j==4 or
                i==4 and j==20 or 
                i==5 and j==2 or
                i==5 and j==22 or
                i==6 and j==0 or 
                i==6 and j==24 or 
                i==7 and j==2 or 
                i==7 and j==22 or 
                i==8 and j==4 or 
                i==8 and j==20 or 
                #i==9 and j==6 or
                i==9 and j==18 or
                i==10 and j==8 or
                i==10 and j==16 or
                i==11 and j==10 or
                i==11 and j==14 or
                i==12 and j==12 or 
        
                i==4 and j==12 or 
                i==5 and j==10 or
                i==5 and j==14 or
                i==6 and j==8 or
                i==6 and j==16 or 
                i==7 and j==6 or 
                #i==7 and j==18 or
                i==8 and j==4 or
                i==8 and j==20 or 
                i==9 and j==2 or
                i==9 and j==22 or
                i==10 and j==0 or 
                i==10 and j==24 or 
                i==11 and j==2 or 
                i==11 and j==22 or 
                i==12 and j==4 or 
                i==12 and j==20 or 
                i==13 and j==6 or
                i==13 and j==18 or
                i==14 and j==8 or
                i==14 and j==16 or
                i==15 and j==10 or
                i==15 and j==14 or
                i==16  and j==12 or 
        
                i==9 and j==10 or 
                i==7 and j==14):
                    print('*',end='')
                else:
                    print('',end=' ')
            print()



class TextRedirector(object):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")

app = ExampleApp()
app.mainloop()