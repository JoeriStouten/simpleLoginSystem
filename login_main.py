from tkinter import *
root = Tk()

#set the lists for usernames and passwords as empty lists
userList = []
passwList = []
#i keeps track of the amount of users
i = 0

#printValue adds a username and a password to userList and passwList
def addToList():
    userList.append(user.get())
    passwList.append(passw.get())

#all the frames that are used
frame = Frame(root, bd=2, relief=RIDGE, width=500)
frame.grid(row=0, column=0)

frame2 = Frame(root, bd=2, relief=RIDGE, width=500)
frame2.grid(row=1, column=0, sticky=W)

frame3 = Frame(root, bd=2, relief=RIDGE, width=200)
frame3.grid(row=0, column=1, sticky=N)

#let the user know to register first
introText = Label(frame, text="Please register first.\n\nUsername:", justify=LEFT)
introText.pack(anchor=W)

#two entry fields for a username and a password
user = StringVar()
username = Entry(frame, textvariable=user, width=40)
username.pack(anchor=W)

userPassw = Label(frame, text="Password:")
userPassw.pack(anchor=W)

passw = StringVar()
password = Entry(frame, textvariable=passw, width=40)
password.pack()

#button to add user to the list
button = Button(frame, command=lambda:[addToList(), addUser()], text="Add")
button.pack()

#----------------------------------------------------------------------------------------------------------------------

#function to show the newly added user on the screen
def addUser():
    global i
    userLabel = Label(frame2, text=userList[i])
    userLabel.pack(anchor=W)
    print(userList)
    print(passwList)
    i += 1

registeredLabel = Label(frame2, text="\nRegistered users::", justify=LEFT)
registeredLabel.pack(anchor=W)

#----------------------------------------------------------------------------------------------------------------------

#function to show a new frame when the user has correctly logged in
def loginFrame():
    frame4 = Frame(root, bd=2,  relief=RIDGE, width=500)
    frame4.grid(row=0, column=0)
    lbl_loggedIn = Label(frame4, text="Logged in!")
    lbl_loggedIn.grid(row=0, column=0)

#the function to login. It will check wether the username is in the userList. If
#so, it will check the index in that list and compare it to the password of the
#same index in passwList. If it checks out, the frames will be removed and a
#message will show that the user is logged in. Else, it will give an error.

def login():
    global loginUsername
    global loginPassword
    if loginUsername.get() in userList and loginPassw.get() in passwList:
        indexUser = userList.index(loginUsername.get())
        indexPassw = passwList.index(loginPassword.get())
        if indexUser == indexPassw:
            print("Logged in!")
            frame.grid_forget()
            frame2.grid_forget()
            frame3.grid_forget()
            loginFrame()
        else:
            print("Username or password is incorrect")
    else:
        print("Username or password is incorrect")

#two entry fields for entering an existing username+password.
loginLabelUser = Label(frame3, text="\n\nLog in:")
loginLabelUser.pack()

loginUser = StringVar()
loginUsername = Entry(frame3, textvariable=loginUser, width=40)
loginUsername.pack(anchor=W)

loginLabelPassw = Label(frame3, text="Password:")
loginLabelPassw.pack(anchor=W)

loginPassw = StringVar()
loginPassword = Entry(frame3, textvariable=loginPassw, width=40)
loginPassword.pack()

#button to login, this will start the function login()
button = Button(frame3, text="Continue...", command=login)
button.pack()

root = mainloop()
