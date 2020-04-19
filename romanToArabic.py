def roman_to_arabic(roman):
  numeralMap = {'M': 1000, 'D':500, 'C': 100, 'L':50, 'X':10, 'V':5, 'I':1}
  intCounter = numeralMap[roman[-1]]
  for i in range(0, len(roman) - 1):
    if numeralMap[roman[i]] < numeralMap[roman[i+1]]:
      intCounter -= numeralMap[roman[i]]
    else:
      intCounter += numeralMap[roman[i]]
  return intCounter    