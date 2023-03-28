

# Q1
# Write a function that takes in a list and returns the same list without duplicates

array = []

def removeDuplicate(array):
    memo = set()
    res = []

    for element in array:
        if not element in memo:
            memo.add(element)
            res.append(element)
    return res

    return list(memo)


# Q2
# Write a class that can take in numbers gradually and can provide the average or max at any time.

class Numbers:
    def __init__(self):
        self.store = []
        self.tmpMax = float('-inf')

    def add(self, num):
        self.store.append(num)
        self.tmpMax = max(self.tmpMax, num)

    def average(self):
        return sum(self.store) / len(self.store)

    def numbersMax(self):
        return self.tmpMax

# Q3
# Get all vehicle info with company name

SELECT Vehicles.license_state, Vehicles.license_number, Companies.name
FROM Vehicles
LEFT OUTTER JOIN Companies
ON Vehicles.company_id = Companies.id

# Write a query to get the timestamp and company_id of all observations.

SELECT Observations.timestamp, Vehicles.company_id
FROM Vehicles
LEFT OUTTER JOIN Obeservations
ON Vehicles.license_state = Observations.license_state
AND Vehicles.license_number = Observations.license_number

# Write a query to get the 10 companies with the most vehicles, and the number of vehicles for each in the database

SELECT SUM(car) as sum, Vehicles.company_id
FROM
(SELECT Vehicles.*
FROM Vehicles) as car
ORDER BY sum
LIMIT 10