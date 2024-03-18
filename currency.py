# ./currency.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:85fe7c80fcda97d42ee34aade06a8cf43b61f7cc
# Generated 2024-03-18 20:26:38.021706 by PyXB version 1.2.6 using Python 3.8.10.final.0
# Namespace http://is550.soap.com

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:ad222278-e54c-11ee-9d69-751adad6a4ed')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://is550.soap.com', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://is550.soap.com}rating
class rating (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'rating')
    _XSDLocation = pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 65, 4)
    _Documentation = None
rating._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=rating, enum_prefix=None)
rating.High = rating._CF_enumeration.addEnumeration(unicode_value='High', tag='High')
rating.Moderate = rating._CF_enumeration.addEnumeration(unicode_value='Moderate', tag='Moderate')
rating.Low = rating._CF_enumeration.addEnumeration(unicode_value='Low', tag='Low')
rating._InitializeFacetMap(rating._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'rating', rating)
_module_typeBindings.rating = rating

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 7, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://is550.soap.com}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'country'), 'country', '__httpis550_soap_com_CTD_ANON_httpis550_soap_comcountry', False, pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 9, 16), )

    
    country = property(__country.value, __country.set, None, None)

    _ElementMap.update({
        __country.name() : __country
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 15, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://is550.soap.com}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'country'), 'country', '__httpis550_soap_com_CTD_ANON__httpis550_soap_comcountry', False, pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 17, 16), )

    
    country = property(__country.value, __country.set, None, None)

    _ElementMap.update({
        __country.name() : __country
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 23, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://is550.soap.com}currency uses Python identifier currency
    __currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currency'), 'currency', '__httpis550_soap_com_CTD_ANON_2_httpis550_soap_comcurrency', False, pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 25, 16), )

    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        __currency.name() : __currency
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 31, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://is550.soap.com}rating uses Python identifier rating
    __rating = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rating'), 'rating', '__httpis550_soap_com_CTD_ANON_3_httpis550_soap_comrating', False, pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 33, 16), )

    
    rating = property(__rating.value, __rating.set, None, None)

    _ElementMap.update({
        __rating.name() : __rating
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 39, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://is550.soap.com}currency uses Python identifier currency
    __currency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currency'), 'currency', '__httpis550_soap_com_CTD_ANON_4_httpis550_soap_comcurrency', True, pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 41, 16), )

    
    currency = property(__currency.value, __currency.set, None, None)

    _ElementMap.update({
        __currency.name() : __currency
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type {http://is550.soap.com}countryFaultType with content type ELEMENT_ONLY
class countryFaultType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://is550.soap.com}countryFaultType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'countryFaultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 46, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://is550.soap.com}errcode uses Python identifier errcode
    __errcode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'errcode'), 'errcode', '__httpis550_soap_com_countryFaultType_httpis550_soap_comerrcode', False, pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 48, 12), )

    
    errcode = property(__errcode.value, __errcode.set, None, None)

    
    # Element {http://is550.soap.com}errtext uses Python identifier errtext
    __errtext = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'errtext'), 'errtext', '__httpis550_soap_com_countryFaultType_httpis550_soap_comerrtext', False, pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 49, 12), )

    
    errtext = property(__errtext.value, __errtext.set, None, None)

    _ElementMap.update({
        __errcode.name() : __errcode,
        __errtext.name() : __errtext
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.countryFaultType = countryFaultType
Namespace.addCategoryObject('typeBinding', 'countryFaultType', countryFaultType)


# Complex type {http://is550.soap.com}currency with content type ELEMENT_ONLY
class currency (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://is550.soap.com}currency with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'currency')
    _XSDLocation = pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 56, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://is550.soap.com}shortName uses Python identifier shortName
    __shortName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shortName'), 'shortName', '__httpis550_soap_com_currency_httpis550_soap_comshortName', False, pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 58, 12), )

    
    shortName = property(__shortName.value, __shortName.set, None, None)

    
    # Element {http://is550.soap.com}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpis550_soap_com_currency_httpis550_soap_comname', False, pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 59, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://is550.soap.com}currentValue uses Python identifier currentValue
    __currentValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'currentValue'), 'currentValue', '__httpis550_soap_com_currency_httpis550_soap_comcurrentValue', False, pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 60, 12), )

    
    currentValue = property(__currentValue.value, __currentValue.set, None, None)

    
    # Element {http://is550.soap.com}rating uses Python identifier rating
    __rating = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rating'), 'rating', '__httpis550_soap_com_currency_httpis550_soap_comrating', False, pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 61, 12), )

    
    rating = property(__rating.value, __rating.set, None, None)

    _ElementMap.update({
        __shortName.name() : __shortName,
        __name.name() : __name,
        __currentValue.name() : __currentValue,
        __rating.name() : __rating
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.currency = currency
Namespace.addCategoryObject('typeBinding', 'currency', currency)


GetCurrencyByCountryRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCurrencyByCountryRequest'), CTD_ANON, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 6, 4))
Namespace.addCategoryObject('elementBinding', GetCurrencyByCountryRequest.name().localName(), GetCurrencyByCountryRequest)

GetCurrencyByCountryRequestFault = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCurrencyByCountryRequestFault'), CTD_ANON_, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 14, 4))
Namespace.addCategoryObject('elementBinding', GetCurrencyByCountryRequestFault.name().localName(), GetCurrencyByCountryRequestFault)

GetCurrencyByCountryResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCurrencyByCountryResponse'), CTD_ANON_2, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 22, 4))
Namespace.addCategoryObject('elementBinding', GetCurrencyByCountryResponse.name().localName(), GetCurrencyByCountryResponse)

GetCurrencyByRatingRequest = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCurrencyByRatingRequest'), CTD_ANON_3, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 30, 4))
Namespace.addCategoryObject('elementBinding', GetCurrencyByRatingRequest.name().localName(), GetCurrencyByRatingRequest)

GetCurrencyByRatingResponse = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GetCurrencyByRatingResponse'), CTD_ANON_4, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 38, 4))
Namespace.addCategoryObject('elementBinding', GetCurrencyByRatingResponse.name().localName(), GetCurrencyByRatingResponse)

countryFault = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'countryFault'), countryFaultType, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 53, 4))
Namespace.addCategoryObject('elementBinding', countryFault.name().localName(), countryFault)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'country'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 9, 16)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'country')), pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 9, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'country'), pyxb.binding.datatypes.string, scope=CTD_ANON_, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 17, 16)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'country')), pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 17, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_()




CTD_ANON_2._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currency'), currency, scope=CTD_ANON_2, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 25, 16)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_2._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currency')), pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 25, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_2()




CTD_ANON_3._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rating'), rating, scope=CTD_ANON_3, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 33, 16)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_3._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rating')), pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 33, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_3()




CTD_ANON_4._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currency'), currency, scope=CTD_ANON_4, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 41, 16)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_4._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currency')), pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 41, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_4()




countryFaultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errcode'), pyxb.binding.datatypes.string, scope=countryFaultType, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 48, 12)))

countryFaultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'errtext'), pyxb.binding.datatypes.string, scope=countryFaultType, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 49, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(countryFaultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errcode')), pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 48, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(countryFaultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'errtext')), pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 49, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
countryFaultType._Automaton = _BuildAutomaton_5()




currency._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shortName'), pyxb.binding.datatypes.string, scope=currency, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 58, 12)))

currency._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=currency, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 59, 12)))

currency._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'currentValue'), pyxb.binding.datatypes.double, scope=currency, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 60, 12)))

currency._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rating'), rating, scope=currency, location=pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 61, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(currency._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shortName')), pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 58, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(currency._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 59, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(currency._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'currentValue')), pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 60, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(currency._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rating')), pyxb.utils.utility.Location('/home/gktrk/Desktop/soap/currency.xsd', 61, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
currency._Automaton = _BuildAutomaton_6()

