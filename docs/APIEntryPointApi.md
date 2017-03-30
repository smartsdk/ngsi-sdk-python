# swagger_client.APIEntryPointApi

All URIs are relative to *http://orion.lab.fiware.org:1026/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrieve_api_resources**](APIEntryPointApi.md#retrieve_api_resources) | **GET** / | 


# **retrieve_api_resources**
> APIEntryPoint retrieve_api_resources()



This resource does not have any attributes. Instead it offers the initial API affordances in the form of the links in the JSON body. It is recommended to follow the “url” link values, [Link](https://tools.ietf.org/html/rfc5988) or Location headers where applicable to retrieve resources. Instead of constructing your own URLs, to keep your client decoupled from implementation details.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: fiware_token
swagger_client.configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.APIEntryPointApi()

try: 
    api_response = api_instance.retrieve_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIEntryPointApi->retrieve_api_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**APIEntryPoint**](APIEntryPoint.md)

### Authorization

[fiware_token](../README.md#fiware_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

