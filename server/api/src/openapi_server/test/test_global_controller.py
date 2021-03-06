# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.acoustic_model import AcousticModel  # noqa: E501
from openapi_server.models.language import Language  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGlobalController(BaseTestCase):
    """GlobalController integration test stubs"""

    def test_download_acoustic_model(self):
        """Test case for download_acoustic_model

        Returns the acoustic model
        """
        headers = { 
            'Accept': 'application/zip',
        }
        response = self.client.open(
            '/api/v1/global/acoustic_models/{acoustic_model_uuid}/model'.format(acoustic_model_uuid='acoustic_model_uuid_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_acoustic_models(self):
        """Test case for get_acoustic_models

        Returns a list of available acoustic models
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/global/acoustic_models',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_languages(self):
        """Test case for get_languages

        Returns a list of available languages
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/global/languages',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
