from flask import Flask, request, Response
from zeep import Client
from zeep.helpers import serialize_object
from currency import *

app = Flask(__name__)

wsdl_url = 'currency.wsdl'
client = Client(wsdl=wsdl_url)

@app.route('/ws', methods=['POST', 'GET'])
def soap():
    soap_request = request.data.decode('utf-8')
    request_object = CreateFromDocument(soap_request)
    country = request_object.country
    print(request_object)
    country = request_object['country']
    print(country)

    soap_response = client.service.GetCurrencyByCountry(soap_request)
    
    soap_response = Response(soap_response, content_type='application/xml')
    
    return soap_response

if __name__ == '__main__':
    app.run(debug=False, port=8080)
