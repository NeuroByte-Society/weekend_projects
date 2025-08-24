import json
import random
import string
import os
from datetime import datetime

class URLShortener:
    def __init__(self, data_file="url_mappings.json"):
        """Initialize the URL Shortener with a data file."""
        self.data_file = data_file
        self.url_mappings = self.load_mappings()
    
    def load_mappings(self):
        """Load existing URL mappings from the JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                return {}
        return {}
    
    def save_mappings(self):
        """Save URL mappings to the JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.url_mappings, file, indent=2)
    
    def generate_short_code(self, length=6):
        """Generate a random short code."""
        characters = string.ascii_letters + string.digits
        while True:
            short_code = ''.join(random.choice(characters) for _ in range(length))
            # Ensure the code doesn't already exist
            if short_code not in self.url_mappings:
                return short_code
    
    def is_valid_url(self, url):
        """Basic URL validation."""
        url = url.strip()
        if not url:
            return False
        
        # Basic check for common URL patterns
        valid_prefixes = ['http://', 'https://', 'ftp://', 'www.']
        has_valid_prefix = any(url.lower().startswith(prefix) for prefix in valid_prefixes)
        
        # Check if it contains a dot (basic domain check)
        has_dot = '.' in url
        
        return has_valid_prefix or has_dot
    
    def shorten_url(self, long_url):
        """Shorten a long URL and return the short code."""
        long_url = long_url.strip()
        
        if not self.is_valid_url(long_url):
            return None, "Invalid URL format. Please include http://, https://, or a valid domain."
        
        # Check if URL already exists
        for short_code, data in self.url_mappings.items():
            if data['url'] == long_url:
                return short_code, f"URL already shortened! Short code: {short_code}"
        
        # Generate new short code
        short_code = self.generate_short_code()
        
        # Store the mapping with metadata
        self.url_mappings[short_code] = {
            'url': long_url,
            'created_at': datetime.now().isoformat(),
            'access_count': 0
        }
        
        # Save to file
        self.save_mappings()
        
        return short_code, "URL shortened successfully!"
    
    def expand_url(self, short_code):
        """Expand a short code back to the original URL."""
        short_code = short_code.strip()
        
        if short_code in self.url_mappings:
            # Increment access count
            self.url_mappings[short_code]['access_count'] += 1
            self.save_mappings()
            
            return self.url_mappings[short_code]['url'], "URL retrieved successfully!"
        else:
            return None, f"Short code '{short_code}' not found."
    
    def list_all_urls(self):
        """List all shortened URLs."""
        if not self.url_mappings:
            return "No URLs have been shortened yet."
        
        result = "\n=== All Shortened URLs ===\n"
        for short_code, data in self.url_mappings.items():
            result += f"Short Code: {short_code}\n"
            result += f"Original URL: {data['url']}\n"
            result += f"Created: {data['created_at'][:19]}\n"
            result += f"Access Count: {data['access_count']}\n"
            result += "-" * 40 + "\n"
        
        return result
    
    def get_stats(self):
        """Get statistics about the URL shortener."""
        total_urls = len(self.url_mappings)
        total_accesses = sum(data['access_count'] for data in self.url_mappings.values())
        
        return f"""
=== URL Shortener Statistics ===
Total URLs shortened: {total_urls}
Total accesses: {total_accesses}
Average accesses per URL: {total_accesses / total_urls if total_urls > 0 else 0:.1f}
"""

def main():
    """Main function to run the URL Shortener CLI."""
    shortener = URLShortener()
    
    print("🔗 Welcome to the Offline URL Shortener!")
    print("=" * 40)
    
    while True:
        print("\nChoose an option:")
        print("1. Shorten a URL")
        print("2. Expand a short code")
        print("3. List all URLs")
        print("4. Show statistics")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            long_url = input("Enter the URL to shorten: ")
            short_code, message = shortener.shorten_url(long_url)
            
            if short_code:
                print(f"\n✅ {message}")
                print(f"🔗 Short code: {short_code}")
            else:
                print(f"\n❌ Error: {message}")
        
        elif choice == '2':
            short_code = input("Enter the short code: ")
            original_url, message = shortener.expand_url(short_code)
            
            if original_url:
                print(f"\n✅ {message}")
                print(f"🌐 Original URL: {original_url}")
            else:
                print(f"\n❌ Error: {message}")
        
        elif choice == '3':
            print(shortener.list_all_urls())
        
        elif choice == '4':
            print(shortener.get_stats())
        
        elif choice == '5':
            print("\n👋 Thank you for using the URL Shortener!")
            break
        
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()