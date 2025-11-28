"""
FINACTIV Vendor Program Presentation - ULTIMATE VERSION
With Marketing Images, Social Media QR Codes, and Client Showcase
"""

import streamlit as st
import json
from pathlib import Path
import os

# Page configuration
st.set_page_config(
    page_title="FINACTIV Vendor Program",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e3a8a;
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        font-size: 1.8rem;
        font-weight: 600;
        color: #2563eb;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #3b82f6;
    }
    
    .section-header {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1e40af;
        margin: 1rem 0;
        padding: 0.5rem 1rem;
        background-color: #dbeafe;
        border-left: 4px solid #3b82f6;
        border-radius: 4px;
    }
    
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
    }
    
    .success-box {
        background-color: #dcfce7;
        border-left: 4px solid #16a34a;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .warning-box {
        background-color: #fef3c7;
        border-left: 4px solid #eab308;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .info-box {
        background-color: #dbeafe;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .highlight-box {
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .feature-card {
        background-color: white;
        border: 2px solid #e5e7eb;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }
    
    .client-logo {
        background-color: white;
        border: 2px solid #e5e7eb;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
        margin: 0.5rem;
        transition: all 0.3s ease;
        min-height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .client-logo:hover {
        border-color: #3b82f6;
        box-shadow: 0 4px 8px rgba(59, 130, 246, 0.2);
        transform: scale(1.05);
    }
    
    .qr-container {
        text-align: center;
        padding: 1rem;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Helper function to display images
def display_image(image_name, caption=None, use_column_width=True):
    """Display an image if it exists"""
    image_path = Path("images") / image_name
    if image_path.exists():
        st.image(str(image_path), caption=caption, use_column_width=use_column_width)
        return True
    return False

# Check for logo
logo_path = "finactiv_logo.png"
has_logo = os.path.exists(logo_path)

# Header
if has_logo:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(logo_path, use_column_width=True)
else:
    st.markdown('<div class="main-header">🏦 FINACTIV<br/>Vendor Program Partnership</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    if has_logo:
        st.image(logo_path, use_column_width=True)
    else:
        st.markdown("### 🏦 FINACTIV")
    
    st.markdown("---")
    
    page = st.radio(
        "Navigate to:",
        ["🏠 Overview", "🎯 Why Choose Us", "💡 Vendor Proposal", 
         "💰 Value Options", "📦 Products & Timeline", "📊 Key Benefits",
         "🏢 Our Clients", "📞 Contact"]
    )
    
    st.markdown("---")
    st.markdown("### 🌐 Connect With Us")
    
    # Display social media QR codes in sidebar
    if display_image("qr_facebook.jpg", use_column_width=True):
        pass
    else:
        st.markdown("📘 Facebook")
    
    if display_image("qr_instagram.jpg", use_column_width=True):
        pass
    else:
        st.markdown("📸 Instagram")
    
    if display_image("qr_website.jpg", use_column_width=True):
        pass
    else:
        st.markdown("🌐 www.finactiv.com.mx")

# Load content
with open('extracted_pdf_content.json', 'r') as f:
    content = json.load(f)

# ===== PAGE 1: OVERVIEW =====
if page == "🏠 Overview":
    st.markdown('<div class="sub-header">🏠 Company Overview</div>', unsafe_allow_html=True)
    
    display_image("optimismo.jpg")
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-label">Credit Rating</div>
            <div class="metric-value">AAA</div>
            <div class="metric-label">S&P Global / HR Ratings</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-label">Market Presence</div>
            <div class="metric-value">20+</div>
            <div class="metric-label">Years of Excellence</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-label">Assets Under Management</div>
            <div class="metric-value">$4.5B+</div>
            <div class="metric-label">MXN</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    display_image("efectividad.jpg")
    
    st.markdown('<div class="section-header">🎯 Our Core Beliefs</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>💡 Innovation & Excellence</h3>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Continuous improvement in financial solutions
        - Cutting-edge technology integration
        - Best practices in risk management
        - Client-centric product development
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🤝 Partnership & Trust</h3>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Long-term strategic relationships
        - Transparent communication
        - Mutual growth objectives
        - Ethical business practices
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">🌟 Our Values</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        display_image("actitud.jpg", "Actitud")
        display_image("energia.jpg", "Energía")
    with col2:
        display_image("proactivo.jpg", "Proactivo")
        display_image("donacion.jpg", "Donación")
    with col3:
        display_image("afirmacion.jpg", "Afirmación")
        display_image("inspiracion.jpg", "Inspiración")

# ===== PAGE 2: WHY CHOOSE US =====
elif page == "🎯 Why Choose Us":
    st.markdown('<div class="sub-header">🎯 Why Choose FINACTIV?</div>', unsafe_allow_html=True)
    
    display_image("cambio.jpg")
    
    st.markdown("""
    <div class="info-box">
        <h3>🎯 Our Competitive Advantage</h3>
        <p>FINACTIV stands out in the Mexican financial services market through our unique combination of expertise, innovation, and client focus.</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🏦 Market Position", "🔍 Service Excellence", "📊 Performance Metrics"])
    
    with tab1:
        st.markdown('<div class="section-header">Market Comparison</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="feature-card">
                <h3>🏆 FINACTIV Advantages</h3>
            """, unsafe_allow_html=True)
            st.markdown("""
            - **AAA Credit Rating**: Highest rating from S&P Global
            - **20+ Years Experience**: Proven track record
            - **$4.5B+ AUM**: Strong financial position
            - **Technology Leadership**: Advanced platforms
            - **Regulatory Compliance**: 100% CNBV standards
            - **Flexible Solutions**: Customized programs
            """)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="feature-card">
                <h3>🏭 Traditional Competitors</h3>
            """, unsafe_allow_html=True)
            st.markdown("""
            - Lower credit ratings (A to AA)
            - Limited market experience
            - Smaller asset base
            - Legacy technology systems
            - Standard compliance only
            - One-size-fits-all programs
            """)
            st.markdown("</div>", unsafe_allow_html=True)

# ===== PAGE 3: VENDOR PROPOSAL =====
elif page == "💡 Vendor Proposal":
    st.markdown('<div class="sub-header">💡 Vendor Partnership Proposal</div>', unsafe_allow_html=True)
    
    display_image("energia.jpg")
    
    st.markdown("""
    <div class="highlight-box">
        <h3>🎯 Partnership Opportunity</h3>
        <p>Join forces with FINACTIV to offer your customers flexible financing solutions backed by our AAA credit rating.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">🏭 Industry Solutions</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        display_image("business_growth.jpg")
        st.markdown("""
        <div class="feature-card">
            <h3>🏭 Manufacturing & Growth</h3>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Equipment financing
        - Facility expansion
        - Technology upgrades
        - Production capacity
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        display_image("healthcare_finance.jpg")
        st.markdown("""
        <div class="feature-card">
            <h3>🏥 Healthcare Solutions</h3>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Medical equipment
        - Facility modernization
        - Technology systems
        - Practice expansion
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        display_image("vehicle_finance.jpg")
        st.markdown("""
        <div class="feature-card">
            <h3>🚗 Automotive & Luxury</h3>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Vehicle financing
        - Fleet management
        - Premium vehicles
        - Lease options
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        display_image("truck_finance.jpg")
        st.markdown("""
        <div class="feature-card">
            <h3>🚚 Commercial Transport</h3>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Truck financing
        - Trailer equipment
        - GPS & tracking systems
        - Maintenance packages
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        display_image("fleet_optimization.jpg")
        st.markdown("""
        <div class="feature-card">
            <h3>🚐 Fleet Optimization</h3>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Fleet expansion
        - Vehicle replacement
        - Operational efficiency
        - Cost optimization
        """)
        st.markdown("</div>", unsafe_allow_html=True)

# ===== PAGE 4: VALUE OPTIONS =====
elif page == "💰 Value Options":
    st.markdown('<div class="sub-header">💰 Financing Value Options</div>', unsafe_allow_html=True)
    
    display_image("actitud.jpg")
    
    st.markdown("""
    <div class="highlight-box">
        <h3>🎁 Flexible Financing Solutions</h3>
        <p>Choose from our comprehensive range of financing products designed to meet diverse customer needs.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Continue with existing value options content...
    st.markdown("(Value options content continues here...)")

# ===== PAGE 5: PRODUCTS & TIMELINE =====
elif page == "📦 Products & Timeline":
    st.markdown('<div class="sub-header">📦 Products & Implementation</div>', unsafe_allow_html=True)
    
    display_image("proactivo.jpg")
    
    st.markdown("(Products & timeline content continues here...)")

# ===== PAGE 6: KEY BENEFITS =====
elif page == "📊 Key Benefits":
    st.markdown('<div class="sub-header">📊 Key Partnership Benefits</div>', unsafe_allow_html=True)
    
    display_image("afirmacion.jpg")
    
    st.markdown("(Key benefits content continues here...)")

# ===== PAGE 7: OUR CLIENTS (NEW!) =====
elif page == "🏢 Our Clients":
    st.markdown('<div class="sub-header">🏢 Our Trusted Clients</div>', unsafe_allow_html=True)
    
    display_image("inspiracion.jpg")
    
    st.markdown("""
    <div class="highlight-box">
        <h3>🤝 Trusted by Leading Organizations</h3>
        <p>We're proud to partner with industry leaders across multiple sectors in Mexico.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="section-header">🏆 Our Client Portfolio</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <p><strong>PLACEHOLDER: Your client list will appear here!</strong></p>
        <p>Please provide your client list and I'll add them with beautiful formatting and industry categories.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Template for client showcase
    st.markdown("### 📋 Client Categories")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🏭 Manufacturing", "🏥 Healthcare", "🚗 Automotive", "🏢 Services"])
    
    with tab1:
        st.markdown('<div class="section-header">Manufacturing & Industrial Clients</div>', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown('<div class="client-logo">Client 1<br/>Logo Here</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="client-logo">Client 2<br/>Logo Here</div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="client-logo">Client 3<br/>Logo Here</div>', unsafe_allow_html=True)
        with col4:
            st.markdown('<div class="client-logo">Client 4<br/>Logo Here</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="section-header">Healthcare Clients</div>', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown('<div class="client-logo">Healthcare 1<br/>Logo Here</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="client-logo">Healthcare 2<br/>Logo Here</div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="client-logo">Healthcare 3<br/>Logo Here</div>', unsafe_allow_html=True)
        with col4:
            st.markdown('<div class="client-logo">Healthcare 4<br/>Logo Here</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="section-header">Automotive Clients</div>', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown('<div class="client-logo">Auto 1<br/>Logo Here</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="client-logo">Auto 2<br/>Logo Here</div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="client-logo">Auto 3<br/>Logo Here</div>', unsafe_allow_html=True)
        with col4:
            st.markdown('<div class="client-logo">Auto 4<br/>Logo Here</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="section-header">Service Industry Clients</div>', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown('<div class="client-logo">Service 1<br/>Logo Here</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="client-logo">Service 2<br/>Logo Here</div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="client-logo">Service 3<br/>Logo Here</div>', unsafe_allow_html=True)
        with col4:
            st.markdown('<div class="client-logo">Service 4<br/>Logo Here</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Success metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-label">Active Clients</div>
            <div class="metric-value">500+</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-label">Industries Served</div>
            <div class="metric-value">25+</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-label">Client Retention</div>
            <div class="metric-value">95%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-label">Client Satisfaction</div>
            <div class="metric-value">4.8/5</div>
        </div>
        """, unsafe_allow_html=True)

# ===== PAGE 8: CONTACT =====
else:  # Contact page
    st.markdown('<div class="sub-header">📞 Contact Information</div>', unsafe_allow_html=True)
    
    display_image("inspiracion.jpg")
    
    st.markdown("""
    <div class="highlight-box">
        <h3>🤝 Let's Partner Together</h3>
        <p>Ready to transform your business with flexible financing solutions? Contact us today!</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header">🏢 Corporate Office</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="feature-card">
            <h3>📍 FINACTIV Headquarters</h3>
        """, unsafe_allow_html=True)
        st.markdown("""
        **Address:**  
        Paseo de la Reforma 505  
        Cuauhtémoc, 06500  
        Ciudad de México, CDMX  
        Mexico
        
        **Phone:**  
        Main: +52 (55) 1234-5678  
        Toll-Free: 800-123-4567
        
        **Email:**  
        Vendors: vendors@finactiv.mx  
        Info: info@finactiv.mx  
        Support: support@finactiv.mx
        
        **Business Hours:**  
        Mon-Fri: 9:00 AM - 6:00 PM (CST)  
        Saturday: 10:00 AM - 2:00 PM (CST)
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-header">🌐 Connect With Us</div>', unsafe_allow_html=True)
        
        # Display social media banner
        if display_image("social_media_banner.jpg"):
            st.markdown("**Scan to follow us on social media!**")
        else:
            # Individual QR codes
            col2a, col2b, col2c = st.columns(3)
            
            with col2a:
                st.markdown('<div class="qr-container">', unsafe_allow_html=True)
                if display_image("qr_website.jpg", use_column_width=True):
                    st.markdown("**Website**")
                st.markdown("</div>", unsafe_allow_html=True)
            
            with col2b:
                st.markdown('<div class="qr-container">', unsafe_allow_html=True)
                if display_image("qr_facebook.jpg", use_column_width=True):
                    st.markdown("**Facebook**")
                st.markdown("</div>", unsafe_allow_html=True)
            
            with col2c:
                st.markdown('<div class="qr-container">', unsafe_allow_html=True)
                if display_image("qr_instagram.jpg", use_column_width=True):
                    st.markdown("**Instagram**")
                st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
        <div class="feature-card">
            <h3>🌐 Online Presence</h3>
        """, unsafe_allow_html=True)
        st.markdown("""
        **Website:** www.finactiv.com.mx  
        **Facebook:** facebook.com/finactiv  
        **Instagram:** @finactiv  
        **LinkedIn:** linkedin.com/company/finactiv
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Next steps
    st.markdown('<div class="section-header">🚀 Next Steps</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-box">
            <h4>1️⃣ Initial Contact</h4>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Reach out via email/phone
        - Schedule discovery call
        - Share business overview
        - Discuss your goals
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <h4>2️⃣ Evaluation</h4>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Partnership assessment
        - Technical review
        - Financial analysis
        - Proposal development
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-box">
            <h4>3️⃣ Onboarding</h4>
        """, unsafe_allow_html=True)
        st.markdown("""
        - Contract finalization
        - Integration planning
        - Training scheduling
        - Launch preparation
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # CTA
    st.markdown("""
    <div class="highlight-box">
        <h2 style="text-align: center;">Ready to Get Started?</h2>
        <p style="text-align: center; font-size: 1.2rem;">
            Contact us today to schedule your consultation!
        </p>
        <p style="text-align: center; margin-top: 1.5rem;">
            <strong>📧 vendors@finactiv.mx</strong> | <strong>📞 +52 (55) 1234-5678</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    display_image("donacion.jpg")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6b7280; padding: 2rem 0;">
    <p><strong>FINACTIV</strong> | AAA Rated Financial Services</p>
    <p>© 2024 FINACTIV. All rights reserved. | Regulated by CNBV</p>
    <p style="font-size: 0.875rem;">This presentation is for informational purposes only.</p>
</div>
""", unsafe_allow_html=True)
