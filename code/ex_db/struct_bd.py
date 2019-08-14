MATCH_TYPES = {
    'date': 'text',
    'trans': 'text',
    'symbol': 'text',
    'qty': 'real',
    'price': 'real'
}


class StructBD:
    BD_NAME = 'stocks'

    def __init__(self, date, trans, symbol, qty, price):
        self.date = date
        self.trans = trans
        self.symbol = symbol
        self.qty = qty
        self.price = price


def get_name_columns():
    # return list(obj.__dict__.keys())
    return tuple(MATCH_TYPES.keys())


def get_type_column():
    # return StructBD.__MATCH_TYPES.get(name_column)
    return tuple(MATCH_TYPES.values())


if __name__ == '__main__':
    obj = StructBD('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
    name = get_name_columns()
    type_name = get_type_column()
    print('Success!')
