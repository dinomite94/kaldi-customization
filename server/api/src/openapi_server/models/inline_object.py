# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class InlineObject(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, audio_file=None):  # noqa: E501
        """InlineObject - a model defined in OpenAPI

        :param audio_file: The audio_file of this InlineObject.  # noqa: E501
        :type audio_file: file
        """
        self.openapi_types = {
            'audio_file': file
        }

        self.attribute_map = {
            'audio_file': 'audio_file'
        }

        self._audio_file = audio_file

    @classmethod
    def from_dict(cls, dikt) -> 'InlineObject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_object of this InlineObject.  # noqa: E501
        :rtype: InlineObject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def audio_file(self):
        """Gets the audio_file of this InlineObject.

        Audio file for decoding  # noqa: E501

        :return: The audio_file of this InlineObject.
        :rtype: file
        """
        return self._audio_file

    @audio_file.setter
    def audio_file(self, audio_file):
        """Sets the audio_file of this InlineObject.

        Audio file for decoding  # noqa: E501

        :param audio_file: The audio_file of this InlineObject.
        :type audio_file: file
        """
        if audio_file is None:
            raise ValueError("Invalid value for `audio_file`, must not be `None`")  # noqa: E501

        self._audio_file = audio_file