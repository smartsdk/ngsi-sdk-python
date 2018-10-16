# coding: utf-8

"""
    ngsi-v2

    NGSI V2 API RC-2018.04  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.entities_api import EntitiesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEntitiesApi(unittest.TestCase):
    """EntitiesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.entities_api.EntitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_entity(self):
        """Test case for create_entity

        """
        pass

    def test_list_entities(self):
        """Test case for list_entities

        """
        pass

    def test_remove_entity(self):
        """Test case for remove_entity

        """
        pass

    def test_replace_all_entity_attributes(self):
        """Test case for replace_all_entity_attributes

        """
        pass

    def test_retrieve_entity(self):
        """Test case for retrieve_entity

        """
        pass

    def test_retrieve_entity_attributes(self):
        """Test case for retrieve_entity_attributes

        """
        pass

    def test_update_existing_entity_attributes(self):
        """Test case for update_existing_entity_attributes

        """
        pass

    def test_update_or_append_entity_attributes(self):
        """Test case for update_or_append_entity_attributes

        """
        pass


if __name__ == '__main__':
    unittest.main()
