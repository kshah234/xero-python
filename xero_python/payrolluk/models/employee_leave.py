# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    OpenAPI spec version: 2.4.0
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class EmployeeLeave(BaseModel):
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
        "leave_id": "str",
        "leave_type_id": "str",
        "description": "str",
        "start_date": "date",
        "end_date": "date",
        "periods": "list[LeavePeriod]",
        "updated_date_utc": "datetime",
    }

    attribute_map = {
        "leave_id": "leaveID",
        "leave_type_id": "leaveTypeID",
        "description": "description",
        "start_date": "startDate",
        "end_date": "endDate",
        "periods": "periods",
        "updated_date_utc": "updatedDateUTC",
    }

    def __init__(
        self,
        leave_id=None,
        leave_type_id=None,
        description=None,
        start_date=None,
        end_date=None,
        periods=None,
        updated_date_utc=None,
    ):  # noqa: E501
        """EmployeeLeave - a model defined in OpenAPI"""  # noqa: E501

        self._leave_id = None
        self._leave_type_id = None
        self._description = None
        self._start_date = None
        self._end_date = None
        self._periods = None
        self._updated_date_utc = None
        self.discriminator = None

        if leave_id is not None:
            self.leave_id = leave_id
        self.leave_type_id = leave_type_id
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        if periods is not None:
            self.periods = periods
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc

    @property
    def leave_id(self):
        """Gets the leave_id of this EmployeeLeave.  # noqa: E501

        The Xero identifier for LeaveType  # noqa: E501

        :return: The leave_id of this EmployeeLeave.  # noqa: E501
        :rtype: str
        """
        return self._leave_id

    @leave_id.setter
    def leave_id(self, leave_id):
        """Sets the leave_id of this EmployeeLeave.

        The Xero identifier for LeaveType  # noqa: E501

        :param leave_id: The leave_id of this EmployeeLeave.  # noqa: E501
        :type: str
        """

        self._leave_id = leave_id

    @property
    def leave_type_id(self):
        """Gets the leave_type_id of this EmployeeLeave.  # noqa: E501

        The Xero identifier for LeaveType  # noqa: E501

        :return: The leave_type_id of this EmployeeLeave.  # noqa: E501
        :rtype: str
        """
        return self._leave_type_id

    @leave_type_id.setter
    def leave_type_id(self, leave_type_id):
        """Sets the leave_type_id of this EmployeeLeave.

        The Xero identifier for LeaveType  # noqa: E501

        :param leave_type_id: The leave_type_id of this EmployeeLeave.  # noqa: E501
        :type: str
        """
        if leave_type_id is None:
            raise ValueError(
                "Invalid value for `leave_type_id`, must not be `None`"
            )  # noqa: E501

        self._leave_type_id = leave_type_id

    @property
    def description(self):
        """Gets the description of this EmployeeLeave.  # noqa: E501

        The description of the leave  (max length = 50)  # noqa: E501

        :return: The description of this EmployeeLeave.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EmployeeLeave.

        The description of the leave  (max length = 50)  # noqa: E501

        :param description: The description of this EmployeeLeave.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError(
                "Invalid value for `description`, must not be `None`"
            )  # noqa: E501

        self._description = description

    @property
    def start_date(self):
        """Gets the start_date of this EmployeeLeave.  # noqa: E501

        Start date of the leave (YYYY-MM-DD)  # noqa: E501

        :return: The start_date of this EmployeeLeave.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this EmployeeLeave.

        Start date of the leave (YYYY-MM-DD)  # noqa: E501

        :param start_date: The start_date of this EmployeeLeave.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError(
                "Invalid value for `start_date`, must not be `None`"
            )  # noqa: E501

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this EmployeeLeave.  # noqa: E501

        End date of the leave (YYYY-MM-DD)  # noqa: E501

        :return: The end_date of this EmployeeLeave.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this EmployeeLeave.

        End date of the leave (YYYY-MM-DD)  # noqa: E501

        :param end_date: The end_date of this EmployeeLeave.  # noqa: E501
        :type: date
        """
        if end_date is None:
            raise ValueError(
                "Invalid value for `end_date`, must not be `None`"
            )  # noqa: E501

        self._end_date = end_date

    @property
    def periods(self):
        """Gets the periods of this EmployeeLeave.  # noqa: E501

        The leave period information. The StartDate, EndDate and NumberOfUnits needs to be specified when you do not want to calculate NumberOfUnits automatically. Using incorrect period StartDate and EndDate will result in automatic computation of the NumberOfUnits.  # noqa: E501

        :return: The periods of this EmployeeLeave.  # noqa: E501
        :rtype: list[LeavePeriod]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this EmployeeLeave.

        The leave period information. The StartDate, EndDate and NumberOfUnits needs to be specified when you do not want to calculate NumberOfUnits automatically. Using incorrect period StartDate and EndDate will result in automatic computation of the NumberOfUnits.  # noqa: E501

        :param periods: The periods of this EmployeeLeave.  # noqa: E501
        :type: list[LeavePeriod]
        """

        self._periods = periods

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this EmployeeLeave.  # noqa: E501

        UTC timestamp of last update to the leave type note  # noqa: E501

        :return: The updated_date_utc of this EmployeeLeave.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this EmployeeLeave.

        UTC timestamp of last update to the leave type note  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this EmployeeLeave.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc
