# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ResourceStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    Upload_InProgress = "0"
    Upload_Failure = "1"
    TextPreparation_Ready = "9"
    TextPreparation_Pending = "10"
    TextPreparation_InProcess = "11"
    TextPreparation_Failure = "12"
    TextPreparation_Success = "13"

    def __init__(self):  # noqa: E501
        """ResourceStatus - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ResourceStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ResourceStatus of this ResourceStatus.  # noqa: E501
        :rtype: ResourceStatus
        """
        return util.deserialize_model(dikt, cls)

    @staticmethod
    def ResourceStateEnum_to_ResourceStatus(resourceState):
        return {
            0: ResourceStatus.Upload_InProgress,
            1: ResourceStatus.Upload_Failure,
            9: ResourceStatus.TextPreparation_Ready,

            10: ResourceStatus.TextPreparation_Pending,
            11: ResourceStatus.TextPreparation_InProcess,
            12: ResourceStatus.TextPreparation_Failure,
            13: ResourceStatus.TextPreparation_Success
            }[resourceState]
