import streamlit as st
import pickle
import time

# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="",
    layout="centered"
)

# Luxury CSS styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Montserrat:wght@300;400;600&display=swap');
    
    .main {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }
    
    h1 {
        font-family: 'Playfair Display', serif;
        color: #d4af37;
        text-align: center;
        font-size: 3.5rem !important;
        letter-spacing: 3px;
        margin-bottom: 10px !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .subtitle {
        font-family: 'Montserrat', sans-serif;
        color: #e8e8e8;
        text-align: center;
        font-size: 1rem;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 50px;
        font-weight: 300;
    }
    
    .luxury-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(212, 175, 55, 0.3);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        margin: 20px 0;
    }
    
    .prediction-box {
        background: linear-gradient(135deg, #d4af37 0%, #f4d03f 100%);
        padding: 50px;
        border-radius: 20px;
        text-align: center;
        margin: 40px 0;
        box-shadow: 0 15px 50px rgba(212, 175, 55, 0.4);
        border: 2px solid #d4af37;
    }
    
    .price-label {
        font-family: 'Montserrat', sans-serif;
        font-size: 14px;
        color: #1a1a2e;
        letter-spacing: 3px;
        text-transform: uppercase;
        font-weight: 600;
    }
    
    .price {
        font-family: 'Playfair Display', serif;
        font-size: 56px;
        font-weight: 700;
        color: #1a1a2e;
        margin: 15px 0;
        text-shadow: 2px 2px 4px rgba(255,255,255,0.2);
    }
    
    .property-details {
        font-family: 'Montserrat', sans-serif;
        color: #1a1a2e;
        font-size: 14px;
        letter-spacing: 1px;
        margin-top: 20px;
    }
    
    .furnished-badge {
        font-family: 'Montserrat', sans-serif;
        font-size: 12px;
        color: #1a1a2e;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-weight: 600;
        margin-top: 15px;
        padding: 8px 20px;
        background: rgba(26, 26, 46, 0.1);
        border-radius: 20px;
        display: inline-block;
    }
    
    label {
        font-family: 'Montserrat', sans-serif !important;
        font-size: 12px !important;
        color: #d4af37 !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        font-weight: 600 !important;
    }
    
    .stNumberInput > div > div > input {
        background: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid rgba(212, 175, 55, 0.5) !important;
        border-radius: 10px !important;
        color: white !important;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 18px !important;
        padding: 10px !important;
    }
    
    .stNumberInput > div > div > input:focus {
        border: 2px solid #d4af37 !important;
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.3) !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #d4af37 0%, #f4d03f 100%);
        color: #1a1a2e;
        font-family: 'Montserrat', sans-serif;
        font-size: 16px;
        font-weight: 600;
        letter-spacing: 3px;
        text-transform: uppercase;
        padding: 18px;
        border-radius: 50px;
        border: 2px solid #d4af37;
        width: 100%;
        margin-top: 30px;
        box-shadow: 0 10px 30px rgba(212, 175, 55, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(212, 175, 55, 0.5);
    }
    
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #d4af37, transparent);
        margin: 30px 0;
    }
    
    .icon {
        font-size: 24px;
        margin-right: 10px;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# Load the model
@st.cache_resource
def load_model():
    try:
        with open('E:\\yash\\jn\\house predictor\\model.h5', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error("Model file not found!")
        return None

model = load_model()

def predict_sale_price(area, bedrooms, bathrooms):
    input_data = [[area, bedrooms, bathrooms]]
    predicted_price = model.predict(input_data)
    # Convert to INR by multiplying by 30
    return predicted_price[0] * 30

# Header
st.markdown('<h1>ESTATE VALUATION</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Luxury Property Price Estimator</p>', unsafe_allow_html=True)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Input section in luxury card
st.markdown('<div class="luxury-card">', unsafe_allow_html=True)

area = st.number_input(
    "🏛️ Property Area (Square Feet)",
    min_value=0,
    max_value=50000,
    value=00,
    step=100
)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input(
        "🛏️ Bedrooms",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )

with col2:
    bathrooms = st.number_input(
        "🚿 Bathrooms",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )

# Predict button
if st.button('✨ Calculate Estate Value'):
    if model is not None:
        st.markdown('</div>', unsafe_allow_html=True)
        
        # 5 second loading with progress bar
        with st.spinner('Analyzing property features and market trends...'):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.05)  # 5 seconds total (100 * 0.05)
                progress_bar.progress(i + 1)
            
            predicted_price = predict_sale_price(area, bedrooms, bathrooms)
        
        st.markdown(f"""
            <div class="prediction-box">
                <div class="price-label">Estimated Market Value</div>
                <div class="price">₹{predicted_price:,.0f}</div>
                <div class="property-details">
                    {area:,} sq ft  •  {bedrooms} Bedrooms  •  {bathrooms} Bathrooms
                </div>
                <div class="furnished-badge">✨ Fully Furnished ✨</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown('</div>', unsafe_allow_html=True)
else:
    st.markdown('</div>', unsafe_allow_html=True)

# Elegant footer
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown(
    '<p style="text-align: center; color: #d4af37; font-family: \'Montserrat\', sans-serif; font-size: 11px; letter-spacing: 2px;">PREMIUM REAL ESTATE ANALYTICS  •  EST. 2025</p>',
    unsafe_allow_html=True
)