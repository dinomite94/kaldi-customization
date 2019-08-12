# coding: utf-8

"""
    Kaldi Customization Server

    Kaldi Customization Server.  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AcousticModel(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'language': 'Language',
        'model_type': 'AcousticModelType',
        'uuid': 'str'
    }

    attribute_map = {
        'name': 'name',
        'language': 'language',
        'model_type': 'model_type',
        'uuid': 'uuid'
    }

    def __init__(self, name=None, language=None, model_type=None, uuid=None):  # noqa: E501
        """AcousticModel - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._language = None
        self._model_type = None
        self._uuid = None
        self.discriminator = None

        self.name = name
        self.language = language
        self.model_type = model_type
        self.uuid = uuid

    @property
    def name(self):
        """Gets the name of this AcousticModel.  # noqa: E501


        :return: The name of this AcousticModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AcousticModel.


        :param name: The name of this AcousticModel.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def language(self):
        """Gets the language of this AcousticModel.  # noqa: E501


        :return: The language of this AcousticModel.  # noqa: E501
        :rtype: Language
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AcousticModel.


        :param language: The language of this AcousticModel.  # noqa: E501
        :type: Language
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def model_type(self):
        """Gets the model_type of this AcousticModel.  # noqa: E501


        :return: The model_type of this AcousticModel.  # noqa: E501
        :rtype: AcousticModelType
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """Sets the model_type of this AcousticModel.


        :param model_type: The model_type of this AcousticModel.  # noqa: E501
        :type: AcousticModelType
        """
        if model_type is None:
            raise ValueError("Invalid value for `model_type`, must not be `None`")  # noqa: E501

        self._model_type = model_type

    @property
    def uuid(self):
        """Gets the uuid of this AcousticModel.  # noqa: E501


        :return: The uuid of this AcousticModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this AcousticModel.


        :param uuid: The uuid of this AcousticModel.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AcousticModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
