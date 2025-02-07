from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Room:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Room Management")
        self.master.geometry("1215x560+0+260")


        # Initialize variables for room details
        self.var_room_no=StringVar()
        x=random.randint(00, 50)
        self.var_room_no.set(str(x))

        self.var_floor=StringVar()
        y=random.randint(00, 25)
        self.var_floor.set(str(y))


        # TITLE BANNER
        # Set up the title banner
        label_title = Label(self.master, text="Room Management System", font =("arial", 27, "bold"),
                            bg = "black", fg = "gold", bd = 4, relief = RIDGE)
        label_title.place(x=0, y=0, width=1215, height=50)


        # COMPANY LOGO
        # Display company logo
        img2 = Image.open("/Users/pop/Downloads/banners - alertpress/POWER TOOLS (2).gif")
        img2 = img2.resize((100, 40), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        label_img = Label(self.master, image = self.photoimg2, bd=0, relief=RIDGE)
        label_img.place(x=1110, y=5, width=100, height=40)


        ######### Label Frame Left Side #########
        # Left-side label frame for room management inputs
        labelframe_ls = LabelFrame(self.master, bd = 2, relief = RIDGE, text = "Manage Rooms",
                                   font = ("arial", 12, "bold"), padx = 2)
        labelframe_ls.place(x=5, y=50, width=540, height=350)


        # Hotel Location Label
        label_hotel_location = Label(labelframe_ls, text = "Hotel Location",
                                     font=("arial", 12, "bold"), padx=2, pady=6)
        label_hotel_location.grid(row=0, column=0, sticky=W)

        # Hotel Location COMBOBOX
        self.var_hotel_location=StringVar()
        combobox_hotel_location = ttk.Combobox(labelframe_ls, textvariable=self.var_hotel_location,font=("arial", 13, "bold"), width=27, state="readonly")
        combobox_hotel_location["value"]=("Manchester", "London", "New York", "Bucharest", "Warsaw", "Las Vegas", "Montreal", "Amsterdam")
        combobox_hotel_location.current(0)
        combobox_hotel_location.grid(row=0, column=1)


        # Floor Label
        label_floor_level = Label(labelframe_ls, text = "Floor Level",
                                 font=("arial", 12, "bold"), padx=2, pady=6)
        label_floor_level.grid(row=1, column=0, sticky=W)

        # Floor Input
        floor_level_input = ttk.Entry(labelframe_ls, textvariable=self.var_floor, width=28 ,font=("arial", 13, "bold"))
        floor_level_input.grid(row=1, column=1)

        # Room Number Label
        label_room_no = Label(labelframe_ls, text = "Room Number",
                                  font=("arial", 12, "bold"), padx=2, pady=6)
        label_room_no.grid(row=2, column=0, sticky=W)

        # Room Number Input
        room_no_input = ttk.Entry(labelframe_ls, textvariable=self.var_room_no, width=28,font=("arial", 13, "bold"))
        room_no_input.grid(row=2, column=1)

        # Room Type Label
        label_room_type = Label(labelframe_ls, text = "Room Type",
                                  font=("arial", 12, "bold"), padx=2, pady=6)
        label_room_type.grid(row=3, column=0, sticky=W)

        # Room Type COMBOBOX
        self.var_room_type=StringVar()
        combobox_room_type = ttk.Combobox(labelframe_ls, textvariable=self.var_room_type, font=("arial", 13, "bold"), width=27, state="readonly")
        combobox_room_type["value"]=("Single", "Double", "Twin Deluxe", "Queen Deluxe", "King Deluxe", "King Executive", "Presidential Suite")
        combobox_room_type.current(0)
        combobox_room_type.grid(row=3, column=1)

        # Room Price Label
        label_room_price = Label(labelframe_ls, text = "Room Price",
                                font=("arial", 12, "bold"), padx=2, pady=6)
        label_room_price.grid(row=4, column=0, sticky=W)

        # Room Price Input
        self.var_room_price=StringVar()
        room_price_input = ttk.Entry(labelframe_ls, textvariable=self.var_room_price, width=28,font=("arial", 13, "bold"))
        room_price_input.grid(row=4, column=1)






        ######### BUTTON FRAME #########
        button_frame = Frame(labelframe_ls, bd=0, relief=RIDGE)
        button_frame.place(x=0, y=200, width=205, height=25)


        # ADD RESERVATION
        add_room_button = Button(button_frame, text="Add", command=self.insert_data, font=("arial", 11, "bold"), bg="black",
                                     fg="gold", width=2)
        add_room_button.grid(row=0, column=0, padx=1, pady=1)


        # UPDATE RESERVATION
        update_room_button = Button(button_frame, text="Update", command=self.update_data, font=("arial", 11, "bold"), bg="black",
                                        fg="gold", width=2)
        update_room_button.grid(row=0, column=1, padx=1, pady=1)


        # RESET RESERVATION
        reset_room_button = Button(button_frame, text="Reset", command=self.reset_data, font=("arial", 11, "bold"), bg="black",
                                       fg="gold", width=2)
        reset_room_button.grid(row=0, column=2, padx=1, pady=1)


        # DELETE RESERVATION
        delete_room_button = Button(button_frame, text="Delete", command=self.delete_data, font=("arial", 11, "bold"), bg="black",
                                        fg="gold", width=2)
        delete_room_button.grid(row=0, column=3, padx=1, pady=1)






        ######### MySQL TABLE FRAME #########
        # Frame for displaying room details in a table
        mysql_table_frame = LabelFrame(self.master, bd=2, relief=RIDGE, text="Room Details", font=("arial", 12, "bold"), padx=2)
        mysql_table_frame.place (x=600, y=50, width=600, height=350)


        # SCROLL BAR
        # Horizontal and vertical scrollbars for the table
        scroll_horizontal = ttk.Scrollbar(mysql_table_frame, orient=HORIZONTAL)
        scroll_vertical = ttk.Scrollbar(mysql_table_frame, orient=VERTICAL)

        # TREEVIEW
        # Configure Treeview (table) for room details
        self.room_data = ttk.Treeview(mysql_table_frame,
                                          columns=("HotelLocation", "RoomNumber", "FloorLevel", "RoomType",  "RoomPrice"),
                                          xscrollcommand=scroll_horizontal.set,
                                          yscrollcommand=scroll_vertical.set)
        # Setup and place scrollbars
        scroll_horizontal.pack(side=BOTTOM, fill=X)
        scroll_vertical.pack(side=RIGHT, fill=Y)

        # Configure scrollbars to control the Treeview
        scroll_horizontal.config(command=self.room_data.xview)
        scroll_vertical.config(command=self.room_data.yview)

        # Add columns and headings to the Treeview
        for col in ("HotelLocation", "RoomNumber", "FloorLevel", "RoomType", "RoomPrice"):
            self.room_data.heading(col, text=col)
            self.room_data.column(col, width=150, stretch=False)

        # Show only column headings
        self.room_data["show"] = "headings"
        self.room_data.pack(fill=BOTH, expand=True)

        # Bind event to capture selected row
        self.room_data.bind("<ButtonRelease-1>", self.get_cursor)

        # Fetch initial data
        self.fetch_data()




    def insert_data(self):
        # Insert new room details into the database
        # Ensure no fields are empty before proceeding
        if self.var_floor.get()=="" or self.var_room_type.get()=="" or self.var_hotel_location.get()=="" or self.var_room_no.get()=="" or self.var_room_price.get()=="":
            messagebox.showerror("Try again..", "Fill all the required fields ", parent=self.master)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO room VALUES(%s, %s, %s, %s, %s)",(
                    self.var_hotel_location.get(),
                    self.var_room_no.get(),
                    self.var_floor.get(),
                    self.var_room_type.get(),
                    self.var_room_price.get(),
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "The room details have been saved!", parent=self.master)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong:{str(es)}", parent=self.master)





    def update_data(self):
        # Update selected room details in the database
        if self.var_floor.get()=="" or self.var_room_type.get()=="" or self.var_hotel_location.get()=="" or self.var_room_no.get()=="" or self.var_room_price.get()=="":
            messagebox.showerror("Try again...", "Select room details", parent=self.master)
            return

        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("""UPDATE room SET HotelLocation=%s, RoomNumber=%s, FloorLevel=%s, 
                                                                RoomType=%s, RoomPrice=%s  WHERE RoomNumber=%s""",


                              (
                                  self.var_hotel_location.get(),
                                  self.var_room_no.get(),
                                  self.var_floor.get(),
                                  self.var_room_type.get(),
                                  self.var_room_price.get(),

                                  self.var_room_no.get(), # used as the unique identifier

                              ))

            conn.commit()
            self.fetch_data()
            conn.close()


            messagebox.showinfo("Success", "Room details updated successfully", parent=self.master)
        # except Exception as es:
        #     messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.master)





    def reset_data(self):
        # Reset input fields to their default values

        # self.var_hotel_location.set(""),
        self.var_room_no.set(""),
        self.var_floor.set(""),
        # self.var_room_type.set(""),
        self.var_room_price.set(""),

        x=random.randint(00, 50)
        self.var_room_no.set(str(x))

        y=random.randint(00, 25)
        self.var_floor.set(str(y))





    def delete_data(self):
        # Delete selected room details from the database
        delete_data = messagebox.askyesno("Hotel Management System",
                                          "Would you like to delete this room details?", parent=self.master)
        if delete_data>0:
            conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
            my_cursor = conn.cursor()
            query="DELETE FROM room WHERE RoomNumber=%s"
            value=(self.var_room_no.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()







    ########## Data Fetch ##########
    def fetch_data(self):
        # Fetch room details from the database and populate the table
        conn = mysql.connector.connect(host="localhost", username="root", password="lemontree", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_data.delete(*self.room_data.get_children())
            for i in rows:
                self.room_data.insert("", END, values=i)
            conn.commit()
        conn.close()




    def get_cursor(self, event):
        # Get selected row's data and populate input fields
        cursor_row = self.room_data.focus() # Get the selected row
        content = self.room_data.item(cursor_row)
        row = content["values"]

        self.var_hotel_location.set(row[0]),
        self.var_room_no.set(row[1]),
        self.var_floor.set(row[2]),
        self.var_room_type.set(row[3]),
        self.var_room_price.set(row[4])











if __name__ == "__main__":
    master = Tk()
    obj = Room(master)
    master.mainloop()