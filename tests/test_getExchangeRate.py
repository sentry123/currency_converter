"""
    Test for get_exchange_rate
"""

import os, sys

dir = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(dir)

sys.path.append(parent)


from src.get_exchange_rate import get_exchange_rate, url_parser


def test_get_exchange_rate1(source):
    exchange_rate_output = url_parser(source)
    parsed_url = (((exchange_rate_output.split('/'))[-1]).split('.'))[-3]
    assert parsed_url == "EUR"


def test_get_exchange_rate2(source, target):
    exchange_rate_output = url_parser(source)
    parsed_url_target, parsed_url_source = (((exchange_rate_output.split('/'))[-1]).split('.'))[-3], \
                                           (((exchange_rate_output.split('/'))[-1]).split('.'))[1]
    assert parsed_url_target == target and parsed_url_source == source
