# coding: utf-8

"""
    Kaldi Customization Server

    Kaldi Customization Server.  # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CallbackObject(object):
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
        'url': 'str',
        'method': 'CallbackMethod'
    }

    attribute_map = {
        'url': 'url',
        'method': 'method'
    }

    def __init__(self, url=None, method=None):  # noqa: E501
        """CallbackObject - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._method = None
        self.discriminator = None

        self.url = url
        self.method = method

    @property
    def url(self):
        """Gets the url of this CallbackObject.  # noqa: E501

        The URL to be called  # noqa: E501

        :return: The url of this CallbackObject.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CallbackObject.

        The URL to be called  # noqa: E501

        :param url: The url of this CallbackObject.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def method(self):
        """Gets the method of this CallbackObject.  # noqa: E501


        :return: The method of this CallbackObject.  # noqa: E501
        :rtype: CallbackMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this CallbackObject.


        :param method: The method of this CallbackObject.  # noqa: E501
        :type: CallbackMethod
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

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
        if not isinstance(other, CallbackObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other