from tkinter import *
import random
root=Tk()

root.title("Luck Friend:")
root.geometry("400x400")
root.configure(background="black")

lbl1=Label(root,text="Enter your friend's names:",bg="black",fg="pink",font=("Arial",18,"bold"))
lbl1.place(relx=0.5, rely=0.2,anchor=CENTER)

enter_name=Entry(root,font=("Arial",18,"bold"))
enter_name.place(relx=0.5,rely=0.3,anchor=CENTER)

lbl_friends=Label(root,font=("Arial",18,"bold"))
lbl_friends.place(relx=0.5,rely=0.5,anchor=CENTER)

Lucky_friend=Label(root,font=("Arial",18,"bold"))
Lucky_friend.place(relx=0.5, rely=0.8,anchor=CENTER)

list1=[]

def addfriend():
    friend_name=enter_name.get()
    list1.append(friend_name)
    lbl_friends["text"]="Your friend list is: "+str(list1)
    
enter=Button(root,text="Enter",command=addfriend,font=("Arial",18,"bold"))
enter.place(relx=0.5,rely=0.4,anchor=CENTER)

def randomFriend():
    l=len(list1)
    r=random.randint(0,l-1)
    print (r)
    Lucky_friend["text"]="Your Lucky Friend is: "+list1[r]
    
button=Button(root,text="Get your lucky friend",command=randomFriend,font=("Arial",18,"bold"))
button.place(relx=0.5, rely=0.6,anchor=CENTER)



root.mainloop()




