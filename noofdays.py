from datetime import date as date_n
def number_of_days(date1,date2):
    return(date2-date1).days

date1=date_n(2000,5,2)
date2=date_n(2022,11,29)
print("number of days between the given dates are",number_of_days(date1,date2))