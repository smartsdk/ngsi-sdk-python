# swagger_client.AttributeValueApi

All URIs are relative to *http://orion.lab.fiware.org:1026/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attribute_value**](AttributeValueApi.md#get_attribute_value) | **GET** /entities/{entityId}/attrs/{attrName}/value | 
[**update_attribute_value**](AttributeValueApi.md#update_attribute_value) | **PUT** /entities/{entityId}/attrs/{attrName}/value | 


# **get_attribute_value**
> AttributeValue get_attribute_value(entity_id, attr_name, type=type)



This operation returns the `value` property with the value of the attribute. * If attribute value is JSON Array or Object:   * If `Accept` header can be expanded to `application/json` or `text/plain` return the value as a JSON with a     response type of application/json or text/plain (whichever is the first in `Accept` header or     `application/json` in the case of `Accept: */*`).   * Else return a HTTP error \"406 Not Acceptable: accepted MIME types: application/json, text/plain\" * If attribute value is a string, number, null or boolean:   * If `Accept` header can be expanded to text/plain return the value as text. In case of a string, citation     marks are used at the begining and end.   * Else return a HTTP error \"406 Not Acceptable: accepted MIME types: text/plain\" Response: * Successful operation uses 200 OK. * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AttributeValueApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Id of the entity in question
attr_name = 'attr_name_example' # str | Name of the attribute to be retrieved.
type = 'type_example' # str | Entity type, to avoid ambiguity in the case there are several entities with the same entity id. (optional)

try:
    api_response = api_instance.get_attribute_value(entity_id, attr_name, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributeValueApi->get_attribute_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity in question | 
 **attr_name** | **str**| Name of the attribute to be retrieved. | 
 **type** | **str**| Entity type, to avoid ambiguity in the case there are several entities with the same entity id. | [optional] 

### Return type

[**AttributeValue**](AttributeValue.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, plain/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_value**
> update_attribute_value(entity_id, attr_name, body, type=type)



The request payload is the new attribute value. * If the request payload MIME type is `application/json`, then the value of the attribute is set to   the JSON object or array coded in the payload (if the payload is not a valid JSON document,   then an error is returned). * If the request payload MIME type is `text/plain`, then the following algorithm is applied to the   payload:   * If the payload starts and ends with citation-marks (`\"`), the value is taken as a string     (the citation marks themselves are not considered part of the string)   * If `true` or `false`, the value is taken as a boolean.   * If `null`, the value is taken as null.   * If these first three tests 'fail', the text is interpreted as a number.   * If not a valid number, then an error is returned and the attribute's value is unchanged. The payload MIME type in the request is specified in the `Content-Type` HTTP header. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AttributeValueApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Id of the entity to be updated.
attr_name = 'attr_name_example' # str | Attribute name.
body = swagger_client.AttributeValue() # AttributeValue | JSON AttributeValue Representation
type = 'type_example' # str | Entity type, to avoid ambiguity in the case there are several entities with the same entity id. (optional)

try:
    api_instance.update_attribute_value(entity_id, attr_name, body, type=type)
except ApiException as e:
    print("Exception when calling AttributeValueApi->update_attribute_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity to be updated. | 
 **attr_name** | **str**| Attribute name. | 
 **body** | [**AttributeValue**](AttributeValue.md)| JSON AttributeValue Representation | 
 **type** | **str**| Entity type, to avoid ambiguity in the case there are several entities with the same entity id. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json, plain/text
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

