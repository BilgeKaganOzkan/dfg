from lxml import etree

# XSD dosyasını yükleyin
schema = etree.XMLSchema(file="currency.xsd")

# XSD dosyasındaki tipleri Python nesnelerine dönüştürün
class MyObject(etree.ElementTree.CustomElementClass):
    __schema = schema
    __namespace = "http://www.example.com/my-schema"

# XML dosyasını okuyun ve Python nesnelerine dönüştürün
root = etree.fromstring(file="currency.xsd", schema=schema)

# Oluşturulan Python nesnelerini kullanın
obj = MyObject(root)