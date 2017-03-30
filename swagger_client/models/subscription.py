# coding: utf-8

"""
    ngsi-v2

    NGSI V2 API

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Subscription(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, description=None, subject=None, notification=None, expires=None, status=None, throttling=None):
        """
        Subscription - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'description': 'str',
            'subject': 'object',
            'notification': 'object',
            'expires': 'datetime',
            'status': 'str',
            'throttling': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'subject': 'subject',
            'notification': 'notification',
            'expires': 'expires',
            'status': 'status',
            'throttling': 'throttling'
        }

        self._id = id
        self._description = description
        self._subject = subject
        self._notification = notification
        self._expires = expires
        self._status = status
        self._throttling = throttling


    @property
    def id(self):
        """
        Gets the id of this Subscription.


        :return: The id of this Subscription.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Subscription.


        :param id: The id of this Subscription.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this Subscription.


        :return: The description of this Subscription.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Subscription.


        :param description: The description of this Subscription.
        :type: str
        """

        self._description = description

    @property
    def subject(self):
        """
        Gets the subject of this Subscription.


        :return: The subject of this Subscription.
        :rtype: object
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """
        Sets the subject of this Subscription.


        :param subject: The subject of this Subscription.
        :type: object
        """

        self._subject = subject

    @property
    def notification(self):
        """
        Gets the notification of this Subscription.


        :return: The notification of this Subscription.
        :rtype: object
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """
        Sets the notification of this Subscription.


        :param notification: The notification of this Subscription.
        :type: object
        """

        self._notification = notification

    @property
    def expires(self):
        """
        Gets the expires of this Subscription.


        :return: The expires of this Subscription.
        :rtype: datetime
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """
        Sets the expires of this Subscription.


        :param expires: The expires of this Subscription.
        :type: datetime
        """

        self._expires = expires

    @property
    def status(self):
        """
        Gets the status of this Subscription.


        :return: The status of this Subscription.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Subscription.


        :param status: The status of this Subscription.
        :type: str
        """

        self._status = status

    @property
    def throttling(self):
        """
        Gets the throttling of this Subscription.


        :return: The throttling of this Subscription.
        :rtype: int
        """
        return self._throttling

    @throttling.setter
    def throttling(self, throttling):
        """
        Sets the throttling of this Subscription.


        :param throttling: The throttling of this Subscription.
        :type: int
        """

        self._throttling = throttling

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
