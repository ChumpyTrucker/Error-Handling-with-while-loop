# Error-Handling-with-while-loop.
while True:
  try:
    age = int(input('What is your age?'))
    10/age
  except ValueError:
    print('Please enter a number' )
    continue
  except ZeroDivisionError:
    print('Please enter age higher than 0')
    break
  else:
    print('Thank you')
    break
  finally:
    print('Ok, I am finslly done ' )
  print('Can you hear me?')
