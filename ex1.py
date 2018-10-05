class Vehicle:

    def __init__(self, company, model, year_of_production, registration_number, engine_power, color):

        self.company = company
        self.model = model
        self.year_of_prod = year_of_production
        self.regist_num = registration_number
        self.engine_pow = engine_power
        self.color = color


    def cost_of_registration(self):

        if int(self.year_of_prod) < 1990:
            registration = 100

        elif int(self.year_of_prod) < 2000:
            registration = 200

        elif int(self.year_of_prod) < 2010:
            registration = 300

        else:
            registration = 400

        registration = registration + 2 * int(self.engine_pow)

        return "Registration will cost " + str(registration) + "EUR."


    def __str__(self):
        return "{0} {1}({2}, {3}, {4}kW, {5})".format(self.company, self.model, self.year_of_prod, self.regist_num, self.engine_pow, self.color)


class Bus(Vehicle):
    def __init__(self,company, model, year_of_prod, regist_number, engine_pow, color, number_of_available_seats, company_1):
        Vehicle.__init__(self, company, model, year_of_prod, regist_number, engine_pow, color)
        self.num_of_avail_seats = number_of_available_seats
        self.company_1 = company_1


    def cost_of_registration(self):
        return "Registration will cost " + str(int(Vehicle.cost_of_registration(self)[23:-4]) + int(self.num_of_avail_seats)) + "EUR."

    def __str__(self):
        return "{0} {1} ({2}, {3}, {4}kW, {5}, available seat: {6})".format(self.company, self.model, self.year_of_prod, self.regist_num, self.engine_pow,self.color,self.num_of_avail_seats)


vehicle1 = Vehicle("BMW", "M5", "2017", "PG-RT435", "441", "white")
bus1 = Bus("Mercedes", "Benz", "1985", "A-32-568", "200", "blue", "50", "Lasta")

print(vehicle1)
print(vehicle1.cost_of_registration())
print("")
print(bus1)
print(bus1.cost_of_registration())