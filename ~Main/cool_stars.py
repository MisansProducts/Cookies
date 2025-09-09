def cool_stars(d):
  for i in range(1, d * 2):
    if i <= d:
      print('*' * i)
    else:
      print('*' * ((d * 2) - i))