import streamlit as st
import time

# Set page config
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

# App title and description
st.title("⚖️ BMI Calculator")
st.write("Calculate your Body Mass Index in seconds!")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    # Weight input
    weight_unit = st.radio("Weight unit:", ("kg", "lbs"))
    weight = st.number_input(f"Enter your weight ({weight_unit}):", min_value=30.0, max_value=300.0, value=70.0, step=0.1)

with col2:
    # Height input
    height_unit = st.radio("Height unit:", ("cm", "feet"))
    if height_unit == "cm":
        height = st.number_input("Enter your height (cm):", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
    else:
        feet = st.number_input("Feet:", min_value=3, max_value=8, value=5)
        inches = st.number_input("Inches:", min_value=0, max_value=11, value=7)
        height = feet * 12 + inches  # Convert to inches

# Convert units to metric if needed
if weight_unit == "lbs":
    weight = weight * 0.453592  # lbs to kg

if height_unit == "feet":
    height = height * 2.54  # inches to cm

# Calculate BMI
if st.button("Calculate BMI"):
    with st.spinner("Calculating..."):
        time.sleep(0.5)  # Small delay for UX
        
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        bmi_rounded = round(bmi, 1)
        
        # Display result with color coding
        st.subheader(f"Your BMI: {bmi_rounded}")
        
        if bmi < 18.5:
            st.error("Underweight (BMI < 18.5)")
            st.info("💡 Consider consulting a nutritionist for healthy weight gain")
        elif 18.5 <= bmi < 25:
            st.success("Normal weight (BMI 18.5-24.9)")
            st.balloons()
        elif 25 <= bmi < 30:
            st.warning("Overweight (BMI 25-29.9)")
            st.info("💡 Regular exercise and balanced diet can help")
        else:
            st.error("Obese (BMI ≥ 30)")
            st.info("💡 Please consult a healthcare professional")
        
        # Show BMI chart
        st.markdown("### BMI Categories:")
        st.image("https://www.cdc.gov/healthyweight/images/assessing/bmi-adult-fb-600x315.jpg", 
                caption="BMI Chart from CDC", width=300)

# Add sidebar with info
with st.sidebar:
    st.header("About BMI")
    st.write("""
    Body Mass Index (BMI) is a person's weight in kilograms divided by the square of height in meters. 
    
    While BMI is a useful screening tool, it has limitations:
    - Doesn't measure body fat directly
    - May overestimate body fat in athletes
    - May underestimate body fat in older adults
    """)
    st.markdown("[Learn more about BMI](https://www.cdc.gov/healthyweight/assessing/bmi/index.html)")

# Add footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | Not a substitute for professional medical advice")