import streamlit as st
import pandas as pd
import time

# ========== CONFIGURATION ==========
st.set_page_config(
    page_title="TechSolutions Inc.",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== STYLE ==========
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# ========== DATA ==========
products = pd.DataFrame({
    "Product": ["Business Pro Software", "AI Analytics Suite", "Cloud Storage Package"],
    "Price": [299.99, 499.99, 149.99],
    "Rating": [4.8, 4.9, 4.6],
    "In Stock": [True, True, True],
    "Description": [
        "Complete business management solution with CRM, accounting, and inventory",
        "Advanced AI-powered data analysis and visualization tools",
        "Secure cloud storage with 1TB space and team collaboration features"
    ],
    "Image": [
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
        "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=765&q=80",
        "https://images.unsplash.com/photo-1639762681057-408e52192e55?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1632&q=80"
    ]
})

team_members = [
    {
        "name": "Alex Johnson",
        "role": "CEO & Founder",
        "bio": "20+ years in tech industry, founded 3 successful startups",
        "image": "https://images.unsplash.com/photo-1560250097-0b93528c311a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80"
    },
    {
        "name": "Sam Lee",
        "role": "CTO",
        "bio": "AI/ML expert with PhD in Computer Science from MIT",
        "image": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80"
    },
    {
        "name": "Taylor Smith",
        "role": "Marketing Director",
        "bio": "Digital marketing strategist with 10 years experience",
        "image": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
    }
]

# ========== PAGES ==========
def home_page():
    # Hero Section
    st.image("https://images.unsplash.com/photo-1467232004584-a241de8bcf5d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1169&q=80",
            use_container_width=True)
    
    st.title("Innovative Technology Solutions")
    st.subheader("Empowering Your Business with Cutting-Edge Software")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ## Transforming Businesses Through Technology
        
        At TechSolutions Inc., we develop software that helps businesses:
        - Streamline operations
        - Make data-driven decisions
        - Enhance team collaboration
        - Scale efficiently
        
        Our solutions are trusted by over 5,000 companies worldwide.
        """)
        
        if st.button("Explore Our Products", type="primary"):
            st.session_state.page = "products"
            st.rerun()
    
    with col2:
        st.image("https://images.unsplash.com/photo-1499951360447-b19be8fe80f5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
               caption="Our team developing the next generation of business software",
               use_container_width=True)
    
    # Features Section
    st.markdown("---")
    st.header("Why Choose Our Solutions")
    
    features = st.columns(3)
    with features[0]:
        st.image("https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
               caption="Comprehensive Features",
               use_container_width=True)
        st.subheader("All-in-One Platform")
        st.write("Integrated solutions that cover all your business needs")
    
    with features[1]:
        st.image("https://images.unsplash.com/photo-1620712943543-bcc4688e7485?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=765&q=80",
               caption="AI-Powered Analytics",
               use_container_width=True)
        st.subheader("Smart Insights")
        st.write("AI-driven analytics to uncover valuable business insights")
    
    with features[2]:
        st.image("https://images.unsplash.com/photo-1639762681057-408e52192e55?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1632&q=80",
               caption="Cloud Technology",
               use_container_width=True)
        st.subheader("Cloud-Based")
        st.write("Access your data securely from anywhere, anytime")

def products_page():
    st.title("Our Products")
    st.markdown("Discover solutions designed to transform your business operations")
    
    # Featured Products
    st.header("Featured Products")
    for _, row in products.iterrows():
        with st.container():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(row["Image"], use_container_width=True)
            with col2:
                st.subheader(row["Product"])
                st.markdown(f"**Price:** ${row['Price']} | **Rating:** {row['Rating']} ⭐")
                st.write(row["Description"])
                
                if st.button("View Details", key=f"view_{row['Product']}"):
                    st.session_state.selected_product = row['Product']
                    st.session_state.page = "product_detail"
                    st.rerun()
            
            st.markdown("---")
    
    # Product Categories
    st.header("Product Categories")
    categories = st.columns(3)
    with categories[0]:
        st.image("https://images.unsplash.com/photo-1555774698-0b77e0d5fac6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
               caption="Business Software",
               use_container_width=True)
        st.subheader("Business Solutions")
        st.write("Complete packages for enterprise management")
    
    with categories[1]:
        st.image("https://images.unsplash.com/photo-1622675363311-3e1904dc1885?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
               caption="Data Analytics",
               use_container_width=True)
        st.subheader("Data & Analytics")
        st.write("Powerful tools for data visualization and analysis")
    
    with categories[2]:
        st.image("https://images.unsplash.com/photo-1626785774573-4b799315345d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1171&q=80",
               caption="Cloud Services",
               use_container_width=True)
        st.subheader("Cloud Services")
        st.write("Secure and scalable cloud infrastructure")

def product_detail_page():
    if 'selected_product' not in st.session_state:
        st.session_state.page = "products"
        st.rerun()
    
    product = products[products['Product'] == st.session_state.selected_product].iloc[0]
    
    st.title(product['Product'])
    st.markdown(f"**Price:** ${product['Price']} | **Rating:** {product['Rating']} ⭐")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(product["Image"], use_container_width=True)
    with col2:
        st.subheader("Product Description")
        st.write(product["Description"])
        
        st.subheader("Key Features")
        st.markdown("""
        - Feature 1: Lorem ipsum dolor sit amet
        - Feature 2: Consectetur adipiscing elit
        - Feature 3: Sed do eiusmod tempor
        - Feature 4: Incididunt ut labore et dolore
        """)
        
        if st.button("Add to Cart", type="primary"):
            st.success("Added to cart!")
            time.sleep(1)
    
    st.markdown("---")
    st.subheader("Technical Specifications")
    st.table(pd.DataFrame({
        "Specification": ["System Requirements", "Supported Platforms", "License Type", "Version"],
        "Details": ["Windows 10+, macOS 10.15+, Linux", "Desktop, Web, Mobile", "Annual Subscription", "3.2.1"]
    }))
    
    st.button("Back to Products", on_click=lambda: st.session_state.update({"page": "products"}))

def about_page():
    st.title("About TechSolutions Inc.")
    st.image("https://images.unsplash.com/photo-1522071820081-009f0129c71c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
            use_container_width=True,
            caption="Our headquarters in San Francisco")
    
    st.header("Our Story")
    st.markdown("""
    Founded in 2010, TechSolutions Inc. began as a small startup with a vision to revolutionize business technology. 
    Today, we're a team of 150+ professionals serving clients across 30 countries.
    
    **Mission:** To empower businesses through innovative, user-friendly technology solutions.
    
    **Vision:** To be the global leader in business transformation software.
    """)
    
    st.markdown("---")
    st.header("Meet Our Leadership Team")
    
    cols = st.columns(len(team_members))
    for i, member in enumerate(team_members):
        with cols[i]:
            st.image(member["image"], width=200, use_container_width=True)
            st.subheader(member["name"])
            st.markdown(f"**{member['role']}**")
            st.write(member["bio"])
    
    st.markdown("---")
    st.header("Our Achievements")
    st.markdown("""
    - 🏆 **2023 Tech Innovator Award** - Silicon Valley Business Journal
    - 🏆 **Best Business Software** - Global Tech Awards 2022
    - 📈 **5,000+ satisfied clients** worldwide
    - 🌍 **30 countries** served across 5 continents
    """)

def contact_page():
    st.title("Contact Us")
    st.markdown("We'd love to hear from you! Reach out for inquiries, support, or partnership opportunities.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.header("Get In Touch")
        with st.form("contact_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            subject = st.selectbox("Subject", ["General Inquiry", "Product Support", "Partnership", "Feedback"])
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                if name and email and message:
                    st.success("Thank you for your message! We'll respond within 24 hours.")
                    time.sleep(2)
                    st.session_state.page = "home"
                    st.rerun()
                else:
                    st.error("Please fill all required fields")
    
    with col2:
        st.header("Our Offices")
        st.image("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
               caption="San Francisco Headquarters",
               use_container_width=True)
        
        st.subheader("Headquarters")
        st.markdown("""
        **Address:** 123 Tech Street, San Francisco, CA 94107  
        **Phone:** (555) 123-4567  
        **Email:** info@techsolutions.com  
        **Hours:** Mon-Fri 9:00 AM - 6:00 PM PST
        """)
        
        st.subheader("Regional Offices")
        st.markdown("""
        - New York
        - London
        - Singapore
        - Tokyo
        """)

# ========== MAIN APP ==========
def main():
    if 'page' not in st.session_state:
        st.session_state.page = "home"
    
    # Sidebar navigation
    with st.sidebar:
        st.image("https://images.unsplash.com/photo-1573164713988-8665fc963095?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1169&q=80",
                width=200,
                use_container_width=True)
        st.title("TechSolutions Inc.")
        
        st.markdown("---")
        if st.button("🏠 Home"):
            st.session_state.page = "home"
        if st.button("🛍️ Products"):
            st.session_state.page = "products"
        if st.button("ℹ️ About Us"):
            st.session_state.page = "about"
        if st.button("📩 Contact"):
            st.session_state.page = "contact"
        
        st.markdown("---")
        st.markdown("**Connect With Us**")
        st.markdown("[Twitter](https://twitter.com) | [LinkedIn](https://linkedin.com)")
        st.markdown("[Facebook](https://facebook.com) | [Instagram](https://instagram.com)")
        
        st.markdown("---")
        st.markdown("""
        **Customer Support**  
        support@techsolutions.com  
        +1 (555) 987-6543
        """)

    # Page routing
    if st.session_state.page == "home":
        home_page()
    elif st.session_state.page == "products":
        products_page()
    elif st.session_state.page == "product_detail":
        product_detail_page()
    elif st.session_state.page == "about":
        about_page()
    elif st.session_state.page == "contact":
        contact_page()

if __name__ == "__main__":
    main()