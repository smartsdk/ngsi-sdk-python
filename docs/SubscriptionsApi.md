# swagger_client.SubscriptionsApi

All URIs are relative to *https://https://api.s.orchestracities.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_new_subscription**](SubscriptionsApi.md#create_a_new_subscription) | **POST** /subscriptions | 
[**delete_subscription**](SubscriptionsApi.md#delete_subscription) | **DELETE** /subscriptions/{subscriptionId} | 
[**retrieve_subscription**](SubscriptionsApi.md#retrieve_subscription) | **GET** /subscriptions/{subscriptionId} | 
[**retrieve_subscriptions**](SubscriptionsApi.md#retrieve_subscriptions) | **GET** /subscriptions | 
[**update_subscription**](SubscriptionsApi.md#update_subscription) | **PATCH** /subscriptions/{subscriptionId} | 


# **create_a_new_subscription**
> create_a_new_subscription(body)



Creates a new subscription. The subscription is represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 201 Created * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Subscription() # Subscription | 

try:
    api_instance.create_a_new_subscription(body)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->create_a_new_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Subscription**](Subscription.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(subscription_id)



Cancels subscription. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | subscription Id.

try:
    api_instance.delete_subscription(subscription_id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription Id. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_subscription**
> Subscription retrieve_subscription(subscription_id)



The response is the subscription represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | subscription Id.

try:
    api_response = api_instance.retrieve_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->retrieve_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription Id. | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_subscriptions**
> list[Subscription] retrieve_subscriptions(limit=limit, offset=offset, options=options)



Returns a list of all the subscriptions present in the system. Response: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
limit = 1.2 # float | Limit the number of types to be retrieved (optional)
offset = 1.2 # float | Skip a number of records (optional)
options = 'options_example' # str | Options dictionary (optional)

try:
    api_response = api_instance.retrieve_subscriptions(limit=limit, offset=offset, options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->retrieve_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Limit the number of types to be retrieved | [optional] 
 **offset** | **float**| Skip a number of records | [optional] 
 **options** | **str**| Options dictionary | [optional] 

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> update_subscription(subscription_id, body)



Only the fields included in the request are updated in the subscription. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | subscription Id.
body = swagger_client.Subscription() # Subscription | 

try:
    api_instance.update_subscription(subscription_id, body)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->update_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| subscription Id. | 
 **body** | [**Subscription**](Subscription.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

