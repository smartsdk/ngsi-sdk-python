# swagger_client.EntitiesApi

All URIs are relative to *http://orion.lab.fiware.org:1026*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity**](EntitiesApi.md#create_entity) | **POST** /entities | 
[**list_entities**](EntitiesApi.md#list_entities) | **GET** /entities | 
[**remove_entity**](EntitiesApi.md#remove_entity) | **DELETE** /entities/{entityId} | 
[**replace_all_entity_attributes**](EntitiesApi.md#replace_all_entity_attributes) | **PUT** /entities/{entityId}/attrs | 
[**retrieve_entity**](EntitiesApi.md#retrieve_entity) | **GET** /entities/{entityId} | 
[**retrieve_entity_attributes**](EntitiesApi.md#retrieve_entity_attributes) | **GET** /entities/{entityId}/attrs | 
[**update_existing_entity_attributes**](EntitiesApi.md#update_existing_entity_attributes) | **PATCH** /entities/{entityId}/attrs | 
[**update_or_append_entity_attributes**](EntitiesApi.md#update_or_append_entity_attributes) | **POST** /entities/{entityId}/attrs | 


# **create_entity**
> create_entity(body, options=options)



The payload is an object representing the entity to be created. The object follows the JSON entity Representation format (described in a \"JSON Entity Representation\" section). Response: * Successful operation uses 201 Created. Reponse includes a `Location` header with the URL of the   created entity. * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.EntitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Entity() # Entity | JSON Entity Representation
options = 'options_example' # str | Options dictionary (optional)

try:
    api_instance.create_entity(body, options=options)
except ApiException as e:
    print("Exception when calling EntitiesApi->create_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Entity**](Entity.md)| JSON Entity Representation | 
 **options** | **str**| Options dictionary | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_entities**
> list[Entity] list_entities(id=id, type=type, id_pattern=id_pattern, type_pattern=type_pattern, q=q, mq=mq, georel=georel, geometry=geometry, coords=coords, limit=limit, offset=offset, attrs=attrs, order_by=order_by, options=options)



Retrieves a list of entities that match different criteria by id, type, pattern matching (either id or type) and/or those which match a query or geographical query (see [Simple Query Language](#simple_query_language) and  [Geographical Queries](#geographical_queries)). A given entity has to match all the criteria to be retrieved (i.e., the criteria is combined in a logical AND way). Note that pattern matching query parameters are incompatible (i.e. mutually exclusive) with their corresponding exact matching parameters, i.e. `idPattern` with `id` and `typePattern` with `type`. The response payload is an array containing one object per matching entity. Each entity follows the JSON entity Representation format (described in \"JSON Entity Representation\" section).  Response code: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.EntitiesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | A comma-separated list of elements. Retrieve entities whose ID matches one of the elements in the list. Incompatible with idPattern. (optional)
type = 'type_example' # str | comma-separated list of elements. Retrieve entities whose type matches one of the elements in the list. Incompatible with `typePattern`. (optional)
id_pattern = 'id_pattern_example' # str | A correctly formated regular expression. Retrieve entities whose ID matches the regular expression. Incompatible with id. (optional)
type_pattern = 'type_pattern_example' # str | A correctly formated regular expression. Retrieve entities whose type matches the regular expression. Incompatible with `type`. (optional)
q = 'q_example' # str | A query expression, composed of a list of statements separated by `;`, i.e., q=statement;statements;statement. See [Simple Query Language specification](#simple_query_language). (optional)
mq = 'mq_example' # str | A query expression for attribute metadata, composed of a list of statements separated by `;`, i.e., mq=statement1;statement2;statement3. See [Simple Query Language specification](#simple_query_language). (optional)
georel = 'georel_example' # str | Spatial relationship between matching entities and a reference shape. See [Geographical Queries](#geographical_queries). (optional)
geometry = 'geometry_example' # str | Geografical area to which the query is restricted. See [Geographical Queries](#geographical_queries). (optional)
coords = 'coords_example' # str | List of latitude-longitude pairs of coordinates separated by ';'. See [Geographical Queries](#geographical_queries). (optional)
limit = 1.2 # float | Limits the number of entities to be retrieved (optional)
offset = 1.2 # float | Establishes the offset from where entities are retrieved (optional)
attrs = 'attrs_example' # str | Comma-separated list of attribute names whose data are to be included in the response. The attributes are retrieved in the order specified by this parameter. If this parameter is not included, the attributes are retrieved in arbitrary order. (optional)
order_by = 'order_by_example' # str | Criteria for ordering results. See \"Ordering Results\" section for details. (optional)
options = 'options_example' # str | Options dictionary (optional)

try:
    api_response = api_instance.list_entities(id=id, type=type, id_pattern=id_pattern, type_pattern=type_pattern, q=q, mq=mq, georel=georel, geometry=geometry, coords=coords, limit=limit, offset=offset, attrs=attrs, order_by=order_by, options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitiesApi->list_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A comma-separated list of elements. Retrieve entities whose ID matches one of the elements in the list. Incompatible with idPattern. | [optional] 
 **type** | **str**| comma-separated list of elements. Retrieve entities whose type matches one of the elements in the list. Incompatible with &#x60;typePattern&#x60;. | [optional] 
 **id_pattern** | **str**| A correctly formated regular expression. Retrieve entities whose ID matches the regular expression. Incompatible with id. | [optional] 
 **type_pattern** | **str**| A correctly formated regular expression. Retrieve entities whose type matches the regular expression. Incompatible with &#x60;type&#x60;. | [optional] 
 **q** | **str**| A query expression, composed of a list of statements separated by &#x60;;&#x60;, i.e., q&#x3D;statement;statements;statement. See [Simple Query Language specification](#simple_query_language). | [optional] 
 **mq** | **str**| A query expression for attribute metadata, composed of a list of statements separated by &#x60;;&#x60;, i.e., mq&#x3D;statement1;statement2;statement3. See [Simple Query Language specification](#simple_query_language). | [optional] 
 **georel** | **str**| Spatial relationship between matching entities and a reference shape. See [Geographical Queries](#geographical_queries). | [optional] 
 **geometry** | **str**| Geografical area to which the query is restricted. See [Geographical Queries](#geographical_queries). | [optional] 
 **coords** | **str**| List of latitude-longitude pairs of coordinates separated by &#39;;&#39;. See [Geographical Queries](#geographical_queries). | [optional] 
 **limit** | **float**| Limits the number of entities to be retrieved | [optional] 
 **offset** | **float**| Establishes the offset from where entities are retrieved | [optional] 
 **attrs** | **str**| Comma-separated list of attribute names whose data are to be included in the response. The attributes are retrieved in the order specified by this parameter. If this parameter is not included, the attributes are retrieved in arbitrary order. | [optional] 
 **order_by** | **str**| Criteria for ordering results. See \&quot;Ordering Results\&quot; section for details. | [optional] 
 **options** | **str**| Options dictionary | [optional] 

### Return type

[**list[Entity]**](Entity.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_entity**
> remove_entity(entity_id, type=type)



Delete the entity. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.EntitiesApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Id of the entity to be deleted
type = 'type_example' # str | Entity type, to avoid ambiguity in the case there are several entities with the same entity id. (optional)

try:
    api_instance.remove_entity(entity_id, type=type)
except ApiException as e:
    print("Exception when calling EntitiesApi->remove_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity to be deleted | 
 **type** | **str**| Entity type, to avoid ambiguity in the case there are several entities with the same entity id. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_all_entity_attributes**
> replace_all_entity_attributes(entity_id, body, type=type, options=options)



The request payload is an object representing the new entity attributes. The object follows the JSON entity Representation format (described in a \"JSON Entity Representation\" above), except that `id` and `type` are not allowed. The attributes previously existing in the entity are removed and replaced by the ones in the request. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.EntitiesApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Id of the entity in question.
body = swagger_client.Attribute() # Attribute | JSON Attribute Representation
type = 'type_example' # str | Entity type, to avoid ambiguity in the case there are several entities with the same entity id. (optional)
options = 'options_example' # str | Operations options (optional)

try:
    api_instance.replace_all_entity_attributes(entity_id, body, type=type, options=options)
except ApiException as e:
    print("Exception when calling EntitiesApi->replace_all_entity_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity in question. | 
 **body** | [**Attribute**](Attribute.md)| JSON Attribute Representation | 
 **type** | **str**| Entity type, to avoid ambiguity in the case there are several entities with the same entity id. | [optional] 
 **options** | **str**| Operations options | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_entity**
> Entity retrieve_entity(entity_id, type=type, attrs=attrs, options=options)



The response is an object representing the entity identified by the ID. The object follows the JSON entity Representation format (described in \"JSON Entity Representation\" section). This operation must return one entity element only, but there may be more than one entity with the same ID (e.g. entities with same ID but different types). In such case, an error message is returned, with the HTTP status code set to 409 Conflict. Response: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.

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
api_instance = swagger_client.EntitiesApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Id of the entity to be retrieved
type = 'type_example' # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)
attrs = 'attrs_example' # str | Comma-separated list of attribute names whose data must be included in the response. The attributes are retrieved in the order specified by this parameter. If this parameter is not included, the attributes are retrieved in arbitrary order, and all the attributes of the entity are included in the response. (optional)
options = 'options_example' # str | Options dictionary (optional)

try:
    api_response = api_instance.retrieve_entity(entity_id, type=type, attrs=attrs, options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitiesApi->retrieve_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity to be retrieved | 
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional] 
 **attrs** | **str**| Comma-separated list of attribute names whose data must be included in the response. The attributes are retrieved in the order specified by this parameter. If this parameter is not included, the attributes are retrieved in arbitrary order, and all the attributes of the entity are included in the response. | [optional] 
 **options** | **str**| Options dictionary | [optional] 

### Return type

[**Entity**](Entity.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_entity_attributes**
> Attribute retrieve_entity_attributes(entity_id, type=type, attrs=attrs, options=options)



This request is similar to retreiving the whole entity, however this one omits the `id` and `type` fields. Just like the general request of getting an entire entity, this operation must return only one entity element. If more than one entity with the same ID is found (e.g. entities with same ID but different type), an error message is returned, with the HTTP status code set to 409 Conflict. Response: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.EntitiesApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Id of the entity to be retrieved
type = 'type_example' # str | Entity type, to avoid ambiguity in the case there are several entities with the same entity id. (optional)
attrs = 'attrs_example' # str | Comma-separated list of attribute names whose data are to be included in the response. The attributes are retrieved in the order specified by this parameter. If this parameter is not included, the attributes are retrieved in arbitrary order, and all the attributes of the entity are included in the response. (optional)
options = 'options_example' # str | Options dictionary (optional)

try:
    api_response = api_instance.retrieve_entity_attributes(entity_id, type=type, attrs=attrs, options=options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EntitiesApi->retrieve_entity_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity to be retrieved | 
 **type** | **str**| Entity type, to avoid ambiguity in the case there are several entities with the same entity id. | [optional] 
 **attrs** | **str**| Comma-separated list of attribute names whose data are to be included in the response. The attributes are retrieved in the order specified by this parameter. If this parameter is not included, the attributes are retrieved in arbitrary order, and all the attributes of the entity are included in the response. | [optional] 
 **options** | **str**| Options dictionary | [optional] 

### Return type

[**Attribute**](Attribute.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_existing_entity_attributes**
> update_existing_entity_attributes(entity_id, body, type=type, options=options)



The request payload is an object representing the attributes to update. The object follows the JSON entity Representation format (described in \"JSON Entity Representation\" section), except that `id` and `type` are not allowed. The entity attributes are updated with the ones in the payload. In addition to that, if one or more attributes in the payload doesn't exist in the entity, an error is returned. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.EntitiesApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Id of the entity to be updated
body = swagger_client.Attribute() # Attribute | JSON Attribute Representation
type = 'type_example' # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)
options = 'options_example' # str | Operations options (optional)

try:
    api_instance.update_existing_entity_attributes(entity_id, body, type=type, options=options)
except ApiException as e:
    print("Exception when calling EntitiesApi->update_existing_entity_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Id of the entity to be updated | 
 **body** | [**Attribute**](Attribute.md)| JSON Attribute Representation | 
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional] 
 **options** | **str**| Operations options | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_or_append_entity_attributes**
> update_or_append_entity_attributes(entity_id, body, type=type, options=options)



The request payload is an object representing the attributes to append or update. The object follows the JSON entity Representation format (described in \"JSON Entity Representation\" section), except that `id` and `type` are not allowed. The entity attributes are updated with the ones in the payload, depending on whether the `append` operation option is used or not. * If `append` is not used: the entity attributes are updated (if they previously exist) or appended   (if they don't previously exist) with the ones in the payload. * If `append` is used (i.e. strict append semantics): all the attributes in the payload not   previously existing in the entity are appended. In addition to that, in case some of the   attributes in the payload already exist in the entity, an error is returned. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.

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
api_instance = swagger_client.EntitiesApi(swagger_client.ApiClient(configuration))
entity_id = 'entity_id_example' # str | Entity id to be updated
body = swagger_client.Attribute() # Attribute | JSON Attribute Representation
type = 'type_example' # str | Entity type, to avoid ambiguity in case there are several entities with the same entity id. (optional)
options = 'options_example' # str | Operations options (optional)

try:
    api_instance.update_or_append_entity_attributes(entity_id, body, type=type, options=options)
except ApiException as e:
    print("Exception when calling EntitiesApi->update_or_append_entity_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| Entity id to be updated | 
 **body** | [**Attribute**](Attribute.md)| JSON Attribute Representation | 
 **type** | **str**| Entity type, to avoid ambiguity in case there are several entities with the same entity id. | [optional] 
 **options** | **str**| Operations options | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

