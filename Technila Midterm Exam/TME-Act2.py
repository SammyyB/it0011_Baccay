date_input = input("Enter the date in the format mm/dd/yyyy: ")
month, day, year = date_input.split("/")

months = ["January", "Febuary", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

month_name = months[int(month) - 1]
print(f"Date Output: {month_name} {int(day)}, {year}")