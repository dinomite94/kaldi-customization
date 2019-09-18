# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class DataPrepStats(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, unique_words_count=None, total_words_count=None, lines_count=None, files_count=None):  # noqa: E501
        """DataPrepStats - a model defined in OpenAPI

        :param unique_words_count: The unique_words_count of this DataPrepStats.  # noqa: E501
        :type unique_words_count: int
        :param total_words_count: The total_words_count of this DataPrepStats.  # noqa: E501
        :type total_words_count: int
        :param lines_count: The lines_count of this DataPrepStats.  # noqa: E501
        :type lines_count: int
        :param files_count: The files_count of this DataPrepStats.  # noqa: E501
        :type files_count: int
        """
        self.openapi_types = {
            'unique_words_count': int,
            'total_words_count': int,
            'lines_count': int,
            'files_count': int
        }

        self.attribute_map = {
            'unique_words_count': 'unique_words_count',
            'total_words_count': 'total_words_count',
            'lines_count': 'lines_count',
            'files_count': 'files_count'
        }

        self._unique_words_count = unique_words_count
        self._total_words_count = total_words_count
        self._lines_count = lines_count
        self._files_count = files_count

    @classmethod
    def from_dict(cls, dikt) -> 'DataPrepStats':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataPrepStats of this DataPrepStats.  # noqa: E501
        :rtype: DataPrepStats
        """
        return util.deserialize_model(dikt, cls)

    @property
    def unique_words_count(self):
        """Gets the unique_words_count of this DataPrepStats.

        The number of unique words  # noqa: E501

        :return: The unique_words_count of this DataPrepStats.
        :rtype: int
        """
        return self._unique_words_count

    @unique_words_count.setter
    def unique_words_count(self, unique_words_count):
        """Sets the unique_words_count of this DataPrepStats.

        The number of unique words  # noqa: E501

        :param unique_words_count: The unique_words_count of this DataPrepStats.
        :type unique_words_count: int
        """

        self._unique_words_count = unique_words_count

    @property
    def total_words_count(self):
        """Gets the total_words_count of this DataPrepStats.

        The total number words  # noqa: E501

        :return: The total_words_count of this DataPrepStats.
        :rtype: int
        """
        return self._total_words_count

    @total_words_count.setter
    def total_words_count(self, total_words_count):
        """Sets the total_words_count of this DataPrepStats.

        The total number words  # noqa: E501

        :param total_words_count: The total_words_count of this DataPrepStats.
        :type total_words_count: int
        """

        self._total_words_count = total_words_count

    @property
    def lines_count(self):
        """Gets the lines_count of this DataPrepStats.

        The number of processed lines  # noqa: E501

        :return: The lines_count of this DataPrepStats.
        :rtype: int
        """
        return self._lines_count

    @lines_count.setter
    def lines_count(self, lines_count):
        """Sets the lines_count of this DataPrepStats.

        The number of processed lines  # noqa: E501

        :param lines_count: The lines_count of this DataPrepStats.
        :type lines_count: int
        """

        self._lines_count = lines_count

    @property
    def files_count(self):
        """Gets the files_count of this DataPrepStats.

        The number of processed files  # noqa: E501

        :return: The files_count of this DataPrepStats.
        :rtype: int
        """
        return self._files_count

    @files_count.setter
    def files_count(self, files_count):
        """Sets the files_count of this DataPrepStats.

        The number of processed files  # noqa: E501

        :param files_count: The files_count of this DataPrepStats.
        :type files_count: int
        """

        self._files_count = files_count
