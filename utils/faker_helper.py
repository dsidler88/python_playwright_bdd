# -*- coding: utf-8 -*-
# @Author  : Daniel Sidler
# @File    : faker_helper.py
from faker import Faker
from faker.providers import BaseProvider, internet

faker = Faker()


def get_faker_ipv4():
    """
    return fake ipv4
    :return:
    """
    faker.add_provider(internet)
    return faker.ipv4()


def get_faker_uuid():
    """
        return uuid
        :return:
        """
    faker.add_provider(BaseProvider)
    return faker.uuid4()


def get_faker_int():
    """
    Random int
    :return:
    """
    faker.add_provider(BaseProvider)
    return faker.random_int()


def get_faker_linux_version():
    """
    Linux Version
    :return:
    """
    faker.add_provider(BaseProvider)
    return faker.linux_platform_token()


def get_faker_linux_processor():
    """
    Processor
    :return:
    """
    faker.add_provider(BaseProvider)
    return faker.linux_processor()


def fake_str(length=10):
    """
    fake string
    :return:
    """
    faker.add_provider(BaseProvider)
    return faker.pystr(min_chars=length, max_chars=length)


print(get_faker_linux_processor())
