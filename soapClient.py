from zeep import Client

# WSDL dosyasının URL'si
wsdl_url = 'currency.wsdl'

# SOAP istemcisini oluştur
client = Client(wsdl=wsdl_url)

# SOAP isteği için gerekli veri
soap_request_data = {
    'country': 'USA'  # Örnek bir ülke adı
}

# SOAP isteğini gönder
response = client.service.GetCurrencyByCountry(soap_request_data)

# Yanıtı yazdır
print("Received SOAP Response:")
print(response)
