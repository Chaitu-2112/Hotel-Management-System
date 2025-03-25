class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True
        self.guest_name = None

    def book_room(self, guest_name):
        if self.is_available:
            self.is_available = False
            self.guest_name = guest_name
            print(f"Room {self.room_number} booked successfully for {guest_name}.")
        else:
            print(f"Room {self.room_number} is already booked.")

    def check_out(self):
        if not self.is_available:
            print(f"{self.guest_name} checked out from Room {self.room_number}.")
            self.is_available = True
            self.guest_name = None
        else:
            print(f"Room {self.room_number} is already available.")

    def show_details(self):
        status = "Available" if self.is_available else f"Booked by {self.guest_name}"
        print(f"Room {self.room_number} ({self.room_type}) - {status} - ₹{self.price}/night")


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room_number, room_type, price):
        room = Room(room_number, room_type, price)
        self.rooms.append(room)

    def show_available_rooms(self):
        print("\nAvailable Rooms:")
        for room in self.rooms:
            if room.is_available:
                room.show_details()

    def book_room(self, room_number, guest_name):
        for room in self.rooms:
            if room.room_number == room_number:
                
                room.book_room(guest_name)
                return
        print("Invalid room number.")

    def check_out(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                room.check_out()
                return
        print("Invalid room number.")

    def show_all_rooms(self):
        print("\nAll Rooms:")
        for room in self.rooms:
            room.show_details()


# Main Program
hotel = Hotel("Grand Palace")

# Adding Rooms
hotel.add_room(101, "Single", 2000)
hotel.add_room(102, "Double", 3000)
hotel.add_room(103, "Suite", 5000)

while True:
    print("\nHotel Management System")
    print("1. Show Available Rooms")
    print("2. Book a Room")
    print("3. Check Out")
    print("4. Show All Rooms")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        hotel.show_available_rooms()
    elif choice == "2":
        room_no = int(input("Enter Room Number: "))
        guest_name = input("Enter Guest Name: ")
        hotel.book_room(room_no, guest_name)
    elif choice == "3":
        room_no = int(input("Enter Room Number: "))
        hotel.check_out(room_no)
    elif choice == "4":
        hotel.show_all_rooms()
    elif choice == "5":
        print("Exiting Hotel Management System.")
        break
    else:
        print("Invalid choice. Try again.")
