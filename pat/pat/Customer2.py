from tkinter import *  # Required for GUI setup
from PIL import ImageTk, Image  # Required for handling image data (e.g., loading images)
from tkinter import ttk


class CustomerDetails:
    def __init__(self,root):
        self.root = root
        # self.root.title ("Customer Details")
        # self.root.geometry ("700x400+0+260")

        CustomerWindow = Frame(self.root, border = 2, relief = RIDGE)
        CustomerWindow.place (x = 5, y = 50, width = 500, height = 500)

        # customer details
        # customer label
        customer_name = Label (CustomerWindow, text = "Full Name", font = ("Times New Roman", 12, "bold"), fg = "black", cursor ="hand2")
        customer_name.grid (row = 0, column = 0, sticky = W)

        # customer name input
        customer_name_input = ttk.Entry(CustomerWindow, width=29, font=("Arial", 12, "bold"))
        customer_name_input.grid (row=0, column=1)

        # customer address
        customer_address = Label(CustomerWindow, text="Address", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2")
        customer_address.grid(row=1, column=0, sticky=W)

        # customer address input
        customer_address_input = ttk.Entry(CustomerWindow, width=29, font=("Arial", 12, "bold"))
        customer_address_input.grid(row=1, column=1)

        # customer email
        customer_email = Label(CustomerWindow, text="Email", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2")
        customer_email.grid(row=2, column=0, sticky=W)

        # customer email input
        customer_email_input = ttk.Entry(CustomerWindow, width=29, font=("Arial", 12, "bold"))
        customer_email_input.grid(row=2, column=1)

        # customer Phone Number
        customer_phone_number = Label(CustomerWindow, text="Phone Number", font=("Times New Roman", 12, "bold"), fg="black",cursor="hand2")
        customer_phone_number.grid(row=3, column=0, sticky=W)

        # customer Phone Number input
        customer_phone_number_input = ttk.Entry(CustomerWindow, width=29, font=("Arial", 12, "bold"))
        customer_phone_number_input.grid(row=3, column=1)

        # customer reward combo box
        customer_reward = Label(CustomerWindow, text="Customer Type", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        customer_reward.grid(row=4, column=0, sticky=W)

        # customer reward combo box
        customer_reward_combo_box = ttk.Combobox(CustomerWindow, width=27, font=("Arial", 12, "bold"))
        customer_reward_combo_box ["value"] = ("Standard", "Premium")
        customer_reward_combo_box.grid(row=4, column=1)



if __name__ == "__main__":
    root = Tk()
    object = CustomerDetails (root)
    root.mainloop()