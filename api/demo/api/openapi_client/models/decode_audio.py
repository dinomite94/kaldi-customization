# coding: utf-8

"""
    Kaldi Customization Server

    Kaldi Customization Server.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DecodeAudio(object):
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
        'transcripts': 'list[object]',
        'audio': 'Audio',
        'session_uuid': 'str'
    }

    attribute_map = {
        'transcripts': 'transcripts',
        'audio': 'audio',
        'session_uuid': 'session_uuid'
    }

    def __init__(self, transcripts=None, audio=None, session_uuid=None):  # noqa: E501
        """DecodeAudio - a model defined in OpenAPI"""  # noqa: E501

        self._transcripts = None
        self._audio = None
        self._session_uuid = None
        self.discriminator = None

        if transcripts is not None:
            self.transcripts = transcripts
        if audio is not None:
            self.audio = audio
        if session_uuid is not None:
            self.session_uuid = session_uuid

    @property
    def transcripts(self):
        """Gets the transcripts of this DecodeAudio.  # noqa: E501


        :return: The transcripts of this DecodeAudio.  # noqa: E501
        :rtype: list[object]
        """
        return self._transcripts

    @transcripts.setter
    def transcripts(self, transcripts):
        """Sets the transcripts of this DecodeAudio.


        :param transcripts: The transcripts of this DecodeAudio.  # noqa: E501
        :type: list[object]
        """

        self._transcripts = transcripts

    @property
    def audio(self):
        """Gets the audio of this DecodeAudio.  # noqa: E501


        :return: The audio of this DecodeAudio.  # noqa: E501
        :rtype: Audio
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this DecodeAudio.


        :param audio: The audio of this DecodeAudio.  # noqa: E501
        :type: Audio
        """

        self._audio = audio

    @property
    def session_uuid(self):
        """Gets the session_uuid of this DecodeAudio.  # noqa: E501


        :return: The session_uuid of this DecodeAudio.  # noqa: E501
        :rtype: str
        """
        return self._session_uuid

    @session_uuid.setter
    def session_uuid(self, session_uuid):
        """Sets the session_uuid of this DecodeAudio.


        :param session_uuid: The session_uuid of this DecodeAudio.  # noqa: E501
        :type: str
        """

        self._session_uuid = session_uuid

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
        if not isinstance(other, DecodeAudio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
