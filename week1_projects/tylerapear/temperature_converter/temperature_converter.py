
c = 100
f = 32
k = 373.15

#Converts Celcius to Farenheit
def cToF(c):
  return (c * (9/5)) + 32

#Converts Farenheit to Celcius
def fToC(f):
  return (f - 32) * (5/9)

#Converts Celcius to Kelvin
def cToK(c):
  return c + 273.15

#Converts Kelvin to Celcius
def kToC(k):
  return k - 273.15

def main():
  
  title = (
    "\033[32m" +
    "\n" + r"  _______                                  _                     _____                          _            " +
    "\n" + r" |__   __|                                | |                   / ____|                        | |           " +
    "\n" + r"    | | ___ _ __ ___  _ __   ___ _ __ __ _| |_ _   _ _ __ ___  | |     ___  _ ____   _____ _ __| |_ ___ _ __ " +
    "\n" + r"    | |/ _ \ '_ ` _ \| '_ \ / _ \ '__/ _` | __| | | | '__/ _ \ | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|" +
    "\n" + r"    | |  __/ | | | | | |_) |  __/ | | (_| | |_| |_| | | |  __/ | |___| (_) | | | \ V /  __/ |  | ||  __/ |   " +
    "\n" + r"    |_|\___|_| |_| |_| .__/ \___|_|  \__,_|\__|\__,_|_|  \___|  \_____\___/|_| |_|\_/ \___|_|   \__\___|_|   " +
    "\n" + r"                     | |                                                                                     " +
    "\n" + r"                     |_|                                                                                     " +
    "\033[0m"
  )
  
  message = ( 
    "\n\033[34mWelcome to Temperature Converter! (by Tyler Pearson - https://github.com/tylerapear)\033[0m" +
    "\nPlease choose one of the following options:" +
    "\n\n(1) Convert from Celcius to Farenheit" +
    "\n(2) Convert from Farenheit to Celcius" +
    "\n(3) Convert from Celcius to Kelvin" +
    "\n(4) Convert from Kelvin to Celcius\n\n: "
  )
  
  print(title)
  
  running = True
  while running:
    
  
    choice = input(message)
    
    source = ""
    destination = ""
    function = None
    
    invalid = True
    while invalid:
      if not choice.isdigit():
        choice = input("\nInvalid choice - Please enter an option between 1 and 4\n\n: ")
      elif int(choice) == 1:
        source = "Celcius"
        destination = "Farenheit"
        function = cToF
        invalid = False
      elif int(choice) == 2:
        source = "Farenheit"
        destination = "Celcius"
        function = fToC
        invalid = False
      elif int(choice) == 3:
        source = "Celcius"
        destination = "Kelvin"
        function = cToK
        invalid = False
      elif int(choice) == 4:
        source = "Kelvin"
        destination = "Celcius"
        function = kToC
        invalid = False
      else:
        choice = input("\nInvalid choice - Please enter an option between 1 and 4\n\n: ")
    
    degrees = input(f'\nConvert how many degrees {source} to {destination}?\n\n: ')
    invalid = True
    while invalid:
      if isinstance(float(degrees), float):
        degrees = float(degrees)
        invalid = False
      else:
        degrees = input("\nInvalid input - Please enter a numerical value\n\n: ")
    
    print(f'\n\033[33m{degrees} degrees {source} is {function(degrees)} {destination}\033[0m\n')
    
    again = input("\nWould you like to perform another conversion? (Y or N)\n\n: ")
    invalid = True
    while invalid:
      if again == "Y" or again == "y":
        running = True
        invalid = False
      elif again == "N" or again == "n":
        running = False
        invalid = False
      else:
        again = input("\nInvalid input - Please enter Y or N\n\n: ")
  
main()