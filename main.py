import pandas

df_hotels = pandas.read_csv('hotels.csv', dtype={"id": str})
df_cards = pandas.read_csv('cards.csv' , dtype=str).to_dict(orient='records')
df_card_security = pandas.read_csv('card_security.csv')


class Hostel:
    
    def __init__(self, hotel_id):
        pass

    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    
    def __init__():
        pass

    def generate():
        pass


class CreditCard:
    def __init__(self, card_number):
        pass

    def validate(self):
        pass


class CardSecurity(CreditCard):
    def authenticate(self):
        pass



print(df_hotels)