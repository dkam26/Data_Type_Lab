def fizz_buzz(positiveInteger):
  try:
      if positiveInteger % 3 is 0 and positiveInteger % 5 is not 0:
        return 'fizz'
      elif positiveInteger %5 is 0 and positiveInteger % 3 is not 0:
        return 'buzz'
      elif positiveInteger % 3 is 0 and positiveInteger % 5 is 0:
        return 'fizzBuzz'
      elif positiveInteger % 3 is not 0 or positiveInteger % 5 is not 0:
        return positiveInteger
  except ValueError:
      return 'Invalid Argument'