# coding: utf-8

"""
    Kaldi Customization Server

    Kaldi Customization Server.  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.project_api import ProjectApi  # noqa: E501
from openapi_client.rest import ApiException


class TestProjectApi(unittest.TestCase):
    """ProjectApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.project_api.ProjectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project(self):
        """Test case for create_project

        Create a new project  # noqa: E501
        """
        pass

    def test_get_project_by_uuid(self):
        """Test case for get_project_by_uuid

        Find project by UUID  # noqa: E501
        """
        pass

    def test_get_projects(self):
        """Test case for get_projects

        Returns a list of available projects  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
