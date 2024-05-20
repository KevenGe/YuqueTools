# coding: utf-8

"""
    语雀 OpenAPI

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V2MemberStatistics(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bizdate': 'str',
        'user_id': 'str',
        'group_id': 'str',
        'organization_id': 'str',
        'write_count': 'str',
        'write_count_30': 'str',
        'write_count_365': 'str',
        'write_doc_count': 'str',
        'write_doc_count_30': 'str',
        'write_doc_count_365': 'str',
        'read_count': 'str',
        'read_count_30': 'str',
        'read_count_365': 'str',
        'like_count': 'str',
        'like_count_30': 'str',
        'like_count_365': 'str',
        'user': 'str'
    }

    attribute_map = {
        'bizdate': 'bizdate',
        'user_id': 'user_id',
        'group_id': 'group_id',
        'organization_id': 'organization_id',
        'write_count': 'write_count',
        'write_count_30': 'write_count_30',
        'write_count_365': 'write_count_365',
        'write_doc_count': 'write_doc_count',
        'write_doc_count_30': 'write_doc_count_30',
        'write_doc_count_365': 'write_doc_count_365',
        'read_count': 'read_count',
        'read_count_30': 'read_count_30',
        'read_count_365': 'read_count_365',
        'like_count': 'like_count',
        'like_count_30': 'like_count_30',
        'like_count_365': 'like_count_365',
        'user': 'user'
    }

    def __init__(self, bizdate=None, user_id=None, group_id=None, organization_id=None, write_count=None, write_count_30=None, write_count_365=None, write_doc_count=None, write_doc_count_30=None, write_doc_count_365=None, read_count=None, read_count_30=None, read_count_365=None, like_count=None, like_count_30=None, like_count_365=None, user=None):  # noqa: E501
        """V2MemberStatistics - a model defined in Swagger"""  # noqa: E501
        self._bizdate = None
        self._user_id = None
        self._group_id = None
        self._organization_id = None
        self._write_count = None
        self._write_count_30 = None
        self._write_count_365 = None
        self._write_doc_count = None
        self._write_doc_count_30 = None
        self._write_doc_count_365 = None
        self._read_count = None
        self._read_count_30 = None
        self._read_count_365 = None
        self._like_count = None
        self._like_count_30 = None
        self._like_count_365 = None
        self._user = None
        self.discriminator = None
        if bizdate is not None:
            self.bizdate = bizdate
        if user_id is not None:
            self.user_id = user_id
        if group_id is not None:
            self.group_id = group_id
        if organization_id is not None:
            self.organization_id = organization_id
        if write_count is not None:
            self.write_count = write_count
        if write_count_30 is not None:
            self.write_count_30 = write_count_30
        if write_count_365 is not None:
            self.write_count_365 = write_count_365
        if write_doc_count is not None:
            self.write_doc_count = write_doc_count
        if write_doc_count_30 is not None:
            self.write_doc_count_30 = write_doc_count_30
        if write_doc_count_365 is not None:
            self.write_doc_count_365 = write_doc_count_365
        if read_count is not None:
            self.read_count = read_count
        if read_count_30 is not None:
            self.read_count_30 = read_count_30
        if read_count_365 is not None:
            self.read_count_365 = read_count_365
        if like_count is not None:
            self.like_count = like_count
        if like_count_30 is not None:
            self.like_count_30 = like_count_30
        if like_count_365 is not None:
            self.like_count_365 = like_count_365
        if user is not None:
            self.user = user

    @property
    def bizdate(self):
        """Gets the bizdate of this V2MemberStatistics.  # noqa: E501


        :return: The bizdate of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._bizdate

    @bizdate.setter
    def bizdate(self, bizdate):
        """Sets the bizdate of this V2MemberStatistics.


        :param bizdate: The bizdate of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._bizdate = bizdate

    @property
    def user_id(self):
        """Gets the user_id of this V2MemberStatistics.  # noqa: E501

        统计日期 (YYYYMMDD)  # noqa: E501

        :return: The user_id of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this V2MemberStatistics.

        统计日期 (YYYYMMDD)  # noqa: E501

        :param user_id: The user_id of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def group_id(self):
        """Gets the group_id of this V2MemberStatistics.  # noqa: E501

        成员 ID  # noqa: E501

        :return: The group_id of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this V2MemberStatistics.

        成员 ID  # noqa: E501

        :param group_id: The group_id of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._group_id = group_id

    @property
    def organization_id(self):
        """Gets the organization_id of this V2MemberStatistics.  # noqa: E501

        团队 ID  # noqa: E501

        :return: The organization_id of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this V2MemberStatistics.

        团队 ID  # noqa: E501

        :param organization_id: The organization_id of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._organization_id = organization_id

    @property
    def write_count(self):
        """Gets the write_count of this V2MemberStatistics.  # noqa: E501

        空间 ID  # noqa: E501

        :return: The write_count of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._write_count

    @write_count.setter
    def write_count(self, write_count):
        """Sets the write_count of this V2MemberStatistics.

        空间 ID  # noqa: E501

        :param write_count: The write_count of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._write_count = write_count

    @property
    def write_count_30(self):
        """Gets the write_count_30 of this V2MemberStatistics.  # noqa: E501

        编辑次数  # noqa: E501

        :return: The write_count_30 of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._write_count_30

    @write_count_30.setter
    def write_count_30(self, write_count_30):
        """Sets the write_count_30 of this V2MemberStatistics.

        编辑次数  # noqa: E501

        :param write_count_30: The write_count_30 of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._write_count_30 = write_count_30

    @property
    def write_count_365(self):
        """Gets the write_count_365 of this V2MemberStatistics.  # noqa: E501

        编辑次数 (30天)  # noqa: E501

        :return: The write_count_365 of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._write_count_365

    @write_count_365.setter
    def write_count_365(self, write_count_365):
        """Sets the write_count_365 of this V2MemberStatistics.

        编辑次数 (30天)  # noqa: E501

        :param write_count_365: The write_count_365 of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._write_count_365 = write_count_365

    @property
    def write_doc_count(self):
        """Gets the write_doc_count of this V2MemberStatistics.  # noqa: E501

        编辑次数 (一年)  # noqa: E501

        :return: The write_doc_count of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._write_doc_count

    @write_doc_count.setter
    def write_doc_count(self, write_doc_count):
        """Sets the write_doc_count of this V2MemberStatistics.

        编辑次数 (一年)  # noqa: E501

        :param write_doc_count: The write_doc_count of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._write_doc_count = write_doc_count

    @property
    def write_doc_count_30(self):
        """Gets the write_doc_count_30 of this V2MemberStatistics.  # noqa: E501

        编辑文档数  # noqa: E501

        :return: The write_doc_count_30 of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._write_doc_count_30

    @write_doc_count_30.setter
    def write_doc_count_30(self, write_doc_count_30):
        """Sets the write_doc_count_30 of this V2MemberStatistics.

        编辑文档数  # noqa: E501

        :param write_doc_count_30: The write_doc_count_30 of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._write_doc_count_30 = write_doc_count_30

    @property
    def write_doc_count_365(self):
        """Gets the write_doc_count_365 of this V2MemberStatistics.  # noqa: E501

        编辑文档数 (30天)  # noqa: E501

        :return: The write_doc_count_365 of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._write_doc_count_365

    @write_doc_count_365.setter
    def write_doc_count_365(self, write_doc_count_365):
        """Sets the write_doc_count_365 of this V2MemberStatistics.

        编辑文档数 (30天)  # noqa: E501

        :param write_doc_count_365: The write_doc_count_365 of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._write_doc_count_365 = write_doc_count_365

    @property
    def read_count(self):
        """Gets the read_count of this V2MemberStatistics.  # noqa: E501

        编辑文档数 (一年)  # noqa: E501

        :return: The read_count of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._read_count

    @read_count.setter
    def read_count(self, read_count):
        """Sets the read_count of this V2MemberStatistics.

        编辑文档数 (一年)  # noqa: E501

        :param read_count: The read_count of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._read_count = read_count

    @property
    def read_count_30(self):
        """Gets the read_count_30 of this V2MemberStatistics.  # noqa: E501

        阅读量  # noqa: E501

        :return: The read_count_30 of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._read_count_30

    @read_count_30.setter
    def read_count_30(self, read_count_30):
        """Sets the read_count_30 of this V2MemberStatistics.

        阅读量  # noqa: E501

        :param read_count_30: The read_count_30 of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._read_count_30 = read_count_30

    @property
    def read_count_365(self):
        """Gets the read_count_365 of this V2MemberStatistics.  # noqa: E501

        阅读量 (30天)  # noqa: E501

        :return: The read_count_365 of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._read_count_365

    @read_count_365.setter
    def read_count_365(self, read_count_365):
        """Sets the read_count_365 of this V2MemberStatistics.

        阅读量 (30天)  # noqa: E501

        :param read_count_365: The read_count_365 of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._read_count_365 = read_count_365

    @property
    def like_count(self):
        """Gets the like_count of this V2MemberStatistics.  # noqa: E501

        阅读量 (一年)  # noqa: E501

        :return: The like_count of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._like_count

    @like_count.setter
    def like_count(self, like_count):
        """Sets the like_count of this V2MemberStatistics.

        阅读量 (一年)  # noqa: E501

        :param like_count: The like_count of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._like_count = like_count

    @property
    def like_count_30(self):
        """Gets the like_count_30 of this V2MemberStatistics.  # noqa: E501

        点赞量  # noqa: E501

        :return: The like_count_30 of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._like_count_30

    @like_count_30.setter
    def like_count_30(self, like_count_30):
        """Sets the like_count_30 of this V2MemberStatistics.

        点赞量  # noqa: E501

        :param like_count_30: The like_count_30 of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._like_count_30 = like_count_30

    @property
    def like_count_365(self):
        """Gets the like_count_365 of this V2MemberStatistics.  # noqa: E501

        点赞量 (30天)  # noqa: E501

        :return: The like_count_365 of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._like_count_365

    @like_count_365.setter
    def like_count_365(self, like_count_365):
        """Sets the like_count_365 of this V2MemberStatistics.

        点赞量 (30天)  # noqa: E501

        :param like_count_365: The like_count_365 of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._like_count_365 = like_count_365

    @property
    def user(self):
        """Gets the user of this V2MemberStatistics.  # noqa: E501

        点赞量 (一年)  # noqa: E501

        :return: The user of this V2MemberStatistics.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this V2MemberStatistics.

        点赞量 (一年)  # noqa: E501

        :param user: The user of this V2MemberStatistics.  # noqa: E501
        :type: str
        """

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(V2MemberStatistics, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V2MemberStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
