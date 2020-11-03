# coding: utf-8

"""
    Xero Projects API

    This is the Xero Projects API  # noqa: E501

    OpenAPI spec version: 2.4.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Error(BaseModel):
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
    openapi_types = {"message": "str", "model_state": "object"}

    attribute_map = {"message": "message", "model_state": "modelState"}

    def __init__(self, message=None, model_state=None):  # noqa: E501
        """Error - a model defined in OpenAPI"""  # noqa: E501

        self._message = None
        self._model_state = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if model_state is not None:
            self.model_state = model_state

    @property
    def message(self):
        """Gets the message of this Error.  # noqa: E501

        Exception message  # noqa: E501

        :return: The message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this Error.

        Exception message  # noqa: E501

        :param message: The message of this Error.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def model_state(self):
        """Gets the model_state of this Error.  # noqa: E501

        Array of Elements of validation Errors  # noqa: E501

        :return: The model_state of this Error.  # noqa: E501
        :rtype: object
        """
        return self._model_state

    @model_state.setter
    def model_state(self, model_state):
        """Sets the model_state of this Error.

        Array of Elements of validation Errors  # noqa: E501

        :param model_state: The model_state of this Error.  # noqa: E501
        :type: object
        """

        self._model_state = model_state
