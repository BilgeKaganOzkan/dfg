import currency

class currencyRepository:
    def __init__(self):
        currencies = {}

        usd = currency.currency()
        usd.shortName = "USD"
        usd.currentValue = 30
        usd.name = "Us Dollar"
        usd.rating = currency.rating.High

        currencies["USA"] = usd

        eur = currency.currency()
        eur.shortName = "EUR"
        eur.currentValue = 26
        eur.name = "EURO"
        eur.rating = currency.rating.High

        currencies["GERMANY"] = eur
        currencies["FRANCE"] = eur
    
    def findCurrency(self, country):
        return self.currencies[country]