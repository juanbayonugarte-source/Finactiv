"""
FINACTIV Vendor Program - Interactive Web Presentation
Streamlit Dashboard for Vendor Partnership Proposals
"""

import streamlit as st
import json
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="FINACTIV Vendor Program",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        font-size: 48px;
        font-weight: bold;
        color: #363B50;
        text-align: center;
        padding: 20px;
        background: linear-gradient(135deg, #363B50 0%, #BD8894 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
    }
    
    .sub-header {
        font-size: 32px;
        font-weight: bold;
        color: #363B50;
        margin-top: 30px;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 3px solid #BD8894;
    }
    
    .section-header {
        font-size: 24px;
        font-weight: 600;
        color: #363B50;
        margin-top: 25px;
        margin-bottom: 15px;
    }
    
    .metric-box {
        background-color: #F5F6F8;
        border-left: 5px solid #BD8894;
        padding: 20px;
        margin: 10px 0;
        border-radius: 5px;
    }
    
    .success-box {
        background-color: #D1FAE5;
        border-left: 5px solid #BD8894;
        padding: 20px;
        margin: 10px 0;
        border-radius: 5px;
    }
    
    .warning-box {
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        padding: 20px;
        margin: 10px 0;
        border-radius: 5px;
    }
    
    .info-box {
        background-color: #F5F6F8;
        border-left: 5px solid #BD8894;
        padding: 20px;
        margin: 10px 0;
        border-radius: 5px;
    }
    
    .highlight-box {
        background: linear-gradient(135deg, #363B50 0%, #BD8894 100%);
        color: white;
        padding: 25px;
        border-radius: 10px;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .feature-card {
        background-color: #F9FAFB;
        border: 2px solid #E5E7EB;
        border-radius: 8px;
        padding: 20px;
        margin: 10px 0;
        transition: transform 0.2s;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    .stat-number {
        font-size: 48px;
        font-weight: bold;
        color: #BD8894;
    }
    
    .stat-label {
        font-size: 16px;
        color: #6B7280;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Main header with logo
# Try to load the FINACTIV logo
logo_path = os.path.join(os.path.dirname(__file__), "finactiv_logo.png")
if os.path.exists(logo_path):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(logo_path, use_container_width=True)
else:
    st.markdown('<div class="main-header">FINACTIV Vendor Program</div>', unsafe_allow_html=True)

st.markdown('<p style="text-align: center; font-size: 20px; color: #6B7280; margin-bottom: 40px;">Financial Solutions Partnership for JSW - November 2025</p>', unsafe_allow_html=True)

# Sidebar navigation with logo
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, use_container_width=True)
else:
    st.sidebar.markdown("### 🏢 FINACTIV")
st.sidebar.markdown("### 📋 Navigation")

page = st.sidebar.radio(
    "Select Section:",
    [
        "🏠 Overview",
        "🎯 Why Choose Us",
        "💡 Vendor Proposal", 
        "💰 Value Options",
        "📦 Products & Timeline",
        "📊 Key Benefits",
        "📞 Contact"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📄 Presentation Info")
st.sidebar.info("""
**Company:** FINACTIV  
**Program:** Vendor Partnership  
**Date:** November 2025  
**Version:** 1.0
""")

# ========================================================================
# PAGE 1: OVERVIEW
# ========================================================================
if page == "🏠 Overview":
    st.markdown('<div class="sub-header">Program Overview</div>', unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div class="metric-box" style="text-align: center;">
            <div class="stat-number">15+</div>
            <div class="stat-label">Years of Experience</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-box" style="text-align: center;">
            <div class="stat-number">500+</div>
            <div class="stat-label">Satisfied Clients</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-box" style="text-align: center;">
            <div class="stat-number">100%</div>
            <div class="stat-label">Mexican Company</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-box" style="text-align: center;">
            <div class="stat-number">24/7</div>
            <div class="stat-label">Client Support</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Value proposition
    st.markdown("""
    <div class="highlight-box">
        <h2 style="color: white; margin-top: 0;">Our Value Proposition</h2>
        <h3 style="color: white;">Specialized Financial Solutions for Small and Medium-Sized Businesses in Mexico</h3>
        <p style="font-size: 18px; color: white;">
        We drive your growth with fast, practical, and flexible leasing and credit solutions
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Core beliefs
    st.markdown('<div class="section-header">What We Believe In</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🎯 Customer Passion</h4>
            <p>We are passionate about our clients and their success</p>
        </div>
        
        <div class="feature-card">
            <h4>🚀 Proactive Leadership</h4>
            <p>We take initiative with positive, proactive leadership</p>
        </div>
        
        <div class="feature-card">
            <h4>🤝 Long-term Relationships</h4>
            <p>We build lasting relationships with integrity and respect</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>⚡ Effectiveness</h4>
            <p>We are proactive in seeking effectiveness</p>
        </div>
        
        <div class="feature-card">
            <h4>👥 Teamwork</h4>
            <p>We work as one unified team</p>
        </div>
        
        <div class="feature-card">
            <h4>⭐ Excellence</h4>
            <p>We strive to do everything with excellence</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Credit rating
    st.markdown("---")
    st.markdown('<div class="section-header">Credit Ratings</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="success-box">
            <h3>HR Ratings</h3>
            <h2 style="color: #BD8894; margin: 10px 0;">BBB+</h2>
            <p><strong>Perspective:</strong> Stable (2024)</p>
            <p>Consistent BBB+ rating from 2019-2024</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
            <h3>Verum</h3>
            <h2 style="color: #BD8894; margin: 10px 0;">BBB+</h2>
            <p><strong>Perspective:</strong> Stable</p>
            <p>Strong counterparty risk and credit quality ratings</p>
        </div>
        """, unsafe_allow_html=True)

# ========================================================================
# PAGE 2: WHY CHOOSE US
# ========================================================================
elif page == "🎯 Why Choose Us":
    st.markdown('<div class="sub-header">Why Choose FINACTIV</div>', unsafe_allow_html=True)
    
    # Market panorama
    st.markdown('<div class="section-header">Market Landscape</div>', unsafe_allow_html=True)
    
    tabs = st.tabs(["Captive Leasers", "Bank Leasers", "Independent Leasers"])
    
    with tabs[0]:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("### Captive Leasing Companies")
        st.markdown("#### Strategic Value")
        st.markdown("""
        - Increase sales of brand equipment by offering payment plans and tailored financial schemes
        - Good option for manufacturers to invest excess cash
        """)
        
        st.markdown("#### Business Model")
        st.markdown("""
        - Leverage manufacturer sales and marketing synergies and distribution channels
        - Complete back-office structuring
        - Profits backed and subsidized by manufacturer: blind discounts, shared expenses
        - Funding backed by manufacturer: direct resources, guarantees
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="success-box">
                <h4>✅ Advantages</h4>
                <ul>
                    <li>Support from manufacturer's sales force</li>
                    <li>Access to best deals</li>
                    <li>Pricing control</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="warning-box">
                <h4>⚠️ Disadvantages</h4>
                <ul>
                    <li>Pressure to take unacceptable credit risks</li>
                    <li>Risk concentration</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("### Bank Leasing Companies")
        st.markdown("#### Strategic Value")
        st.markdown("""
        - Seek to expand financial services ("share the wallet")
        - Can leverage economies of scale in client base and back-office/funding synergies
        """)
        
        st.markdown("#### Business Model")
        st.markdown("- Utilize bank's distribution and placement channels")
        st.markdown('</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="success-box">
                <h4>✅ Advantages</h4>
                <ul>
                    <li>Operational synergies and economies of scale</li>
                    <li>Broad client base</li>
                    <li>Strong funding capabilities</li>
                    <li>Back-office synergies</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="warning-box">
                <h4>⚠️ Disadvantages</h4>
                <ul>
                    <li>Require specialization for asset management</li>
                    <li>Must comply with Basel requirements</li>
                    <li>In-house client sectors/activities not served</li>
                    <li>Product commoditization by price vs. brand</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with tabs[2]:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("### Independent Leasing Companies (FINACTIV)")
        st.markdown("#### Strategic Value")
        st.markdown("""
        - Initiatives from independent or strategic investors
        - Not limited or conflicted with manufacturers or clients
        """)
        
        st.markdown("#### Business Model")
        st.markdown("""
        - Origination subject to special strategies and niches
        - Varied origination sources: Self-promotion, Internet, Vendor Programs, End Users, Brokers
        - Profits based on focus towards more profitable market niches
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="success-box">
                <h4>✅ Advantages</h4>
                <ul>
                    <li>Experience and flexibility</li>
                    <li>Easy schemes and structuring</li>
                    <li>Freedom to move across different niches</li>
                    <li>Compete by differentiation: service, efficiency, coverage, risks</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="warning-box">
                <h4>⚠️ Disadvantages</h4>
                <ul>
                    <li>Regional coverage limitations</li>
                    <li>More limited marketing budgets</li>
                    <li>Limited client base</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Competitive advantages
    st.markdown('<div class="section-header">Our Competitive Advantages</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>⚡ Speed</h4>
            <p><strong>Pre-approval in 48 hours</strong></p>
            <p>With just 3 documents</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🎯 Service</h4>
            <p><strong>We take time to understand your needs</strong></p>
            <p>Customized solutions designed for you</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>💡 Flexibility</h4>
            <p><strong>Fixed or variable rates</strong></p>
            <p>Expert knowledge of leasing equipment</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Markets served
    st.markdown("---")
    st.markdown('<div class="section-header">Markets We Serve</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("#### We serve financing needs for equipment in:")
    st.markdown("""
    - 🚚 **Transportation** - Commercial vehicles and fleets
    - 🏭 **Industrial Equipment** - Manufacturing and production machinery
    - 🏥 **Medical Equipment** - Healthcare facilities equipment
    """)
    
    st.markdown("#### Company Sizes:")
    st.markdown("Small • Medium • Large • Multinational • International")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Value focus
    st.markdown("---")
    st.markdown("""
    <div class="highlight-box">
        <h3 style="color: white; text-align: center;">We Focus On</h3>
        <h2 style="color: white; text-align: center; margin-top: 20px;">
        Asset-Based Financing with Liquid Secondary Markets
        </h2>
    </div>
    """, unsafe_allow_html=True)

# ========================================================================
# PAGE 3: VENDOR PROPOSAL
# ========================================================================
elif page == "💡 Vendor Proposal":
    st.markdown('<div class="sub-header">Vendor Partnership Proposal</div>', unsafe_allow_html=True)
    
    # Why vendor program
    st.markdown('<div class="section-header">Why a Vendor Program?</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h3>🏢 Benefits for FINACTIV</h3>
            <ul>
                <li><strong>Resource Maximization:</strong> Administration, funding, systems</li>
                <li><strong>Capability</strong> to design credit models/structures/pricing for specific markets</li>
                <li><strong>Higher Placement Volume</strong></li>
                <li><strong>Competitive Pricing</strong></li>
                <li><strong>Independence</strong> in risk-taking and funding</li>
                <li><strong>Tailored Financial Solutions</strong> for each client's needs</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
            <h3>🎯 Benefits for Partners</h3>
            <ul>
                <li><strong>Complete Financing Solution</strong> for your clients</li>
                <li><strong>Sales Potential:</strong> 2x in 12 months, up to 5x in 4 years</li>
                <li><strong>Accelerates Sales Cycle</strong> - reduces days in accounts receivable</li>
                <li><strong>Customer Loyalty</strong> - Repeat and stable sales</li>
                <li><strong>Improved Margins</strong> through better pricing</li>
                <li><strong>No Capital Requirements</strong></li>
                <li><strong>Shorter, Predictable Response Times</strong></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Win-win synergy
    st.markdown("""
    <div class="highlight-box">
        <h2 style="color: white; text-align: center;">Win-Win Synergy</h2>
        <h3 style="color: white; text-align: center; margin-top: 20px;">
        Partner Contribution + FINACTIV = Added Value, Customer Loyalty & Revenue
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # What we bring
    st.markdown("---")
    st.markdown('<div class="section-header">Partnership Structure</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("#### 🏢 FINACTIV Provides")
        st.markdown("""
        - **Business Line:** SMEs
        - **Complete Process** from application to funding
        - **Credit Expertise** and risk assessment
        - **Funding Solutions**
        - **Operational Infrastructure**
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.markdown("#### 🤝 Partner Provides")
        st.markdown("""
        - **Business Line:** All business segments
        - **Client Referrals:** Current and potential customers
        - **Sales Channel** integration
        - **Market Knowledge** and relationships
        """)
        
        st.markdown("#### Partner Receives")
        st.markdown("""
        - **Cash Payment** for equipment
        - **Increased Sales Volume**
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Commercial proposal
    st.markdown("---")
    st.markdown('<div class="section-header">Commercial Proposal Details</div>', unsafe_allow_html=True)
    
    st.markdown("""
    | **Parameter** | **Details** |
    |---------------|-------------|
    | **Products** | Simple Credit • Financial Leasing • Pure Leasing/Renting |
    | **Amount per Client** | Up to $20 million MXN |
    | **Terms** | 12 to 60 months + possibility of 3 MGC (Capital Grace Months) |
    | **Interest Rates** | 16.50% to 19.50% • Fixed or Variable |
    | **Commission/Legal Expenses** | 2.20% to 3.00% • $17,500 - $25,000 |
    | **Down Payment/Initial Rent** | 15% down payment • Initial rent from 2.0% to 25.0% |
    | **Security Deposit** | 2 Months |
    | **Residual Value (Financial Leasing)** | 36m = 35% • 48m = 25% • 60m = 25% |
    | **Company Profile** | SMEs with minimum annual sales of $10 million MXN |
    | **Economic Sectors** | All except Construction, Mining, Security, and Government |
    | **Equipment to Finance** | Industrial Equipment |
    | **Equipment Insurance** | Financed, paid cash, contracted with FINACTIV |
    """)
    
    # Keys to success
    st.markdown("---")
    st.markdown('<div class="section-header">Keys to Success</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>📚 Training</h4>
            <p><strong>Initial and Quarterly Training</strong></p>
            <ul>
                <li>Credit & Leasing products</li>
                <li>Quote calculator</li>
                <li>Forms and checklists</li>
                <li>Credit process</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🏢 Plant/Office Visits</h4>
            <p><strong>Continuous Face-to-Face Presence</strong></p>
            <ul>
                <li>Visit plant every 15 days or monthly</li>
                <li>FINACTIV executive availability</li>
                <li>On-site support</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>🤝 Client Visits</h4>
            <p><strong>Joint Prospect Visits</strong></p>
            <ul>
                <li>Product explanations</li>
                <li>Quotations</li>
                <li>Forms and checklist support</li>
                <li>Complete file preparation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box">
        <h4>🎯 Service Excellence</h4>
        <p><strong>Service = Presence + Follow-up + Timely Responses + Punctual Attention</strong></p>
    </div>
    """, unsafe_allow_html=True)
    
    # Working session
    st.markdown("---")
    st.markdown('<div class="section-header">Working Session Topics</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h4>We will define together:</h4>
        <ul>
            <li><strong>📦 Products to Operate:</strong> Financial Leasing/Pure Leasing, Simple Credit</li>
            <li><strong>💰 Pricing:</strong> Rates and commissions</li>
            <li><strong>📈 Promotion:</strong> Mutual incentives, Sales team incentives</li>
            <li><strong>📣 Advertising:</strong> Digital marketing (e-books, e-Flyers, social media), Web quotation tools (users), Mutual portal links</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ========================================================================
# PAGE 4: VALUE OPTIONS
# ========================================================================
elif page == "💰 Value Options":
    st.markdown('<div class="sub-header">Value-Added Options</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <p style="font-size: 18px;">
        These special financing options provide additional flexibility to meet your clients' cash flow needs
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Four main products
    st.markdown('<div class="section-header">4 Core Products</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>1️⃣ Capital Grace Period (MGC)</h3>
            <h4>Grace on Capital Payments</h4>
            <ul>
                <li><strong>Grace Period:</strong> Up to 6 months</li>
                <li><strong>Modality:</strong> 3 months grace + Credit term</li>
                <li><strong>Example:</strong> 3+48 = 51 months total</li>
                <li><strong>Benefit:</strong> Capital Grace = Working Capital</li>
                <li><strong>Impact:</strong> 3 MGC = 8% Working Capital</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <h3>2️⃣ Initial Payment Terms</h3>
            <h4>Term for Down Payments</h4>
            <ul>
                <li><strong>Term:</strong> 1 to 3 months WITHOUT INTEREST</li>
                <li><strong>Concepts:</strong> Monthly installments in deposit</li>
                <li><strong>Benefit:</strong> Spread initial payment over time</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>3️⃣ Seasonal Payments (Low-High)</h3>
            <h4>High-Low Annual Seasonal Payments</h4>
            <ul>
                <li>Payments adapted to each company's annual cycle</li>
                <li>Higher payments during high-revenue seasons</li>
                <li>Lower payments during low-revenue seasons</li>
                <li><strong>Benefit:</strong> Aligned with business cash flow</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <h3>4️⃣ Simple Credit with Mortgage Guarantee</h3>
            <h4>Working Capital Financing</h4>
            <ul>
                <li>Secured by real estate collateral</li>
                <li>Provides additional working capital</li>
                <li>Flexible terms and conditions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Business verticals
    st.markdown("---")
    st.markdown('<div class="section-header">Business Verticals</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h4>🚚 Transportation Equipment</h4>
            <ul>
                <li>Commercial vehicles</li>
                <li>Fleet financing</li>
                <li>Specialized transport</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
            <h4>🏭 Industrial Equipment</h4>
            <ul>
                <li>Manufacturing machinery</li>
                <li>Production equipment</li>
                <li>Specialized tools</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="success-box">
            <h4>🏥 Medical Equipment</h4>
            <ul>
                <li>Hospital equipment</li>
                <li>Diagnostic devices</li>
                <li>Treatment systems</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Added value diagram
    st.markdown("---")
    st.markdown('<div class="section-header">Our Added Value Approach</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
        <h3 style="color: white; text-align: center;">6 Pillars of Added Value</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>⚡ Opportunity</h4>
            <ul>
                <li>Fast and responsible responses</li>
                <li>We look for the "YES" in every operation</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <h4>🤝 Relationships</h4>
            <ul>
                <li>Long-term relationships based on trust</li>
                <li>Honesty and integrity</li>
                <li>Highly reliable personnel</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>🏗️ Structure</h4>
            <ul>
                <li>Study and propose options that make clients successful</li>
                <li>Product, term, down payment, guarantees, co-signer</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <h4>🎯 Service</h4>
            <ul>
                <li>Each client has unique needs</li>
                <li>Customized solutions</li>
                <li>Dedicated time and attention</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>💰 Price</h4>
            <ul>
                <li>Differentiated rates by: term, credit bureau, client risk profile</li>
                <li>Capital grace options</li>
                <li>Term for initial payments</li>
            </ul>
        </div>
        
        <div class="feature-card">
            <h4>➕ Other Benefits</h4>
            <ul>
                <li>Electronic account statements</li>
                <li>Electronic invoicing</li>
                <li>Single reference number</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ========================================================================
# PAGE 5: PRODUCTS & TIMELINE
# ========================================================================
elif page == "📦 Products & Timeline":
    st.markdown('<div class="sub-header">Products and Services</div>', unsafe_allow_html=True)
    
    # APP Renta leasing details
    st.markdown('<div class="section-header">🚗 APP Renta (Pure Leasing) - Full Service</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h4>Complete Vehicle Management Solution</h4>
        <p>All-inclusive leasing with maintenance, insurance, and support services across all of Mexico</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Service details table
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>📍 Coverage</h4>
            <p><strong>All of Mexico</strong></p>
            <p>Wired or Wireless GPS</p>
        </div>
        
        <div class="feature-card">
            <h4>🚘 Auto Pool</h4>
            <p><strong>Jetta or Sentra</strong></p>
            <p>Fleet ≥30 units: Free for 30 natural days</p>
            <p>Delivery in 48 hrs (Metro) or 96 hrs (Interior)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        | **Service** | **Details** |
        |-------------|-------------|
        | **🛰️ GPS** | Wired or Wireless • Cash or Financed • Annual adjustment with lower renewal cost |
        | **🛡️ Insurance** | Cash or Financed • Annual payment in February |
        | **🚗 Registration** | Annual payment included |
        | **🔧 Preventive Maintenance** | According to service booklet • At agency up to 60,000 km • Based on client's vehicle policy |
        | **🔨 Corrective Maintenance** | Based on client's vehicle policy |
        | **🔩 Tires** | Change at 50-60K km |
        | **🔋 Battery** | Change at 30-40K km |
        | **📋 Management Services** | Fine payments • Vehicle detained • License plate changes • Etc. |
        """)
    
    # Process timeline
    st.markdown("---")
    st.markdown('<div class="section-header">⏱️ Application Process Timeline</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="success-box">
        <h3>Fast Pre-Approval: 48 Hours</h3>
        <p>We guarantee a response to your credit application within 2 business days</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Timeline visualization
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>Day 1</h4>
            <h5>📝 Application</h5>
            <ul>
                <li>Submit 3 required documents</li>
                <li>Complete credit application</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>Day 2</h4>
            <h5>🔍 Review</h5>
            <ul>
                <li>Credit analysis</li>
                <li>Risk assessment</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>Day 3</h4>
            <h5>✅ Pre-Approval</h5>
            <ul>
                <li>Credit decision</li>
                <li>Terms and conditions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <h4>Day 4-5</h4>
            <h5>📄 Documentation</h5>
            <ul>
                <li>Contract preparation</li>
                <li>Funding arrangement</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Required documents
    st.markdown("---")
    st.markdown('<div class="section-header">📋 Required Documents</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-box">
            <h4>1. Company Information</h4>
            <ul>
                <li>Business registration</li>
                <li>Tax ID (RFC)</li>
                <li>Legal representative ID</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <h4>2. Financial Information</h4>
            <ul>
                <li>Recent bank statements</li>
                <li>Financial statements</li>
                <li>Tax returns</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-box">
            <h4>3. Equipment Details</h4>
            <ul>
                <li>Equipment quotation</li>
                <li>Specifications</li>
                <li>Purpose of use</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Flexible terms
    st.markdown("---")
    st.markdown("""
    <div class="highlight-box">
        <h2 style="color: white; text-align: center;">Flexible Financing Terms</h2>
        <div style="display: flex; justify-content: space-around; margin-top: 30px;">
            <div style="text-align: center;">
                <h1 style="color: white;">12-60</h1>
                <p style="color: white;">Months Terms Available</p>
            </div>
            <div style="text-align: center;">
                <h1 style="color: white;">2-25%</h1>
                <p style="color: white;">Down Payment Range</p>
            </div>
            <div style="text-align: center;">
                <h1 style="color: white;">$20M</h1>
                <p style="color: white;">Maximum Amount per Client</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ========================================================================
# PAGE 6: KEY BENEFITS
# ========================================================================
elif page == "📊 Key Benefits":
    st.markdown('<div class="sub-header">Key Benefits Summary</div>', unsafe_allow_html=True)
    
    # Best option banner
    st.markdown("""
    <div class="highlight-box">
        <h2 style="color: white; text-align: center;">The Best Option to Power Your Business</h2>
        <h4 style="color: white; text-align: center; margin-top: 20px;">
        Activating and Driving Your Business Forward
        </h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Main benefits
    st.markdown('<div class="section-header">Why Partner with FINACTIV</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
            <h3>🚀 Fast & Flexible Solutions</h3>
            <p>We adapt our products to your specific needs with agile and efficient processes</p>
            <ul>
                <li>Pre-approval in 48 hours</li>
                <li>Simple application with 3 documents</li>
                <li>Flexible terms and structures</li>
                <li>Fixed or variable rates</li>
            </ul>
        </div>
        
        <div class="success-box">
            <h3>🎯 Personalized Attention</h3>
            <p>An expert executive will accompany you throughout the entire process</p>
            <ul>
                <li>Dedicated account manager</li>
                <li>24/7 client support</li>
                <li>Guaranteed satisfaction</li>
                <li>Long-term relationships</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="success-box">
            <h3>🗺️ National Coverage</h3>
            <p>To serve you wherever your business requires</p>
            <ul>
                <li>All Mexico coverage</li>
                <li>Regional presence</li>
                <li>Fast response times</li>
                <li>Local market knowledge</li>
            </ul>
        </div>
        
        <div class="success-box">
            <h3>💯 100% Mexican Company</h3>
            <p>Understanding and supporting Mexican businesses</p>
            <ul>
                <li>15+ years of experience</li>
                <li>500+ satisfied clients</li>
                <li>Made with passion for Mexico</li>
                <li>BBB+ credit rating</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Comprehensive services
    st.markdown("---")
    st.markdown('<div class="section-header">Our Complete Service Portfolio</div>', unsafe_allow_html=True)
    
    tabs = st.tabs(["Financial Products", "Value Options", "Industries Served", "Support Services"])
    
    with tabs[0]:
        st.markdown("""
        <div class="info-box">
            <h4>💰 Financial Products</h4>
            <ul>
                <li><strong>Simple Credit:</strong> Traditional term loans for equipment purchase</li>
                <li><strong>Financial Leasing:</strong> Lease-to-own option with residual value</li>
                <li><strong>Pure Leasing (APP Renta):</strong> Full-service operational leasing</li>
                <li><strong>Mortgage-Backed Credit:</strong> Working capital secured by real estate</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.markdown("""
        <div class="info-box">
            <h4>✨ Value-Added Options</h4>
            <ul>
                <li><strong>Capital Grace Period (MGC):</strong> Up to 6 months payment deferral</li>
                <li><strong>Initial Payment Terms:</strong> 1-3 months interest-free for down payment</li>
                <li><strong>Seasonal Payments:</strong> High-Low payment structure aligned with cash flow</li>
                <li><strong>Flexible Terms:</strong> 12-60 months + grace periods</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[2]:
        st.markdown("""
        <div class="info-box">
            <h4>🏭 Industries We Serve</h4>
            <ul>
                <li><strong>Transportation:</strong> Commercial vehicles, fleet management</li>
                <li><strong>Industrial:</strong> Manufacturing equipment, production machinery</li>
                <li><strong>Medical:</strong> Hospital equipment, diagnostic devices</li>
                <li><strong>Company Sizes:</strong> Small, Medium, Large, Multinational</li>
                <li><strong>Minimum Sales:</strong> $10 million MXN annually</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with tabs[3]:
        st.markdown("""
        <div class="info-box">
            <h4>🛠️ Support Services</h4>
            <ul>
                <li><strong>Training:</strong> Initial and quarterly training for partner teams</li>
                <li><strong>On-site Visits:</strong> Regular plant/office presence</li>
                <li><strong>Joint Client Visits:</strong> Support for prospect meetings</li>
                <li><strong>Digital Tools:</strong> Online quotation calculators, marketing materials</li>
                <li><strong>Account Management:</strong> Electronic statements, single reference number</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Success metrics
    st.markdown("---")
    st.markdown('<div class="section-header">Partnership Success Metrics</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-box" style="text-align: center;">
            <div class="stat-number">2x</div>
            <div class="stat-label">Sales in 12 Months</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-box" style="text-align: center;">
            <div class="stat-number">5x</div>
            <div class="stat-label">Sales in 4 Years</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-box" style="text-align: center;">
            <div class="stat-number">48h</div>
            <div class="stat-label">Pre-Approval Time</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-box" style="text-align: center;">
            <div class="stat-number">$20M</div>
            <div class="stat-label">Max per Client</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Client testimonial section
    st.markdown("---")
    st.markdown("""
    <div class="highlight-box">
        <h2 style="color: white; text-align: center;">Joining Forces</h2>
        <h4 style="color: white; text-align: center; margin-top: 20px;">
        To Offer Complete and Timely Financial Solutions
        </h4>
        <p style="color: white; text-align: center; font-size: 18px; margin-top: 20px;">
        Our vendor partners benefit from increased sales, improved customer loyalty, and enhanced margins—all with zero capital requirements.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ========================================================================
# PAGE 7: CONTACT
# ========================================================================
elif page == "📞 Contact":
    st.markdown('<div class="sub-header">Contact Information</div>', unsafe_allow_html=True)
    
    # Main contact info
    st.markdown("""
    <div class="highlight-box">
        <h2 style="color: white; text-align: center;">Let's Connect</h2>
        <h4 style="color: white; text-align: center; margin-top: 20px;">
        Ready to grow your business with flexible financing solutions?
        </h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact details
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-box">
            <h3>🏢 Corporate Office - Toluca</h3>
            <p><strong>Address:</strong></p>
            <p>Avenida Independencia 1900A<br>
            Zona Industrial<br>
            Toluca, Estado de México<br>
            C.P. 50071</p>
            
            <p><strong>📞 Phone:</strong><br>
            (722) 211 50 86</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-box">
            <h3>🌐 Online Presence</h3>
            <p><strong>Website:</strong><br>
            <a href="http://www.finactiv.com.mx" target="_blank">www.finactiv.com.mx</a></p>
            
            <p><strong>Social Media:</strong><br>
            Follow us on social networks for updates, tips, and financial solutions</p>
            
            <p><strong>Online Tools:</strong><br>
            • Quotation Calculator<br>
            • Client Portal<br>
            • Application Forms</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Next steps
    st.markdown('<div class="section-header">Next Steps</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>1️⃣ Schedule a Meeting</h4>
            <p>Contact us to arrange an initial consultation</p>
            <ul>
                <li>Discuss your needs</li>
                <li>Review partnership options</li>
                <li>Q&A session</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>2️⃣ Working Session</h4>
            <p>Define program details together</p>
            <ul>
                <li>Products and pricing</li>
                <li>Incentive structure</li>
                <li>Marketing support</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>3️⃣ Launch Partnership</h4>
            <p>Begin our successful collaboration</p>
            <ul>
                <li>Team training</li>
                <li>System integration</li>
                <li>Start funding clients</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # CTA
    st.markdown("---")
    st.markdown("""
    <div class="success-box">
        <h3 style="text-align: center;">Ready to Get Started?</h3>
        <p style="text-align: center; font-size: 18px; margin-top: 20px;">
        Contact us today to discuss how FINACTIV can help grow your business through our Vendor Program
        </p>
        <p style="text-align: center; margin-top: 30px;">
            <strong style="font-size: 24px;">📞 (722) 211 50 86</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Our clients
    st.markdown("---")
    st.markdown('<div class="section-header">Our Satisfied Clients</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.markdown("#### We're Proud to Serve:")
    st.markdown("""
    Over 500 small and medium-sized businesses across Mexico trust FINACTIV for their financing needs. 
    Our clients span multiple industries including transportation, manufacturing, and healthcare.
    """)
    st.markdown("**Join our growing list of successful partnerships!**")
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; padding: 20px;">
    <p><strong>FINACTIV - Vendor Program Presentation</strong></p>
    <p>© 2025 FINACTIV. All rights reserved.</p>
    <p>November 2025 | Version 1.0</p>
</div>
""", unsafe_allow_html=True)
