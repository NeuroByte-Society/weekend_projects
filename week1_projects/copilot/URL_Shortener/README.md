# 🔗 URL Shortener (Offline)

A simple, beginner-friendly Python project that creates short codes for long URLs and stores them locally. This tool works completely offline - no internet connection required once it's running!

## 📋 What This Project Does

- **Shorten URLs**: Takes long website links and creates short, memorable codes
- **Expand URLs**: Retrieves original URLs using short codes
- **Local Storage**: Saves all mappings in a JSON file (`url_mappings.json`)
- **Statistics**: Tracks usage and provides insights
- **Offline Operation**: Works without internet connectivity

## 🎯 Features

- ✅ Generate 6-character alphanumeric short codes (e.g., `abc123`)
- ✅ Validate URL formats before shortening
- ✅ Prevent duplicate URLs (returns existing short code)
- ✅ Track access count for each shortened URL
- ✅ List all shortened URLs with metadata
- ✅ Display usage statistics
- ✅ User-friendly command-line interface
- ✅ Persistent data storage in JSON format

## 🚀 How to Run

1. **Prerequisites**: Make sure you have Python 3.6+ installed
2. **Download**: Save the `URL_Shortener.py` file to your computer
3. **Run**: Open terminal/command prompt and navigate to the file location
4. **Execute**: Run the command:
   ```bash
   python URL_Shortener.py
   ```

## 💡 How to Use

The program presents a menu with 5 options:

### 1. Shorten a URL
```
Enter the URL to shorten: https://www.example.com/very/long/path
✅ URL shortened successfully!
🔗 Short code: aBc123
```

### 2. Expand a short code
```
Enter the short code: aBc123
✅ URL retrieved successfully!
🌐 Original URL: https://www.example.com/very/long/path
```

### 3. List all URLs
Shows all shortened URLs with creation dates and access counts.

### 4. Show statistics
Displays total URLs shortened and access statistics.

### 5. Exit
Closes the program safely.

## 📝 Example Usage

### Input/Output Examples:

**Shortening a URL:**
```
Input: https://github.com/NeuroByte-Society/weekend_projects
Output: Short code generated → K7m2Np
```

**Expanding a code:**
```
Input: K7m2Np
Output: https://github.com/NeuroByte-Society/weekend_projects
```

**Invalid URL handling:**
```
Input: not-a-valid-url
Output: ❌ Error: Invalid URL format. Please include http://, https://, or a valid domain.
```

## 🗂️ Data Storage

The program creates a `url_mappings.json` file that stores:
- Short code mappings
- Original URLs
- Creation timestamps
- Access count for each URL

Example JSON structure:
```json
{
  "K7m2Np": {
    "url": "https://github.com/NeuroByte-Society/weekend_projects",
    "created_at": "2024-01-15T10:30:45",
    "access_count": 3
  }
}
```

## 🛠️ Technical Details

**Language**: Python 3.6+
**Dependencies**: Only built-in Python modules:
- `json` - For data storage
- `random` & `string` - For generating short codes
- `os` - For file operations
- `datetime` - For timestamps

**Key Functions**:
- `generate_short_code()` - Creates unique 6-character codes
- `shorten_url()` - Maps long URLs to short codes
- `expand_url()` - Retrieves original URLs
- `is_valid_url()` - Validates URL format

## 🎓 What I Learned

- **File I/O**: Reading from and writing to JSON files
- **Data Validation**: Checking URL formats and handling edge cases
- **User Interface**: Creating an interactive command-line menu
- **Data Structures**: Using dictionaries for efficient key-value mapping
- **Error Handling**: Managing invalid inputs gracefully
- **Code Organization**: Structuring code with classes and methods

## 🔧 Possible Enhancements

- Custom short code length options
- URL expiration dates
- Import/export functionality
- Basic analytics dashboard
- QR code generation for short URLs
- Bulk URL processing

## 📁 File Structure

```
URL_Shortener/
├── URL_Shortener.py    # Main program file
├── README.md           # This documentation
└── url_mappings.json   # Generated data file (created when first URL is shortened)
```

## 🚨 Notes

- The `url_mappings.json` file is created automatically when you shorten your first URL
- All data is stored locally - no data is sent to external servers
- Short codes are case-sensitive
- The program performs basic URL validation but doesn't verify if URLs actually exist

---

**Project by**: @copilot for NeuroByte Society Weekend Projects
**Difficulty**: Beginner-friendly
**Estimated time**: 2-3 hours