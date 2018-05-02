# swagger-client
NGSI V2 API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v2
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# create an instance of the API class
api_instance = swagger_client.APIEntryPointApi()

try:
    api_response = api_instance.retrieve_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIEntryPointApi->retrieve_api_resources: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.s.orchestracities.com/context/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIEntryPointApi* | [**retrieve_api_resources**](docs/APIEntryPointApi.md#retrieve_api_resources) | **GET** / | 
*AttributeValueApi* | [**get_attribute_value**](docs/AttributeValueApi.md#get_attribute_value) | **GET** /entities/{entityId}/attrs/{attrName}/value | 
*AttributeValueApi* | [**update_attribute_value**](docs/AttributeValueApi.md#update_attribute_value) | **PUT** /entities/{entityId}/attrs/{attrName}/value | 
*AttributesApi* | [**get_attribute_data**](docs/AttributesApi.md#get_attribute_data) | **GET** /entities/{entityId}/attrs/{attrName} | 
*AttributesApi* | [**remove_a_single_attribute**](docs/AttributesApi.md#remove_a_single_attribute) | **DELETE** /entities/{entityId}/attrs/{attrName} | 
*AttributesApi* | [**update_attribute_data**](docs/AttributesApi.md#update_attribute_data) | **PUT** /entities/{entityId}/attrs/{attrName} | 
*BatchOperationsApi* | [**query**](docs/BatchOperationsApi.md#query) | **POST** /op/query | 
*BatchOperationsApi* | [**update**](docs/BatchOperationsApi.md#update) | **POST** /op/update | 
*EntitiesApi* | [**create_entity**](docs/EntitiesApi.md#create_entity) | **POST** /entities | 
*EntitiesApi* | [**list_entities**](docs/EntitiesApi.md#list_entities) | **GET** /entities | 
*EntitiesApi* | [**remove_entity**](docs/EntitiesApi.md#remove_entity) | **DELETE** /entities/{entityId} | 
*EntitiesApi* | [**replace_all_entity_attributes**](docs/EntitiesApi.md#replace_all_entity_attributes) | **PUT** /entities/{entityId}/attrs | 
*EntitiesApi* | [**retrieve_entity**](docs/EntitiesApi.md#retrieve_entity) | **GET** /entities/{entityId} | 
*EntitiesApi* | [**retrieve_entity_attributes**](docs/EntitiesApi.md#retrieve_entity_attributes) | **GET** /entities/{entityId}/attrs | 
*EntitiesApi* | [**update_existing_entity_attributes**](docs/EntitiesApi.md#update_existing_entity_attributes) | **PATCH** /entities/{entityId}/attrs | 
*EntitiesApi* | [**update_or_append_entity_attributes**](docs/EntitiesApi.md#update_or_append_entity_attributes) | **POST** /entities/{entityId}/attrs | 
*SubscriptionsApi* | [**create_a_new_subscription**](docs/SubscriptionsApi.md#create_a_new_subscription) | **POST** /subscriptions | 
*SubscriptionsApi* | [**delete_subscription**](docs/SubscriptionsApi.md#delete_subscription) | **DELETE** /subscriptions/{subscriptionId} | 
*SubscriptionsApi* | [**retrieve_subscription**](docs/SubscriptionsApi.md#retrieve_subscription) | **GET** /subscriptions/{subscriptionId} | 
*SubscriptionsApi* | [**retrieve_subscriptions**](docs/SubscriptionsApi.md#retrieve_subscriptions) | **GET** /subscriptions | 
*SubscriptionsApi* | [**update_subscription**](docs/SubscriptionsApi.md#update_subscription) | **PATCH** /subscriptions/{subscriptionId} | 
*TypesApi* | [**retrieve_entity_type**](docs/TypesApi.md#retrieve_entity_type) | **GET** /types/{entityType} | 
*TypesApi* | [**retrieve_entity_types**](docs/TypesApi.md#retrieve_entity_types) | **GET** /types/ | 


## Documentation For Models

 - [APIEntryPoint](docs/APIEntryPoint.md)
 - [Attribute](docs/Attribute.md)
 - [AttributeValue](docs/AttributeValue.md)
 - [BatchOperation](docs/BatchOperation.md)
 - [Entity](docs/Entity.md)
 - [EntityType](docs/EntityType.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Query](docs/Query.md)
 - [QueryPattern](docs/QueryPattern.md)
 - [Subscription](docs/Subscription.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



