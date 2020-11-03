# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.4.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class PaymentFrequencyType(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    FORTNIGHTLY = "FORTNIGHTLY"
    QUARTERLY = "QUARTERLY"
    TWICEMONTHLY = "TWICEMONTHLY"
    FOURWEEKLY = "FOURWEEKLY"
    YEARLY = "YEARLY"
