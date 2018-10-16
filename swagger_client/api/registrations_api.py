# coding: utf-8

"""
    ngsi-v2

    NGSI V2 API RC-2018.04  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class RegistrationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_registrations(self, body, **kwargs):  # noqa: E501
        """create_registrations  # noqa: E501

        Creates a new context provider registration. This is typically used for binding context sources as providers of certain data. The registration is represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 201 Created * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_registrations(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Registration body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_registrations_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_registrations_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_registrations_with_http_info(self, body, **kwargs):  # noqa: E501
        """create_registrations  # noqa: E501

        Creates a new context provider registration. This is typically used for binding context sources as providers of certain data. The registration is represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 201 Created * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_registrations_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param Registration body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_registrations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_registrations`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/registrations', 'POST',
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

    def delete_registration(self, registration_id, **kwargs):  # noqa: E501
        """delete_registration  # noqa: E501

        Cancels a context provider registration. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_registration(registration_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str registration_id: registration Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_registration_with_http_info(registration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_registration_with_http_info(registration_id, **kwargs)  # noqa: E501
            return data

    def delete_registration_with_http_info(self, registration_id, **kwargs):  # noqa: E501
        """delete_registration  # noqa: E501

        Cancels a context provider registration. Response: * Successful operation uses 204 No Content * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_registration_with_http_info(registration_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str registration_id: registration Id. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['registration_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_registration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'registration_id' is set
        if ('registration_id' not in params or
                params['registration_id'] is None):
            raise ValueError("Missing the required parameter `registration_id` when calling `delete_registration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'registration_id' in params:
            path_params['registrationId'] = params['registration_id']  # noqa: E501

        query_params = []

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
            '/registrations/{registrationId}', 'DELETE',
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

    def retrieve_registration(self, registration_id, **kwargs):  # noqa: E501
        """retrieve_registration  # noqa: E501

        The response is the registration represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.retrieve_registration(registration_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str registration_id: registration Id. (required)
        :return: RegistrationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.retrieve_registration_with_http_info(registration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_registration_with_http_info(registration_id, **kwargs)  # noqa: E501
            return data

    def retrieve_registration_with_http_info(self, registration_id, **kwargs):  # noqa: E501
        """retrieve_registration  # noqa: E501

        The response is the registration represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 200 OK * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.retrieve_registration_with_http_info(registration_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str registration_id: registration Id. (required)
        :return: RegistrationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['registration_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_registration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'registration_id' is set
        if ('registration_id' not in params or
                params['registration_id'] is None):
            raise ValueError("Missing the required parameter `registration_id` when calling `retrieve_registration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'registration_id' in params:
            path_params['registrationId'] = params['registration_id']  # noqa: E501

        query_params = []

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
            '/registrations/{registrationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegistrationResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_registrations(self, **kwargs):  # noqa: E501
        """retrieve_registrations  # noqa: E501

        Lists all the context provider registrations present in the system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.retrieve_registrations(async=True)
        >>> result = thread.get()

        :param async bool
        :param float limit: Limit the number of types to be retrieved
        :param float offset: Skip a number of records
        :param str options: Options dictionary
        :return: list[RegistrationResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.retrieve_registrations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_registrations_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_registrations_with_http_info(self, **kwargs):  # noqa: E501
        """retrieve_registrations  # noqa: E501

        Lists all the context provider registrations present in the system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.retrieve_registrations_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param float limit: Limit the number of types to be retrieved
        :param float offset: Skip a number of records
        :param str options: Options dictionary
        :return: list[RegistrationResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'options']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_registrations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'options' in params:
            query_params.append(('options', params['options']))  # noqa: E501

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
            '/registrations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RegistrationResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_registration(self, registration_id, body, **kwargs):  # noqa: E501
        """update_registration  # noqa: E501

        Creates a new context provider registration. This is typically used for binding context sources as providers of certain data. The registration is represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 201 Created * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_registration(registration_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str registration_id: registration Id. (required)
        :param Registration body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.update_registration_with_http_info(registration_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_registration_with_http_info(registration_id, body, **kwargs)  # noqa: E501
            return data

    def update_registration_with_http_info(self, registration_id, body, **kwargs):  # noqa: E501
        """update_registration  # noqa: E501

        Creates a new context provider registration. This is typically used for binding context sources as providers of certain data. The registration is represented by a JSON object as described at the beginning of this section. Response: * Successful operation uses 201 Created * Errors use a non-2xx and (optionally) an error payload. See subsection on \"Error Responses\" for more details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_registration_with_http_info(registration_id, body, async=True)
        >>> result = thread.get()

        :param async bool
        :param str registration_id: registration Id. (required)
        :param Registration body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['registration_id', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_registration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'registration_id' is set
        if ('registration_id' not in params or
                params['registration_id'] is None):
            raise ValueError("Missing the required parameter `registration_id` when calling `update_registration`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_registration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'registration_id' in params:
            path_params['registrationId'] = params['registration_id']  # noqa: E501

        query_params = []

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
            '/registrations/{registrationId}', 'PATCH',
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