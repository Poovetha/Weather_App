from Base.file import FileHandler


class Bookmark(FileHandler):

    def __init__(self):
        super().__init__("Data/bookmarks.json")

    def add_city(self, username):
        data = self.read()

        city = input("Enter city: ").title()

        if username not in data:
            data[username] = []

        if city in data[username]:
            print(f"{city} is already bookmarked ")
        else:
            data[username].append(city)
            self.write(data)
            print(f"{city} added to bookmarks ")

    def remove_city(self, username):
        data = self.read()

        city = input("Enter city to remove: ").title()

        if username in data and city in data[username]:
            data[username].remove(city)
            self.write(data)
            print(f"{city} removed from bookmarks ")
        else:
            print("City not found ")

    def view_cities(self, username):
        data = self.read()

        if username not in data or len(data[username]) == 0:
            print("No bookmarked cities ")
        else:
            print("\nYour Bookmarked Cities:")
            for i, city in enumerate(data[username], start=1):
                print(f"{i}. {city}")