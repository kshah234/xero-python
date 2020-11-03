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


class Benefit(BaseModel):
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
        "id": "str",
        "name": "str",
        "category": "str",
        "liability_account_id": "str",
        "expense_account_id": "str",
        "standard_amount": "float",
        "percentage": "float",
        "calculation_type": "str",
        "current_record": "bool",
        "subject_to_nic": "bool",
        "subject_to_pension": "bool",
        "subject_to_tax": "bool",
        "is_calculating_on_qualifying_earnings": "bool",
        "show_balance_to_employee": "bool",
    }

    attribute_map = {
        "id": "id",
        "name": "name",
        "category": "category",
        "liability_account_id": "liabilityAccountId",
        "expense_account_id": "expenseAccountId",
        "standard_amount": "standardAmount",
        "percentage": "percentage",
        "calculation_type": "calculationType",
        "current_record": "currentRecord",
        "subject_to_nic": "subjectToNIC",
        "subject_to_pension": "subjectToPension",
        "subject_to_tax": "subjectToTax",
        "is_calculating_on_qualifying_earnings": "isCalculatingOnQualifyingEarnings",
        "show_balance_to_employee": "showBalanceToEmployee",
    }

    def __init__(
        self,
        id=None,
        name=None,
        category=None,
        liability_account_id=None,
        expense_account_id=None,
        standard_amount=None,
        percentage=None,
        calculation_type=None,
        current_record=None,
        subject_to_nic=None,
        subject_to_pension=None,
        subject_to_tax=None,
        is_calculating_on_qualifying_earnings=None,
        show_balance_to_employee=None,
    ):  # noqa: E501
        """Benefit - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._category = None
        self._liability_account_id = None
        self._expense_account_id = None
        self._standard_amount = None
        self._percentage = None
        self._calculation_type = None
        self._current_record = None
        self._subject_to_nic = None
        self._subject_to_pension = None
        self._subject_to_tax = None
        self._is_calculating_on_qualifying_earnings = None
        self._show_balance_to_employee = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.category = category
        self.liability_account_id = liability_account_id
        self.expense_account_id = expense_account_id
        if standard_amount is not None:
            self.standard_amount = standard_amount
        self.percentage = percentage
        self.calculation_type = calculation_type
        if current_record is not None:
            self.current_record = current_record
        if subject_to_nic is not None:
            self.subject_to_nic = subject_to_nic
        if subject_to_pension is not None:
            self.subject_to_pension = subject_to_pension
        if subject_to_tax is not None:
            self.subject_to_tax = subject_to_tax
        if is_calculating_on_qualifying_earnings is not None:
            self.is_calculating_on_qualifying_earnings = (
                is_calculating_on_qualifying_earnings
            )
        if show_balance_to_employee is not None:
            self.show_balance_to_employee = show_balance_to_employee

    @property
    def id(self):
        """Gets the id of this Benefit.  # noqa: E501

        unique identifier in Xero  # noqa: E501

        :return: The id of this Benefit.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Benefit.

        unique identifier in Xero  # noqa: E501

        :param id: The id of this Benefit.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Benefit.  # noqa: E501

        Name of the employer pension  # noqa: E501

        :return: The name of this Benefit.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Benefit.

        Name of the employer pension  # noqa: E501

        :param name: The name of this Benefit.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def category(self):
        """Gets the category of this Benefit.  # noqa: E501

        Category type of the employer pension  # noqa: E501

        :return: The category of this Benefit.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Benefit.

        Category type of the employer pension  # noqa: E501

        :param category: The category of this Benefit.  # noqa: E501
        :type: str
        """
        if category is None:
            raise ValueError(
                "Invalid value for `category`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["StakeholderPension", "Other", "None"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}".format(  # noqa: E501
                    category, allowed_values
                )
            )

        self._category = category

    @property
    def liability_account_id(self):
        """Gets the liability_account_id of this Benefit.  # noqa: E501

        Xero identifier for Liability Account  # noqa: E501

        :return: The liability_account_id of this Benefit.  # noqa: E501
        :rtype: str
        """
        return self._liability_account_id

    @liability_account_id.setter
    def liability_account_id(self, liability_account_id):
        """Sets the liability_account_id of this Benefit.

        Xero identifier for Liability Account  # noqa: E501

        :param liability_account_id: The liability_account_id of this Benefit.  # noqa: E501
        :type: str
        """
        if liability_account_id is None:
            raise ValueError(
                "Invalid value for `liability_account_id`, must not be `None`"
            )  # noqa: E501

        self._liability_account_id = liability_account_id

    @property
    def expense_account_id(self):
        """Gets the expense_account_id of this Benefit.  # noqa: E501

        Xero identifier for Expense Account  # noqa: E501

        :return: The expense_account_id of this Benefit.  # noqa: E501
        :rtype: str
        """
        return self._expense_account_id

    @expense_account_id.setter
    def expense_account_id(self, expense_account_id):
        """Sets the expense_account_id of this Benefit.

        Xero identifier for Expense Account  # noqa: E501

        :param expense_account_id: The expense_account_id of this Benefit.  # noqa: E501
        :type: str
        """
        if expense_account_id is None:
            raise ValueError(
                "Invalid value for `expense_account_id`, must not be `None`"
            )  # noqa: E501

        self._expense_account_id = expense_account_id

    @property
    def standard_amount(self):
        """Gets the standard_amount of this Benefit.  # noqa: E501

        Standard amount of the employer pension  # noqa: E501

        :return: The standard_amount of this Benefit.  # noqa: E501
        :rtype: float
        """
        return self._standard_amount

    @standard_amount.setter
    def standard_amount(self, standard_amount):
        """Sets the standard_amount of this Benefit.

        Standard amount of the employer pension  # noqa: E501

        :param standard_amount: The standard_amount of this Benefit.  # noqa: E501
        :type: float
        """

        self._standard_amount = standard_amount

    @property
    def percentage(self):
        """Gets the percentage of this Benefit.  # noqa: E501

        Percentage of gross of the employer pension  # noqa: E501

        :return: The percentage of this Benefit.  # noqa: E501
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this Benefit.

        Percentage of gross of the employer pension  # noqa: E501

        :param percentage: The percentage of this Benefit.  # noqa: E501
        :type: float
        """
        if percentage is None:
            raise ValueError(
                "Invalid value for `percentage`, must not be `None`"
            )  # noqa: E501

        self._percentage = percentage

    @property
    def calculation_type(self):
        """Gets the calculation_type of this Benefit.  # noqa: E501

        Calculation Type of the employer pension (FixedAmount or PercentageOfGross).  # noqa: E501

        :return: The calculation_type of this Benefit.  # noqa: E501
        :rtype: str
        """
        return self._calculation_type

    @calculation_type.setter
    def calculation_type(self, calculation_type):
        """Sets the calculation_type of this Benefit.

        Calculation Type of the employer pension (FixedAmount or PercentageOfGross).  # noqa: E501

        :param calculation_type: The calculation_type of this Benefit.  # noqa: E501
        :type: str
        """
        if calculation_type is None:
            raise ValueError(
                "Invalid value for `calculation_type`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["FixedAmount", "PercentageOfGross", "None"]  # noqa: E501
        if calculation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `calculation_type` ({0}), must be one of {1}".format(  # noqa: E501
                    calculation_type, allowed_values
                )
            )

        self._calculation_type = calculation_type

    @property
    def current_record(self):
        """Gets the current_record of this Benefit.  # noqa: E501

        Identifier of a record is active or not.  # noqa: E501

        :return: The current_record of this Benefit.  # noqa: E501
        :rtype: bool
        """
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        """Sets the current_record of this Benefit.

        Identifier of a record is active or not.  # noqa: E501

        :param current_record: The current_record of this Benefit.  # noqa: E501
        :type: bool
        """

        self._current_record = current_record

    @property
    def subject_to_nic(self):
        """Gets the subject_to_nic of this Benefit.  # noqa: E501

        Identifier of subject To NIC  # noqa: E501

        :return: The subject_to_nic of this Benefit.  # noqa: E501
        :rtype: bool
        """
        return self._subject_to_nic

    @subject_to_nic.setter
    def subject_to_nic(self, subject_to_nic):
        """Sets the subject_to_nic of this Benefit.

        Identifier of subject To NIC  # noqa: E501

        :param subject_to_nic: The subject_to_nic of this Benefit.  # noqa: E501
        :type: bool
        """

        self._subject_to_nic = subject_to_nic

    @property
    def subject_to_pension(self):
        """Gets the subject_to_pension of this Benefit.  # noqa: E501

        Identifier of subject To pension  # noqa: E501

        :return: The subject_to_pension of this Benefit.  # noqa: E501
        :rtype: bool
        """
        return self._subject_to_pension

    @subject_to_pension.setter
    def subject_to_pension(self, subject_to_pension):
        """Sets the subject_to_pension of this Benefit.

        Identifier of subject To pension  # noqa: E501

        :param subject_to_pension: The subject_to_pension of this Benefit.  # noqa: E501
        :type: bool
        """

        self._subject_to_pension = subject_to_pension

    @property
    def subject_to_tax(self):
        """Gets the subject_to_tax of this Benefit.  # noqa: E501

        Identifier of subject To Tax  # noqa: E501

        :return: The subject_to_tax of this Benefit.  # noqa: E501
        :rtype: bool
        """
        return self._subject_to_tax

    @subject_to_tax.setter
    def subject_to_tax(self, subject_to_tax):
        """Sets the subject_to_tax of this Benefit.

        Identifier of subject To Tax  # noqa: E501

        :param subject_to_tax: The subject_to_tax of this Benefit.  # noqa: E501
        :type: bool
        """

        self._subject_to_tax = subject_to_tax

    @property
    def is_calculating_on_qualifying_earnings(self):
        """Gets the is_calculating_on_qualifying_earnings of this Benefit.  # noqa: E501

        Identifier of calculating on qualifying earnings  # noqa: E501

        :return: The is_calculating_on_qualifying_earnings of this Benefit.  # noqa: E501
        :rtype: bool
        """
        return self._is_calculating_on_qualifying_earnings

    @is_calculating_on_qualifying_earnings.setter
    def is_calculating_on_qualifying_earnings(
        self, is_calculating_on_qualifying_earnings
    ):
        """Sets the is_calculating_on_qualifying_earnings of this Benefit.

        Identifier of calculating on qualifying earnings  # noqa: E501

        :param is_calculating_on_qualifying_earnings: The is_calculating_on_qualifying_earnings of this Benefit.  # noqa: E501
        :type: bool
        """

        self._is_calculating_on_qualifying_earnings = (
            is_calculating_on_qualifying_earnings
        )

    @property
    def show_balance_to_employee(self):
        """Gets the show_balance_to_employee of this Benefit.  # noqa: E501

        display the balance to employee  # noqa: E501

        :return: The show_balance_to_employee of this Benefit.  # noqa: E501
        :rtype: bool
        """
        return self._show_balance_to_employee

    @show_balance_to_employee.setter
    def show_balance_to_employee(self, show_balance_to_employee):
        """Sets the show_balance_to_employee of this Benefit.

        display the balance to employee  # noqa: E501

        :param show_balance_to_employee: The show_balance_to_employee of this Benefit.  # noqa: E501
        :type: bool
        """

        self._show_balance_to_employee = show_balance_to_employee
