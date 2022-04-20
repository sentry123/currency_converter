"""

"""
from typing import Optional
import pandas as pd
from get_raw_data import get_raw_data
from get_exchange_rate import get_exchange_rate


def get_data(identifier: str, target_currency: Optional[str] = None) -> pd.DataFrame:
    """

    :param identifier:
    :param target_currency:
    :return:
    """
    if not target_currency:
        return get_raw_data(identifier)
    else:
        source_currency = (identifier.split('.'))[12]
        return get_exchange_rate(source_currency, target_currency)


get_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N", "GBP")
