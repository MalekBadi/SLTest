import streamlit as st

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9 / 5) + 32

def main():
    st.title("🌡️ Temperature Converter")
    st.markdown("Convert between Fahrenheit and Celsius (Centigrades)")
    
    # Select conversion direction
    conversion_type = st.radio(
        "Select conversion direction:",
        ["Fahrenheit to Celsius", "Celsius to Fahrenheit"],
        horizontal=True
    )
    
    st.divider()
    
    if conversion_type == "Fahrenheit to Celsius":
        # Input field for Fahrenheit
        fahrenheit = st.number_input(
            "Enter temperature in Fahrenheit (°F):",
            value=32.0,
            step=0.1,
            format="%.2f"
        )
        
        # Convert button
        st.button("Convert to Celsius", type="primary")
        
        # Automatic conversion display
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.success(f"**{fahrenheit}°F = {celsius:.2f}°C**")
        
    else:  # Celsius to Fahrenheit
        # Input field for Celsius
        celsius = st.number_input(
            "Enter temperature in Celsius (°C):",
            value=0.0,
            step=0.1,
            format="%.2f"
        )
        
        # Convert button
        st.button("Convert to Fahrenheit", type="primary")
        
        # Automatic conversion display
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.success(f"**{celsius}°C = {fahrenheit:.2f}°F**")

if __name__ == "__main__":
    main()
