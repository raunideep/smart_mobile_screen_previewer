import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Multi-Device Preview Tool")

# Initialize session state for URL tracking
if "target_url" not in st.session_state:
    st.session_state.target_url = ""

st.title("📱 Smart Mobile & Device Screen Previewer")

# Text input linked with session state
target_url = st.text_input(
    "Enter Website URL (e.g., https://example.com):", 
    value=st.session_state.target_url, 
    key="url_input"
)

if target_url != st.session_state.target_url:
    st.session_state.target_url = target_url

processed_url = st.session_state.target_url
if processed_url and not processed_url.startswith("http://") and not processed_url.startswith("https://"):
    processed_url = "https://" + processed_url

if not processed_url:
    st.info("👆 Please enter a website URL above to start previewing across devices.")
else:
    st.markdown("---")
    
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
    
    # Arrow UI component pointing to the dropdown
    st.markdown(
        """
        <div style="margin-top: 5px; margin-bottom: 10px; font-family: sans-serif;">
            <span style="font-size: 22px; color: #a855f7; font-weight: bold;">╰──➤ Select the view</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    dev_info = device_options[selected_device]
    w = dev_info["width"]
    h = dev_info["height"]
    dev_type = dev_info["type"]
    
    border_radius = "35px" if dev_type == "iPhone" else ("20px" if dev_type == "Android" else "10px")
    border_style = "12px solid #222" if dev_type in ["iPhone", "Android"] else "6px solid #444"
    
    html_code = f"""
    <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-top: 15px; font-family: sans-serif;">
        <div style="font-weight: bold; color: #ffffff; margin-bottom: 12px; font-size: 18px;">
            🎯 Active Preview: {selected_device}
        </div>
        
        <div style="border: {border_style}; border-radius: {border_radius}; overflow: hidden; width: {w if isinstance(w, str) else str(w) + 'px'}; height: {h}px; background: white; box-shadow: 0 8px 25px rgba(0,0,0,0.8);">
            <iframe src="{processed_url}" width="100%" height="100%" style="border:none;"></iframe>
        </div>
    </div>
    """
    
    components.html(html_code, height=h + 120, scrolling=True)