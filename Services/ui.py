from Base.User import User
from Services.Bookmark import Bookmark
from Services.weather import Weather
from Services.Dairy import Diary

class UI:

    def __init__(self):
        self.user = User("profile")
        self.bookmark = Bookmark()
        self.weather = Weather()
        self.diary = Diary()

    def show_login_info(self):
        print("\n========= Weather Diary =========")
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        print("=================================")

    def start(self):
        while True:
            self.show_login_info()

            try:
                choice = int(input("Enter your choice: "))
            except:
                print("Invalid input ")
                continue

            if choice == 1:
                username = self.login()
                if username:
                    self.main_menu(username)

            elif choice == 2:
                self.signup()

            elif choice == 3:
                print("Thank You ")
                break

            else:
                print("Invalid choice ")

    def login(self):
        data = self.user.read()

        if not data:
            print("No users found. Please sign up ")
            return None

        attempts = 0

        
        while attempts < 3:
            username = input("Enter Username: ")

            if username in data and data[username]["disable"] == True:
                print("Your Account is already disabled")

            password = input("Enter Password: ")

            hashed = self.user.hash_password(password)

            if username in data and data[username]["password"] == hashed:
                return username
            
            else:
                print("Invalid username or password ")
                attempts += 1

        print("Too many failed attempts. Exiting ")
        exit()

    def signup(self):
        data = self.user.read()

        name = input("Enter Name: ")

        email = input("Enter Email: ")
        if "@" not in email or "." not in email.split("@")[-1]:
            print("Invalid email")
            return

        username = input("Enter Username: ")

        if len(username) < 4 or " " in username:
            print("Invalid username")
            return
        
        elif username in data:
            print("Username already exists")
            return

        attempts = 3

        while attempts > 0:
            password = input("Enter Password: ")

            if len(password) >= 6 and any(c.isdigit() for c in password):
                break

            else:
                attempts -= 1
                print(f"Weak password , Try Again")

        if attempts == 0:
            print("Too many failed attempts")
            return

        hashed = self.user.hash_password(password)

        data[username] = {
            "name": name,
            "email": email,
            "password": hashed,
            "disable": False
        }

        self.user.write(data)

        print("Account created successfully. Please login")

    def main_menu(self, username):
        while True:
            data = self.user.read()
            name = data[username]["name"]

            print(f"\n====== Weather Diary | Hi, {name} ===")
            print("1. Add bookmarked city")
            print("2. Remove bookmarked city")
            print("3. View bookmarked cities")
            print("4. Check weather for a city")
            print("5. View diary entries")
            print("6. Filter diary by city")
            print("7. View diary statistics")
            print("8. Logout")
            print("9. Disable a user")
            print("10. Exit")
            print("========================================")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.bookmark.add_city(username)

            elif choice == "2":
                self.bookmark.remove_city(username)

            elif choice == "3":
                self.bookmark.view_cities(username)

            elif choice == "4":
                city = input("Enter city name: ")
                weather = self.weather.get_weather(city)

                if weather:
                    print("\nWeather Details ")
                    print(f"City: {weather['city']}")
                    print(f"Temperature: {weather['temperature']}°C")
                    print(f"Description: {weather['description']}")
                    print(f"Humidity: {weather['humidity']}%")
                    print(f"Wind: {weather['wind']} km/h")

                    print("\n1. Add note")
                    print("2. Go back")

                    option = int(input("Enter choice: "))

                    if option == 1:
                        note = input("Enter your note: ")
                    elif option == 2:
                        note = ""
                    else:
                        note = ""
                        print("Invalid Choice, Without Note entry has saved")

                    self.diary.add_entry(username, weather, note)

            elif choice == "5":
                self.diary.view_entries(username)

            elif choice == "6":
                self.diary.filter_by_city(username)

            elif choice == "7":
                self.diary.statistics(username)

            elif choice == "8":
                print("You have been logged out ")
                return
            
            elif choice == "9":
                d_name = input("Enter the Username to disable : ")
                data = self.user.read()

                if d_name not in data:
                    print("User not found")

                elif data[d_name].get("disable") == True:
                    print("This user is already disabled")

                else:
                    data[d_name]["disable"] = True

                    self.user.write(data)
                    print("User disabled successfully")


            elif choice == "10":
                print("bye Byeee!!! ")
                exit()
