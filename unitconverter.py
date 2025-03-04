# Project 01: Unit Convertor
# Build a Google Unit Convertor using Python and Streamlit:

import streamlit as st # type: ignore
st.markdown(
"""
<style>
body{
    background-color: #000000;
    color: #ffffff;
}
.stApp{
background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
padding: 20px;
border-radius: 10px;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
h1{
text-align: center;
font-size: 36px;
color:white;
}
.stButton>button{
background: linear-gradient(45deg,rgb(170, 205, 235), #351c75);
color: black;
font-size: 18px;
paddingL 10px 20px;
border-radius: 5px;
transition: 0.3s;
box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
}
.stButton>button:hover{
transform: scale(1.05);
background: linear-gradient(45deg, #92fe9d, #00c9ff);
color: black;
}
.result-box{
font0size: 24px;
font-weight: bold;
text-color: #000000;
text-align: center;
background: rgba(255, 255, 255, 0.8);
padding: 20px;
border-radius: 10px;
margin-top: 20px;
box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}
.footer{
text-align: center;
margin-top: 20px;
font-size: 14px;
color: black;
}
</style>
""",
unsafe_allow_html=True    
)

# Title and Description
st.markdown("<h1>🚀 Unit Converter using Python and Streamlit </h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, Weight and Temperature.")

# Unit Conversion Functions
conversion_type = st.sidebar.selectbox("Select Conversion Type",["Length", "Weight", "Temperature"])

# Input Field
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)

# Column Layout
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Millimeters", "Centimeters", "Miles", "Feet", "Yards", "Inches"])
        with col2:
            to_unit = st.selectbox("To", ["Meters", "Kilometers", "Millimeters", "Centimeters", "Miles", "Feet", "Yards", "Inches"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
        with col2:
            to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celcius", "Farenhite", "Kelvin"])
        with col2:
            to_unit =st.selectbox("To", ["Celcius", "Farenhite", "Kelvin"])

# Converted function
def length_converter(value, from_unit, to_unit):
    
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Miles": 0.000621371,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Inches": 39.3701,
        "Millimeters": 1000,
}
    return(value / length_units[from_unit] * length_units[to_unit])

def weight_converter(value, from_unit, to_unit):
    
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1000000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return(value / weight_units[from_unit] * weight_units[to_unit])

def temperature_converter(value, from_unit, to_unit):
    
    if from_unit == "Celcius":
        return (value * 9/5 + 32) if to_unit == "Farenhite" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Farenhite":
       return (value - 32) * 5/9 if to_unit == "Celcius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value 
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celcius" else (value - 273.15) * 9/5 + 32 if to_unit == "Farenhite" else value
    return value

# button for conversion
if st.button("🤖Convert"):
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result: .2f} {to_unit}</div>", unsafe_allow_html=True )

st.markdown("<div class='footer'>Developed by Sarah Survery</div>", unsafe_allow_html=True)






