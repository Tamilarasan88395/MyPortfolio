import streamlit as st
from streamlit_option_menu import option_menu
from email.message import EmailMessage
from decouple import config
import smtplib

# Page configuration
st.set_page_config(
    page_title="Tamil Arasan SS - Portfolio", 
    page_icon="📊", 
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E86AB;
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #A23B72;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .contact-info {
        text-align: center;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Navigation menu
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Me", "Experience", "Projects", "Skills", "Contact"],
        icons=["house", "person-circle", "briefcase", "folder", "gear", "envelope"],
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#302b2b"},
            "icon": {"color": "#000000", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px"},
            "nav-link-selected": {"background-color": "#2E86AB"},
        }
    )

# Home Section
if selected == "Home":
    st.markdown('<h1 class="main-header">Tamil Arasan SS</h1>', unsafe_allow_html=True)
    st.markdown('<h2 class="sub-header">Software Developer | Data Analyst</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="contact-info">📧 tamilarasan88385@gmail.com | 📱 +91 8838547887</div>', unsafe_allow_html=True)
    
    st.write("---")

    # Professional summary
    st.title("Professional Summary")
    st.subheader("""
    Passionate Software Developer and Data Analyst with proven expertise in backend analytics statistical analysis, and data-driven decision making. Currently driving user engagement and productivity improvements at Resulticks Edge Solution Technologies through innovative analytical solutions and automated reporting systems.""")
    
    # Current role highlight
    st.info("🔥 **Currently:** Software Developer | Data Analytics at Resulticks Edge Solution Technologies, Chennai")

# About Me Section
elif selected == "About Me":
    st.title("About Me")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("D:/streamlit/assets_/profile.png", width=250)
        st.header("🎓 Education")
        st.write("**Bachelor of Commerce with Computer Application**")
        st.write("Sona College of Arts and Science")
        st.write("CGPA: 8.2 (Nov 2021 – May 2024)")
    
    with col2:
        st.header("Hello! I'm Tamil Arasan SS")
        st.write("""
        I'm a dedicated Software Developer and Data Analyst with a passion for transforming raw data 
        into actionable insights. With hands-on experience in backend analytics, statistical analysis, 
        and business intelligence, I specialize in developing solutions that drive measurable business impact.
        
        **What drives me:**
        - 📊 Creating data-driven solutions that improve business performance
        - 🔧 Building efficient backend systems and APIs
        - 📈 Developing interactive dashboards and analytical reports
        - 🎯 Solving complex business problems through innovative technology
        
        **My journey:**
        Started as a Data Analyst Intern and progressed to a Software Developer role, consistently 
        delivering projects that exceed performance expectations. I've led teams, conducted workshops, 
        and contributed to significant cost reductions and productivity improvements across organizations.
        """)
    
    st.write("---")
    
    # Certifications
    st.title("🏆 Certifications & Achievements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🐍 The Complete Python Pro Bootcamp (Udemy)**
        - May 2024
        - 100+ hands-on projects in data science, automation, and web development
        
        **📊 Google Data Analytics Professional Certificate**
        - January 2024
        - Comprehensive data analysis using Excel, SQL, R, and Tableau
        """)
    
    with col2:
        st.markdown("""
        **🗣️ Public Speaking & Workshops (March 2025)**
        - Conducted guest events on Data Analysis and Big Data
        - Live web application demos using Python, SQL, and Flask
        
        **📈 Microsoft Excel Certification**
        - September 2023
        - Advanced Excel functions, pivot tables, and visualization
        """)

# Experience Section
elif selected == "Experience":
    st.title("Professional Experience")
    
    # Current role
    st.subheader("Resulticks Edge Solution Technologies")
    st.write("**Software Developer (Backend Analytics)** | Chennai, Tamil Nadu | Jan 2025 – Present")
    st.write("""
    - 🎯 Developed ROI Analysis feature using statistical analysis techniques
    - 📊 Created Dynamic Analysis solutions using Pandas for advanced data manipulation
    - 🚀 Automated manual analytical reports through optimized SQL queries integrated with 3+ Flask APIs
    """)
    
    st.write("---")
    
    # Previous roles
    st.subheader("QBrainX Inc")
    st.write("**Data Analyst Intern** | Coimbatore, Tamil Nadu | Jun 2024 – Oct 2024")
    st.write("""
    - 📊 Analyzed 2+ million historical data records to identify patterns and forecast trends
    - 💹 Delivered 12% increase in sales and record-high profits
    - 📋 Created interactive Power BI dashboards for stakeholder decision-making
    """)
    
    st.write("---")
    
    st.subheader("Sona Star Innovation Private Limited")
    st.write("**Data Analyst Intern** | Salem, Tamil Nadu | Feb 2024 – Mar 2024")
    st.write("""
    - 💰 Achieved 25% cost reduction through strategic data analysis
    - 👥 Led team to collect, clean, and process 10,000+ hostel product records
    - 📊 Delivered 3 interactive Power BI dashboards
    """)

# Projects Section
elif selected == "Projects":
    st.title(" Projects")
    
    # Project 1
    st.subheader("Event Recommendation System")
    st.write("**September 2024**")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        **Objective:** Develop an intelligent system to recommend events based on user behavior patterns
        
        **Key Achievements:**
        - 📊 Analyzed 5,000+ event records to identify user behavior patterns
        - 🎯 Improved user engagement by 20% through accurate recommendations
        - 🔄 Implemented clustering algorithms for event categorization
        - 📈 Enhanced recommendation accuracy by 18%
        
        **Technologies Used:** Python, Scikit-Learn, Pandas, Machine Learning Algorithms
        """)
    
    with col2:
        st.metric("Events Analyzed", "5K+")
        st.metric("User Engagement", "↗️ 20%")
        st.metric("Accuracy Improvement", "↗️ 18%")
    
    st.write("---")
    
    # Project 2
    st.subheader("Customer Satisfaction Toward Smart Watches")
    st.write("**October 2023**")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        **Objective:** Analyze smartwatch adoption patterns and improve rural community engagement
        
        **Key Achievements:**
        - 👥 Led a team of 4 members across comprehensive market research
        - 📍 Conducted surveys across 5 locations
        - 📋 Collected 150+ responses on smartwatch usage patterns
        - 🏘️ Achieved 15% increase in smartwatch adoption in rural communities
        
        **Technologies Used:** Data Collection, Statistical Analysis, Power BI, Excel
        """)
    
    with col2:
        st.metric("Team Members", "4")
        st.metric("Survey Responses", "150+")
        st.metric("Rural Adoption", "↗️ 15%")
# Skills Section
elif selected == "Skills":
    st.header("Technical Skills & Expertise")
    
    # Technical Skills
    st.subheader("💻 Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Programming Languages**")
        st.progress(0.9)
        st.write("Python")
        st.progress(0.8)
        st.write("SQL")
        
        st.markdown("**Data Analysis & Visualization**")
        st.progress(0.9)
        st.write("Pandas, NumPy")
        st.progress(0.8)
        st.write("Power BI")
        st.progress(0.7)
        st.write("Excel")
    
    with col2:
        st.markdown("**Web Development & APIs**")
        st.progress(0.8)
        st.write("Flask, Django")
        st.progress(0.7)
        st.write("REST API")
        
        st.markdown("**Tools & Technologies**")
        st.progress(0.8)
        st.write("Git/GitHub")
        st.progress(0.7)
        st.write("Postman")
        st.progress(0.8)
        st.write("Scikit-Learn")
    
    st.write("---")
    
    # Soft Skills
    st.header("🤝 Soft Skills")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Communication & Leadership**
        - 🗣️ Data Storytelling
        - 👥 Team Leadership
        - 🎤 Public Speaking
        """)
    
    with col2:
        st.markdown("""
        **Analytical & Problem-Solving**
        - 🔍 Critical Thinking
        - 📊 Analytical Thinking
        - 🧩 Problem-Solving
        """)
    
    with col3:
        st.markdown("""
        **Collaboration & Productivity**
        - 🤝 Collaborative Teamwork
        - 📋 Project Management
        - 🎯 Goal-Oriented Approach
        """)
    
    st.write("---")
    
    # Skill Categories
    st.header("📊 Skill Categories")
    
    skills_data = {
        "Data Analysis": ["Python", "Pandas", "NumPy", "SQL", "Statistical Analysis"],
        "Visualization": ["Power BI", "Excel", "Dashboard Development", "Data Storytelling"],
        "Web Development": ["Flask", "Django", "REST API", "Backend Development"],
        "Machine Learning": ["Scikit-Learn", "Clustering Algorithms", "Predictive Modeling"],
        "Tools": ["Git/GitHub", "Postman", "MS Office Suite", "Google Workspace"]
    }
    
    for category, skills in skills_data.items():
        with st.expander(f"🔧 {category}"):
            st.write(", ".join(skills))

# Contact Section
elif selected == "Contact":

    sender_email = config('SENDER_EMAIL')
    sender_password = config('SENDER_PASSWORD')
    receiver_email = config('RECEIVER_EMAIL')

    st.title("Get In Touch")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📞 Contact Information")
        st.markdown("""
        **📧 Email:** tamilarasan88385@gmail.com
        
        **📱 Phone:** +91 8838547887
        
        **🌐 LinkedIn:** [Connect with me on LinkedIn](https://www.linkedin.com/in/tamilarasanss/)
        
        **💻 GitHub:** [Check out my projects](https://github.com/Tamilarasan88395)
        
        **📍 Location:** Chennai, Tamil Nadu, India
        """)
        
        st.header("🎯 Open to Opportunities")
        st.info("""
        I'm actively seeking opportunities in:
        - Backend Development
        - Data Analytics
        - Machine Learning
        - Business Intelligence
        """)
    
    with col2:
        st.header("💌 Send me a message")

        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message", height=150)

            submitted = st.form_submit_button("Send Message")

            if submitted:
                if name and email and message:
                    try:
                        msg = EmailMessage()
                        msg.set_content(f"From: {name} <{email}>\n\n{message}")
                        msg['Subject'] = subject
                        msg['From'] = sender_email
                        msg['To'] = receiver_email
                        msg['Reply-To'] = email

                        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                            smtp.login(sender_email, sender_password)
                            smtp.send_message(msg)

                        st.success("Thank you for your message! I'll get back to you soon.")
                        st.balloons()
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
                else:
                    st.error("Please fill in all required fields.")
    
    st.write("---")
    
    # Professional summary
    st.header("🚀 Let's Connect!")
    st.write("""
    I'm always interested in discussing new opportunities, collaborating on interesting projects, 
    or simply connecting with fellow professionals in the tech industry. Whether you're looking 
    for a data analyst, backend developer, or someone passionate about turning data into insights, 
    I'd love to hear from you!
    
    Feel free to reach out through any of the channels above. I typically respond within 24 hours.
    """)

# Footer
st.write("---")