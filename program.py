import datetime as dt


class Record:
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        if date == '' or date == dt.datetime.now().date():
            date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment = comment


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.record = []

    def add_record(self, record):
        self.record.append(Record)

    def get_week_stats(self):
        week_count = 0
        today = dt.date.today()
        week_age = today - dt.timedelta(days=7)
        for i in self.record:
            if week_age <= i.date <= today:
                week_count += i.amount
        return week_count


class CashCalculator(Calculator):
    def get_today_stats(self, limit):
        for i in self.record:
            if i.date == dt.datetime.now().date():
               self.limit -= i.amount

    def get_today_cash_remained(self, currency):
        if self.limit > 0:
            return f"На сегодня осталось {self.limit} {currency}"
        elif self.limit == 0:
            return f"Денег нет, держись"
        elif self.limit < 0:
            return f"Денег нет, держись: твой долг {self.limit} {currency}"


class CaloriesCalculator(Calculator):
    def __init__(self, eaten):
        self.eaten = 0

    def get_today_stats(self):
        for i in self.record:
            if i.date == dt.datetime.now().date():
               self.eaten += i.amount

    def get_calories_remained(self):
        if self.limit > self.eaten:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - self.eaten} кКал"
        elif self.limit <= self.eaten:
            return "Хватит есть!"
        

# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе")) 
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained("rub"))
# должно напечататься
# На сегодня осталось 555 руб