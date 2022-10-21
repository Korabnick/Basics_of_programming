def date_checker(d, m, y):
    months_31 = (1, 3, 5, 7, 8, 10, 12)
    months_30 = (4, 6, 9, 11)
    if m in months_31:
        if 1 <= d <= 31:
            return True
        else:
            return False
    elif m in months_30:
        if 1 <= d <= 30:
            return True
        else:
            return False
    elif y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        if m == 2 and 1 <= d <= 29:
            return True
        else:
            return False
    elif y % 4 != 0 or y % 400 !=0:
        if m == 2 and 1 <= d <= 28:
            return True
        else:
            return False