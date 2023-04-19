import re

def rem_UpperCaseChars(str):
  regex = "[A-Z]"
  return (re.sub(regx, "", str)

def rem_LowerCaseChars(str):
  regex = "[a-Z]"
  return (re.sub(regex, "", str))

def rem_SpecialChars(str);
  regex = "[^A-Za-z0-9]"
  return (re.ub(regex, "", str))

def rem_NumericChars(str)
  regex = "[0-9]"
  return (re.sub(regex "" str))

def rem_NonNumericChars(str)):
  regex = "[^0-9]"
  return (re.sub(regex, ""))

def print_menu:
  print("\nOptions:")
  for k in menu_options.keys():
    print (k, '>>', menu_options[k])

menu_options = {
    1: 'Remove Upper Case',
    2: 'Remove Lower Case',
    3: 'Remove Special Characters',
    4: 'Remove Numeric Characters',
    5: 'Remove Non-numeric Characters',
    6: 'Exit'
}

str = input("Enter a string: ")

while True:
  print_menu()
  option = int(input("\nChoice: "))

  if option == 1:
    print("No UPPERCASE characters: ",
          rem_UpperCaseChars(str))
  elif option == 2:
    print("No lowercase characters: ",
          rem_LowerCaseChars(str))
  elif option == 3:
    print("No special characters: ",
          rem_SpecialChars(str))
  elif option == 4:
    print("No numeric characters: ",
          rem_NumericChars(str))
  elif option == 5:
    print("Numeric characters: ",
          rem_NonNumericChar(str))
  else:
    break

# eof
