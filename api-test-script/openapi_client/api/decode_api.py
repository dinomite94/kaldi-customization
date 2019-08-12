# coding: utf-8

"""
    Kaldi Customization Server

    Kaldi Customization Server.  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class DecodeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_decode_result(self, project_uuid, training_version, decode_uuid, **kwargs):  # noqa: E501
        """Get the result of a decoding task  # noqa: E501

        Returns the result of a decoding task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_decode_result(project_uuid, training_version, decode_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_uuid: UUID of the project (required)
        :param int training_version: Training version of the project (required)
        :param str decode_uuid: UUID of the decoding task (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DecodeMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_decode_result_with_http_info(project_uuid, training_version, decode_uuid, **kwargs)  # noqa: E501

    def get_decode_result_with_http_info(self, project_uuid, training_version, decode_uuid, **kwargs):  # noqa: E501
        """Get the result of a decoding task  # noqa: E501

        Returns the result of a decoding task  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_decode_result_with_http_info(project_uuid, training_version, decode_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_uuid: UUID of the project (required)
        :param int training_version: Training version of the project (required)
        :param str decode_uuid: UUID of the decoding task (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DecodeMessage, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['project_uuid', 'training_version', 'decode_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_decode_result" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_uuid' is set
        if ('project_uuid' not in local_var_params or
                local_var_params['project_uuid'] is None):
            raise ApiValueError("Missing the required parameter `project_uuid` when calling `get_decode_result`")  # noqa: E501
        # verify the required parameter 'training_version' is set
        if ('training_version' not in local_var_params or
                local_var_params['training_version'] is None):
            raise ApiValueError("Missing the required parameter `training_version` when calling `get_decode_result`")  # noqa: E501
        # verify the required parameter 'decode_uuid' is set
        if ('decode_uuid' not in local_var_params or
                local_var_params['decode_uuid'] is None):
            raise ApiValueError("Missing the required parameter `decode_uuid` when calling `get_decode_result`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_uuid' in local_var_params:
            path_params['project_uuid'] = local_var_params['project_uuid']  # noqa: E501
        if 'training_version' in local_var_params:
            path_params['training_version'] = local_var_params['training_version']  # noqa: E501
        if 'decode_uuid' in local_var_params:
            path_params['decode_uuid'] = local_var_params['decode_uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/project/{project_uuid}/training/{training_version}/decode/{decode_uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DecodeMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_decodings(self, project_uuid, training_version, **kwargs):  # noqa: E501
        """List of all decodings  # noqa: E501

        Returns a list of all decodings for this training version  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_decodings(project_uuid, training_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_uuid: UUID of the project (required)
        :param int training_version: Training version of the project (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[DecodeMessage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_decodings_with_http_info(project_uuid, training_version, **kwargs)  # noqa: E501

    def get_decodings_with_http_info(self, project_uuid, training_version, **kwargs):  # noqa: E501
        """List of all decodings  # noqa: E501

        Returns a list of all decodings for this training version  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_decodings_with_http_info(project_uuid, training_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_uuid: UUID of the project (required)
        :param int training_version: Training version of the project (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[DecodeMessage], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['project_uuid', 'training_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_decodings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_uuid' is set
        if ('project_uuid' not in local_var_params or
                local_var_params['project_uuid'] is None):
            raise ApiValueError("Missing the required parameter `project_uuid` when calling `get_decodings`")  # noqa: E501
        # verify the required parameter 'training_version' is set
        if ('training_version' not in local_var_params or
                local_var_params['training_version'] is None):
            raise ApiValueError("Missing the required parameter `training_version` when calling `get_decodings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_uuid' in local_var_params:
            path_params['project_uuid'] = local_var_params['project_uuid']  # noqa: E501
        if 'training_version' in local_var_params:
            path_params['training_version'] = local_var_params['training_version']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/project/{project_uuid}/training/{training_version}/decode', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DecodeMessage]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def start_decode(self, project_uuid, training_version, audio_file, **kwargs):  # noqa: E501
        """Decode audio to text  # noqa: E501

        Decode audio data to text using the trained project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_decode(project_uuid, training_version, audio_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_uuid: UUID of the project (required)
        :param int training_version: Training version of the project (required)
        :param file audio_file: Audio file for decoding (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DecodeTaskReference
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.start_decode_with_http_info(project_uuid, training_version, audio_file, **kwargs)  # noqa: E501

    def start_decode_with_http_info(self, project_uuid, training_version, audio_file, **kwargs):  # noqa: E501
        """Decode audio to text  # noqa: E501

        Decode audio data to text using the trained project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.start_decode_with_http_info(project_uuid, training_version, audio_file, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project_uuid: UUID of the project (required)
        :param int training_version: Training version of the project (required)
        :param file audio_file: Audio file for decoding (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DecodeTaskReference, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['project_uuid', 'training_version', 'audio_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method start_decode" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project_uuid' is set
        if ('project_uuid' not in local_var_params or
                local_var_params['project_uuid'] is None):
            raise ApiValueError("Missing the required parameter `project_uuid` when calling `start_decode`")  # noqa: E501
        # verify the required parameter 'training_version' is set
        if ('training_version' not in local_var_params or
                local_var_params['training_version'] is None):
            raise ApiValueError("Missing the required parameter `training_version` when calling `start_decode`")  # noqa: E501
        # verify the required parameter 'audio_file' is set
        if ('audio_file' not in local_var_params or
                local_var_params['audio_file'] is None):
            raise ApiValueError("Missing the required parameter `audio_file` when calling `start_decode`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_uuid' in local_var_params:
            path_params['project_uuid'] = local_var_params['project_uuid']  # noqa: E501
        if 'training_version' in local_var_params:
            path_params['training_version'] = local_var_params['training_version']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'audio_file' in local_var_params:
            local_var_files['audio_file'] = local_var_params['audio_file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/project/{project_uuid}/training/{training_version}/decode', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DecodeTaskReference',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
