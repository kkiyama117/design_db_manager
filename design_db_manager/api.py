"""京大のイベント
"""


def prepare(factory, method, **kwargs):
    return "", "", kwargs


def event_parser(factory, method: str, **kwargs):
    """hook to call event list factory

    call any function

    Args:
        factory: :obj:`kueventparser.events.EventManager` or :obj:`str`
        method (str): 取得の仕方. 'get' or 'get_all'
        kwargs (dict): kwargs for method selected by args
            date or (year and month) ... get_all method
            url ... get

    Returns:
        method selected by args
    """
    _factory, _method, _kwargs = prepare(factory, method, **kwargs)
    return getattr(_factory, _method)(**_kwargs)


def main():
    pass


if __name__ == '__main__':
    main()
