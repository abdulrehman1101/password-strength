import streamlit as st
import re

# Custom CSS
st.markdown(
    """
    <style>
        .weak {color: white; background-color: red; padding: 10px; border-radius: 5px; text-align: center;}
        .moderate {color: black; background-color: yellow; padding: 10px; border-radius: 5px; text-align: center;}
        .strong {color: white; background-color: orange; padding: 10px; border-radius: 5px; text-align: center;}
        .very-strong {color: white; background-color: green; padding: 10px; border-radius: 5px; text-align: center;}
        
        /* Button Styling */
        .stButton > button {
            background-color: #60A5FA !important; /* blue-400 */
            color: white !important;
            border-radius: 5px;
            padding: 10px 20px;
            border: none;
            transition: background-color 0.3s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #3B82F6 !important; /* blue-500 */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def check_password_strength(password: str) -> str:
    strength = 0
    remarks = "Weak"
    css_class = "weak"
    
    # Criteria
    length_error = len(password) < 8
    digit_error = not re.search(r"\d", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    special_char_error = not re.search(r"[@$!%*?&]", password)
    
    # Calculating strength
    if not length_error:
        strength += 1
    if not digit_error:
        strength += 1
    if not uppercase_error:
        strength += 1
    if not lowercase_error:
        strength += 1
    if not special_char_error:
        strength += 1
    
    # Assign remarks and CSS class
    if strength == 5:
        remarks = "Very Strong"
        css_class = "very-strong"
    elif strength == 4:
        remarks = "Strong"
        css_class = "strong"
    elif strength == 3:
        remarks = "Moderate"
        css_class = "moderate"
    elif strength <= 2:
        remarks = "Weak"
        css_class = "weak"
    
    return remarks, css_class

# Streamlit UI
st.title("🔑 Password Strength Checker")
st.markdown("#### Enter your password below to check its security level")
password = st.text_input("Enter Your Password", type="password")

if st.button("Check Password Strength"):
    if password:
        strength, css_class = check_password_strength(password)
        st.markdown(f'<div class="{css_class}">{strength}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a password to check its strength.")
    