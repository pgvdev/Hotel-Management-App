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


        # MAIN BODY CONTENT
        # Create the main frame for the application's content
        self.main_frame = Frame(self.master, bd=2, relief=RIDGE)
        self.main_frame.place(x=0, y=200, width=1440, height=600)



        # MAIN BODY IMAGE
        # Load and display the main body image
        img3 = Image.open("/Users/pop/Downloads/mainimage.png")
        img3 = img3.resize((1440, 668), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        label1_img = Label(self.main_frame, image = self.photoimg3, bd=0, relief=RIDGE)
        label1_img.place(x=0, y=0, width=1435, height=594)


        # CUSTOMER BUTTON
        # Button to open the customer details window

        customer_image_button = Image.open("/Users/pop/Downloads/customer.png")
        customer_image_button = customer_image_button.resize((94, 29), Image.Resampling.LANCZOS)
        self.customer_image_button = ImageTk.PhotoImage(customer_image_button)


        customer_button = Button(self.master, text = "", image = self.customer_image_button, command = self.CustomerDetails, bd=0, cursor ="hand1")
        customer_button.place(x=550, y=125)


        # RESERVATION BUTTON
        # Button to open the reservation details window

        reservation_image_button = Image.open("/Users/pop/Downloads/reservation.png")
        reservation_image_button = reservation_image_button.resize((94, 29), Image.Resampling.LANCZOS)
        self.reservation_image_button = ImageTk.PhotoImage(reservation_image_button)

        reservations_button = Button(self.master, text = "", image = self.reservation_image_button, command = self.ReservationDetails, bd=0, cursor ="hand1")
        reservations_button.place(x=650, y=125)


        # ROOMS BUTTON
        # Button to open the room details window

        room_image_button = Image.open("/Users/pop/Downloads/room.png")
        room_image_button = room_image_button.resize((94, 29), Image.Resampling.LANCZOS)
        self.room_image_button = ImageTk.PhotoImage(room_image_button)


        rooms_button = Button(self.master, text = "",image = self.room_image_button, command=self.RoomDetails, bd=0, cursor ="hand1")
        rooms_button.place(x=750, y=125)


    # Function to open the customer details window
    def CustomerDetails(self):
        self.new_frame = Toplevel(self.master)
        self.new_frame.geometry("1440x560+0+0")
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
