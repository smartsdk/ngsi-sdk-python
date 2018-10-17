# swagger_client.RegistrationsApi

All URIs are relative to *http://orion.lab.fiware.org:1026/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_registrations**](RegistrationsApi.md#create_registrations) | **POST** /registrations | 
[**delete_registration**](RegistrationsApi.md#delete_registration) | **DELETE** /registrations/{registrationId} | 
[**retrieve_registration**](RegistrationsApi.md#retrieve_registration) | **GET** /registrations/{registrationId} | 
[**retrieve_registrations**](RegistrationsApi.md#retrieve_registrations) | **GET** /registrations | 
[**update_registration**](RegistrationsApi.md#update_registration) | **PATCH** /registrations/{registrationId} | 


# **create_registrations**
> create_registrations(body)



Creates a new context provider registration. This is typically used for binding context sources as providers of certain data. The registration is represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 201 Created * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: fiware_token
configuration = swagger_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RegistrationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Registration() # Registration | 

try:
    api_instance.create_registrations(body)
except ApiException as e:
    print("Exception when calling RegistrationsApi->create_registrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Registration**](Registration.md)|  | 

### Return type

void (empty response body)

### Authorization

[fiware_token](../README.md#fiware_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration**
> delete_registration(registration_id)



Cancels a context provider registration. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: fiware_token
configuration = swagger_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RegistrationsApi(swagger_client.ApiClient(configuration))
registration_id = 'registration_id_example' # str | registration Id.

try:
    api_instance.delete_registration(registration_id)
except ApiException as e:
    print("Exception when calling RegistrationsApi->delete_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| registration Id. | 

### Return type

void (empty response body)

### Authorization

[fiware_token](../README.md#fiware_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_registration**
> RegistrationResponse retrieve_registration(registration_id)



The response is the registration represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: fiware_token
configuration = swagger_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RegistrationsApi(swagger_client.ApiClient(configuration))
registration_id = 'registration_id_example' # str | registration Id.

try:
    api_response = api_instance.retrieve_registration(registration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationsApi->retrieve_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| registration Id. | 

### Return type

[**RegistrationResponse**](RegistrationResponse.md)

### Authorization

[fiware_token](../README.md#fiware_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_registrations**
> list[RegistrationResponse] retrieve_registrations(limit=limit, offset=offset, options=options)



Lists all the context provider registrations present in the system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: fiware_token
configuration = swagger_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RegistrationsApi(swagger_client.ApiClient(configuration))
limit = 1.2 # float | Limit the number of types to be retrieved (optional)
offset = 1.2 # float | Skip a number of records (optional)
options = 'options_example' # str | Options dictionary (optional)

try:
    api_response = api_instance.retrieve_registrations(limit=limit, offset=offset, options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistrationsApi->retrieve_registrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Limit the number of types to be retrieved | [optional] 
 **offset** | **float**| Skip a number of records | [optional] 
 **options** | **str**| Options dictionary | [optional] 

### Return type

[**list[RegistrationResponse]**](RegistrationResponse.md)

### Authorization

[fiware_token](../README.md#fiware_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_registration**
> update_registration(registration_id, body)



Creates a new context provider registration. This is typically used for binding context sources as providers of certain data. The registration is represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 201 Created * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: fiware_token
configuration = swagger_client.Configuration()
configuration.api_key['X-Auth-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RegistrationsApi(swagger_client.ApiClient(configuration))
registration_id = 'registration_id_example' # str | registration Id.
body = swagger_client.Registration() # Registration | 

try:
    api_instance.update_registration(registration_id, body)
except ApiException as e:
    print("Exception when calling RegistrationsApi->update_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| registration Id. | 
 **body** | [**Registration**](Registration.md)|  | 

### Return type

void (empty response body)

### Authorization

[fiware_token](../README.md#fiware_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

