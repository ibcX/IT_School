import datetime
from datetime import timedelta

"""
1. Scrie o clasa care repr. o Agenda (Notebook).
Atribute:
    - nr pagini (la contructor)
    - culoare (la constructor)
    - continut - lista de stringuri ["continut pagina", "continut pag."]
Metode:
    - scrie in Agenda
    - vezi nr de pag goale
    - vezi nr pag scrise
"""


class Notebook:
    def __init__(self, page_number, colour):
        self.page_number = page_number
        self.colour = colour
        self.content = {}

    def write_in_agenda(self, page, page_content):
        self.content[page] = page_content

    def written_pages(self):
        written_pages_number = len(self.content.keys())
        print(
            f"The number of the written pages in the {self.colour} notebook, with a total number of pages of {self.page_number}, is: {written_pages_number}")

    def empty_pages(self):
        empty_pages_number = self.page_number - len(self.content.keys())
        print(
            f"The number of the empty pages in the {self.colour} notebook, with a total number of pages of {self.page_number}, is: {empty_pages_number}")


red_notebook = Notebook(200, "red")

red_notebook.write_in_agenda(10, "ABC")
red_notebook.empty_pages()
red_notebook.written_pages()

"""
2. Scrie o clasa care repr. un Utilizator
Atr:
 - nume (c)
 - prenume(c)
 - telefon(c)
 - email(c)
 - activ - bool
Meth:
 - activate
 - deactivate
 - update_email - 1 param
 - update_phone - 1 param
 - print_user_info
"""


class User:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.activ_user = False

    def activate(self):
        self.activ_user = True

    def deactivate(self):
        self.activ_user = False

    def update_phone(self, new_phone):
        self.phone = new_phone

    def update_email(self, new_email):
        self.email = new_email

    def activity(self):
        if not self.activ_user:
            return "inactiv"
        else:
            return "activ"

    def print_user_info(self):
        print(f"""
    {__class__.__name__}'s information is: 
    First name: {self.first_name}
    Last name: {self.last_name}
    phone: {self.phone}
    email: {self.email}
    user {self.activity()}
    """)


Bogdan = User("Bogdan", "Iacob", "000", "iacob.cezar@gmail.com")
Mihai = User("Mihai", "Popescu", "000", "")

Bogdan.update_phone("0741756687")
Bogdan.update_email("iacob.cezar@gmail.com")
Bogdan.print_user_info()
Bogdan.activate()
Bogdan.print_user_info()

"""
3. Scrie o clasa UserManager
Atr:
 - users = lista de utilizatori activi
 Meth:
  - add_user(User)
  - get_user_by_email
  - remove_user
  - drop_all
  - create_default_user
"""


class UserManager:

    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user.activ_user:
            self.users.append(user)

    def get_user_by_email(self, email):
        for user in self.users:
            if email == user.email:
                user.print_user_info()
                return user
        print("No user was found with this email address.")

    def remove_user(self, user):
        self.users.remove(user)

    def drop_all(self):
        self.users.clear()

    def create_default_user(self):
        default = User("default", "user", "", "")
        return default


manager = UserManager()
default_user = manager.create_default_user()
manager.add_user(Bogdan)
manager.add_user(Mihai)
default_user.activate()
manager.add_user(default_user)
Mihai.activate()
Mihai.update_email("mihai@yahoo.com")
manager.add_user(Mihai)
print(manager.users)
manager.get_user_by_email("iacob.cezar@gmail.com")
manager.remove_user(Bogdan)
manager.get_user_by_email("mihai@yahoo.com")
manager.get_user_by_email("")
manager.drop_all()

"""
4. Scrie o clasa ce repr. o cursa aeriana
Atr:
 - aeroport_plecare  (c)
 - aeroport_sosire (c)
 - data_ora_plecare (c)
 - data_ora_sosire (c)
 - pret_per_loc (c)
Meth:
 - get_duration
 - get_price_tva (pret_per_loc + tva)

5. Scrie o clasa ce repr. un Bilet de avion
Atr:
 - nume posesor (c)
 - cursa -> de tip cursa aeriana definita mai sus (c)
 - loc (c)
Meth:
 - print_ticket -> printeaza info despre cursa si loc (nume, durata, pret, loc)
"""


class Airline:
    def __init__(self, name, departure_airport, arrival_airport, date_hour_departure, date_hour_arrival, price_seat):
        self.name = name
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.date_hour_departure = date_hour_departure
        self.date_hour_arrival = date_hour_arrival
        self.price_seat = price_seat

    def get_duration(self):
        duration = self.date_hour_arrival - self.date_hour_departure
        seconds = timedelta.total_seconds(duration)
        hours, minutes = divmod(seconds, 3600)
        minutes = minutes/60
        print(
            f"The total duration of the {self.departure_airport} - {self.arrival_airport} flight is: {int(hours)} hours"
            f" and {int(minutes)} minutes.")
        return duration

    def get_price_tva(self):
        price_tva = self.price_seat * 1.19
        return price_tva


date_time_departure = datetime.datetime(2022, 10, 1, 12, 10)
date_time_arrival = datetime.datetime(2022, 10, 1, 13, 0)
wizz = Airline("Wizzair", "Cluj", "Bucuresti", date_time_departure, date_time_arrival, 500)
wizz.get_duration()


class AirplaneTicket:
    def __init__(self, name, airline, seat):
        self.name = name
        self.airline = airline
        self.seat = seat

    def print_ticket(self):
        print(f"""
Ticket information:
    Customer: {self.name}
    Flight: {self.airline.name}, from {self.airline.departure_airport} to {self.airline.arrival_airport}
    Total duration: {self.airline.get_duration()}
    Price, incl. VAT: {self.airline.price_seat}
    Seat: {self.seat}
        """)


ticket_1 = AirplaneTicket("Bogdan", wizz, "2F")
ticket_1.print_ticket()