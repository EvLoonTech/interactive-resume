import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Evan Looney | Interactive Resume", page_icon="📈", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.title("Evan Michael Looney")
    
    # Multiple Locations Added Here
    st.write("📍 **Current:** Somerville, MA")
    st.write("📍 **Home:** North Haven, CT")
    
    st.divider()
    st.write("📞 203-893-8872")
    st.write("🎓 Tufts University | Expected May 2027")
    st.write("📈 Cumulative GPA: 3.63/4, Dean’s List (All Semesters)")
    
    st.divider()
    st.write("✉️ **Email:** evan.looney@tufts.edu")
    st.write("✉️ **Secondary Email:** evlooney@gmail.com")
    st.write("🔗 **LinkedIn:** [www.linkedin.com/in/evan-looney](https://www.linkedin.com/in/evan-looney)")
    st.write("🔗 **GitHub:** [Your GitHub Link](#)")
    
    st.divider()
    st.download_button(
        label="📄 Download Standard PDF",
        data="PDF_PLACEHOLDER",
        file_name="Evan_Looney_Resume.pdf",
        mime="application/pdf"
    )

# --- HEADER SECTION ---
st.title("Evan Michael Looney")
st.subheader("Applied Mathematics | Data Modeling | Actuarial Science")
st.write("""
Welcome to my interactive resume. I am a senior at Tufts University studying Applied Mathematics with a minor in French. 
I specialize in leveraging Python and Excel to build robust financial and statistical models. This site is an exploratory space 
where I showcase my professional background, technical projects, and personal interests.
""")

st.divider()

# --- MAIN CONTENT TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["💼 Experience", "📊 Projects & Skills", "🎓 Education", "🎧 Interests & Leadership"])

# --- TAB 1: EXPERIENCE ---
with tab1:
    st.header("Professional Experience")
    
    st.subheader("Teaching Assistant Grader, MATH 0021: Introduction to Statistics")
    st.caption("Tufts University Department of Mathematics | Fall 2026")
    st.write("- Evaluate undergraduate statistical coursework and provide structured, detailed feedback.")
    
    st.subheader("Quality Control Inspector & Machine Operator")
    st.caption("HPI Manufacturing, Inc. (Hamden, CT) | May 2025 – Current")
    st.write("- Operated CNC machinery & performed detailed quality control inspections, ensuring that products strictly adhered to technical specifications and quality standards.")
    st.write("- Applied analytical judgment and close attention to detail to identify defects and root causes, maintaining production accuracy and reducing rework.")
    st.write("- Managed B2B customer relationships and coordinated shipment logistics to ensure accurate, on-time order fulfillment.")
    st.write("- Gained hands on exposure to operational and financial due diligence through customer interactions, shipment coordination, and internal process review.")

    st.subheader("Homework Helper")
    st.caption("Community Action Partners (Medford, MA) | September 2024 – Present")
    st.write("- Assisted 30+ local middle school students with homework & exam preparation, motivating strong academic outcomes & confidence.")
    st.write("- Tailored explanations and strategies to individual learning styles.")
    st.write("- Ensured student productivity between dismissal & parent/guardian pickup.")
    
    st.subheader("Committee Intern")
    st.caption("North Haven Democratic Town Committee (North Haven, CT) | Jul 2021 – Oct 2021")
    st.write("- Supported local political committee operations and administration.")

# --- TAB 2: PROJECTS & SKILLS ---
with tab2:
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.header("Technical Projects")
        st.subheader("Health Plan Pricing Model")
        st.write("""
        Developed a comprehensive pricing model using Python and Microsoft Excel to simulate health insurance claim 
        frequency and severity distributions. The model calculates key plan metrics and evaluates deductible structures.
        """)
        
        with st.expander("Try a Mini Simulation: Claim Severity Distribution"):
            st.write("Adjust the slider to see how a simulated distribution of claims shifts.")
            severity = st.slider("Mean Claim Severity ($)", min_value=1000, max_value=10000, value=5000, step=500)
            
            np.random.seed(42)
            mu = np.log(severity) - (0.5 * 0.5**2) 
            synthetic_claims = np.random.lognormal(mean=mu, sigma=0.5, size=1000)
            
            chart_data = pd.DataFrame(synthetic_claims, columns=["Claim Amount"])
            st.area_chart(chart_data["Claim Amount"].head(50)) 
            
    with col2:
        st.header("Technical Skills")
        st.write("- **Programming Languages:** Python (NumPy, SciPy, Pandas, Matplotlib), MATLAB (Linear Programming).")
        st.write("- **Software:** Advanced Excel (Pivot Tables, VLOOKUP, Data Filtering), Microsoft Office, Google Drive, AI.")
        st.write("- **Languages:** French.")

# --- TAB 3: EDUCATION ---
with tab3:
    st.header("Education & Certifications")
    
    st.subheader("Tufts University")
    st.write("**BS Applied Mathematics, Minor French** | Expected May 2027")
    st.write("- **Relevant Coursework:** Statistics & Probability, Mathematical Modeling, Linear Algebra, Data Analysis.")
    
    st.subheader("Université Paris Cité")
    st.write("**Tufts In Paris Study Abroad Program** | Spring 2026")
    st.write("- Immersed in French language and culture while studying in Paris.")
    
    st.divider()
    
    st.subheader("Actuarial Exams")
    st.write("🏆 **SOA Exam P (Probability):** Passed – September 2026")
    st.write("⏳ **SOA Exam FM (Financial Mathematics):** Sitting – Early 2027")

    st.divider()

    st.subheader("Additional Education")
    st.write("**University of Pennsylvania (Coursera)** | Jun 2021 - Jul 2021")
    st.write("- An Introduction to American Law.")

# --- TAB 4: INTERESTS & LEADERSHIP ---
with tab4:
    colA, colB = st.columns(2)
    with colA:
        st.header("Leadership Experience")
        
        st.subheader("Lead Evaluator")
        st.caption("FPSP of CT | Oct 2019 – May 2023")
        st.write("- Graded & provided detailed feedback on submissions from 120+ junior-middle division competitors (ages 8-14) participating in Future Problem Solving Program of Connecticut.")
        st.write("- Led 15+ fellow evaluators in completing the grading process & adequately critiquing work.")
        
        st.subheader("Court Leader")
        st.caption("ACEing Autism | May 2021 – Jun 2023")
        st.write("- Coached tennis to children on the autism spectrum.")
        st.write("- Worked on communication skills between participants, encouraging collaborations.")
        st.write("- Supervised 10+ volunteers in completing activities effectivelys.")

        st.subheader("High School Leadership & Honors")
        st.write("- Class of 2023 Treasurer.")
        st.write("- Memberships: Mu Alpha Theta, French Honor Society, National Honor Society, Science Honor Society, Student Council, Math Team, Diversity Team.")
        st.write("- Awards: Rensallear Polytechnic Institute Medal (May 2022), Society of Women's Engineers Certificate (May 2022), SCC Scholar Athlete (Jun 2022).")

    with colB:
        st.header("Beyond Work and Acadamics")
        
        # Subheaders added to categorize interests
        st.subheader("Entertainment")
        st.write("**Video Games:** Been playing Xbox, Nintendo, and mobile games of all sorts since 2014. Especially love single players, sandboxes, and select indie games and single player FPS's")
        st.write("**Shows:** I love shows when I can actually get into them. I've seen A LOT of anime...")
        st.write("**Sports:** Diehard UCONN basketball fam. Longtime NBA and NFL fan. Fantasy Football expert. Love watching pro tennis.")
    
        st.subheader("Active")
        st.write("**Dog:** Hanging out with my 8-year-old cockapoo Atticus. Dogs > Humans")
        st.write("**Tennis and Pickleball:** Still always enjoy any oppurtunity I get to play racquet sports.")
        
        st.subheader("Works in progress")
        st.write("**Cooking:** Grillmaster exploring baking and stovetop cooking.")
        st.write("**Running:** Logging miles, running intervals.")
        st.write("**Music Production:** Chopping soul samples and producing boom bap/hip-hop beats in Logic Pro X and GarageBand.")
        st.write("**Jounaling:** I'm huge on mental health and have been committed to journalling since Summer 2026.")