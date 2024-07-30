import pandas

df_hotels = pandas.read_csv('hotels.csv', dtype={"id": str})
df_cards = pandas.read_csv('cards.csv' , dtype=str).to_dict(orient='records')
df_card_security = pandas.read_csv('card_security.csv', dtype=str)


class Hotel:
    
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df_hotels.loc[df_hotels["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"] = "no"
        df_hotels.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df_hotels.loc[df_hotels["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
        

class ReservationTicket:
    def __init__(self, hotel_object, customer_name):
        self.customer_name = customer_name
        self.hotel_name = hotel_object.hotel_name

    def generate(self):
        content = f"Reservation for {self.customer_name} at {self.hotel_name} completed successfully."
        return content


class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number

    def validate(self, expiration , cvc , holder):
        card_data = {"number": self.card_number, "expiration": expiration, "cvc": cvc, "holder": holder}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCard(CreditCard):
    def authenticate(self, password):
        saved_password = df_card_security.loc[df_card_security["number"] == self.card_number, "password"].squeeze()
        if password == saved_password:
            return True
        else:
            return False


print(df_hotels)
hotel_id = input("Enter hotel id that you want to book: ")
hotel = Hotel(hotel_id)

if hotel.available():
    customer_name = input("Enter your name: ")
    card = SecureCard("1234")
    if card.validate("12/26", "123", "JOHN SMITH"):
        # password = input("Enter your card password: ")
        if card.authenticate("mypass"):
            ticket = ReservationTicket(hotel, customer_name)
            hotel.book()
            print(ticket.generate())
        else:
            print("Card authentication failed")
    else:
        print("Facing issue with card validation")
else:
    print("Hotel is not available for booking")