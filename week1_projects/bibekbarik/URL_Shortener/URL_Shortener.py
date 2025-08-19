import json
import os
import random   # imports all necessary modules
import string

data_store = 'url_data.json'  # file to store the mapped urls with it's unique codes

# a function to loads data inside the local file(data_store.json) or empty dict
def load_data():
    if os.path.exists(data_store):
        with open(data_store, 'r') as f:
            return json.load(f)
    return {}

# a function to save data inside the data_store.json file
def save_data(data):
    with open(data_store, 'w') as f:
        json.dump(data, f)

# a function to generate a 6 digits random code that is use to map the original long url
def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# function to map the generated random short code with original long url
def shorten_url(url, data):
    code = generate_code()
    while code in data:
        code = generate_code()
    data[code] = url
    save_data(data)
    return code

# function return the original url with the given code
def get_url(code, data):
    return data.get(code)

def main():
    data = load_data()
    choice = input("Enter [1] to shorten, [2] to retrive: ").strip()
    if choice == '1':
        url = input("Enter the url to shorten: ").strip()
        code = shorten_url(url, data)
        print(f"Short code: {code}")
    elif choice == '2':
        code = input("Enter short code: ").strip()
        original = get_url(code, data)
        if original:
            print(f"Original URL: {original}")
        else:
            print("No URL found for this code.")
    else:
        print("Invalid choice.")

if __name__=="__main__":
    main()