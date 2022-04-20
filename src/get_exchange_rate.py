"""
get_exchange_rate function fetches the exchangerate data from the appropriate URL and converts it to a pandas
DataFrame,with columns TIME_PERIOD and OBS_VALUE,corresponding to value of
generic:ObsDimension and generic:ObsValue tags from the XML.OBS_VALUE is converted
to float.
"""
import os, sys

dir = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(dir)

sys.path.append(parent)

import pandas as pd
from src.request_handler import request_handler


def get_exchange_rate(source: str, target: str = "EUR") -> pd.DataFrame:
    """

    :param source: str
    :param target: str
    :return: returns a pandas dataframe containing the ObsDimension and ObsValue from the api response xml
    """
    url = url_parser()
    print("url  =>  "+url)
    return request_handler(url)


def url_parser(source, target):
    url = "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M." + source + "." + target + ".SP00.A?detail=dataonly"
    return url
