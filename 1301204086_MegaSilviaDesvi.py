class data:
    def __init__(self, name, nik):
        self.name = name
        self.nik = nik

#create list of data
data = [
    data("Mega Silvia Desvi", "1301204086"),
    ]

# print names and nik
for data in data:
        print(f"Name: {data.name}, NIK: {data.nik}")
