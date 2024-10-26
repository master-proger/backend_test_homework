import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if not date:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_count = 0
        today = dt.datetime.now().date()
        for i in self.records:
            if i.date == today:
               today_count += i.amount
        return today_count

    def get_week_stats(self):
        week_count = 0
        today = dt.date.today()
        week_age = today - dt.timedelta(days=7)
        for i in self.records:
            if week_age <= i.date <= today:
                week_count += i.amount
        return week_count

    def today_stats(self):
        return self.limit - self.get_today_stats()


class CashCalculator(Calculator):
    def get_today_cash_remained(self, currency):
        today_stats = super().today_stats()
        if today_stats > 0:
            return f"На сегодня осталось {today_stats} {currency}"
        elif today_stats == 0:
            return "Денег нет, держись"
        else:
            return f"Денег нет, держись: твой долг {today_stats} {currency}"


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.limit > self.get_today_stats():
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - self.get_today_stats()} кКал"
        else:
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