class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = self.validate_id(item_id)
        self.name = self.validate_name(name)
        self.description = description
        self.price = self.validate_price(price)

    def validate_id(self, item_id):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer.")
        return item_id

    def validate_name(self, name):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        return name.strip()
    
    def validate_price(self, price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        return price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: {self.price}"


class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self):
        print("\n==========================")
        print("[1] ADD ITEM")
        print("==========================")
        try:
            item_id = int(input("Enter Item ID: "))
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            name = input("Enter Item Name: ")
            description = input("Enter Item Description: ")
            price = float(input("Enter Item Price: "))
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
        print("==========================")

    def read_item(self):
        print("\n==========================")
        print("[2] VIEW ITEM")
        print("==========================")
        try:
            item_id = int(input("Enter Item ID to view: "))
            item = self.items.get(item_id)
            if item:
                print(item)
            else:
                print("Item not found.")
        except ValueError:
            print("Invalid input. Please enter a valid Item ID.")
        print("==========================")
    
    def update_item(self):
        print("\n==========================")
        print("[3] UPDATE ITEM")
        print("==========================")
        try:
            item_id = int(input("Enter Item ID to update: "))
            if item_id not in self.items:
                raise ValueError("Item not found.")
            name = input("Enter new name (leave blank to keep current): ")
            description = input("Enter new description (leave blank to keep current): ")
            price = input("Enter new price (leave blank to keep current): ")
            if name:
                self.items[item_id].name = self.items[item_id].validate_name(name)
            if description:
                self.items[item_id].description = description
            if price:
                self.items[item_id].price = self.items[item_id].validate_price(float(price))
            print("Item updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")
        print("==========================")
    
    def delete_item(self):
        print("\n==========================")
        print("[4] DELETE ITEM")
        print("==========================")
        try:
            item_id = int(input("Enter Item ID to delete: "))
            if item_id in self.items:
                del self.items[item_id]
                print("Item deleted successfully.")
            else:
                print("Item not found.")
        except ValueError:
            print("Invalid input. Please enter a valid Item ID.")
        print("==========================")

    def list_items(self):
        print("\n==========================")
        print("[5] LIST ALL ITEMS")
        print("==========================")
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)
        print("==========================")


def main():
    manager = ItemManager()
    while True:
        print("\n==========================")
        print(" ITEM MANAGEMENT SYSTEM ")
        print("==========================")
        print("[1] ADD ITEM")
        print("[2] VIEW ITEM")
        print("[3] UPDATE ITEM")
        print("[4] DELETE ITEM")
        print("[5] LIST ALL ITEMS")
        print("[6] EXIT")
        print("==========================")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            manager.create_item()
        elif choice == "2":
            manager.read_item()
        elif choice == "3":
            manager.update_item()
        elif choice == "4":
            manager.delete_item()
        elif choice == "5":
            manager.list_items()
        elif choice == "6":
            print("\n==========================")
            print("Exiting... Thank you!")
            print("==========================")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()