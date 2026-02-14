import streamlit as st
import hashlib
import requests

st.set_page_config(page_title="Password Breach Checker", page_icon="🔐")

st.title("🔐 Password Breach Checker")
st.write("Check whether your password has appeared in known data breaches.")
st.warning("Your password is never stored or sent directly.")

password = st.text_input("Enter your password", type="password")

def check_password(password):
    sha1 = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    for line in response.text.splitlines():
        h, count = line.split(":")
        if h == suffix:
            return int(count)
    return 0

if st.button("Check Password"):
    if password == "":
        st.error("Please enter a password")
    else:
        count = check_password(password)
        if count > 0:
            st.error(f"❌ Password found {count} times in data breaches")
        else:
            st.success("✅ Password NOT found in known breaches")
