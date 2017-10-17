# coding: utf-8

"""
    Fanlens API

     Fanlens API to handle \"activities\". Predictions are performed automatically and can be managed here ## Concepts The API consists of 4 main concepts: sources, activities and tags (bundled in tagsets) and models used for predictions. * An activity is a text based action performed by a user, e.g. a Facebook Comment or a Tweet. * A source is the originator of these activities and is used for importing. Currently Facebook, Twitter, and Generic Sources are supported. * A tag is a piece of meta information that is used to build specialized speech models, e.g. \"positive\", or \"negative\". They are bundled in tagsets for convenience, e.g. \"Emotion\".

    OpenAPI spec version: 4.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ModelQuery(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'source_ids': 'list[int]',
        'tagset_id': 'float'
    }

    attribute_map = {
        'source_ids': 'source_ids',
        'tagset_id': 'tagset_id'
    }

    def __init__(self, source_ids=None, tagset_id=None):
        """
        ModelQuery - a model defined in Swagger
        """

        self._source_ids = None
        self._tagset_id = None

        if source_ids is not None:
          self.source_ids = source_ids
        if tagset_id is not None:
          self.tagset_id = tagset_id

    @property
    def source_ids(self):
        """
        Gets the source_ids of this ModelQuery.
        list of sources to use, empty list means all

        :return: The source_ids of this ModelQuery.
        :rtype: list[int]
        """
        return self._source_ids

    @source_ids.setter
    def source_ids(self, source_ids):
        """
        Sets the source_ids of this ModelQuery.
        list of sources to use, empty list means all

        :param source_ids: The source_ids of this ModelQuery.
        :type: list[int]
        """

        self._source_ids = source_ids

    @property
    def tagset_id(self):
        """
        Gets the tagset_id of this ModelQuery.
        the tagset id to find, must be accessible by user

        :return: The tagset_id of this ModelQuery.
        :rtype: float
        """
        return self._tagset_id

    @tagset_id.setter
    def tagset_id(self, tagset_id):
        """
        Sets the tagset_id of this ModelQuery.
        the tagset id to find, must be accessible by user

        :param tagset_id: The tagset_id of this ModelQuery.
        :type: float
        """

        self._tagset_id = tagset_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ModelQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
