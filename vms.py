from tkinter import *
from tkinter.messagebox import *
import re
from tkinter.scrolledtext import *
from tkinter import simpledialog
from sqlite3 import *
from datetime import datetime

root = Tk()
root.title("Visitor Management System")
root.geometry("900x800+400+10")
root.configure(bg="lightsteelblue")
f = ("Times New Roman", 30, "bold")
n = "navyblue"
l = "lightsteelblue"
b = "skyblue"

labtitle = Label(root,text="Visitor Management System",font=f,bg="deepskyblue")
labtitle.place(x=200,y=20)

def f1():
	admin.deiconify()
	root.withdraw()
	entuser.delete(0,END)
	entpassword.delete(0,END)


def f2():
	root.deiconify()
	admin.withdraw()
	entname.delete(0,END)
	entphone.delete(0,END)
	entin.delete(0,END)
	entout.delete(0,END)
	office.set(0)
	entname.focus()


def f4():
	admin.deiconify()
	view.withdraw()

def exit():
	answer = askyesno("Exit Confirmation","Are you sure you want to exit?")
	if answer:
		root.destroy()	


def validatename(name):
	if not name:
		showerror("ERROR!!", "Name field cannot be empty")
		entname.delete(0,END)
		return False
	if not name.isalpha():
		showerror("Error", "Name can only contain alphabetical characters")
		entname.delete(0,END)
		return False
	if not (2 <= len(name) <= 50):
		showerror("Error", "Name must be between 2 to 50 characters long")
		entname.delete(0,END)
		return False
	return True
		

def validatephone(phone):
	if not phone:
		showerror("Error", "Phone number field cannot be empty")
		entphone.delete(0,END)
		return False
	if not phone.isdigit():
		showerror("Error", "Phone number field cannot be empty")
		entphone.delete(0,END)
		return False
	if int(phone) < 0:
		showerror("Error", "Phone number cannot be negative")
		entphone.delete(0, END)
		return False
	if len(phone) != 10:
		showerror("Error", "Phone number must be exactly 10 digits long")
		entphone.delete(0,END)
		return False
	return True	
		
			
def validateintime():
	current_time = datetime.now().strftime('%H:%M:%S')
	entered_time = entin.get()

	if not entered_time :
		showerror("Error", "Please enter the time")
		return False

	if not re.match(r'^\d{2}:\d{2}:\d{2}$', entered_time):
		showerror("Error", "Please enter time in HH:MM:SS format")
		return False
	return True

def validateouttime():

	current_time = datetime.now().strftime('%H:%M:%S')
	entered_time = entout.get()

	if not entered_time :
		showerror("Error", "Please enter the time")
		return False

	if not re.match(r'^\d{2}:\d{2}:\d{2}$', entered_time):
		showerror("Error", "Please enter time in HH:MM:SS format")
		return False
	return True

def submit():
	name = entname.get()
	phone = entphone.get()
	in_time = entin.get()
	out_time = entout.get()
	selected_office = office.get()

	if validatename(name) and validatephone(phone) and validateintime():
		if not out_time:  
			showerror("Error", "Please provide the out-time")
			return
		if not validateouttime():  
			return
		if selected_office == 0: 
			showerror("Error", "Please select an office")
			return

		con = None
		try:
			con = connect("visitor.db")
			cursor = con.cursor()
			sql = "INSERT INTO visitor VALUES (?,?,?,?,?)"
			cursor.execute(sql,(name,phone,in_time,out_time,selected_office))
			con.commit()
			showinfo("Success", "Visitor details added successfully")
			entname.delete(0,END)
			entphone.delete(0,END)
			entin.delete(0,END)
			entout.delete(0,END)
			office.set(0)
			entname.focus()

		except Exception as e:
			con.rollback()
			showerror("Error", f"Error occurred: {str(e)}")
		finally:
			if con is not None:
				con.close()
			
def show():
	scrdata.delete(1.0,END)
	con = None
	try:
		con = connect("visitor.db")
		cursor = con.cursor()
		sql = "SELECT * FROM visitor"
		cursor.execute(sql)
		data = cursor.fetchall()
		info =""
		for d in data:
			info += f"Name: {d[0]} \tPhone: {int(d[1])} \tIn-time: {d[2]} \nOut-time: {d[3]} \tOffice No: {d[4]}\n"
		scrdata.insert("end",info)
	
	except Exception as e:
		showerror("Error",f"Error occurred:{str(e)}")
	finally:
		if con is not None:
			con.close()

def login():	
	username = "admin"
	password = "abc123"
	if entuser.get() == username and entpassword.get() == password:
		showinfo("Login Success","You successfully logged in.")
		view.deiconify()
		admin.withdraw()
		show()
		entuser.delete(0,END)
		entpassword.delete(0,END)

	else:
		showerror("ERROR","Invalid login.")
		entuser.delete(0,END)
		entpassword.delete(0,END)

def delete():
	con = None
	try:
		con = connect("visitor.db")
		cursor = con.cursor()
		phone = simpledialog.askstring("Input", "Enter visitor phone number to delete:")
		if phone:
			cursor.execute("SELECT * FROM visitor WHERE phone = ?", (phone,))
			row = cursor.fetchone()
			if row:
				confirmation = askyesno("Confirm Deletion", "Are you sure you want to delete the visitor record?")
				if confirmation:
					sql = "DELETE FROM visitor WHERE phone = ?"
					cursor.execute(sql, (phone,))
					con.commit()
					show() 
					showinfo("Success", "Visitor record deleted successfully.")
				else:
					showinfo("Cancelled", "Deletion cancelled.")
			else:
				showinfo("Not Found", "Visitor with the entered phone number does not exist.")
		else:
			showwarning("No Input", "Phone number cannot be empty.")
	except Exception as e:
		showerror("Error", e)
	finally:
		if con is not None:
			con.close()
	


labname = Label(root,text="Name :",font=f,bg=l,fg=n)
labname.place(x=130,y=100)
entname = Entry(root,font=f,width=20)
entname.place(x=270,y=100)

labphone = Label(root,text="Phone No. :",font=f,bg=l,fg=n)
labphone.place(x=60,y=170)
entphone = Entry(root,font=f,width=20)
entphone.place(x=270,y=170)


labin = Label(root,text="In Time :",font=f,bg=l,fg=n)
labin.place(x=80,y=240)
entin = Entry(root,font=f,width=20)
entin.place(x=270,y=240)

labout = Label(root,text="Out Time :",font=f,bg=l,fg=n)
labout.place(x=50,y=310)
entout = Entry(root, font=f, width=20)
entout.place(x=270,y=310)

labselect = Label(root,text="Select office:",font=f,bg=l,fg=n)
labselect.place(x=50,y=365)
office = IntVar()
office.set(0)

rb1 = Radiobutton(root,text="Office 1",font=f,bg=l,fg=n,variable=office,value=1)
rb1.place(x=300,y=390)
rb2 = Radiobutton(root,text="Office 2",font=f,bg=l,fg=n,variable=office,value=2)
rb2.place(x=300,y=450)
rb3 = Radiobutton(root,text="Office 3",font=f,bg=l,fg=n,variable=office,value=3)
rb3.place(x=300,y=500)
rb4 = Radiobutton(root,text="Office 4",font=f,bg=l,fg=n,variable=office,value=4)
rb4.place(x=300,y=550)
rb5 = Radiobutton(root,text="Office 5",font=f,bg=l,fg=n,variable=office,value=5)
rb5.place(x=300,y=600)

btnsubmit = Button(root,text="Submit",font=f,bg="Skyblue",command=submit)
btnsubmit.place(x=200,y=670)

btnadmin = Button(root, text="Admin Login", font=f, bg="skyblue", command=f1)
btnadmin.place(x=450, y=670)

admin = Toplevel(root)
admin.title("Admin login")
admin.geometry("900x800+400+10")
admin.configure(bg="lightsteelblue")
labtitle=Label(admin,text="Admin login",bg="deepskyblue",font=f)
labtitle.place(x=300,y=80)

labuser = Label(admin,text="Username :",font=f,bg=l,fg=n)
labuser.place(x=200,y=200)
entuser = Entry(admin,font=f,width=15)
entuser.place(x=400,y=200)

labpassword = Label(admin,font=f,text="Password :",fg=n,bg=l)
labpassword.place(x=200,y=300)
entpassword = Entry(admin,font=f,width=15,show="*")
entpassword.place(x=400,y=300)

btnlogin = Button(admin,text="Login",font=f,bg="skyblue",command=login)
btnlogin.place(x=340,y=400)
btnback = Button(admin,text="Back",font=f,bg="skyblue",command=f2)
btnback.place(x=340,y=500)

view = Toplevel(admin)
view.title("Admin login")
view.geometry("900x800+400+10")
view.configure(bg="lightsteelblue")
s=("Times New Roman",24,"bold")
labtitle=Label(view,text="Visitor's info",bg="deepskyblue",font=f)
labtitle.place(x=300,y=30)

scrdata = ScrolledText(view,width=53,height=15,font=s)
scrdata.place(x=20,y=100)
btnback = Button(view,text="Back",font=f,width=10,bg="skyblue",command=f4)
btnback.place(x=200,y=660)
btndel = Button(view,text="Delete",font=f,width=10,bg="skyblue",command = delete)
btndel.place(x=500,y=660)










root.protocol("WM_DELETE_WINDOW",exit)




root.mainloop()