# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TrainingStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    Init = "100"
    TextPrep_Pending = "150"
    TextPrep_Failure = "151"
    Trainable = "200"
    Training_DataPrep_Pending = "205"
    Training_DataPrep_InProgress = "206"
    Training_DataPrep_Success = "207"
    Training_DataPrep_Failure = "208"
    Training_Pending = "210"
    Training_In_Progress = "220"
    Training_Success = "300"
    Training_Failure = "320"

    def __init__(self):  # noqa: E501
        """TrainingStatus - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'TrainingStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TrainingStatus of this TrainingStatus.  # noqa: E501
        :rtype: TrainingStatus
        """
        return util.deserialize_model(dikt, cls)
