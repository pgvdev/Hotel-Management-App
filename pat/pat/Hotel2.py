from tkinter import *  # Required for GUI setup
from PIL import ImageTk, Image  # Required for handling image data (e.g., loading images)
from tkcalendar import Calendar
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl





class HotelInterface:
    def __init__(self, root):
        self.root = root
        self.root.title ("Lemon Tree Hotel")
        self.root.geometry ("1024x600+0+0")




        # self.cal = None




        #menu frame
        menu_frame = Frame (self.root, bd = 2, relief = RIDGE)   #bd=border  #relife=widge effect
        menu_frame.place(x = 0, y = 0, width = 1024, height = 45)


        #menu buttons
        label_menu = Button (menu_frame, text = "Customer", command=self.display_customer_details, font = ("Times New Roman", 12, "bold"), bg = "pink", fg = "black", cursor ="hand2")
        label_menu.place(x = 10, y = 11, width = 100)

        label_menu = Button (menu_frame, text = "Reservation", command=self.display_reservation_details, font = ("Times New Roman", 12, "bold"), bg = "pink", fg = "black", cursor ="hand2")
        label_menu.place(x = 120, y = 11, width = 100)

        label_menu = Label(menu_frame, text="Services", font=("Times New Roman", 12, "bold"), bg="pink", fg="black", cursor="hand2")
        label_menu.place(x = 230, y = 11, width=100)

        label_menu = Button(menu_frame, text="Checkout", command=self.go_checkout, font=("Times New Roman", 12, "bold"), bg="pink", fg="black", cursor="hand2")
        label_menu.place(x=340, y=11, width=100)

        label_menu = Label(menu_frame, text="Contact", font=("Times New Roman", 12, "bold"), bg="pink", fg="black", cursor="hand2")
        label_menu.place(x=450, y=11, width=100)

        # Welcome message
        messagebox.showinfo(title="Welcome!", message="Welcome to the Lemon Tree Booking System!", parent=self.root)



    def display_customer_details(self):

        CustomerWindow = Frame(self.root, border = 2, relief = RIDGE)
        CustomerWindow.place (x = 5, y = 50, width = 500, height = 500)

        # customer details
        # customer label
        customer_name = Label (CustomerWindow, text = "Full Name", font = ("Times New Roman", 12, "bold"), fg = "black", cursor ="hand2")
        customer_name.grid (row = 0, column = 0, sticky = W)

        # customer name input
        self.customer_name_input = ttk.Entry(CustomerWindow, width=29, font=("Arial", 12, "bold"))
        self.customer_name_input.grid (row=0, column=1)

        # customer address
        customer_address = Label(CustomerWindow, text="Address", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2")
        customer_address.grid(row=1, column=0, sticky=W)

        # customer address input
        self.customer_address_input = ttk.Entry(CustomerWindow, width=29, font=("Arial", 12, "bold"))
        self.customer_address_input.grid(row=1, column=1)

        # customer email
        customer_email = Label(CustomerWindow, text="Email", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2")
        customer_email.grid(row=2, column=0, sticky=W)

        # customer email input
        self.customer_email_input = ttk.Entry(CustomerWindow, width=29, font=("Arial", 12, "bold"))
        self.customer_email_input.grid(row=2, column=1)

        # customer Phone Number
        customer_phone_number = Label(CustomerWindow, text="Phone Number", font=("Times New Roman", 12, "bold"), fg="black",cursor="hand2")
        customer_phone_number.grid(row=3, column=0, sticky=W)

        # customer Phone Number input
        self.customer_phone_number_input = ttk.Entry(CustomerWindow, width=29, font=("Arial", 12, "bold"))
        self.customer_phone_number_input.grid(row=3, column=1)

        # customer reward combo box
        customer_reward = Label(CustomerWindow, text="Customer Type", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        customer_reward.grid(row=4, column=0, sticky=W)

        # customer reward combo box
        self.customer_reward_combo_box = ttk.Combobox(CustomerWindow, width=27, font=("Arial", 12, "bold"))
        self.customer_reward_combo_box ["value"] = ("Standard", "Premium")
        self.customer_reward_combo_box.grid(row=4, column=1)

        label_menu = Button (CustomerWindow, text = "Add Customer", command=self.add_customer_info, font = ("Times New Roman", 12, "bold"), bg = "pink", fg = "black", cursor ="hand2")
        label_menu.place(x = 390, y = 11, width = 100)





    def add_customer_info(self):
        if not all([self.customer_name_input.get(),
                    self.customer_address_input.get(),
                    self.customer_email_input.get(),
                    self.customer_phone_number_input.get(),
                    self.customer_reward_combo_box.get()]):

            messagebox.showerror("Error", "Customer details not initialized. Please fill the form first.")
            return

        # Create a frame to display customer details
        show_customer_details = Frame(self.root, border=2, relief=RIDGE)
        show_customer_details.place(x=500, y=50, width=500, height=500)

        # Get values from input fields
        self.customer_name = self.customer_name_input.get()
        self.customer_address = self.customer_address_input.get()
        self.customer_email = self.customer_email_input.get()
        self.customer_phone_number = self.customer_phone_number_input.get()
        self.customer_type = self.customer_reward_combo_box.get()

        messagebox.showinfo("Success", "Customer details added successfully!")

    # Display the details in the new frame
        details = {
            "Full Name": self.customer_name,
            "Address": self.customer_address,
            "Email": self.customer_email,
            "Phone Number": self.customer_phone_number,
            "Customer Type":self.customer_type,
        }

        for i, (key, value) in enumerate(details.items()):
            Label(show_customer_details, text=f"{key}:", font=("arial", 12, "bold")).place(x=10, y=i * 30)
            Label(show_customer_details, text=value, font=("arial", 12)).place(x=150, y=i * 30)

        label_menu = Button (show_customer_details, text = "Create reservation", command=self.display_reservation_details, font = ("Times New Roman", 12, "bold"), bg = "pink", fg = "black", cursor ="hand2")
        label_menu.place(x = 390, y = 11, width = 100)

    def checkin_Date(self):
        # Retrieve the selected date from the calendar
        if self.cal:
            selected_date = self.cal.get_date()
            self.label_checkin.config(text=f"Check-In: {selected_date}")
        else:
            messagebox.showerror("Error", "Calendar is not initialized!")


    def checkout_Date(self):
        # Retrieve the selected date from the calendar
        if self.cal:
            selected_date = self.cal.get_date()
            self.label_checkout.config(text=f"Check-Out: {selected_date}")
        else:
            messagebox.showerror("Error", "Calendar is not initialized!")





    def display_reservation_details(self):
        ReservationWindow = Frame(self.root, border=2, relief=RIDGE)
        ReservationWindow.place(x=5, y=50, width=500, height=500)

        # number of rooms combo box
        number_of_rooms = Label(ReservationWindow, text="Number of Rooms", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        number_of_rooms.grid(row=0, column=0, sticky=W)

        # number of rooms combo box
        self.number_of_rooms_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        self.number_of_rooms_combo_box["value"] = ("1", "2", "3", "4", "5", "6")
        self.number_of_rooms_combo_box.grid(row=0, column=1)


        # booking date label
        booking_date = Label(ReservationWindow, text="Booking Date", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2")
        booking_date.grid(row=1, column=0, sticky=W)

        # # booking date input
        # self.booking_date_input = DateEntry(ReservationWindow, width=29, font=("Arial", 12, "bold"))
        # self.booking_date_input.grid(row=20, column=1)


        # Add a calendar widget
        self.cal = Calendar(ReservationWindow, selectmode='day', year=2025, month=1, day=13)
        self.cal.grid(row=16, column=1)

        # Add a button to get the selected date
        Button(ReservationWindow, text="Get Check-In Date", command=self.checkin_Date).grid(row=17, column=1, pady=10)

        # Label to display selected date
        self.label_checkin = Label(ReservationWindow, text="", font=("Arial", 12, "bold"))
        self.label_checkin.grid(row=1, column=1, pady=10)

        # Add a button to get the selected date
        Button(ReservationWindow, text="Get Check-out Date", command=self.checkout_Date).grid(row=18, column=1, pady=10)

        # Label to display selected date
        self.label_checkout = Label(ReservationWindow, text="", font=("Arial", 12, "bold"))
        self.label_checkout.grid(row=1, column=2, pady=10)



        # Purpose of Staying combo box
        purpose_of_staying = Label(ReservationWindow, text="Purpose of Staying", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        purpose_of_staying.grid(row=2, column=0, sticky=W)

        # Purpose of Staying input
        self.purpose_of_staying_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        self.purpose_of_staying_combo_box["value"] = ("Work", "Leisure")
        self.purpose_of_staying_combo_box.grid(row=2, column=1)


        # Room Type combo box
        room_type = Label(ReservationWindow, text="Room Type", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        room_type.grid(row=3, column=0, sticky=W)

        # Room Type input
        self.room_type_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        self.room_type_combo_box["value"] = ("Single", "Double")
        self.room_type_combo_box.grid(row=3, column=1)

        # # customer reward combo box
        # customer_reward = Label(CustomerWindow, text="Customer Type", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        # customer_reward.grid(row=4, column=0, sticky=W)
        #
        # # customer reward combo box
        # customer_reward_combo_box = ttk.Combobox(CustomerWindow, width=27, font=("Arial", 12, "bold"))
        # customer_reward_combo_box["value"] = ("Standard", "Premium")
        # customer_reward_combo_box.grid(row=4, column=1)


        # Number of Adults combo box
        number_of_adults = Label(ReservationWindow, text="Number of Adults", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        number_of_adults.grid(row=4, column=0, sticky=W)

        # Number of Adults combo box
        self.number_of_adults_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        self.number_of_adults_combo_box["value"] = ("1", "2", "3", "4", "5")
        self.number_of_adults_combo_box.grid(row=4, column=1)


        # Number of Children combo box
        number_of_children = Label(ReservationWindow, text="Number of Children", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        number_of_children.grid(row=5, column=0, sticky=W)

        # Number of Adults combo box
        self.number_of_children_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        self.number_of_children_combo_box["value"] = ("0", "1", "2", "3", "4", "5")
        self.number_of_children_combo_box.grid(row=5, column=1)


        # Pets Included combo box
        pets_included = Label(ReservationWindow, text="Pets Included", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        pets_included.grid(row=6, column=0, sticky=W)

        # Number of Adults combo box
        self.pets_included_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        self.pets_included_combo_box["value"] = ("Yes", "No")
        self.pets_included_combo_box.grid(row=6, column=1)

        # Payment Method combo box
        payment_method = Label(ReservationWindow, text="Payment Method", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        payment_method.grid(row=7, column=0, sticky=W)

        # Payment Method combo box
        self.payment_method_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        self.payment_method_combo_box["value"] = ("Bank Transfer", "Debit Card", "Credit Card", "PayPal", "Apple Pay", "Google Pay")
        self.payment_method_combo_box.grid(row=7, column=1)

        label_menu = Button (ReservationWindow, text = "Add Reservation", command=self.add_reservation_info, font = ("Times New Roman", 12, "bold"), bg = "pink", fg = "black", cursor ="hand2")
        label_menu.place(x = 390, y = 11, width = 100)







    def add_reservation_info(self):
        if not all([self.number_of_rooms_combo_box.get(),
                    self.label_checkin.cget("text"),
                    self.label_checkout.cget("text"),
                    self.purpose_of_staying_combo_box.get(),
                    self.room_type_combo_box.get(),
                    self.number_of_adults_combo_box.get(),
                    self.number_of_children_combo_box.get(),
                    self.pets_included_combo_box.get(),
                    self.payment_method_combo_box.get()]):

            messagebox.showerror("Error", "Reservation details not initialized. Please fill the form first.")
            return


        # Combine check-in and check-out dates into a single string
        checkin_date = self.label_checkin.cget("text").replace("Check-In: ", "")
        checkout_date = self.label_checkout.cget("text").replace("Check-Out: ", "")
        self.booking_date = f"{checkin_date} to {checkout_date}"



        # Create a frame to display reservation details
        show_reservation_details = Frame(self.root, border=2, relief=RIDGE)
        show_reservation_details.place(x=500, y=50, width=500, height=500)

        # Get values from input fields
        self.number_of_rooms = self.number_of_rooms_combo_box.get()
        # self.booking_date = self.label_checkin.cget("text"), self.label_checkout.cget("text")
        self.purpose_of_staying = self.purpose_of_staying_combo_box.get()
        self.room_type = self.room_type_combo_box.get()
        self.number_of_adults = self.number_of_adults_combo_box.get()
        self.number_of_children = self.number_of_children_combo_box.get()
        self.pets_included = self.pets_included_combo_box.get()
        self.payment_method = self.payment_method_combo_box.get()

        messagebox.showinfo("Success", "Reservation details added successfully!")


    # Display the details in the new frame
        details = {
            "Number of Rooms": self.number_of_rooms,
            "Booking Date": self.booking_date,
            "Purpose of Staying": self.purpose_of_staying,
            "Room Type": self.room_type,
            "Number of Adults": self.number_of_adults,
            "Number of Children": self.number_of_children,
            "Pets": self.pets_included,
            "Payment Method": self.payment_method,
        }

        for i, (key, value) in enumerate(details.items()):
            Label(show_reservation_details, text=f"{key}:", font=("arial", 12, "bold")).place(x=10, y=i * 30)
            Label(show_reservation_details, text=value, font=("arial", 12)).place(x=150, y=i * 30)



        label_menu = Button (show_reservation_details, text = "Go to Checkout", command=self.go_checkout, font = ("Times New Roman", 12, "bold"), bg = "pink", fg = "black", cursor ="hand2")
        label_menu.place(x = 390, y = 11, width = 100)



    def go_checkout(self):
        # Create a frame to display checkout details
        show_checkout_details = Frame(self.root, border=2, relief=RIDGE)
        show_checkout_details.place(x=500, y=50, width=500, height=500)



        # Get values from input fields
        customer_name = self.customer_name_input.get(),
        customer_address = self.customer_address_input.get(),
        customer_email = self.customer_email_input.get(),
        customer_phone_number = self.customer_phone_number_input.get()
        customer_type = self.customer_reward_combo_box.get()

        number_of_rooms = self.number_of_rooms_combo_box.get(),
        booking_date = self.label_checkin.cget("text"), self.label_checkout.cget("text"),
        purpose_of_staying = self.purpose_of_staying_combo_box.get(),
        room_type = self.room_type_combo_box.get(),
        number_of_adults = self.number_of_adults_combo_box.get(),
        number_of_children = self.number_of_children_combo_box.get(),
        pets_included = self.pets_included_combo_box.get(),
        payment_method = self.payment_method_combo_box.get()


        # Display the details in the new frame
        details = {
            "Full Name": customer_name,
            "Address": customer_address,
            "Email": customer_email,
            "Phone Number": customer_phone_number,
            "Customer Type": customer_type,

            "Number of Rooms": number_of_rooms,
            "Booking Date": booking_date,
            "Purpose of Staying": purpose_of_staying,
            "Room Type": room_type,
            "Number of Adults": number_of_adults,
            "Number of Children": number_of_children,
            "Pets": pets_included,
            "Payment Method": payment_method,
        }

        for i, (key, value) in enumerate(details.items()):
            Label(show_checkout_details, text=f"{key}:", font=("arial", 12, "bold")).place(x=10, y=i * 30)
            Label(show_checkout_details, text=value, font=("arial", 12)).place(x=150, y=i * 30)


        # Add meals information based on customer type
        self.display_meals_info(show_checkout_details, customer_type)

        label_menu = Button (show_checkout_details, text = "Pay Now", command=self.payment_confirmation, font = ("Times New Roman", 12, "bold"), bg = "pink", fg = "black", cursor ="hand2")
        label_menu.place(x = 390, y = 11, width = 100)



    def display_meals_info(self, frame, customer_type):

        # Display meals included or no benefits applied based on customer type
        if customer_type == "Premium":
            meals_info = "Meals Included: Breakfast, Lunch, Dinner"
        else:
            meals_info = "No benefits applied"

        Label(frame, text="Benefits:", font=("arial", 12, "bold")).place(x=10, y=390)
        Label(frame, text=meals_info, font=("arial", 12)).place(x=150, y=390)




    def payment_confirmation(self):
        confirmation = messagebox.askyesno("Payment Confirmation",
                            "Would you like to continue with this payment?", parent=self.root)
        if not confirmation:
            return

        filepath = r"/Users/pop/Downloads/hotelmanagement.xlsx"


        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            heading = [
                "Full Name", "Address", "Email", "Phone Number", "Customer Type",
                "Number of Rooms", "Booking Date", "Purpose of Staying", "Room Type",
                "Number of Adults", "Number of Children", "Pets", "Payment Method"
            ]
            sheet.append(heading)
            workbook.save(filepath)

        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([
            self.customer_name, self.customer_address, self.customer_email, self.customer_phone_number, self.customer_type,
            self.number_of_rooms, self.booking_date, self.purpose_of_staying, self.room_type,
            self.number_of_adults, self.number_of_children, self.pets_included, self.payment_method
        ])
        workbook.save(filepath)
        messagebox.showinfo("Success", "Payment and booking details saved successfully!")


# def CustomerDetails(self):
    #
    #     self.CustomerFrame = Toplevel(self.root)
    #     self.Application = CustomerDetails(self.CustomerFrame)


    # def ReservationDetails(self):
    #
    #     self.ReservationFrame = Toplevel(self.root)
    #     self.Application = ReservationDetails(self.ReservationFrame)


if __name__ == "__main__":
    root = Tk()
    object = HotelInterface (root)
    root.mainloop()