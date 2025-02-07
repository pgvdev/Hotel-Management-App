from tkinter import *  # Required for GUI setup
from PIL import ImageTk, Image  # Required for handling image data (e.g., loading images)
from tkinter import ttk


class ReservationDetails:
    def __init__(self,root):
        self.root = root
        self.root.title("Reservation Details")
        self.root.geometry("700x400+0+260")

        ReservationWindow = LabelFrame(self.root, border=2, relief=RIDGE)
        ReservationWindow.place(x=5, y=50, width=500, height=500)

        # number of rooms combo box
        number_of_rooms = Label(ReservationWindow, text="Number of Rooms", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        number_of_rooms.grid(row=0, column=0, sticky=W)

        # number of rooms combo box
        number_of_rooms_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        number_of_rooms_combo_box["value"] = ("1", "2", "3", "4", "5", "6")
        number_of_rooms_combo_box.grid(row=0, column=1)


        # booking date label
        booking_date = Label(ReservationWindow, text="Booking Date", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2")
        booking_date.grid(row=1, column=0, sticky=W)

        # booking date input
        booking_date_input = ttk.Entry(ReservationWindow, width=29, font=("Arial", 12, "bold"))
        booking_date_input.grid(row=1, column=1)

        # Purpose of Staying combo box
        purpose_of_staying = Label(ReservationWindow, text="Purpose of Staying", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        purpose_of_staying.grid(row=2, column=0, sticky=W)

        # Purpose of Staying input
        purpose_of_staying_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        purpose_of_staying_combo_box["value"] = ("Work", "Leisure")
        purpose_of_staying_combo_box.grid(row=2, column=1)


        # Room Type combo box
        room_type = Label(ReservationWindow, text="Room Type", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        room_type.grid(row=3, column=0, sticky=W)

        # Room Type input
        room_type_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        room_type_combo_box["value"] = ("Single", "Double")
        room_type_combo_box.grid(row=3, column=1)

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
        number_of_adults_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        number_of_adults_combo_box["value"] = ("1", "2", "3", "4", "5")
        number_of_adults_combo_box.grid(row=4, column=1)


        # Number of Children combo box
        number_of_children = Label(ReservationWindow, text="Number of Children", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        number_of_children.grid(row=5, column=0, sticky=W)

        # Number of Adults combo box
        number_of_children_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        number_of_children_combo_box["value"] = ("0", "1", "2", "3", "4", "5")
        number_of_children_combo_box.grid(row=5, column=1)


        # Pets Included combo box
        pets_included = Label(ReservationWindow, text="Pets Included", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        pets_included.grid(row=6, column=0, sticky=W)

        # Number of Adults combo box
        pets_included_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        pets_included_combo_box["value"] = ("Yes", "No")
        pets_included_combo_box.grid(row=6, column=1)

        # Payment Method combo box
        payment_method = Label(ReservationWindow, text="Payment Method", font=("Times New Roman", 12, "bold"), fg="black", cursor="hand2", padx=2, pady=6)
        payment_method.grid(row=7, column=0, sticky=W)

        # Payment Method combo box
        payment_method_combo_box = ttk.Combobox(ReservationWindow, width=27, font=("Arial", 12, "bold"))
        payment_method_combo_box["value"] = ("Bank Transfer", "Debit Card", "Credit Card", "PayPal", "Apple Pay", "Google Pay")
        payment_method_combo_box.grid(row=7, column=1)





if __name__ == "__main__":
    root = Tk()
    object = ReservationDetails (root)
    root.mainloop()

