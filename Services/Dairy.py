from Base.file import FileHandler
from datetime import datetime


class Diary(FileHandler):

    def __init__(self):
        super().__init__("Data/diary.json")

    def add_entry(self, username, weather, note=""):
        data = self.read()  

        if username not in data:
            data[username] = []

        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "city": weather["city"],
            "temperature": int(weather["temperature"]),
            "description": weather["description"],
            "note": note
        }

        data[username].append(entry)

        self.write(data)

        print("Diary entry saved ")

    def view_entries(self, username):
        data = self.read()

        if username not in data or len(data[username]) == 0:
            print("No diary entries found ")
            return

        print("\nYour Diary Entries ")

        for entry in data[username]:
            print("*----------------------------*")
            print(f"Time: {entry['timestamp']}")
            print(f"City: {entry['city']}")
            print(f"Temp: {entry['temperature']}°C")
            print(f"Weather: {entry['description']}")
            print(f"Note: {entry['note']}")
            print("*----------------------------*")

    def filter_by_city(self, username):
        data = self.read()

        if username not in data or len(data[username]) == 0:
            print("No diary entries found ")
            return

        city = input("Enter city name: ").title()

        found = False

        print(f"\nEntries for {city}")

        for entry in data[username]:
            if entry["city"] == city:
                print("----------------------------")
                print(f"Time: {entry['timestamp']}")
                print(f"Temp: {entry['temperature']}°C")
                print(f"Weather: {entry['description']}")
                print(f"Note: {entry['note']}")
                found = True

        if not found:
            print("No entries found for this city ")

    def statistics(self, username):
        data = self.read()

        if username not in data or len(data[username]) == 0:
            print("No diary entries found ")
            return

        entries = data[username]

        total = 0
        sum_temp = 0

        hottest = entries[0]
        coldest = entries[0]

        unique_cities = set()

        for entry in entries:
            temp = entry["temperature"]
            city = entry["city"]

            total += 1

            sum_temp += temp

            if temp > hottest["temperature"]:
                hottest = entry

            if temp < coldest["temperature"]:
                coldest = entry

            unique_cities.add(city)

        avg_temp = round(sum_temp / total, 2)

        print("\nDiary Statistics")
        print(f"Total entries: {total}")
        print(f"Hottest: {hottest['city']} ({hottest['temperature']}°C)")
        print(f"Coldest: {coldest['city']} ({coldest['temperature']}°C)")
        print(f"Average temperature: {avg_temp}°C")
        print(f"Unique cities: {unique_cities}")