"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import unittest

import ynab_api
from ynab_api.api.budgets_api import BudgetsApi  # noqa: E501


class TestBudgetsApi(unittest.TestCase):
    """BudgetsApi unit test stubs"""

    def setUp(self):
        self.api = BudgetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_budget_by_id(self):
        """Test case for get_budget_by_id

        Single budget  # noqa: E501
        """
        pass

    def test_get_budget_settings_by_id(self):
        """Test case for get_budget_settings_by_id

        Budget Settings  # noqa: E501
        """
        pass

    def test_get_budgets(self):
        """Test case for get_budgets

        List budgets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
