class WeatherRecord:
    def __init__(self, date, city, temperature):
        self.date = date        
        self.city = city
        self.temperature = temperature 

    def __repr__(self):
        return f"({self.date}, {self.city}, {self.temperature}°C)"

class WeatherDataStorage:
    def __init__(self, years, cities):
        """
        years  : list of years (e.g., [2024, 2025])
        cities : list of city names (e.g., ["Delhi", "Mumbai"])
        """
        self.years = years
        self.cities = cities
        self.num_years = len(years)
        self.num_cities = len(cities)

        self.data = [[None for _ in range(self.num_cities)]
                     for _ in range(self.num_years)]

    def insert(self, year, city, temperature):
        if year in self.years and city in self.cities:
            row = self.years.index(year)
            col = self.cities.index(city)
            self.data[row][col] = temperature
            print(f"Inserted {temperature}°C for {city} in {year}")
        else:
            print(" Invalid year or city!")

    def delete(self, year, city):
        if year in self.years and city in self.cities:
            row = self.years.index(year)
            col = self.cities.index(city)
            self.data[row][col] = None
            print(f"Deleted record for {city} in {year}")
        else:
            print(" Invalid year or city!")

    def retrieve(self, city, year):
        if year in self.years and city in self.cities:
            row = self.years.index(year)
            col = self.cities.index(city)
            return self.data[row][col]
        return None

    def row_major_access(self):
        print("\n Row-major traversal:")
        for r in range(self.num_years):
            for c in range(self.num_cities):
                print(f"[{self.years[r]}, {self.cities[c]}] = {self.data[r][c]}")

    def column_major_access(self):
        print("\n Column-major traversal:")
        for c in range(self.num_cities):
            for r in range(self.num_years):
                print(f"[{self.years[r]}, {self.cities[c]}] = {self.data[r][c]}")

    def handle_sparse_data(self):
        print("\n Sparse Data (Missing records):")
        found_missing = False
        for r in range(self.num_years):
            for c in range(self.num_cities):
                if self.data[r][c] is None:
                    print(f"Missing data for {self.cities[c]} in {self.years[r]}")
                    found_missing = True
        if not found_missing:
            print("No missing records.")

    def analyze_complexity(self):
        print("\n--- Time & Space Complexity ---")
        print("Insert: O(1)   -> Direct index access")
        print("Delete: O(1)   -> Direct index access")
        print("Retrieve: O(1) -> Direct index access")
        print("Row-major traversal: O(n*m)")
        print("Column-major traversal: O(n*m)")
        print(f"Space Complexity: O(n*m) = {self.num_years} x {self.num_cities}")

if __name__ == "__main__":

    years = list(map(int, input("Enter years : ").split(",")))
    cities = input("Enter city names : ").split(",")

    storage = WeatherDataStorage(years, cities)

    while True:
        print("\n==== Weather Data Storage Menu ====")
        print("1. Insert Record")
        print("2. Delete Record")
        print("3. Retrieve Record")
        print("4. Row-Major Traversal")
        print("5. Column-Major Traversal")
        print("6. Handle Sparse Data")
        print("7. Analyze Complexity")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            year = int(input("Enter year: "))
            city = input("Enter city: ")
            temp = float(input("Enter temperature: "))
            storage.insert(year, city, temp)

        elif choice == "2":
            year = int(input("Enter year: "))
            city = input("Enter city: ")
            storage.delete(year, city)

        elif choice == "3":
            year = int(input("Enter year: "))
            city = input("Enter city: ")
            result = storage.retrieve(city, year)
            if result is not None:
                print(f" Temperature for {city} in {year}: {result}°C")
            else:
                print(" No record found.")

        elif choice == "4":
            storage.row_major_access()

        elif choice == "5":
            storage.column_major_access()

        elif choice == "6":
            storage.handle_sparse_data()

        elif choice == "7":
            storage.analyze_complexity()

        elif choice == "8":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-8.")
