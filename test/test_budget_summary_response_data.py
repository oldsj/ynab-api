"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

import ynab_api
from ynab_api.model.budget_summary import BudgetSummary

globals()['BudgetSummary'] = BudgetSummary
from ynab_api.model.budget_summary_response_data import BudgetSummaryResponseData


class TestBudgetSummaryResponseData(unittest.TestCase):
    """BudgetSummaryResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBudgetSummaryResponseData(self):
        """Test BudgetSummaryResponseData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BudgetSummaryResponseData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
