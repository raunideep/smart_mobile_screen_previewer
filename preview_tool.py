import streamlit as st
import streamlit.components.v1 as components

# --- Page Setup ---
st.set_page_config(layout="wide", page_title="Multi-Device Preview Tool")

# --- Custom CSS for Refresh Button ---
st.markdown("""
    <style>
    /* Style for the refresh button container */
    .refresh-container {
        display: flex;
        justify-content: center; /* Center horizontally */
        align-items: center;     /* Center vertically */
        margin-top: -10px;       /* Adjust space above */
        margin-bottom: 5px;     /* Adjust space below */
    }

    /* Style for the actual button */
    .stButton > button {
        background-color: #a855f7; /* Same color as the arrow text */
        color: white;
        border: none;
        padding: 8px 20px;
        border-radius: 20px;
        font-family: sans-serif;
        font-weight: bold;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    /* Hover effect for the button */
    .stButton > button:hover {
        background-color: #9333ea; /* Darker shade on hover */
    }

    /* Hide the Streamlit default footer and menu for a cleaner app look */
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Main App Content ---
st.title("📱 Smart Mobile & Device Screen Previewer")

# --- Input Field ---
target_url = st.text_input("Enter Website URL (e.g., https://example.com):", "")

# --- URL Auto-Fix ---
if target_url and not target_url.startswith("http://") and not target_url.startswith("https://"):
    target_url = "https://" + target_url

# --- Conditional Rendering ---
if not target_url:
    st.info("👆 Please enter a website URL above to start previewing across devices.")
else:
    st.markdown("---")
    
    # --- Device Selection (Dropdown) ---
    device_options = {
        "📱 iPhone SE / Standard (375x667)": {"width": 375, "height": 667, "type": "iPhone"},
        "📱 iPhone Pro / 14-15 (390x844)": {"width": 390, "height": 844, "type": "iPhone"},
        "📱 iPhone Pro Max (430x932)": {"width": 430, "height": 932, "type": "iPhone"},
        "🤖 Android Mobile - Standard (360x800)": {"width": 360, "height": 800, "type": "Android"},
        "🤖 Android Mobile - Large/Ultra (412x915)": {"width": 412, "height": 915, "type": "Android"},
        "📋 Tablet / iPad View (768x1024)": {"width": 768, "height": 700, "type": "Tablet"},
        "💻 Laptop / Desktop View (100%)": {"width": "100%", "height": 650, "type": "Desktop"}
    }
    
    selected_device = st.selectbox("🔍 Select Popular Mobile Models & Views:", list(device_options.keys()))
    
    # --- Refresh Button ---
    # Create a container for positioning the button
    col_l, col_mid, col_r = st.columns([1, 3, 1])
    with col_mid:
        st.markdown('<div class="refresh-container">', unsafe_allow_html=True)
        if st.button('🔄 Refresh Preview'):
            # Streamlit's rerun mechanism handles the refresh automatically
            pass
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Device Info & Styling ---
    dev_info = device_options[selected_device]
    w = dev_info["width"]
    h = dev_info["height"]
    dev_type = dev_info["type"]
    
    border_radius = "35px" if dev_type == "iPhone" else ("20px" if dev_type == "Android" else "10px")
    border_style = "12px solid #222" if dev_type in ["iPhone", "Android"] else "6px solid #444"
    
    # --- HTML/CSS for Iframe and Wrapper ---
    # Note: The `?t={st.session_state.get('refresh_counter', 0)}` is a trick to force iframe reload
    # However, since the user is just navigating, a simple state change (or no change) will cause Streamlit
    # to re-render the `components.html` with the same URL, which also forces the iframe to reload.
    # The button click itself causes a rerun, which is enough.
    
    html_code = f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: 5px; font-family: sans-serif;">
        <div style="font-weight: bold; color: #ffffff; margin-bottom: 12px; font-size: 18px;">
            🎯 Active Preview: {selected_device}
        </div>
        
        <div style="border: {border_style}; border-radius: {border_radius}; overflow: hidden; width: {w if isinstance(w, str) else str(w) + 'px'}; height: {h}px; background: white; box-shadow: 0 8px 25px rgba(0,0,0,0.8);">
            <iframe src="{target_url}" width="100%" height="100%" style="border:none;"></iframe>
        </div>
    </div>
    """
    
    components.html(html_code, height=h + 120, scrolling=True)