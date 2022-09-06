"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import sys
import unittest

import ynab_api
from ynab_api.model.payee_location import PayeeLocation

globals()['PayeeLocation'] = PayeeLocation
from ynab_api.model.payee_location_response_data import PayeeLocationResponseData


class TestPayeeLocationResponseData(unittest.TestCase):
    """PayeeLocationResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPayeeLocationResponseData(self):
        """Test PayeeLocationResponseData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PayeeLocationResponseData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
