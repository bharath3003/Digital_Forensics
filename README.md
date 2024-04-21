**Project Description:**

This project allows you to check whether your browser has visited any known malicious websites by analyzing your browser history. It is specifically designed for Mozilla Firefox.

### Prerequisites:

- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) installed on your system.

### Setup:

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/bharath3003/Digital_Forensics.git
   ```

2. Navigate to the project directory.

   ```bash
   cd Digital_Forensics
   ```

3. Open Firefox and find your Firefox profile directory:
   - Type `about:support` in the Firefox address bar.
   - Look for the "Profile Folder" entry to find your profile directory.

4. Update the `firefox_profile_path` variable in `test.py` with your Firefox profile directory.

### Configuration:

1. Create a `.env` file in the project directory.

2. Add your VirusTotal API key to the `.env` file:

   ```
   API_KEY=your_virustotal_api_key
   ```

### Running the Project:

Run the `test.py` script to analyze your browser history:

```bash
python test.py
```

The script will check your browser history for any visits to malicious websites using the VirusTotal API.

Enjoy secure browsing!
