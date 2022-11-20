import random 
import time

class DateTime:
    def __init__(self) -> None:
        hour, min, sec, AMPM = time.strftime("%I %M %S %p").split()
        hour, min, sec = int(hour), int(min), int(sec)
        date, month, year, day = time.strftime("%d %B %Y %A").split()
        self.time = {
          'hour': hour,
          'min' : min,
          'sec' : sec,
          'AMPM': AMPM,
        }
        self.date = {
            'date' : date,
            'month' : month,
            'year' : year,
            'day' : day,
        }
       

class Data:
    def __init__(self):
        self.sales = {
            'Footware' : random.randint(1000, 2000),
            'Garments' : random.randint(15000, 25000),
            'Gadgets' : random.randint(7000, 14000)
        }

        self.revenue = {
            'Footware' : self.sales['Footware'] * 11000,
            'Garments' : self.sales['Garments'] * 11000,
            'Gadgets' : self.sales['Gadgets'] * 45000
        }


if __name__ == '__main__':
    Today = DateTime()
    print(Today.date)

          
          