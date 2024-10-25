import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []


class Record(Calculator):
    def __init__(self, limit, record, amount, date, comment):
        super().__init__(limit, record)
        self.amount = amount
        self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        if date == None or date == dt.datetime.now().date():
            date = dt.datetime.now().date()
        self.comment = comment


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def add_record(self, record):
        self.record.append(Record())

    def get_today_stats(self):
        self.limit -=

    def get_today_cash_remained(self, currency):
        pass

    def get_week_stats(self):
        pass


class CaloriesCalculator(Calculator):
    def __init__(self):
        pass


a = CashCalculator(1, 2, 3)
a.add_record(1, 2, 3)