# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.4.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class CISSetting(BaseModel):
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
    openapi_types = {"cis_enabled": "bool", "rate": "int"}

    attribute_map = {"cis_enabled": "CISEnabled", "rate": "Rate"}

    def __init__(self, cis_enabled=None, rate=None):  # noqa: E501
        """CISSetting - a model defined in OpenAPI"""  # noqa: E501

        self._cis_enabled = None
        self._rate = None
        self.discriminator = None

        if cis_enabled is not None:
            self.cis_enabled = cis_enabled
        if rate is not None:
            self.rate = rate

    @property
    def cis_enabled(self):
        """Gets the cis_enabled of this CISSetting.  # noqa: E501

        Boolean that describes if the contact is a CIS Subcontractor  # noqa: E501

        :return: The cis_enabled of this CISSetting.  # noqa: E501
        :rtype: bool
        """
        return self._cis_enabled

    @cis_enabled.setter
    def cis_enabled(self, cis_enabled):
        """Sets the cis_enabled of this CISSetting.

        Boolean that describes if the contact is a CIS Subcontractor  # noqa: E501

        :param cis_enabled: The cis_enabled of this CISSetting.  # noqa: E501
        :type: bool
        """

        self._cis_enabled = cis_enabled

    @property
    def rate(self):
        """Gets the rate of this CISSetting.  # noqa: E501

        CIS Deduction rate for the contact if he is a subcontractor. If the contact is not CISEnabled, then the rate is not returned  # noqa: E501

        :return: The rate of this CISSetting.  # noqa: E501
        :rtype: int
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this CISSetting.

        CIS Deduction rate for the contact if he is a subcontractor. If the contact is not CISEnabled, then the rate is not returned  # noqa: E501

        :param rate: The rate of this CISSetting.  # noqa: E501
        :type: int
        """

        self._rate = rate
