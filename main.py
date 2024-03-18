from flask import Flask, request, Response
from zeep import Client

app = Flask(__name__)

# WSDL dosyasını yükle
wsdl_url = 'currency.wsdl'  # WSDL dosyasının URL'si
client = Client(wsdl=wsdl_url)

# SOAP endpoint'i
@app.route('/ws', methods=['POST'])
def soap():
    # Gelen SOAP isteğini al
    soap_request = request.data
    
    # SOAP isteğini işle
    # Zeep kullanarak SOAP isteğini işleyebilirsiniz
    soap_response = client.service.GetCurrencyByCountry(soap_request)
    
    # SOAP yanıtını oluştur
    soap_response = Response(soap_response, content_type='application/xml')
    
    # SOAP yanıtını gönder
    return soap_response

if __name__ == '__main__':
    app.run(debug=True)
