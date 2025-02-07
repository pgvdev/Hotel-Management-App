from tkinter import *  # Required for GUI setup
from PIL import ImageTk, Image  # Required for handling image data (e.g., loading images)
from customer import Customer
from reservations import Reservations
from room import Room

# Main class for the Hotel Management System
class HotelManagementSystem:
    def __init__(self, master):
        # Initialize the main application window
        self.master = master
        self.master.title("Lemon Tree Hotel Reservation System")  # Set the window title
        self.master.geometry("1440x900+0+0")  # Set the window size and position

        # TOP BANNER
        # Load and display the top banner image
        img1 = Image.open("/Users/pop/Downloads/travelbanner.png")
        img1 = img1.resize((1440, 200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        label_img = Label(self.master, image = self.photoimg1, bd=0, relief=RIDGE)
        label_img.place(x=0, y=0, width=1440, height=200)


        # # COMPANY LOGO
        # img2 = Image.open("/Users/pop/Downloads/banners - alertpress/POWER TOOLS (2).gif")
        # img2 = img2.resize((1440, 900), Image.Resampling.LANCZOS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)
        #
        # label_img = Label(self.master, image = self.photoimg2, bd=4, relief=RIDGE)
        # label_img.place(x=600, y=0, width=230, height=150)


        # # TITLE BANNER
        # label_title = Label(self.master, text="Hotel Management System", font =("times new roman", 27, "bold"),
        #                     bg = "black", fg = "gold", bd = 0, relief = RIDGE)
        # label_title.place(x=0, y=150, width=1440, height=50)


        # MAIN BODY CONTENT
        # Create the main frame for the application's content
        main_frame = Frame(self.master, bd=2, relief=RIDGE)
        main_frame.place(x=0, y=200, width=1440, height=600)


        # MENU LABEL
        # Add a menu label at the top of the menu section
        label_menu= Label(main_frame, text="Menu", font =("times new roman", 20, "bold"),
                          bg = "black", fg = "gold", bd = 0, relief = RIDGE)
        label_menu.place(x=0, y=0, width=210)


        # BUTTON FRAME
        # Create a frame for menu buttons
        button_frame = Frame(main_frame, bg="black", bd=4, relief=RIDGE)
        button_frame.place(x=0, y=35, width=198, height=145)


        # CUSTOMER BUTTON
        # Button to open the customer details window
        customer_button = Button(button_frame, text = "Customer", command = self.CustomerDetails,  width = 22, font =("times new roman", 14, "bold"),
                               bg = "black", fg = "gold", bd = 0, cursor ="hand1")
        customer_button.grid(row=0, column=0, pady=1)


        # RESERVATION BUTTON
        # Button to open the reservation details window
        reservations_button = Button(button_frame, text = "Reservations", command = self.ReservationDetails, width = 22, font =("times new roman", 14, "bold"),
                                 bg = "black", fg = "gold", bd = 0, cursor ="hand1")
        reservations_button.grid(row=1, column=0, pady=1)


        # ROOMS BUTTON
        # Button to open the room details window
        rooms_button = Button(button_frame, text = "Rooms",command=self.RoomDetails,  width = 22, font =("times new roman", 14, "bold"),
                                 bg = "black", fg = "gold", bd = 0, cursor ="hand1")
        rooms_button.grid(row=2, column=0, pady=1)


        # REPORT BUTTON
        report_button = Button(button_frame, text = "Reports", width = 22, font =("times new roman", 14, "bold"),
                                 bg = "black", fg = "gold", bd = 0, cursor ="hand1")
        report_button.grid(row=3, column=0, pady=1)


        # LOG OUT BUTTON
        logout_button = Button(button_frame, text = "Log Out", width = 22, font =("times new roman", 14, "bold"),
                                 bg = "black", fg = "gold", bd = 0, cursor ="hand1")
        logout_button.grid(row=4, column=0, pady=1)


        # MAIN BODY IMAGE
        # Load and display the main body image
        img3 = Image.open("/Users/pop/Downloads/mainimage.png")
        img3 = img3.resize((1250, 668), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        label1_img = Label(main_frame, image = self.photoimg3, bd=0, relief=RIDGE)
        label1_img.place(x=200, y=0, width=1234, height=594)


        # FOOTER IMAGE 1
        # Load and display the first footer image
        img4 = Image.open("/Users/pop/Downloads/footerimage.png")
        img4 = img4.resize((200, 200), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        label1_img = Label(main_frame, image = self.photoimg4, bd=0, relief=RIDGE)
        label1_img.place(x=0, y=185, width=200, height=190)


        # FOOTER IMAGE 2
        # Load and display the second footer image
        img5 = Image.open("/Users/pop/Downloads/footerimage2.png")
        img5 = img5.resize((200, 220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        label1_img = Label(main_frame, image = self.photoimg5, bd=0, relief=RIDGE)
        label1_img.place(x=0, y=375, width=200, height=220)


    # Function to open the customer details window
    def CustomerDetails(self):
        self.new_frame = Toplevel(self.master)
        self.app = Customer(self.new_frame)

    # Function to open the reservation details window
    def ReservationDetails(self):
        self.new_frame = Toplevel(self.master)
        self.app = Reservations(self.new_frame)

    # Function to open the room details window
    def RoomDetails(self):
        self.new_frame = Toplevel(self.master)
        self.app = Room(self.new_frame)




# Entry point of the program
if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(master=root)
    root.mainloop()
