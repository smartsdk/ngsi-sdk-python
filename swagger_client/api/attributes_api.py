# coding: utf-8

"""
    ngsi-v2

    NGSI V2 API  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AttributesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_attribute_data(self, entity_id, attr_name, **kwargs):  # noqa: E501
        """get_attribute_data  # noqa: E501

        Returns a JSON object with the attribute data of the attribute. The object follows the JSON Representation for attributes (described in \"JSON Attribute Representation\" section). Response: * Successful operation uses 200 OK. * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_attribute_data(entity_id, attr_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity_id: Id of the entity (required)
        :param str attr_name: Name of the attribute to be retrieved. (required)
        :param str type: Entity type, to avoid ambiguity in the case there are several entities with the same entity id.
        :return: Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_attribute_data_with_http_info(entity_id, attr_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_attribute_data_with_http_info(entity_id, attr_name, **kwargs)  # noqa: E501
            return data

    def get_attribute_data_with_http_info(self, entity_id, attr_name, **kwargs):  # noqa: E501
        """get_attribute_data  # noqa: E501

        Returns a JSON object with the attribute data of the attribute. The object follows the JSON Representation for attributes (described in \"JSON Attribute Representation\" section). Response: * Successful operation uses 200 OK. * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_attribute_data_with_http_info(entity_id, attr_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity_id: Id of the entity (required)
        :param str attr_name: Name of the attribute to be retrieved. (required)
        :param str type: Entity type, to avoid ambiguity in the case there are several entities with the same entity id.
        :return: Entity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_id', 'attr_name', 'type']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_attribute_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_attribute_data`")  # noqa: E501
        # verify the required parameter 'attr_name' is set
        if ('attr_name' not in params or
                params['attr_name'] is None):
            raise ValueError("Missing the required parameter `attr_name` when calling `get_attribute_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501
        if 'attr_name' in params:
            path_params['attrName'] = params['attr_name']  # noqa: E501

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/entities/{entityId}/attrs/{attrName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Entity',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_a_single_attribute(self, entity_id, attr_name, **kwargs):  # noqa: E501
        """remove_a_single_attribute  # noqa: E501

        Removes an entity attribute. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_a_single_attribute(entity_id, attr_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity_id: Id of the entity. (required)
        :param str attr_name: Attribute name. (required)
        :param str type: Entity type, to avoid ambiguity in the case there are several entities with the same entity id.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.remove_a_single_attribute_with_http_info(entity_id, attr_name, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_a_single_attribute_with_http_info(entity_id, attr_name, **kwargs)  # noqa: E501
            return data

    def remove_a_single_attribute_with_http_info(self, entity_id, attr_name, **kwargs):  # noqa: E501
        """remove_a_single_attribute  # noqa: E501

        Removes an entity attribute. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.remove_a_single_attribute_with_http_info(entity_id, attr_name, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity_id: Id of the entity. (required)
        :param str attr_name: Attribute name. (required)
        :param str type: Entity type, to avoid ambiguity in the case there are several entities with the same entity id.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_id', 'attr_name', 'type']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_a_single_attribute" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `remove_a_single_attribute`")  # noqa: E501
        # verify the required parameter 'attr_name' is set
        if ('attr_name' not in params or
                params['attr_name'] is None):
            raise ValueError("Missing the required parameter `attr_name` when calling `remove_a_single_attribute`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501
        if 'attr_name' in params:
            path_params['attrName'] = params['attr_name']  # noqa: E501

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/entities/{entityId}/attrs/{attrName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_attribute_data(self, entity_id, attr_name, body, **kwargs):  # noqa: E501
        """update_attribute_data  # noqa: E501

        The request payload is an object representing the new attribute data. Previous attribute data is replaced by the one in the request. The object follows the JSON Representation for attributes (described in \"JSON Attribute Representation\" section). Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_attribute_data(entity_id, attr_name, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity_id: Id of the entity to update (required)
        :param str attr_name: Attribute name (required)
        :param object body: (required)
        :param str type: Entity type, to avoid ambiguity in case there are several entities with the same entity id.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_attribute_data_with_http_info(entity_id, attr_name, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_attribute_data_with_http_info(entity_id, attr_name, body, **kwargs)  # noqa: E501
            return data

    def update_attribute_data_with_http_info(self, entity_id, attr_name, body, **kwargs):  # noqa: E501
        """update_attribute_data  # noqa: E501

        The request payload is an object representing the new attribute data. Previous attribute data is replaced by the one in the request. The object follows the JSON Representation for attributes (described in \"JSON Attribute Representation\" section). Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for   more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_attribute_data_with_http_info(entity_id, attr_name, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str entity_id: Id of the entity to update (required)
        :param str attr_name: Attribute name (required)
        :param object body: (required)
        :param str type: Entity type, to avoid ambiguity in case there are several entities with the same entity id.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_id', 'attr_name', 'body', 'type']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_attribute_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `update_attribute_data`")  # noqa: E501
        # verify the required parameter 'attr_name' is set
        if ('attr_name' not in params or
                params['attr_name'] is None):
            raise ValueError("Missing the required parameter `attr_name` when calling `update_attribute_data`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_attribute_data`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501
        if 'attr_name' in params:
            path_params['attrName'] = params['attr_name']  # noqa: E501

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/entities/{entityId}/attrs/{attrName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
