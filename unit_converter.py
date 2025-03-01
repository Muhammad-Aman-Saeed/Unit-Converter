# Project 01: Unit Conveter
# Build a Google Unit conveter using Python and Streamlit:


import streamlit as st # type: ignore
st.markdown(
    """
    <style>
    body {
        background-color: #00bfff
        color: white;  
    }
    .stApp {
        background: linear-gradient (135deg,rgb(30, 85, 103), rgb(10, 25, 30) );
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }

    .stButton>button {
        background: linear-gradient (45 deg, rgb(83, 125, 159) , rgb(83, 132, 149));
        color: Black;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 5px;
        transition: 0.3s;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .stButton>button: hover {
        transform: scale(1.05);
        background: linear-gradient (45deg, rgb(103, 159, 185), rgb(103, 166, 196));
        color: black;
    }
    .result-box{
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 5px;
        margin-top: 20px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
        color; black;
    }
    </style>
    """,
    unsafe_allow_html = True
)


# Title And Details


st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write ("This is a simple unit converter application built with Python and Streamlit.")


#sidebar
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)


if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Feet", "Miles", "Yards", "Inches","Centimeters","Millimeters"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Feet", "Miles", "Yards", "Inches","Centimeters","Millimeters"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])


# Conversion Logic  
def convert_length(value,from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Feet": 3.28084,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Inches": 39.3701,
        "Centimeters": 100,
        "Millimeters": 1000
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1000000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value


    # Conversion Button

if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result: .4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Developed by Aman Saeed</div>", unsafe_allow_html=True)


