# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.acoustic_model import AcousticModel
from openapi_server.models.training import Training
from openapi_server.models.user import User
from openapi_server import util

from openapi_server.models.acoustic_model import AcousticModel  # noqa: E501
from openapi_server.models.training import Training  # noqa: E501
from openapi_server.models.user import User  # noqa: E501

class Project(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, uuid=None, acoustic_model=None, parent=None, trainings=None, creation_timestamp=None, owner=None):  # noqa: E501
        """Project - a model defined in OpenAPI

        :param name: The name of this Project.  # noqa: E501
        :type name: str
        :param uuid: The uuid of this Project.  # noqa: E501
        :type uuid: str
        :param acoustic_model: The acoustic_model of this Project.  # noqa: E501
        :type acoustic_model: AcousticModel
        :param parent: The parent of this Project.  # noqa: E501
        :type parent: str
        :param trainings: The trainings of this Project.  # noqa: E501
        :type trainings: List[Training]
        :param creation_timestamp: The creation_timestamp of this Project.  # noqa: E501
        :type creation_timestamp: datetime
        :param owner: The owner of this Project.  # noqa: E501
        :type owner: User
        """
        self.openapi_types = {
            'name': str,
            'uuid': str,
            'acoustic_model': AcousticModel,
            'parent': str,
            'trainings': List[Training],
            'creation_timestamp': datetime,
            'owner': User
        }

        self.attribute_map = {
            'name': 'name',
            'uuid': 'uuid',
            'acoustic_model': 'acoustic_model',
            'parent': 'parent',
            'trainings': 'trainings',
            'creation_timestamp': 'creation_timestamp',
            'owner': 'owner'
        }

        self._name = name
        self._uuid = uuid
        self._acoustic_model = acoustic_model
        self._parent = parent
        self._trainings = trainings
        self._creation_timestamp = creation_timestamp
        self._owner = owner

    @classmethod
    def from_dict(cls, dikt) -> 'Project':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Project of this Project.  # noqa: E501
        :rtype: Project
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Project.


        :return: The name of this Project.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.


        :param name: The name of this Project.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def uuid(self):
        """Gets the uuid of this Project.


        :return: The uuid of this Project.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Project.


        :param uuid: The uuid of this Project.
        :type uuid: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def acoustic_model(self):
        """Gets the acoustic_model of this Project.


        :return: The acoustic_model of this Project.
        :rtype: AcousticModel
        """
        return self._acoustic_model

    @acoustic_model.setter
    def acoustic_model(self, acoustic_model):
        """Sets the acoustic_model of this Project.


        :param acoustic_model: The acoustic_model of this Project.
        :type acoustic_model: AcousticModel
        """
        if acoustic_model is None:
            raise ValueError("Invalid value for `acoustic_model`, must not be `None`")  # noqa: E501

        self._acoustic_model = acoustic_model

    @property
    def parent(self):
        """Gets the parent of this Project.

        UUID of the parent project  # noqa: E501

        :return: The parent of this Project.
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Project.

        UUID of the parent project  # noqa: E501

        :param parent: The parent of this Project.
        :type parent: str
        """

        self._parent = parent

    @property
    def trainings(self):
        """Gets the trainings of this Project.


        :return: The trainings of this Project.
        :rtype: List[Training]
        """
        return self._trainings

    @trainings.setter
    def trainings(self, trainings):
        """Sets the trainings of this Project.


        :param trainings: The trainings of this Project.
        :type trainings: List[Training]
        """

        self._trainings = trainings

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this Project.


        :return: The creation_timestamp of this Project.
        :rtype: datetime
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this Project.


        :param creation_timestamp: The creation_timestamp of this Project.
        :type creation_timestamp: datetime
        """

        self._creation_timestamp = creation_timestamp

    @property
    def owner(self):
        """Gets the owner of this Project.


        :return: The owner of this Project.
        :rtype: User
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Project.


        :param owner: The owner of this Project.
        :type owner: User
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner
