# from enum import Enum
from enum import Enum
Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
Weekday=Enum('Weekday',('Mon','Tue','Jan'))

a=Month.Jan.value
print(a)
# for name,member in Month.__members__.items():
#     print(name,member,member.value)

# @unique
class Day(Enum):
    Mon=1
    Tue=2
    Wed=3

print(Day.Mon)

