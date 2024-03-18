from zeep import Client

# WSDL dosyasının URL'si
wsdl_url = 'currency.wsdl'

# SOAP istemcisini oluştur
client = Client(wsdl=wsdl_url)

soap_request_data = {
    'country': 'USA'
}

# Mesaj oluştur
request_message = client.get_element('{http://is550.soap.com}GetCurrencyByCountryRequest')
message = request_message(country=soap_request_data['country'])
response = client.service.GetCurrencyByCountry(message)

# Yanıtı yazdır
print("Received SOAP Response:")
print(response)
