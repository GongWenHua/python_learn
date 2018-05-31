try:
    r = 10 / 0
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
