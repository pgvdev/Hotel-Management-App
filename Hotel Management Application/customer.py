from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


# Secondary class for the Hotel Management System
class Customer:
    def __init__(self, master):
        # Initialize the main application window
        self.master = master
        self.master.title("Customer Management")
        self.master.geometry("1215x560+0+260")



        # Initialize customer variables using Tkinter StringVar for dynamic binding
        self.var_customerID=StringVar()
        x=random.randint(1000, 9999)
        self.var_customerID.set(str(x))

        # Define variables for customer attributes
        self.var_customer_title=StringVar()
        self.var_customer_name=StringVar()
        self.var_customer_dob=StringVar()
        self.var_customer_gender=StringVar()
        self.var_customer_address=StringVar()
        self.var_customer_postcode=StringVar()
        self.var_customer_phone_number=StringVar()
        self.var_customer_email=StringVar()
        self.var_customer_country=StringVar()
        self.var_customer_type=StringVar()



        # TITLE BANNER
        # Add title banner
        label_title = Label(self.master, text="Add Customer Details", font =("arial", 27, "bold"),
                            bg = "black", fg = "gold", bd = 4, relief = RIDGE)
        label_title.place(x=0, y=0, width=1215, height=50)


        # COMPANY LOGO
        # Add company logo
        img2 = Image.open("/Users/pop/Downloads/banners - alertpress/POWER TOOLS (2).gif")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        label_img = Label(self.master, image = self.photoimg2, bd=0, relief=RIDGE)
        label_img.place(x=1110, y=5, width=100, height=40)


        ######### Label Frame Left Side #########
        # Create left-side frame for customer details input
        labelframe_ls = LabelFrame(self.master, bd = 2, relief = RIDGE, text = "Customer Details",
                                   font = ("arial", 12, "bold"), padx = 2)
        labelframe_ls.place(x=5, y=50, width=365, height=500)


        # Add input fields for customer details with labels and widgets
        # Customer ID Label
        label_customer_id = Label(labelframe_ls, text = "Customer ID",
                                  font=("arial", 12, "bold"), padx=2, pady=6)
        label_customer_id.grid(row=0, column=0, sticky=W)

        # Customer ID Input (read-only as it's auto-generated)
        id_input = ttk.Entry(labelframe_ls, textvariable=self.var_customerID, width=29, state="readonly" ,font=("arial", 13, "bold"))
        id_input.grid(row=0, column=1)


        # Customer TITLE Label
        label_customer_title = Label(labelframe_ls, text = "Title",
                                      font=("arial", 12, "bold"), padx=2, pady=6)
        label_customer_title.grid(row=1, column=0, sticky=W)

        # Customer TITLE COMBOBOX
        # Select title field
        combo_title = ttk.Combobox(labelframe_ls, textvariable=self.var_customer_title, font=("arial", 13, "bold"), width=28, state="readonly")
        combo_title["value"]=("Mr.", "Mrs.", "Dr.")
        combo_title.current(0)
        combo_title.grid(row=1, column=1)


        # Customer NAME Label
        label_customer_name = Label(labelframe_ls, text = "Full Name",
                                  font=("arial", 12, "bold"), padx=2, pady=6)
        label_customer_name.grid(row=2, column=0, sticky=W)

        # Customer NAME Input
        name_input = ttk.Entry(labelframe_ls, textvariable=self.var_customer_name,width=29, font=("arial", 13, "bold"))
        name_input.grid(row=2, column=1)


        # Customer DOB Label
        label_customer_dob = Label(labelframe_ls, text = "Date of Birth",
                                    font=("arial", 12, "bold"), padx=2, pady=6)
        label_customer_dob.grid(row=3, column=0, sticky=W)

        # Customer DOB Input
        dob_input = ttk.Entry(labelframe_ls, textvariable=self.var_customer_dob,width=29, font=("arial", 13, "bold"))
        dob_input.grid(row=3, column=1)


        # Customer GENDER Label
        label_customer_gender = Label(labelframe_ls, text = "Gender",
                                  font=("arial", 12, "bold"), padx=2, pady=6)
        label_customer_gender.grid(row=4, column=0, sticky=W)

        # Customer GENDER Combobox
        combo_gender = ttk.Combobox(labelframe_ls, textvariable=self.var_customer_gender, font=("arial", 13, "bold"), width=28, state="readonly")
        combo_gender["value"]=("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=4, column=1)


        # Customer ADDRESS Label
        label_customer_address = Label(labelframe_ls, text = "Address",
                                        font=("arial", 12, "bold"), padx=2, pady=6)
        label_customer_address.grid(row=5, column=0, sticky=W)

        # Customer ADDRESS Input
        address_input = ttk.Entry(labelframe_ls, textvariable=self.var_customer_address,width=29, font=("arial", 13, "bold"))
        address_input.grid(row=5, column=1)


        # Customer POSTCODE Label
        label_customer_postcode = Label(labelframe_ls, text = "Postcode",
                                      font=("arial", 12, "bold"), padx=2, pady=6)
        label_customer_postcode.grid(row=6, column=0, sticky=W)

        # Customer POSTCODE Input
        postcode_input = ttk.Entry(labelframe_ls, textvariable=self.var_customer_postcode, width=29, font=("arial", 13, "bold"))
        postcode_input.grid(row=6, column=1)


        # Customer PHONE NUMBER Label
        label_customer_mobile = Label(labelframe_ls, text = "Phone Number",
                                        font=("arial", 12, "bold"), padx=2, pady=6)
        label_customer_mobile.grid(row=7, column=0, sticky=W)

        # Customer PHONE NUMBER Input
        mobile_input = ttk.Entry(labelframe_ls, textvariable=self.var_customer_phone_number, width=29, font=("arial", 13, "bold"))
        mobile_input.grid(row=7, column=1)


        # Customer EMAIL Label
        label_customer_email = Label(labelframe_ls, text = "Email Address",
                                      font=("arial", 12, "bold"), padx=2, pady=6)
        label_customer_email.grid(row=8, column=0, sticky=W)

        # Customer EMAIL Input
        email_input = ttk.Entry(labelframe_ls, textvariable=self.var_customer_email, width=29, font=("arial", 13, "bold"))
        email_input.grid(row=8, column=1)


        # Customer COUNTRY Label
        label_customer_country = Label(labelframe_ls, text = "Country",
                                      font=("arial", 12, "bold"), padx=2, pady=6)
        label_customer_country.grid(row=9, column=0, sticky=W)

        # Customer COUNTRY Combobox
        combo_country = ttk.Combobox(labelframe_ls, textvariable=self.var_customer_country, font=("arial", 13, "bold"), width=28, state="readonly")
        combo_country["value"]=("United Kingdom", "United States", "European")
        combo_country.current(0)
        combo_country.grid(row=9, column=1)


        # Customer REWARD Label - COMBOBOX
        label_customer_reward = Label(labelframe_ls, text = "Customer Type",
                                           font=("arial", 12, "bold"), padx=2, pady=6)
        label_customer_reward.grid(row=10, column=0, sticky=W)

        # Customer REWARD Combobox
        combo_reward = ttk.Combobox(labelframe_ls, textvariable=self.var_customer_type, font=("arial", 13, "bold"), width=28, state="readonly")
        combo_reward["value"]=("Standard", "Premium")
        combo_reward.current(0)
        combo_reward.grid(row=10, column=1)


        ######### BUTTON FRAME #########
        button_frame = Frame(labelframe_ls, bd=0, relief=RIDGE)
        button_frame.place(x=4, y=340, width=352, height=139)


        # ADD CUSTOMER
        add_customer_button = Button(button_frame, text="Submit Details", command=self.insert_data, font=("arial", 16, "bold"), bg="black",
                                     fg="gold", width=34)
        add_customer_button.grid(row=0, column=0, padx=2, pady=2)


        # UPDATE CUSTOMER
        update_customer_button = Button(button_frame, text="Update Details", command=self.update_data, font=("arial", 16, "bold"), bg="black",
                                     fg="gold", width=34)
        update_customer_button.grid(row=1, column=0, padx=2, pady=2)


        # RESET CUSTOMER
        reset_customer_button = Button(button_frame, text="Reset Details", command=self.reset_data, font=("arial", 16, "bold"), bg="black",
                                       fg="gold", width=34)
        reset_customer_button.grid(row=2, column=0, padx=2, pady=2)


        # DELETE CUSTOMER
        delete_customer_button = Button(button_frame, text="Delete Details", command=self.delete_data, font=("arial", 16, "bold"), bg="black",
                                     fg="gold", width=34)
        delete_customer_button.grid(row=3, column=0, padx=2, pady=2)


        ######### MySQL TABLE FRAME #########
        # Add MySQL table frame for displaying data
        mysql_table_frame = LabelFrame(self.master, bd=2, relief=RIDGE, text="Customer Search System", font=("arial", 12, "bold"), padx=2)
        mysql_table_frame.place (x=380, y=50, width=825, height=500)

        # Search functionality
        # Search LABEL
        label_search = Label(mysql_table_frame, text = "Filter By", bg="yellow", fg="black")
        label_search.grid(row=0, column=0, sticky=W, padx=2)


        # Search COMBOBOX
        self.search_var=StringVar()
        self.search_columns = {
            "Customer ID": "CustomerID",
            "Full Name": "FullName",
            "Date of Birth": "DateofBirth",
            "Gender": "Gender",
            "Address": "Address",
            "Postcode": "Postcode",
            "Phone Number": "PhoneNumber",
            "Email Address": "Email",
            "Country": "Country",
            "Customer Type": "CustomerType",
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
        show_all_button = Button(mysql_table_frame, text="Show All Details", command=self.fetch_data, font=("arial", 10, "bold"), bg="black",
                                     fg="gold", width=10)
        show_all_button.grid(row=0, column=4, padx=2, pady=2)



        ######### DISPLAY DATA TABLE FRAME #########

        display_data_table = Frame(mysql_table_frame, bd=2, relief=RIDGE)
        display_data_table.place(x=3, y=50, width=810, height=350)


        # SCROLL BAR
        scroll_horizontal = ttk.Scrollbar(display_data_table, orient=HORIZONTAL)
        scroll_vertical = ttk.Scrollbar(display_data_table, orient=VERTICAL)

        # TREEVIEW
        self.customer_data = ttk.Treeview(display_data_table,
                                          columns=("Customer ID", "Title", "Full Name", "Date of Birth", "Gender", "Address",
                                                    "Postcode", "Phone Number", "Email", "Country", "Customer Type"),
                                          xscrollcommand=scroll_horizontal.set,
                                          yscrollcommand=scroll_vertical.set)
        # Place scrollbars
        scroll_horizontal.pack(side=BOTTOM, fill=X)
        scroll_vertical.pack(side=RIGHT, fill=Y)

        # Configure scrollbars to control the Treeview
        scroll_horizontal.config(command=self.customer_data.xview)
        scroll_vertical.config(command=self.customer_data.yview)

        # Place Treeview
        self.customer_data.pack(fill=BOTH, expand=True)
        self.customer_data.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

        # Configure Treeview Headings
        for col in ("Customer ID", "Title", "Full Name", "Date of Birth", "Gender", "Address",
                    "Postcode", "Phone Number", "Email", "Country", "Customer Type"):
            self.customer_data.heading(col, text=col)
            self.customer_data.column(col, width=150, stretch=False)

        # Display only the defined columns
        self.customer_data["show"] = 'headings'

    def insert_data(self):
        """Insert customer data into the database."""
        # Code for inserting data...
        if self.var_customer_phone_number.get()=="" or self.var_customer_dob.get()=="":
            messagebox.showerror("Try again..", "Fill all the required fields ", parent=self.master)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                        self.var_customerID.get(),
                                        self.var_customer_title.get(),
                                        self.var_customer_name.get(),
                                        self.var_customer_dob.get(),
                                        self.var_customer_gender.get(),
                                        self.var_customer_address.get(),
                                        self.var_customer_postcode.get(),
                                        self.var_customer_phone_number.get(),
                                        self.var_customer_email.get(),
                                        self.var_customer_country.get(),
                                        self.var_customer_type.get(),

                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "The customer details have been saved!")
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.master)


    def fetch_data(self):
        """Fetch and display all customer data."""
        # Code for fetching data...
        conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.customer_data.delete(*self.customer_data.get_children())
            for i in rows:
                self.customer_data.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event):
        #Populate the input fields with the selected row's data from the Treeview.

        # Get the selected row in the Treeview
        cursor_row = self.customer_data.focus()

        # Retrieve data from the selected row
        content = self.customer_data.item(cursor_row)
        row = content["values"]

        # Ensure a row is selected before attempting to populate fields
        if row:
            # Populate input fields with the data from the selected row
            self.var_customerID.set(row[0]),
            self.var_customer_title.set(row[1]),
            self.var_customer_name.set(row[2]),
            self.var_customer_dob.set(row[3]),
            self.var_customer_gender.set(row[4]),
            self.var_customer_address.set(row[5]),
            self.var_customer_postcode.set(row[6]),
            self.var_customer_phone_number.set(row[7]),
            self.var_customer_email.set(row[8]),
            self.var_customer_country.set(row[9]),
            self.var_customer_type.set(row[10])


    def update_data(self):
        """Update customer details."""
        # Code for updating data...
        if self.var_customer_phone_number.get()=="":
            messagebox.showerror("Try again...", "Enter phone number", parent=self.master)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("""UPDATE customer SET Title=%s, FullName=%s, DateofBirth=%s, Gender=%s, Address=%s,
                              Postcode=%s, PhoneNumber=%s, Email=%s, Country=%s, CustomerType=%s WHERE CustomerID=%s""",

                              (
                                self.var_customer_title.get(),
                                self.var_customer_name.get(),
                                self.var_customer_dob.get(),
                                self.var_customer_gender.get(),
                                self.var_customer_address.get(),
                                self.var_customer_postcode.get(),
                                self.var_customer_phone_number.get(),
                                self.var_customer_email.get(),
                                self.var_customer_country.get(),
                                self.var_customer_type.get(),
                                self.var_customerID.get(),
                              ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details has been updated", parent=self.master)



    def reset_data(self):
        """Reset input fields to default values."""
        # Code for resetting fields...

        # self.var_customerID.set(""),
        # self.var_customer_title.set(""),
        self.var_customer_name.set(""),
        self.var_customer_dob.set(""),
        # self.var_customer_gender.set(""),
        self.var_customer_address.set(""),
        self.var_customer_postcode.set(""),
        self.var_customer_phone_number.set(""),
        self.var_customer_email.set(""),
        # self.var_customer_country.set(""),
        # self.var_customer_type.set("")

        x = random.randint(1000,9999)
        self.var_customerID.set(str(x))



    def delete_data(self):
        """Delete selected customer details."""
        # Code for deleting data...
        delete_data = messagebox.askyesno("Hotel Management System",
                                          "Would you like to delete this customer details?", parent=self.master)
        if delete_data>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
            my_cursor = conn.cursor()
            query="delete from customer where CustomerID=%s"
            value=(self.var_customerID.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()



    ########## Data Fetch ##########
    def search_data(self):
        """Search for customer details based on filters."""
        # Code for searching data...
        conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
        my_cursor = conn.cursor()

        try:
            # Get the selected column and its database equivalent
            selected_column = self.search_var.get()
            db_column = self.search_columns.get(selected_column, selected_column)  # Default to selected_column

            # Prepare the query
            query = f"SELECT * FROM customer WHERE {db_column} LIKE %s"
            value = ("%" + self.search_input.get() + "%",)

            # Execute the query
            my_cursor.execute(query, value)
            rows = my_cursor.fetchall()

            if len (rows)!=0:
                self.customer_data.delete(*self.customer_data.get_children())
                for i in rows:
                    self.customer_data.insert("", END, values=i)
            else:
                messagebox.showinfo("No Results", "No matching records found.", parent=self.master)
            conn.commit()
        finally:
            conn.close()



if __name__ == "__main__":
    master = Tk()
    obj = Customer(master)
    master.mainloop()