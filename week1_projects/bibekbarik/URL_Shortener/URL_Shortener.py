import json
import os
import random   # imports all necessary modules
import string

data_store = 'url_data.json'  # file to store the mapped urls with it's unique codes

# a function to loads data inside the local file(data_store.json) or empty dict
def load_data():
    if not os.path.exists(data_store):
        return {}
    try:
        with open(data_store, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}
    
# a function to save data inside the data_store.json file
def save_data(data):
    with open(data_store, 'w') as f:
        json.dump(data, f)

# a function to generate a 6 digits random code that is use to map the original long url
def generate_code(existing_codes, length=6):
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(chars, k=length))
        if code not in existing_codes:      #uniqueness check here
            return code

# function to map the generated random short code with original long url
def shorten_url(url, data):
    if not url:
        raise ValueError('URL cannot be empty')
    
    code = generate_code(data)  # pass the existing data/code
    data[code] = url
    save_data(data)
    return code

# function return the original url with the given code
def get_url(code, data):
    return data.get(code)

# this function return all shortened URLs safely 
def list_urls(data):
    if not isinstance(data, dict):
        print("Error: Data store is corrupted or invalid.")
        return

    if not data:
        print("No URLs stored yet.")
        return

    for code, url in data.items():
        print(f"{code} -> {url}")

# this function delete a shortened URL by its code
def delete_url(code, data):
    if not isinstance(data, dict):
        print("Error: Data store is corrupted or invalid.")
        return False

    if not code:
        print("Error: Code cannot be empty.")
        return False

    if code in data:
        removed = data.pop(code)
        try:
            save_data(data)
            print(f"Deleted: {code} -> {removed}")
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
    else:
        print("Code not found.")
        return False

def main():
    data = load_data()
    print("\n=== URL Shortener ===")
    while True:
        print("\nChoose an option below:")
        print("[1] Shorten a URL")
        print("[2] Retrieve original URL")
        print("[3] List all URLs")
        print("[4] Delete a short code")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            url = input("Enter the URL to shorten: ").strip()
            code = shorten_url(url, data)
            print(f"Short code: {code}")

        elif choice == '2':
            code = input("Enter short code: ").strip()
            original = get_url(code, data)
            if original:
                print(f"Original URL: {original}")
            else:
                print("No URL found for this code.")

        elif choice == '3':
            list_urls(data)

        elif choice == '4':
            code = input("Enter short code to delete: ").strip()
            delete_url(code, data)

        elif choice == '5':
            print("Exiting... Have a great day!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__=="__main__":
    main()