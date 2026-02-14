#  Password Breach Checker

A Streamlit-based cybersecurity application that checks whether a password
has appeared in known data breaches using SHA-1 hashing and the
Have I Been Pwned API.

## Technologies Used
- Python 3.13
- Streamlit
- Requests

## How It Works
1. User enters a password
2. Password is hashed using SHA-1
3. First 5 characters of hash are sent to the API (k-anonymity)
4. Result is displayed without exposing the password

## How to Run
```bash
pip install streamlit requests
streamlit run app.py
## Author
- Name: Basil Varghese
- GitHub: https://github.com/vabasil2003

