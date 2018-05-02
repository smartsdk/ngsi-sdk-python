# swagger_client.AttributesApi

All URIs are relative to *https://https://api.s.orchestracities.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attribute_data**](AttributesApi.md#get_attribute_data) | **GET** /entities/{entityId}/attrs/{attrName} | 
[**remove_a_single_attribute**](AttributesApi.md#remove_a_single_attribute) | **DELETE** /entities/{entityId}/attrs/{attrName} | 
[**update_attribute_data**](AttributesApi.md#update_attribute_data) | **PUT** /entities/{entityId}/attrs/{attrName} | 


# **get_attribute_data**
> Entity get_attribute_data(entity_id, attr_name, type=type)



Returns a JSON object with the attribute data of the attribute. The object follows the JSON Representation for attributes (described in \"JSON Attribute Representation\" section). Response: * Successful operation uses 200 OK. * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Id of the entity
attr_name = 'attr_name_example' # str | Name of the attribute to be retrieved.
type = 'type_example' # str | Entity type, to avoid ambiguity in the case there are several entities with the same entity id. (optional)

try:
    api_response = api_instance.get_attribute_data(entity_id, attr_name, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttributesApi->get_attribute_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity | 
 **attr_name** | **str**| Name of the attribute to be retrieved. | 
 **type** | **str**| Entity type, to avoid ambiguity in the case there are several entities with the same entity id. | [optional] 

### Return type

[**Entity**](Entity.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_a_single_attribute**
> remove_a_single_attribute(entity_id, attr_name, type=type)



Removes an entity attribute. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Id of the entity.
attr_name = 'attr_name_example' # str | Attribute name.
type = 'type_example' # str | Entity type, to avoid ambiguity in the case there are several entities with the same entity id. (optional)

try:
    api_instance.remove_a_single_attribute(entity_id, attr_name, type=type)
except ApiException as e:
    print("Exception when calling AttributesApi->remove_a_single_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity. | 
 **attr_name** | **str**| Attribute name. | 
 **type** | **str**| Entity type, to avoid ambiguity in the case there are several entities with the same entity id. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_attribute_data**
> update_attribute_data(entity_id, attr_name, body, type=type)



The request payload is an object representing the new attribute data. Previous attribute data is replaced by the one in the request. The object follows the JSON Representation for attributes (described in \"JSON Attribute Representation\" section). Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.AttributesApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Id of the entity to update
attr_name = 'attr_name_example' # str | Attribute name
body = NULL # object | 
type = 'type_example' # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)

try:
    api_instance.update_attribute_data(entity_id, attr_name, body, type=type)
except ApiException as e:
    print("Exception when calling AttributesApi->update_attribute_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity to update | 
 **attr_name** | **str**| Attribute name | 
 **body** | **object**|  | 
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

