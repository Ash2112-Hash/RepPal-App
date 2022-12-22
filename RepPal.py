# Ashwin Unnithan
# RepPal - the assitative exercise app which controls an automated bicep/hamstring curler (regulated by a raspberry PI)
# Last Updated: 2022/07/09

"""
# Imports classes from the gpiozero module
from gpiozero import Motor      # imports the Motor class
from gpiozero import Button as gpiozeroButton   #Imports the Button class
"""

from tkinter import * #Imports all elements from the tkinter module
import time #imports the time module
import sys
import tkinter # imports the sys module

"""
def move_motor(op_time,motor): # defines the function: move_motor to activate and move the actuator
    # function accepts a time and a actuator object as parameters to move the components forward and backward in cycles 
    motor.forward()
    time.sleep(op_time)
    motor.backward()
    time.sleep(op_time)
    motor.stop()


def rep_time(motor_time, motor, btn, rep_count): # defines the function: rep_time to move the actuator based on the amount of reps entered by user
    # The function accepts a specfied time, motor object, btn object and rep_count, the function moves the acuator based on the reps entered and allows user to exit the exercise once the button is held for the time of a single rep(9 seconds)
    print("\n", "To stop the workout after a rep, press and hold the button")
    time.sleep(2)

    for i in range(3,0, -1):
        print(i)
        time.sleep(1)
    stop_count=0
    print("\n")

    while stop_count < rep_count:
        move_motor(motor_time, motor)
        stop_count +=1
        if btn.is_pressed == True:
            stop_count = rep_count
            print("The button has been pressed")
    
    print("Your workout has finished")


def run_op(reps):  # defines the function: rep_ops to move to run the above functions and commence the start of the program
    # function accepts a specified amount of reps from user, initiates a actuator and button class and executes previos functions for the exercise regiment

    print("Press the button to set up your workout!")
    actuator = Motor(12,16) # acuator objects connected to pins 12 and 16
    button = gpiozeroButton(7) # button object connected to pin 7

    # Executes the exercise regiment and checks for errors
    try: 
        button.wait_for_press()

        rep_time(9,actuator, button, reps)

    except:
        print("An invalid input was entered. Reload the app!")
"""


def add_account_info(data):
    prompts = ["Username: ", "Email: ", "Password: "]
    id = 0
    with open("user_data.txt", "a") as user_file:
        user_file.seek(0, 2)
        for elm in data:
            user_file.write(prompts[id] + elm + "\t")
            id+=1
        user_file.write("\n")


def calories_burned(MET, duration, body_weight): # defines the function: calories_burned to calculate the amount of calories burned during bicep or hamstring excercise
    cals = (MET*body_weight)*(duration/60)
    return cals


def Stats(Rep_Data, selection_fct): # defines the function: Stats to display the stats page and the amount of reps completed
    try:
        ##### Initiates the tkinter window and its properties #####
        window = Tk()
        window.title("RepPal")
        window.geometry("360x800")
        window.configure(bg = "#29272f")
        canvas = Canvas(
            window,
            bg = "#29272f",
            height = 800,
            width = 360,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)
        mono = Text(window, height = 100000)
        mono.configure(font = ("Monotxt_IV50",1000,"bold"))
        #####

        ##### Defines the textboxes and images for the page ######
        background_img = PhotoImage(file = f"bg_4.png")
        background = canvas.create_image(
            190.0, 383.5,
            image=background_img)

        
        if selection_fct == "bicep":
            cals_burned = calories_burned(3, 60, 70)
            
            label0 = Label(
            bd = 0,
            bg = "#2f353d",
            highlightthickness= 0,
            fg = "white",
            font = mono,
            text= str(Rep_Data) + " Reps" + "\n \n" + str(cals_burned) +  " Cals Burned")

            label0.place(
                x = 29, y = 287,
                width = 130,
                height = 55)
        
        else:
            cals_burned = calories_burned(4, 60, 70)
            label1 = Label(
            bd = 0,
            bg = "#2f353d",
            highlightthickness= 0,
            fg = "white",
            font = mono,
            text= str(Rep_Data) + " Reps" + "\n \n" + str(cals_burned) + " Cals Burned")

            label1.place(
                x = 200, y = 287,
                width = 130,
                height = 55)  

        window.resizable(False, False)
        window.mainloop()

    except:
        error_win = Tk()
        
        error_win.geometry("360x800")
        
        # Create text widget and specify size.
        T = Text(error_win, height = 5, width = 52)
        
        # Create label
        l = Label(error_win, text = "Unexpected Error")
        l.config(font =("Courier", 14))
        
        error_msg = "Unknown or incorrect value entered. Reload RepPal"
        
        # Create button for next text.
        b1 = Button(error_win, text = "Next", )
        
        # Create an Exit button.
        b2 = Button(error_win, text = "Exit", command = error_win.destroy)
        
        l.pack()
        T.pack()
        b1.pack()
        b2.pack()
        
        # Insert The Fact.
        T.insert(tkinter.END, error_msg)
        
        error_win.mainloop()
        print("Unknown or incorrect value entered. Reload RepPal")
        # displayed if user enters a incorrect value



def Workout(): # defines the function: Workout to display the workout options and allow user to enter reps

    try:

        ##### Initiates the tkinter window and its properties #####
        window = Tk()
        window.title("RepPal")
        window.geometry("360x800")
        window.configure(bg="#29272f")
        canvas = Canvas(
            window,
            bg="#29272f",
            height=800,
            width=360,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)
        ######

        def bicep_clicked(): # defines function to close the window once the bicep button is clicked
            selection = "bicep"
            window.destroy()
            Stats(reps.get(), selection)
            run_op(reps.get())


        def hamstring_clicked(): # defines function to close the window once the bicep button is clicked
            selection = "hamstring"
            window.destroy()
            Stats(reps.get(), selection)
            #run_op(reps.get())

        ##### Defines the textboxes and images for the page ######
        background_img = PhotoImage(file=f"bg_3.png")
        background = canvas.create_image(
            182.0, 311.0,
            image=background_img)


        entry0_img = PhotoImage(file=f"img_textBox0.png")
        entry0_bg = canvas.create_image(
            174.0, 656.5,
            image=entry0_img)

        reps = IntVar(window, value = 0)
        entry0 = Entry(
            bd=0,
            bg="#353641",
            highlightthickness=0,
            textvariable= reps,
            fg = "white")

        entry0.place(
            x=45.5, y=628,
            width=257.0,
            height=55)


        img1 = PhotoImage(file=f"bicep.png")
        b1 = Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=bicep_clicked,
            relief="flat")

        b1.place(
            x=182, y=207,
            width=174,
            height=207)

        img2 = PhotoImage(file=f"calf.png")
        b2 = Button(
            image=img2,
            borderwidth=0,
            highlightthickness=0,
            command=hamstring_clicked,
            relief="flat")

        b2.place(
            x=-11, y=321,
            width=185,
            height=237)

        window.resizable(False, False)
        window.mainloop() 
        

    except:
        error_win = Tk()
        
        error_win.geometry("360x800")
        
        # Create text widget and specify size.
        T = Text(error_win, height = 5, width = 52)
        
        # Create label
        l = Label(error_win, text = "Unexpected Error")
        l.config(font =("Courier", 14))
        
        error_msg = "Unknown or incorrect value entered. Reload RepPal"
        
        # Create button for next text.
        b1 = Button(error_win, text = "Next", )
        
        # Create an Exit button.
        b2 = Button(error_win, text = "Exit", command = error_win.destroy)
        
        l.pack()
        T.pack()
        b1.pack()
        b2.pack()
        
        # Insert The Fact.
        T.insert(tkinter.END, error_msg)
        
        error_win.mainloop()
        print("Unknown or incorrect value entered. Reload RepPal")
        # displayed if user enters a incorrect value
    


def SignUp(): # defines the function: SignUp to allow user to enter their account info

    try:
        ##### Initiates the tkinter window and its properties #####
        window = Tk()
        window.title("RepPal")

        window.geometry("360x800")
        window.configure(bg = "#29272f")
        canvas = Canvas(
            window,
            bg = "#29272f",
            height = 800,
            width = 360,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)
        #####

        def btn_clicked(): # defines function to close the window once button is clicked and call the next page
            window.destroy()
            data = [username.get(), email.get(), password.get()]
            add_account_info(data)
            Workout()

        username = StringVar(window, value = "")
        email = StringVar(window, value = "")
        password = StringVar(window, value = "")

        ##### Defines the textboxes and images for the page ######
        entry0_img = PhotoImage(file = f"img_textBox0.png")
        entry0_bg = canvas.create_image(
            181.0, 240.5,
            image = entry0_img)

        entry0 = Entry(
            bd = 0,
            bg = "#353641",
            highlightthickness = 0,
            fg = "white",
            textvariable= username)

        entry0.place(
            x = 52.5, y = 212,
            width = 257.0,
            height = 55)

        entry1_img = PhotoImage(file = f"img_textBox1.png")
        entry1_bg = canvas.create_image(
            180.0, 346.5,
            image = entry1_img)

        entry1 = Entry(
            bd = 0,
            bg = "#353641",
            highlightthickness = 0,
            fg = "white",
            selectforeground= "white", 
            textvariable=email)

        entry1.place(
            x = 51.5, y = 318,
            width = 257.0,
            height = 55)

        entry2_img = PhotoImage(file = f"img_textBox2.png")
        entry2_bg = canvas.create_image(
            179.0, 452.5,
            image = entry2_img)

        entry2 = Entry(
            bd = 0,
            bg = "#353641",
            highlightthickness = 0,
            fg = "white",
            show = "*",
            textvariable=password)

        entry2.place(
            x = 50.5, y = 424,
            width = 257.0,
            height = 55)

        background_img = PhotoImage(file = f"sign_bg.png")
        background = canvas.create_image(
            182.5, 421.0,
            image=background_img)

        next_bt_img = PhotoImage(file = f"next_btn.png")
        next_bt = Button(
            image = next_bt_img,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        next_bt.place(
            x = 51, y = 512,
            width = 263,
            height = 75)

        window.resizable(False, False)
        window.mainloop()

        
    except:
        error_win = Tk()
        
        error_win.geometry("360x800")
        
        # Create text widget and specify size.
        T = Text(error_win, height = 5, width = 52)
        
        # Create label
        l = Label(error_win, text = "Unexpected Error")
        l.config(font =("Courier", 14))
        
        error_msg = "Unknown or incorrect value entered. Reload RepPal"
        
        # Create button for next text.
        b1 = Button(error_win, text = "Next", )
        
        # Create an Exit button.
        b2 = Button(error_win, text = "Exit", command = error_win.destroy)
        
        l.pack()
        T.pack()
        b1.pack()
        b2.pack()
        
        # Insert The Fact.
        T.insert(tkinter.END, error_msg)
        
        error_win.mainloop()
        print("Unknown or incorrect value entered. Reload RepPal")
        # displayed if user enters a incorrect value


def Start(): # defines the function: Start to display the starting window for the app

    try:
        ##### Initiates the tkinter window and its properties #####
        window = Tk()
        window.title("RepPal")

        window.geometry("360x800")
        window.configure(bg="#29272f")
        canvas = Canvas(
            window,
            bg="#29272f",
            height=800,
            width=360,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)
        #####

        def btn_clicked(): # defines function to close the window once button is clicked and call the next page
            window.destroy()
            SignUp()
            
        ##### Defines the textboxes and images for the page ######
        background_img = PhotoImage(file=f"start_bg.png")
        background = canvas.create_image(
            232.5, 400.0,
            image=background_img)

        img0 = PhotoImage(file=f"img0.png")
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        b0.place(
            x=31, y=520,
            width=300,
            height=105)

        window.resizable(False, False)
        window.mainloop()
        #####

    except:
        error_win = Tk()
        
        error_win.geometry("360x800")
        
        # Create text widget and specify size.
        T = Text(error_win, height = 5, width = 52)
        
        # Create label
        l = Label(error_win, text = "Unexpected Error")
        l.config(font =("Courier", 14))
        
        error_msg = "Unknown or incorrect value entered. Reload RepPal"
        
        # Create button for next text.
        b1 = Button(error_win, text = "Next", )
        
        # Create an Exit button.
        b2 = Button(error_win, text = "Exit", command = error_win.destroy)
        
        l.pack()
        T.pack()
        b1.pack()
        b2.pack()
        
        # Insert The Fact.
        T.insert(tkinter.END, error_msg)
        
        error_win.mainloop()
        print("Unknown or incorrect value entered. Reload RepPal")
        # displayed if user enters a incorrect value

Start()
# calls the Start function to display the start page and display the other pages of the app based on user controls
