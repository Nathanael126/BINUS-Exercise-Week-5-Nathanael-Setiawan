from datetime import datetime
Date = lambda a : a.strftime("%d/%m/%Y")
Time = lambda a : a.strftime("%H:%M:%S")
print("Date: " + Date(datetime.now()))
print("Time: " + Time(datetime.now()))