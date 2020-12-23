from tkinter import *
from better_profanity import  profanity


class Slang:
    def __init__(self,root):
        self.root=root
        self.root.title("Slang Detector")
        self.root.geometry("500x360")
        self.root.iconbitmap("logo508.ico")
        self.root.resizable(0,0)


        def on_enter1(e):
            but_slang['background']="black"
            but_slang['foreground']="cyan"
            
            

        def on_leave1(e):
            but_slang['background']="SystemButtonFace"
            but_slang['foreground']="SystemButtonText"


        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
            
            

        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"


        def clear():
            text_input.delete('1.0',END)
            text_output.delete('1.0',END)


        def slangs():
            s=text_input.get('1.0',END)
            custom_words=["madarchot","bhenchot","chutya","chut",\
                "choot","Madarchot","Bhenchot","gand"]
            profanity.add_censor_words(custom_words)
            censored_text=profanity.censor(s)
            text_output.insert(END,censored_text)






#===================frame==========================#
        
        mainframe=Frame(self.root,width=500,height=360,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=150,relief="ridge",bd=3,bg="cyan")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=150,relief="ridge",bd=3,bg="cyan")
        secondframe.place(x=0,y=150)

        thirdframe=Frame(mainframe,width=494,height=55,relief="ridge",bd=3,bg="gray77")
        thirdframe.place(x=0,y=300)

#==========================button=========================#

        but_slang=Button(thirdframe,width=15,text="See Slangs",font=('times new roman',14),cursor="hand2",command=slangs)
        but_slang.place(x=60,y=5)
        but_slang.bind("<Enter>",on_enter1)
        but_slang.bind("<Leave>",on_leave1)




        but_clear=Button(thirdframe,width=15,text="Clear",font=('times new roman',14),cursor="hand2",command=clear)
        but_clear.place(x=270,y=5)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


#=========================firstframe=======================#
        
        text_input=Text(firstframe,width=53,height=6,font=('times new roman',14))
        text_input.place(x=3,y=5)

#==========================secondframe======================#
        text_output=Text(secondframe,width=53,height=6,font=('times new roman',14))
        text_output.place(x=3,y=5)



if __name__ == "__main__":
    root=Tk()
    Slang(root)
    root.mainloop()