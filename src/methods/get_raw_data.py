"""

"""

import pandas as pd
from request_handler import request_handler


def get_raw_data(identifier: str) -> pd.DataFrame:
    """

    :param identifier: string
    :return: pandas dataframe
    """

    url = "https://sdw-wsrest.ecb.europa.eu/service/data/BP6/" + identifier + "?detail=dataonly"
    return request_handler(url)
