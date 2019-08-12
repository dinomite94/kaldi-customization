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


class Project(object):
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
        'uuid': 'str',
        'acoustic_model': 'AcousticModel',
        'parent': 'str',
        'trainings': 'list[Training]',
        'creation_timestamp': 'datetime',
        'owner': 'User'
    }

    attribute_map = {
        'name': 'name',
        'uuid': 'uuid',
        'acoustic_model': 'acoustic_model',
        'parent': 'parent',
        'trainings': 'trainings',
        'creation_timestamp': 'creation_timestamp',
        'owner': 'owner'
    }

    def __init__(self, name=None, uuid=None, acoustic_model=None, parent=None, trainings=None, creation_timestamp=None, owner=None):  # noqa: E501
        """Project - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._uuid = None
        self._acoustic_model = None
        self._parent = None
        self._trainings = None
        self._creation_timestamp = None
        self._owner = None
        self.discriminator = None

        self.name = name
        self.uuid = uuid
        self.acoustic_model = acoustic_model
        if parent is not None:
            self.parent = parent
        if trainings is not None:
            self.trainings = trainings
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        self.owner = owner

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501


        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.


        :param name: The name of this Project.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this Project.  # noqa: E501


        :return: The uuid of this Project.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Project.


        :param uuid: The uuid of this Project.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def acoustic_model(self):
        """Gets the acoustic_model of this Project.  # noqa: E501


        :return: The acoustic_model of this Project.  # noqa: E501
        :rtype: AcousticModel
        """
        return self._acoustic_model

    @acoustic_model.setter
    def acoustic_model(self, acoustic_model):
        """Sets the acoustic_model of this Project.


        :param acoustic_model: The acoustic_model of this Project.  # noqa: E501
        :type: AcousticModel
        """
        if acoustic_model is None:
            raise ValueError("Invalid value for `acoustic_model`, must not be `None`")  # noqa: E501

        self._acoustic_model = acoustic_model

    @property
    def parent(self):
        """Gets the parent of this Project.  # noqa: E501

        UUID of the parent project  # noqa: E501

        :return: The parent of this Project.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Project.

        UUID of the parent project  # noqa: E501

        :param parent: The parent of this Project.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def trainings(self):
        """Gets the trainings of this Project.  # noqa: E501


        :return: The trainings of this Project.  # noqa: E501
        :rtype: list[Training]
        """
        return self._trainings

    @trainings.setter
    def trainings(self, trainings):
        """Sets the trainings of this Project.


        :param trainings: The trainings of this Project.  # noqa: E501
        :type: list[Training]
        """

        self._trainings = trainings

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this Project.  # noqa: E501


        :return: The creation_timestamp of this Project.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this Project.


        :param creation_timestamp: The creation_timestamp of this Project.  # noqa: E501
        :type: datetime
        """

        self._creation_timestamp = creation_timestamp

    @property
    def owner(self):
        """Gets the owner of this Project.  # noqa: E501


        :return: The owner of this Project.  # noqa: E501
        :rtype: User
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Project.


        :param owner: The owner of this Project.  # noqa: E501
        :type: User
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

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
        if not isinstance(other, Project):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
