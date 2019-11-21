from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

# ==============================FrontEnd======================================


class Root(Tk):
	def __init__(self,*args,**kwargs):
		Tk.__init__(self, *args, **kwargs)

		self.title('Diet Plan')
		self.geometry('800x500')
		self.minsize(800,500)

		container = Frame(self,bg="#010a1a") 
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		#=================Menubar================

		menubar =Menu(self)	#Telling root that we have a menubar for you
		self.config(menu=menubar)	#Configuring roo to hae the menu as the menubar told before

		#submenues
		subMenu = Menu(menubar, tearoff=False)	#adding a new menu

		#adding cascade
		menubar.add_cascade(label="File", menu=subMenu)	#adding menu name

		#adding drop down list
		subMenu.add_command(label="Open")	#adding option in dropdown
		subMenu.add_command(label='Exit')	#adding option in dropdown

		#adding help
		subMenu = Menu(menubar, tearoff=False)
		menubar.add_cascade(label ='Help', menu = subMenu)

		#adding drop down
		subMenu.add_command(label='About Us')

		

		# ===============Adding Frames===============
		
		self.frames = {}

		for F in (Home,Login,StylesList):
			frame = F(container, self)
			self.frames[F]=frame
			# frame.pack(fill="both", expand=True)
			frame.grid(row=0, column=0, sticky='nsew')
		self.show_frame(Home)
		
	def show_frame(self,f):
		frame = self.frames[f]
		frame.tkraise()





class Home(Frame):
	"""This is the landing page this will contain the overview of all the styles and the graphs related to it"""
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,bg="#03183b")	# dark blue --> #03183b light blue --> #14477d
		self.controller = controller
		self.parent = parent
		
		self.grid_columnconfigure(0,weight=1)
		self.grid_columnconfigure(1,weight=10)
		self.grid_rowconfigure(1, weight=1)


		self.Logo_fr = Frame(self, padx=10, bd=2, pady=10, relief=RIDGE, bg="#1e2057")
		self.Logo_fr.grid(row=0, column=0, padx=1, pady=1, columnspan=2, sticky="nsew")

		self.sidebar_fr = Frame(self, padx=1, bd=2, pady=1, relief=RIDGE, bg="#1e2057")
		self.sidebar_fr.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")

		self.graphs_fr = Frame(self, padx=1, bd=2, pady=1, relief=RIDGE, bg="#291e57")
		self.graphs_fr.grid(row=1, column=1, padx=1, pady=1, sticky="nsew")
		self.graphs_fr.grid_rowconfigure(0, weight=1)
		self.graphs_fr.grid_rowconfigure(1, weight=1)
		self.graphs_fr.grid_columnconfigure(0, weight=1)
		self.graphs_fr.grid_columnconfigure(1, weight=1)


		# Logo Frame Widgets
		self.loginbtn = Button(self.Logo_fr,text ="Login", font=('arial',8,'bold'), height=1, width=10, bd=2, bg = "#eb4034" ,command = lambda:controller.show_frame(Login))
		self.loginbtn.pack(side="right")


		# Sidebar Frame widgets
		self.btn1 = Button(self.sidebar_fr,text ="Button 1", font=('arial',10,'bold'), height=1, width=20, bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn1.pack(side="top", padx=1, fill="both")

		self.btn2 = Button(self.sidebar_fr,text ="Button 2", font=('arial',10,'bold'), height=1, width=16, bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn2.pack(side="top",  padx=1, fill="both")

		self.btn3 = Button(self.sidebar_fr,text ="Button 3", font=('arial',10,'bold'), height=1, width=16, bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn3.pack(side="top", padx=1, fill="both")

		self.btn4 = Button(self.sidebar_fr,text ="Button 4", font=('arial',10,'bold'), height=1, width=16, bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn4.pack(side="top", padx=1, fill="both")



		# Graph Frame widgets

		# Frames to hold the value 
		self.photo_1 = ImageTk.PhotoImage(Image.open("first_plot.jpg").resize((250,250),Image.ANTIALIAS))
		self.graph_1 = Label(self.graphs_fr, bd=1, image=self.photo_1)
		self.graph_1.grid(row=0, column=0, padx=2,pady=2, sticky="nsew")

		self.photo_2 = ImageTk.PhotoImage(Image.open("second_plot.jpg").resize((250,250),Image.ANTIALIAS))		# tkinter work only with gif and png images
		self.graph_2 = Label(self.graphs_fr, bd=1, image=self.photo_2)
		self.graph_2.grid(row=1, column=0, padx=2,pady=2, sticky="nsew")

		self.photo_3 = ImageTk.PhotoImage(Image.open("first_plot.jpg").resize((250,250),Image.ANTIALIAS))
		self.graph_3 = Label(self.graphs_fr, bd=1, image=self.photo_3)
		self.graph_3.grid(row=0, column=1, padx=2,pady=2, sticky="nsew")

		self.photo_4 = ImageTk.PhotoImage(Image.open("second_plot.jpg").resize((250,250),Image.ANTIALIAS))
		self.graph_4 = Label(self.graphs_fr, bd=1, image=self.photo_4)
		self.graph_4.grid(row=1, column=1, padx=2,pady=2, sticky="nsew")




class Login(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,bg="#03183b")	#red-- #eb4034
		self.controller = controller
		self.parent = parent

		self.loginFrame = Frame(self, padx=40, pady=10, relief=RIDGE, bg='#28326b')
		self.loginFrame.pack(expand=True)

		self.hdng_lbl = Label(self.loginFrame, text ="LOGIN",font=('Helvetica',18), fg = "#abb1cf" ,bg = "#28326b")	
		self.hdng_lbl.pack(side = "top", expand=True, pady=20) 		# grid(row=0, column=0, sticky='ew', padx = 10, pady = 10)

		self.username = StringVar()
		self.password = StringVar()

		self.usrnm_lbl = Label(self.loginFrame, text ="Username",font=('Helvetica',10), fg = "#abb1cf" ,bg = "#28326b")	
		self.usrnm_lbl.pack(expand=True)  	# grid(row=0, column=0, sticky='nsew', padx = 10, pady = 10)

		self.usrnm_entry = Entry(self.loginFrame, width = 30, textvariable=self.username)	
		self.usrnm_entry.pack(expand=True)

		# empty lablel to adjust spacing
		self.empty_lbl = Label(self.loginFrame, height=1, bg = "#28326b")	
		self.empty_lbl.pack(expand=True,pady=0.1) 

		self.pswd_lbl = Label(self.loginFrame, text ="Password",font=('Helvetica',10), fg = "#abb1cf" ,bg = "#28326b")	
		self.pswd_lbl.pack(expand=True) 

		self.pswd_entry = Entry(self.loginFrame, width = 30, show="*", textvariable=self.password)	
		self.pswd_entry.pack(expand=True)

		# empty lablel to adjust spacing
		self.empty_lbl = Label(self.loginFrame, height=1, bg = "#28326b")	
		self.empty_lbl.pack(expand=True,pady=0.1) 

		self.loginbtn = Button(self.loginFrame,text ="Login", font=('arial',12,'bold'), height=1, width=8, bd=2,fg ="white", bg = "#616df2" , command = self.get_ID)
		self.loginbtn.pack(side = "left", pady=10)

		self.homebtn = Button(self.loginFrame,text ="Go Back", font=('arial',12,'bold'), height=1, width=8, bd=2,fg ="white", bg = "#616df2" , command = lambda:controller.show_frame(Home))
		self.homebtn.pack(side = "right", pady=10)


	def get_ID(self):
		print(self.username.get())
		print(self.password.get())
		self.controller.show_frame(StylesList)



class StylesList(Frame):
	def __init__(self,parent,controller):
		Frame.__init__(self,parent,bg="#03183b")	#red-- #eb4034
		self.controller = controller
		self.parent = parent

		# Frames

		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=2)
		self.grid_rowconfigure(2, weight=100)

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=5)

		self.sidebar_fr = Frame(self, bd=1, padx=4, pady=1, relief=RIDGE, bg='#2f3b57')
		self.sidebar_fr.grid(row=0,column=0, rowspan=3,sticky='nsew')

		self.btns_fr = Frame(self, bd=1, padx=4, pady=1, relief=RIDGE, bg='#28326b')
		self.btns_fr.grid(row=0,column=1,sticky='nsew')
		# self.btns_fr.grid_columnconfigure(0, weight=1)
		# self.btns_fr.grid_columnconfigure(1, weight=1)
		# self.btns_fr.grid_columnconfigure(2, weight=1)
		# self.btns_fr.grid_columnconfigure(3, weight=1)
		# self.btns_fr.grid_columnconfigure(4, weight=1)
		# self.btns_fr.grid_columnconfigure(5, weight=1)
		# self.btns_fr.grid_columnconfigure(6, weight=1)
		# self.btns_fr.grid_columnconfigure(7, weight=1)
		# self.btns_fr.grid_columnconfigure(8, weight=1)
		# self.btns_fr.grid_columnconfigure(9, weight=1)
		# self.btns_fr.grid_columnconfigure(10, weight=1)


		self.details_fr = Frame(self, bd=1, padx=4, pady=1, relief=RIDGE, bg='#28326b')
		self.details_fr.grid(row=1,column=1, sticky='nsew')

		self.list_fr = Frame(self, bd=1, padx=4, pady=1, relief=RIDGE, bg='#28326b')
		self.list_fr.grid(row=2,column=1, sticky='nsew')
		self.list_fr.grid_rowconfigure(0, weight=1)
		self.list_fr.grid_rowconfigure(1, weight=10)


		# widgets


		# ===================================Sidebar Widgets=================================

		self.logo_lbl = Label(self.sidebar_fr, height=2, text ="LOGO", font=('arial',12,'bold'), bd=2,fg ="white", bg = "red")	
		self.logo_lbl.pack(fill="x") 

		#creating a search frame allows to align things properly in that frame only
		self.srch_fr = Frame(self.sidebar_fr, bg='#2f3b57')
		self.srch_fr.pack(pady=5, fill="x")
		self.srch_fr.grid_columnconfigure(0, weight=2)
		self.srch_fr.grid_columnconfigure(1, weight=1)

		self.srch = StringVar()
		self.srch_entry = Entry(self.srch_fr, textvariable=self.srch)	
		self.srch_entry.grid(row=0, column=0,padx=1, sticky='nsew')				# pack(side = "left" , pady=1, fill="x")

		self.search = Button(self.srch_fr,text ="S", font=('arial',12,'bold'), fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.search.grid(row=0, column=1, padx=2, sticky='nsew')				# pack(side = "right" , pady=1, fill="x")
 

		self.btn2 = Button(self.sidebar_fr,text ="Button 2", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn2.pack(pady=1, fill="x")

		self.btn3 = Button(self.sidebar_fr,text ="Button 3", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn3.pack(pady=1, fill="x")

		self.btn4 = Button(self.sidebar_fr,text ="Button 4", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn4.pack(pady=1, fill="x")

		self.btn5 = Button(self.sidebar_fr,text ="Button 5", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn5.pack(pady=1, fill="x")

		self.btn6 = Button(self.sidebar_fr,text ="Button 6", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn6.pack(pady=1, fill="x")

		self.btn7 = Button(self.sidebar_fr,text ="Button 7", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn7.pack(pady=1, fill="x")

		self.btn8 = Button(self.sidebar_fr,text ="Button 8", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn8.pack(pady=1, fill="x")

		self.btn9 = Button(self.sidebar_fr,text ="Button 9", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn9.pack(pady=1, fill="x")

		self.btn10 = Button(self.sidebar_fr,text ="Button 10", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn10.pack(pady=1, fill="x")




		#===================================Top Button Widgets=================================================================

		self.btn1 = Button(self.btns_fr,text ="Button 1", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn1.pack(side="left",expand=True, padx=1, fill="both")

		self.btn2 = Button(self.btns_fr,text ="Button 2", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn2.pack(side="left",expand=True,  padx=1, fill="both")

		self.btn3 = Button(self.btns_fr,text ="Button 3", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn3.pack(side="left",expand=True, padx=1, fill="both")

		self.btn4 = Button(self.btns_fr,text ="Button 4", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn4.pack(side="left",expand=True, padx=1, fill="both")

		self.btn5 = Button(self.btns_fr,text ="Button 5", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn5.pack(side="left",expand=True, padx=1, fill="both")

		self.btn6 = Button(self.btns_fr,text ="Button 6", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn6.pack(side="left",expand=True, padx=1, fill="both")

		self.btn7 = Button(self.btns_fr,text ="Button 7", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn7.pack(side="left",expand=True, padx=1, fill="both")

		self.btn8 = Button(self.btns_fr,text ="Button 8", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn8.pack(side="left",expand=True, padx=1, fill="both")

		self.btn9 = Button(self.btns_fr,text ="Button 9", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn9.pack(side="left",expand=True, padx=1, fill="both")

		self.btn10 = Button(self.btns_fr,text ="Button 10", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn10.pack(side="left",expand=True, padx=1, fill="both")





		# =======================================lower Button Frame==========================================

		self.btn1 = Button(self.details_fr,text ="Button 1", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn1.pack(side="left",expand=True, padx=1, fill="both")

		self.btn2 = Button(self.details_fr,text ="Button 2", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn2.pack(side="left",expand=True,  padx=1, fill="both")

		self.btn3 = Button(self.details_fr,text ="Button 3", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn3.pack(side="left",expand=True, padx=1, fill="both")

		self.btn4 = Button(self.details_fr,text ="Button 4", font=('arial',12,'bold'), bd=2, fg ="white", bg = "#616df2" ) 	# , command = self.get_ID)
		self.btn4.pack(side="left",expand=True, padx=1, fill="both")




		# ==========================================List Frame================================================

		#use Tree View

		self.style_lbx = Listbox(self.list_fr, font=('Verdana',16))
		self.style_lbx.pack(side=LEFT,fill="both",expand=True)
		self.style_sbr = Scrollbar(self.list_fr,)
		self.style_sbr.pack(side=RIGHT,fill="both")
		self.style_sbr.config(command= self.style_lbx.yview)
		self.style_lbx.config(yscrollcommand=self.style_sbr.set)







app = Root()
app.mainloop()











































