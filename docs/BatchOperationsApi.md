# swagger_client.BatchOperationsApi

All URIs are relative to *https://api.s.orchestracities.com/context/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query**](BatchOperationsApi.md#query) | **POST** /op/query | 
[**update**](BatchOperationsApi.md#update) | **POST** /op/update | 


# **query**
> list[object] query(body, limit=limit, offset=offset, order_by=order_by, options=options)



The response payload is an Array containing one object per matching entity, or an empty array `[]` if  no entities are found. The entities follow the JSON entity Representation format (described in the section \"JSON Entity Representation\"). The payload may contain the following elements (all of them optional): + `entities`: a list of entites to search for. Each element is represented by a JSON object with the   following elements:     + `id` or `idPattern`: Id or pattern of the affected entities. Both cannot be used at the same       time, but at least one of them must be present.     + `type` or `typePattern`: Type or type pattern of the entities to search for. Both cannot be used at       the same time. If omitted, it means \"any entity type\". + `attributes`: a list of attribute names to search for. If omitted, it means \"all attributes\".  Response code: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.BatchOperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Query() # Query | 
limit = 1.2 # float | Limit the number of entities to be retrieved. (optional)
offset = 1.2 # float | Skip a number of records. (optional)
order_by = 'order_by_example' # str | Criteria for ordering results. See \"Ordering Results\" section for details. (optional)
options = 'options_example' # str | Options dictionary (optional)

try:
    api_response = api_instance.query(body, limit=limit, offset=offset, order_by=order_by, options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchOperationsApi->query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Query**](Query.md)|  | 
 **limit** | **float**| Limit the number of entities to be retrieved. | [optional] 
 **offset** | **float**| Skip a number of records. | [optional] 
 **order_by** | **str**| Criteria for ordering results. See \&quot;Ordering Results\&quot; section for details. | [optional] 
 **options** | **str**| Options dictionary | [optional] 

### Return type

**list[object]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> update(body, options=options)



This operation allows to create, update and/or delete several entities in a single batch operation. The payload is an object with two properties: + `actionType`, to specify the kind of update action to do: either APPEND, APPEND_STRICT, UPDATE,   DELETE. + `entities`, an array of entities, each one specified using the JSON entity Representation format   (described in the section \"JSON Entity Representation\"). Response: * Successful operation uses 204 No Content. * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.BatchOperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.BatchOperation() # BatchOperation | 
options = 'options_example' # str | Options dictionary (optional)

try:
    api_instance.update(body, options=options)
except ApiException as e:
    print("Exception when calling BatchOperationsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchOperation**](BatchOperation.md)|  | 
 **options** | **str**| Options dictionary | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

