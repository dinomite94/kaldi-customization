# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class CreateProjectObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, acoustic_model=None):  # noqa: E501
        """CreateProjectObject - a model defined in OpenAPI

        :param name: The name of this CreateProjectObject.  # noqa: E501
        :type name: str
        :param acoustic_model: The acoustic_model of this CreateProjectObject.  # noqa: E501
        :type acoustic_model: str
        """
        self.openapi_types = {
            'name': str,
            'acoustic_model': str
        }

        self.attribute_map = {
            'name': 'name',
            'acoustic_model': 'acoustic_model'
        }

        self._name = name
        self._acoustic_model = acoustic_model

    @classmethod
    def from_dict(cls, dikt) -> 'CreateProjectObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateProjectObject of this CreateProjectObject.  # noqa: E501
        :rtype: CreateProjectObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateProjectObject.

        Name of the new project  # noqa: E501

        :return: The name of this CreateProjectObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateProjectObject.

        Name of the new project  # noqa: E501

        :param name: The name of this CreateProjectObject.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def acoustic_model(self):
        """Gets the acoustic_model of this CreateProjectObject.

        UUID of the acoustic model  # noqa: E501

        :return: The acoustic_model of this CreateProjectObject.
        :rtype: str
        """
        return self._acoustic_model

    @acoustic_model.setter
    def acoustic_model(self, acoustic_model):
        """Sets the acoustic_model of this CreateProjectObject.

        UUID of the acoustic model  # noqa: E501

        :param acoustic_model: The acoustic_model of this CreateProjectObject.
        :type acoustic_model: str
        """
        if acoustic_model is None:
            raise ValueError("Invalid value for `acoustic_model`, must not be `None`")  # noqa: E501

        self._acoustic_model = acoustic_model