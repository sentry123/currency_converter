"""
get_raw_data function fetches the data from the appropriate URL and convert it to a pandas DataFrame.
"""

import pandas as pd
from request_handler import request_handler


def get_raw_data(identifier: str) -> pd.DataFrame:
    """

    :param identifier: string
    :return: pandas dataframe
    """
    print(f" identifier  =>  {identifier}")
    url = "https://sdw-wsrest.ecb.europa.eu/service/data/BP6/" + identifier + "?detail=dataonly"
    print(url)
    return request_handler(url)
