from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from tkcalendar import DateEntry
from time import strftime
from datetime import datetime, timedelta
import mysql.connector
from tkinter import messagebox

# Class to handle reservation-related functionalities
class Reservations:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Reservation Management")
        self.master.geometry("1215x560+0+260")



        # Define variables to hold data
        self.search_customer_combobox=StringVar()
        self.search_customer_input=StringVar()
        self.var_hotel_location=StringVar()

        # Generate a random booking ID
        self.var_bookingID=StringVar()
        x=random.randint(1000, 9999)
        self.var_bookingID.set(str(x))

        # Variables for reservation details
        self.var_checkinDate=StringVar()
        self.var_checkoutDate=StringVar()
        self.var_room_type=StringVar()
        self.var_available_rooms=StringVar()
        self.var_purpose_of_stay=StringVar()
        self.var_adults=StringVar()
        self.var_children=StringVar()
        self.var_special_note=StringVar()
        self.var_discount=StringVar()
        self.var_VAT=StringVar()
        self.var_total_cost=StringVar()
        self.var_payment_method=StringVar()


        # # Default values for dates
        # self.var_checkinDate.set(datetime.now().strftime("%d/%m/%Y"))
        # self.var_checkoutDate.set((datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y"))


        # TITLE BANNER
        label_title = Label(self.master, text="Booking System", font =("arial", 27, "bold"),
                            bg = "black", fg = "gold", bd = 4, relief = RIDGE)
        label_title.place(x=0, y=0, width=1215, height=50)


        # COMPANY LOGO
        img2 = Image.open("/Users/pop/Downloads/banners - alertpress/POWER TOOLS (2).gif")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        label_img = Label(self.master, image = self.photoimg2, bd=0, relief=RIDGE)
        label_img.place(x=1110, y=5, width=100, height=40)






        ######### Label Frame Left Side #########
        # Create the left-side frame for reservation details
        labelframe_ls = LabelFrame(self.master, bd = 2, relief = RIDGE, text = "Reservation Details",
                                   font = ("arial", 12, "bold"), padx = 2)
        labelframe_ls.place(x=5, y=50, width=365, height=500)

        # Search Customer COMBOBOX
        self.search_customer_columns = {
            "Customer ID": "CustomerID",
            "Full Name": "FullName",
            "Phone Number": "PhoneNumber",
            "Email Address": "Email",
        }

        combobox_search_customer = ttk.Combobox(labelframe_ls, textvariable=self.search_customer_combobox, font=("arial", 13, "bold"), width=10, state="readonly")
        combobox_search_customer["value"] = list(self.search_customer_columns.keys())
        combobox_search_customer.current(0)
        combobox_search_customer.grid(row=0, column=0)

        # Search Customer Input
        search_customer_input = ttk.Entry(labelframe_ls, textvariable=self.search_customer_input, width=20,font=("arial", 14, "bold"))
        search_customer_input.grid(row=0, column=1, sticky=W)

        # Fetch Data Button
        fetchData_button = Button(labelframe_ls, command=self.fetch_customer_search, text="Search", font=("arial", 11, "bold"), bg="black",
                                     fg="gold", width=4)
        fetchData_button.place(x=284, y=1)


        # Booking ID Label
        label_booking_id = Label(labelframe_ls, text = "Booking ID",
                                 font=("arial", 12, "bold"), padx=2, pady=6)
        label_booking_id.grid(row=1, column=0, sticky=W)

        # Booking ID Input
        booking_id_input = ttk.Entry(labelframe_ls, textvariable=self.var_bookingID, width=28, state="readonly" ,font=("arial", 13, "bold"))
        booking_id_input.grid(row=1, column=1)

        # Hotel Location Label
        label_hotel_location = Label(labelframe_ls, text = "Hotel Location",
                                     font=("arial", 12, "bold"), padx=2, pady=6)
        label_hotel_location.grid(row=2, column=0, sticky=W)

        # Hotel Location COMBOBOX
        combobox_hotel_location = ttk.Combobox(labelframe_ls, textvariable=self.var_hotel_location, font=("arial", 13, "bold"), width=27, state="readonly")
        combobox_hotel_location["value"]=("Manchester", "London", "New York", "Bucharest", "Warsaw", "Las Vegas", "Montreal", "Amsterdam")
        combobox_hotel_location.current(0)
        combobox_hotel_location.grid(row=2, column=1)


        # Check-in Date Label
        label_checkin_date = Label(labelframe_ls, text = "Check-in Date",
                                  font=("arial", 12, "bold"), padx=2, pady=6)
        label_checkin_date.grid(row=3, column=0, sticky=W)

        # Check-in Date Calendar
        self.var_checkinDate = StringVar()
        checkin_date_input = DateEntry(labelframe_ls, textvariable=self.var_checkinDate, width=27, font=("arial", 13, "bold"),
                                       date_pattern="dd/mm/yyyy",
                                       background="white",  # Set background color to white
                                       foreground="black",  # Set text color to black
                                       selectbackground="gray",  # Background color for selected date
                                       selectforeground="white"  # Text color for selected date
                                       )
        checkin_date_input.grid(row=3, column=1)


        # Check-out Date Label
        label_checkout_date = Label(labelframe_ls, text = "Check-out Date",
                                   font=("arial", 12, "bold"), padx=2, pady=6)
        label_checkout_date.grid(row=4, column=0, sticky=W)

        # Check-out Date Calendar
        self.var_checkoutDate = StringVar()
        checkout_date_input = DateEntry(labelframe_ls, textvariable=self.var_checkoutDate, width=27, font=("arial", 13, "bold"),
                                        date_pattern="dd/mm/yyyy",
                                        background="white",  # Set background color to white
                                        foreground="black",  # Set text color to black
                                        selectbackground="gray",  # Background color for selected date
                                        selectforeground="white"  # Text color for selected date
                                        )
        checkout_date_input.grid(row=4, column=1)


        # Room Type Label
        label_room_type = Label(labelframe_ls, text = "Room Type",
                                     font=("arial", 12, "bold"), padx=2, pady=6)
        label_room_type.grid(row=5, column=0, sticky=W)


        # Room Type COMBOBOX
        combobox_room_type = ttk.Combobox(labelframe_ls, textvariable=self.var_room_type,font=("arial", 13, "bold"), width=27, state="readonly")
        combobox_room_type["value"]=("Single", "Double", "Twin Deluxe", "Queen Deluxe", "King Deluxe", "King Executive", "Presidential Suite")
        combobox_room_type.current(0)
        combobox_room_type.grid(row=5, column=1)


        # Room Availability Label
        label_available_rooms = Label(labelframe_ls, text = "Room Number",
                                       font=("arial", 12, "bold"), padx=2, pady=6)
        label_available_rooms.grid(row=6, column=0, sticky=W)


        conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT RoomNumber FROM room")
        rows=my_cursor.fetchall()


        # Room Availability COMBOBOX
        combobox_available_rooms = ttk.Combobox(labelframe_ls, textvariable=self.var_available_rooms, font=("arial", 13, "bold"), width=27, state="readonly")
        combobox_available_rooms["value"]=rows
        combobox_available_rooms.current(0)
        combobox_available_rooms.grid(row=6, column=1)



        # Purpose of Stay Label
        label_purpose_of_stay = Label(labelframe_ls, text = "Purpose Of Stay",
                                font=("arial", 12, "bold"), padx=2, pady=6)
        label_purpose_of_stay.grid(row=7, column=0, sticky=W)

        # Purpose of Stay COMBOBOX
        combobox_purpose_of_stay = ttk.Combobox(labelframe_ls, textvariable=self.var_purpose_of_stay,font=("arial", 13, "bold"), width=27)
        combobox_purpose_of_stay["value"]=("Clean Environment", "A Perfect Sweet Escape", "24 x 7 Service and Security",
                                           "Convenient in Terms of Location", "A Significant Variety of Dining Options",
                                           "Very Clean Bedding", "A Family Holiday", "Other")
        combobox_purpose_of_stay.current(0)
        combobox_purpose_of_stay.grid(row=7, column=1)

        # Number of Adults Label
        label_adults = Label(labelframe_ls, text = "Adults",
                                      font=("arial", 12, "bold"), padx=2, pady=6)
        label_adults.grid(row=8, column=0, sticky=W)

        # Number of Adults Spinbox
        adults_spinbox = Spinbox(labelframe_ls, from_=1, to=10, textvariable=self.var_adults,width=28 ,font=("arial", 13, "bold"))
        adults_spinbox.grid(row=8, column=1)

        # Number of Children Label
        label_children = Label(labelframe_ls, text = "Children",
                             font=("arial", 12, "bold"), padx=2, pady=6)
        label_children.grid(row=9, column=0, sticky=W)

        # Number of Children Spinbox
        children_spinbox = Spinbox(labelframe_ls, from_=0, to=10, textvariable=self.var_children,width=28 ,font=("arial", 13, "bold"))
        children_spinbox.grid(row=9, column=1)

        # Special Note Label
        label_special_note = Label(labelframe_ls, text = "Special Note",
                               font=("arial", 12, "bold"), padx=2, pady=6)
        label_special_note.grid(row=10, column=0, sticky=W)

        # Special Note Input
        special_note_input = ttk.Entry(labelframe_ls, textvariable=self.var_special_note,width=28,font=("arial", 13, "bold"))
        special_note_input.grid(row=10, column=1)

        # Discount Label
        label_discount = Label(labelframe_ls, text = "Discount",
                                 font=("arial", 12, "bold"), padx=2, pady=6)
        label_discount.grid(row=11, column=0, sticky=W)

        # Discount Input
        discount_input = ttk.Entry(labelframe_ls, textvariable=self.var_discount,width=28 ,font=("arial", 13, "bold"))
        discount_input.grid(row=11, column=1)

        # VAT Tax Label
        label_vat_tax = Label(labelframe_ls, text = "VAT",
                                   font=("arial", 12, "bold"), padx=2, pady=6)
        label_vat_tax.grid(row=12, column=0, sticky=W)

        # VAT Tax Input
        vat_tax_input = ttk.Entry(labelframe_ls, textvariable=self.var_VAT,width=28 ,font=("arial", 13, "bold"))
        vat_tax_input.grid(row=12, column=1)

        # Total Cost Label
        label_total_cost = Label(labelframe_ls, text = "Total Cost",
                              font=("arial", 12, "bold"), padx=2, pady=6)
        label_total_cost.grid(row=13, column=0, sticky=W)

        # Total Cost Input
        total_cost_input = ttk.Entry(labelframe_ls, textvariable=self.var_total_cost, width=28 ,font=("arial", 13, "bold"))
        total_cost_input.grid(row=13, column=1)

        # Payment Method Label
        label_payment_method = Label(labelframe_ls, text = "Payment Method",
                                      font=("arial", 12, "bold"), padx=2, pady=6)
        label_payment_method.grid(row=14, column=0, sticky=W)

        # Payment Method COMBOBOX
        combobox_payment_method = ttk.Combobox(labelframe_ls, textvariable=self.var_payment_method, font=("arial", 13, "bold"), width=27, state="readonly")
        combobox_payment_method["value"]=("Cash", "Credit Card", "Debit Card", "Google Pay", "Apple Pay", "PayPal", "Gift Card", "Klarna")
        combobox_payment_method.current(0)
        combobox_payment_method.grid(row=14, column=1)

        # Bill Payment

        bill_payment_button = Button(labelframe_ls, text="Check Out", command=self.total, font=("arial", 13, "bold"), bg="black",
                                     fg="gold", width=13)
        bill_payment_button.place(x=210, y=446)

        ######### BUTTON FRAME #########
        button_frame = Frame(labelframe_ls, bd=0, relief=RIDGE)
        button_frame.place(x=0, y=447, width=205, height=25)


        # ADD RESERVATION
        add_reservation_button = Button(button_frame, text="Add", command=self.insert_data, font=("arial", 11, "bold"), bg="black",
                                     fg="gold", width=2)
        add_reservation_button.grid(row=0, column=0, padx=1, pady=1)


        # UPDATE RESERVATION
        update_reservation_button = Button(button_frame, text="Update", command=self.update_data, font=("arial", 11, "bold"), bg="black",
                                        fg="gold", width=2)
        update_reservation_button.grid(row=0, column=1, padx=1, pady=1)


        # RESET RESERVATION
        reset_reservation_button = Button(button_frame, text="Reset", command=self.reset_data, font=("arial", 11, "bold"), bg="black",
                                       fg="gold", width=2)
        reset_reservation_button.grid(row=0, column=2, padx=1, pady=1)


        # DELETE RESERVATION
        delete_reservation_button = Button(button_frame, text="Delete", command=self.delete_data, font=("arial", 11, "bold"), bg="black",
                                        fg="gold", width=2)
        delete_reservation_button.grid(row=0, column=3, padx=1, pady=1)


        # Right side IMAGE
        img3 = Image.open("/Users/pop/Downloads/banners - alertpress/POWER TOOLS (2).gif")
        img3 = img3.resize((550, 300), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        label_img = Label(self.master, image = self.photoimg3, bd=0, relief=RIDGE)
        label_img.place(x=650, y=57, width=550, height=225)




        ######### MySQL TABLE FRAME #########
        mysql_table_frame = LabelFrame(self.master, bd=2, relief=RIDGE, text="Booking Search System", font=("arial", 12, "bold"), padx=2)
        mysql_table_frame.place (x=378, y=290, width=825, height=260)


        # Search LABEL
        label_search = Label(mysql_table_frame, text = "Filter By", bg="yellow", fg="black")
        label_search.grid(row=0, column=0, sticky=W, padx=2)


        # Search COMBOBOX
        self.search_var=StringVar()
        self.search_columns = {
            "Hotel Location": "HotelLocation",
            "Booking ID": "BookingID",
            "Check-in Date": "checkinDate",
            "Check-out Date": "checkoutDate",
            "Room Type": "RoomType",
        }

        combobox_search = ttk.Combobox(mysql_table_frame, textvariable=self.search_var,font=("arial", 13, "bold"), width=24, state="readonly")
        combobox_search["value"] = list(self.search_columns.keys())
        combobox_search.current(0)
        combobox_search.grid(row=0, column=1, padx=2)


        # Search INPUT
        self.search_input=StringVar()
        search_input = ttk.Entry(mysql_table_frame, width=24, textvariable=self.search_input, font=("arial", 13, "bold"))
        search_input.grid(row=0, column=2, padx=2)


        # Search BUTTON
        search_button = Button(mysql_table_frame, text="Search Details", command=self.search_data, font=("arial", 10, "bold"), bg="black",
                               fg="gold", width=10)
        search_button.grid(row=0, column=3, padx=2, pady=2)

        # ShowAll BUTTON
        show_all_button = Button(mysql_table_frame, text="Show All Details", command=self.fetch_data,  font=("arial", 10, "bold"), bg="black",
                                 fg="gold", width=10)
        show_all_button.grid(row=0, column=4, padx=2, pady=2)





        ######### DISPLAY DATA TABLE FRAME #########

        display_data_table = Frame(mysql_table_frame, bd=2, relief=RIDGE)
        display_data_table.place(x=3, y=38, width=810, height=200)


        # SCROLL BAR
        scroll_horizontal = ttk.Scrollbar(display_data_table, orient=HORIZONTAL)
        scroll_vertical = ttk.Scrollbar(display_data_table, orient=VERTICAL)

        # TREEVIEW
        self.reservation_data = ttk.Treeview(display_data_table,
                                          columns=("CustomerID", "BookingID", "HotelLocation",  "checkinDate", "checkoutDate", "RoomType",
                                                   "RoomNumber", "PurposeOfStay", "Adults", "Children", "SpecialNote",
                                                   "Discount", "VAT", "TotalCost", "PaymentMethod"),
                                          xscrollcommand=scroll_horizontal.set,
                                          yscrollcommand=scroll_vertical.set)
        # Place scrollbars
        scroll_horizontal.pack(side=BOTTOM, fill=X)
        scroll_vertical.pack(side=RIGHT, fill=Y)

        # Configure scrollbars to control the Treeview
        scroll_horizontal.config(command=self.reservation_data.xview)
        scroll_vertical.config(command=self.reservation_data.yview)

        # Place Treeview
        self.reservation_data.pack(fill=BOTH, expand=True)
        self.reservation_data.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        # Configure Treeview Headings
        for col in ("CustomerID", "BookingID","HotelLocation", "checkinDate", "checkoutDate", "RoomType",
                    "RoomNumber", "PurposeOfStay", "Adults", "Children", "SpecialNote",
                    "Discount", "VAT", "TotalCost", "PaymentMethod"):
            self.reservation_data.heading(col, text=col)
            self.reservation_data.column(col, width=110, stretch=False)

        # Display only the defined columns
        self.reservation_data["show"] = 'headings'

        self.reservation_data.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()




    def insert_data(self):
        if self.search_customer_input.get()=="" or self.var_checkinDate.get()=="":
            messagebox.showerror("Try again..", "Fill all the required fields ", parent=self.master)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
                my_cursor=conn.cursor()

                # Insert reservation details into the database
                my_cursor.execute("insert into reservations values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                    self.search_customer_input.get(),
                    self.var_bookingID.get(),
                    self.var_hotel_location.get(),
                    self.var_checkinDate.get(),
                    self.var_checkoutDate.get(),
                    self.var_room_type.get(),
                    self.var_available_rooms.get(),
                    self.var_purpose_of_stay.get(),
                    self.var_adults.get(),
                    self.var_children.get(),
                    self.var_special_note.get(),
                    self.var_discount.get(),
                    self.var_VAT.get(),
                    self.var_total_cost.get(),
                    self.var_payment_method.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "The reservation details have been saved!", parent=self.master)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.master)



    def apply_discount(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
            my_cursor = conn.cursor()

            # Fetch Customer Type from Database
            customer_id = self.search_customer_input.get()
            my_cursor.execute("SELECT CustomerType FROM customer WHERE CustomerID = %s", (customer_id,))
            customer_type = my_cursor.fetchone()

            if not customer_type:
                messagebox.showerror("Error", "Customer not found. Please check Customer ID.", parent=self.master)
                conn.close()
                return

            customer_type = customer_type[0].lower()  # Ensure case insensitivity

            # Apply Discount Based on Customer Type
            if customer_type == "premium":
                discount_value = "10"  # Example: 10% discount for Premium customers
                self.var_discount.set(discount_value)
                self.var_VAT.set("0")  # Clear special note for Premium customers
            else:
                discount_value = "0"  # No discount for Standard customers
                self.var_discount.set(discount_value)
                self.var_VAT.set("20")

            conn.close()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch customer type: {str(e)}", parent=self.master)




    def update_data(self):
        if self.search_customer_input.get()=="":
            messagebox.showerror("Try again...", "Select customer details", parent=self.master)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("""UPDATE reservations SET HotelLocation=%s, checkinDate=%s, checkoutDate=%s, 
                                                                RoomType=%s, RoomNumber=%s, PurposeOfStay=%s, Adults=%s, 
                                                                Children=%s, SpecialNote=%s, Discount=%s, VAT=%s, TotalCost=%s, 
                                                                PaymentMethod=%s WHERE BookingID=%s""",

                              (
                                  self.var_hotel_location.get(),
                                  self.var_checkinDate.get(),
                                  self.var_checkoutDate.get(),
                                  self.var_room_type.get(),
                                  self.var_available_rooms.get(),
                                  self.var_purpose_of_stay.get(),
                                  self.var_adults.get(),
                                  self.var_children.get(),
                                  self.var_special_note.get(),
                                  self.var_discount.get(),
                                  self.var_VAT.get(),
                                  self.var_total_cost.get(),
                                  self.var_payment_method.get(),
                                  self.var_bookingID.get()
                              ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Reservation details has been updated succesfully", parent=self.master)




    def reset_data(self):
        # self.search_customer_input.set(""),
        # self.var_bookingID.set(""),
        # self.var_hotel_location.set(""),
        self.var_checkinDate.set(""),
        self.var_checkoutDate.set(""),
        # self.var_room_type.set(""),
        self.var_available_rooms.set(""),
        # self.var_purpose_of_stay.set(""),
        self.var_adults.set(""),
        self.var_children.set(""),
        self.var_special_note.set(""),
        self.var_discount.set(""),
        self.var_VAT.set(""),
        self.var_total_cost.set(""),
        # self.var_payment_method.set("")

        x = random.randint(1000,9999)
        self.var_bookingID.set(str(x))




    def delete_data(self):
        delete_data = messagebox.askyesno("Hotel Management System",
                                          "Would you like to delete this reservation details?", parent=self.master)
        if delete_data>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
            my_cursor = conn.cursor()
            query="DELETE FROM reservations WHERE BookingID=%s"
            value=(self.var_bookingID.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()




    ########## Data Fetch ##########
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from reservations")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.reservation_data.delete(*self.reservation_data.get_children())
            for i in rows:
                self.reservation_data.insert("", END, values=i)
            conn.commit()
        conn.close()






    def get_cursor(self, event):
        cursor_row = self.reservation_data.focus()
        content = self.reservation_data.item(cursor_row)
        row = content["values"]

        self.search_customer_input.set(row[0]),
        self.var_bookingID.set(row[1]),
        self.var_hotel_location.set(row[2]),
        self.var_checkinDate.set(row[3]),
        self.var_checkoutDate.set(row[4]),
        self.var_room_type.set(row[5]),
        self.var_available_rooms.set(row[6]),
        self.var_purpose_of_stay.set(row[7]),
        self.var_adults.set(row[8]),
        self.var_children.set(row[9]),
        self.var_special_note.set(row[10]),
        self.var_discount.set(row[11]),
        self.var_VAT.set(row[12]),
        self.var_total_cost.set(row[13]),
        self.var_payment_method.set(row[14])




    def fetch_customer_search(self):
        if self.search_customer_input.get() == "":
            messagebox.showerror("Try again...", "Please select a customer or provide search input", parent=self.master)
            return
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
            my_cursor = conn.cursor()

            try:
                # Check if searching a customer or a reservation
                selected_column = self.search_customer_combobox.get()
                db_column = self.search_customer_columns.get(selected_column, selected_column)

                # Query for customer details
                query_customer = (f"SELECT CustomerID, FullName, DateofBirth, Gender, Address, Postcode, PhoneNumber, "
                                  f"Email, Country, CustomerType FROM customer WHERE {db_column} LIKE %s")
                value_customer = ("%" + self.search_customer_input.get() + "%",)
                my_cursor.execute(query_customer, value_customer)
                customer_rows = my_cursor.fetchmany(1)

                if not customer_rows:
                    messagebox.showinfo("No Results", "No matching customer found.", parent=self.master)
                    return


                # Apply Discount Based on Customer Type
                self.apply_discount()


                # Display customer details
                display_data_frame = Frame(self.master, bd=4, relief=RIDGE, padx=2)
                display_data_frame.place(x=380, y=57, width=260, height=225)

                labels = ["CustomerID", "Full Name", "Date of Birth", "Gender", "Address", "Postcode",
                          "Phone Number", "Email", "Country", "Customer Type"]
                for i, label in enumerate(labels):
                    Label(display_data_frame, text=f"{label}:", font=("arial", 12, "bold")).place(x=0, y=i * 22)
                    Label(display_data_frame, text=customer_rows[0][i], font=("arial", 12, "bold")).place(x=120, y=i * 22)

                # Query for reservation details
                selected_reservation_column = self.search_var.get()
                reservation_column = self.search_columns.get(selected_reservation_column, selected_reservation_column)
                query_reservation = f"SELECT * FROM reservations WHERE {reservation_column} LIKE %s"
                value_reservation = ("%" + self.search_customer_input.get() + "%",)
                my_cursor.execute(query_reservation, value_reservation)
                reservation_rows = my_cursor.fetchall()

                if reservation_rows:
                    self.reservation_data.delete(*self.reservation_data.get_children())
                    for row in reservation_rows:
                        self.reservation_data.insert("", END, values=row)

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.master)
            finally:
                conn.close()



    # def fetch_customer_search(self):
    #     if self.search_customer_input.get() == "":
    #         messagebox.showerror("Try again...", "Please select a customer", parent=self.master)
    #         return
    #     else:
    #         conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
    #         my_cursor=conn.cursor()
    #         query= "SELECT CustomerID FROM customer WHERE CustomerID=%s"
    #         value=(self.search_customer_input.get(),)
    #         my_cursor.execute(query, value)
    #         row=my_cursor.fetchone()
    #
    #         if row is None:
    #             messagebox.showerror("Try again...","The specified details could not be found", parent=self.master)
    #         else:
    #             conn.commit()
    #             conn.close()
    #
    #             display_data_frame = Frame(self.master, bd=4, relief=RIDGE, padx=2)
    #             display_data_frame.place(x=380, y=57, width=260, height=225)
    #
    #
    #
    #             # Display Window - Customer ID Label
    #             display_customerID_label = Label(display_data_frame, text="CustomerID:", font=("arial", 12, "bold"))
    #             display_customerID_label.place(x=0, y=0)
    #
    #             display_customerID_output = Label(display_data_frame, text = row, font=("arial", 12, "bold"))
    #             display_customerID_output.place(x=95, y=0)
    #
    #
    #
    #             # Display Window - Full Name Label
    #             conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
    #             my_cursor=conn.cursor()
    #             query= "SELECT FullName FROM customer WHERE CustomerID=%s"
    #             value=(self.search_customer_input.get(),)
    #             my_cursor.execute(query, value)
    #             row=my_cursor.fetchone()
    #
    #             display_fullName_label = Label(display_data_frame, text="Full Name:", font=("arial", 12, "bold"))
    #             display_fullName_label.place(x=0, y=22)
    #
    #             display_fullName_output = Label(display_data_frame, text = row, font=("arial", 12, "bold"))
    #             display_fullName_output.place(x=95, y=22)
    #
    #
    #
    #
    #
    #
    #             # Display Window - Date of Birth Label
    #             conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
    #             my_cursor=conn.cursor()
    #             query= "SELECT DateofBirth FROM customer WHERE CustomerID=%s"
    #             value=(self.search_customer_input.get(),)
    #             my_cursor.execute(query, value)
    #             row=my_cursor.fetchone()
    #
    #             display_dob_label = Label(display_data_frame, text="Date of Birth:", font=("arial", 12, "bold"))
    #             display_dob_label.place(x=0, y=44)
    #
    #             display_dob_output = Label(display_data_frame, text = row, font=("arial", 12, "bold"))
    #             display_dob_output.place(x=95, y=44)
    #
    #
    #
    #
    #
    #             # Display Window - Gender Label
    #             conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
    #             my_cursor=conn.cursor()
    #             query= "SELECT Gender FROM customer WHERE CustomerID=%s"
    #             value=(self.search_customer_input.get(),)
    #             my_cursor.execute(query, value)
    #             row=my_cursor.fetchone()
    #
    #             display_gender_label = Label(display_data_frame, text="Gender:", font=("arial", 12, "bold"))
    #             display_gender_label.place(x=0, y=66)
    #
    #             display_gender_output = Label(display_data_frame, text = row, font=("arial", 12, "bold"))
    #             display_gender_output.place(x=95, y=66)
    #
    #
    #
    #
    #
    #             # Display Window - Address Label
    #             conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
    #             my_cursor=conn.cursor()
    #             query= "SELECT Address FROM customer WHERE CustomerID=%s"
    #             value=(self.search_customer_input.get(),)
    #             my_cursor.execute(query, value)
    #             row=my_cursor.fetchone()
    #
    #             display_address_label = Label(display_data_frame, text="Address:", font=("arial", 12, "bold"))
    #             display_address_label.place(x=0, y=88)
    #
    #             display_address_output = Label(display_data_frame, text = row, font=("arial", 12, "bold"))
    #             display_address_output.place(x=95, y=88)
    #
    #
    #
    #
    #
    #
    #             # Display Window - Postcode Label
    #             conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
    #             my_cursor=conn.cursor()
    #             query= "SELECT Postcode FROM customer WHERE CustomerID=%s"
    #             value=(self.search_customer_input.get(),)
    #             my_cursor.execute(query, value)
    #             row=my_cursor.fetchone()
    #
    #             display_postcode_label = Label(display_data_frame, text="Postcode:", font=("arial", 12, "bold"))
    #             display_postcode_label.place(x=0, y=110)
    #
    #             display_postcode_output = Label(display_data_frame, text = row, font=("arial", 12, "bold"))
    #             display_postcode_output.place(x=95, y=110)
    #
    #
    #
    #
    #
    #
    #             # Display Window - Phone Number Label
    #             conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
    #             my_cursor=conn.cursor()
    #             query= "SELECT PhoneNumber FROM customer WHERE CustomerID=%s"
    #             value=(self.search_customer_input.get(),)
    #             my_cursor.execute(query, value)
    #             row=my_cursor.fetchone()
    #
    #             display_phoneNumber_label = Label(display_data_frame, text="Phone Number:", font=("arial", 12, "bold"))
    #             display_phoneNumber_label.place(x=0, y=132)
    #
    #             display_phoneNumber_output = Label(display_data_frame, text = row, font=("arial", 12, "bold"))
    #             display_phoneNumber_output.place(x=95, y=132)
    #
    #
    #
    #
    #
    #
    #             # Display Window - Email Address Label
    #             conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
    #             my_cursor=conn.cursor()
    #             query= "SELECT Email FROM customer WHERE CustomerID=%s"
    #             value=(self.search_customer_input.get(),)
    #             my_cursor.execute(query, value)
    #             row=my_cursor.fetchone()
    #
    #             display_email_label = Label(display_data_frame, text="Email:", font=("arial", 12, "bold"))
    #             display_email_label.place(x=0, y=154)
    #
    #             display_email_output = Label(display_data_frame, text = row, font=("arial", 12, "bold"))
    #             display_email_output.place(x=95, y=154)
    #
    #
    #
    #
    #
    #
    #             # Display Window - Country Label
    #             conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
    #             my_cursor=conn.cursor()
    #             query= "SELECT Country FROM customer WHERE CustomerID=%s"
    #             value=(self.search_customer_input.get(),)
    #             my_cursor.execute(query, value)
    #             row=my_cursor.fetchone()
    #
    #             display_country_label = Label(display_data_frame, text="Country:", font=("arial", 12, "bold"))
    #             display_country_label.place(x=0, y=174)
    #
    #             display_country_output = Label(display_data_frame, text = row, font=("arial", 12, "bold"))
    #             display_country_output.place(x=95, y=174)
    #
    #
    #
    #
    #
    #
    #             # Display Window - Customer Type Label
    #             conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
    #             my_cursor=conn.cursor()
    #             query= "SELECT CustomerType FROM customer WHERE CustomerID=%s"
    #             value=(self.search_customer_input.get(),)
    #             my_cursor.execute(query, value)
    #             row=my_cursor.fetchone()
    #
    #             display_customerType_label = Label(display_data_frame, text="Customer Type:", font=("arial", 12, "bold"))
    #             display_customerType_label.place(x=0, y=196)
    #
    #             display_customerType_output = Label(display_data_frame, text = row, font=("arial", 12, "bold"))
    #             display_customerType_output.place(x=95, y=196)



    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
        my_cursor = conn.cursor()

        try:
            # Get the selected column and its database equivalent
            selected_column = self.search_var.get()
            db_column = self.search_columns.get(selected_column, selected_column)  # Default to selected_column

            # Prepare the query
            query = f"SELECT * FROM reservations WHERE {db_column} LIKE %s"
            value = ("%" + self.search_input.get() + "%",)

            # Execute the query
            my_cursor.execute(query, value)
            rows = my_cursor.fetchall()

            if len (rows)!=0:
                self.reservation_data.delete(*self.reservation_data.get_children())
                for i in rows:
                    self.reservation_data.insert("", END, values=i)
            else:
                messagebox.showinfo("No Results", "No matching records found.", parent=self.master)
            conn.commit()
        finally:
            conn.close()





    def total(self):
        try:
            # Parse the check-in and check-out dates
            checkin_date = datetime.strptime(self.var_checkinDate.get(), "%d/%m/%Y")
            checkout_date = datetime.strptime(self.var_checkoutDate.get(), "%d/%m/%Y")

            # Calculate the number of days
            num_days = (checkout_date - checkin_date).days
            if num_days <= 0:
                raise ValueError("Check-out date must be after check-in date.")

            # Validate room availability
            if not self.var_available_rooms.get().isdigit() or int(self.var_available_rooms.get()) <= 0:
                raise ValueError("No rooms available for the selected type.")

            # Room base rate
            room_type_rates = {
                "Single": 100,
                "Double": 150,
                "Twin Deluxe": 200,
                "Queen Deluxe": 250,
                "King Deluxe": 300,
                "King Executive": 400,
                "Presidential Suite": 500,
            }
            room_rate = room_type_rates.get(self.var_room_type.get(), 100)  # Default to £100 if not listed

            # Calculate the total cost before VAT and discounts
            base_cost = room_rate * num_days

            # Apply discount
            discount = float(self.var_discount.get() or 0)  # Default to 0 if no discount is entered
            discount_amount = base_cost * (discount / 100)

            # Calculate VAT
            vat = float(self.var_VAT.get() or 0)  # Default to 0 if no VAT is entered
            vat_amount = (base_cost - discount_amount) * (vat / 100)

            # Final total cost
            total_cost = base_cost - discount_amount + vat_amount

            # Update payment details
            self.var_total_cost.set(f"£{total_cost:.2f}")

            # Display calculation details
            messagebox.askyesnocancel(
                "Calculation Details",
                f"Initial Cost: £{base_cost:.2f}\n"
                f"Discount ({discount}%): -£{discount_amount:.2f}\n"
                f"VAT ({vat}%): +£{vat_amount:.2f}\n"
                f"Total Cost: £{total_cost:.2f}\n"
                f"\n"
                f"Would you like to Pay Now?",
                parent=self.master,
            )
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}", parent=self.master)


if __name__ == "__main__":
    master = Tk()
    obj = Reservations(master)
    master.mainloop()