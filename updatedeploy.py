import streamlit as st

# Dummy database
users_db = {}
session_state = {"logged_in_user": None}

def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users_db and users_db[username] == password:
            session_state["logged_in_user"] = username
            st.success("Login successful")
            main_page()
        else:
            st.error("Invalid username or password")

    if st.button("Register"):
        register_page()

def register_page():
    st.title("Register")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if username in users_db:
            st.error("Username already exists")
        else:
            users_db[username] = password
            st.success("Registration successful")
            login_page()

def main_page():
    if not session_state["logged_in_user"]:
        login_page()
        return

    st.title(f"Welcome, {session_state['logged_in_user']}!")

    skill = st.selectbox("Select your skill", ["Programming", "Data Analysis", "Design", "Marketing", "Management", "Engineering"])
    certificate = st.selectbox("Select your certificate", ["None", "PMP", "AWS Certified", "Cisco Certified", "Google Analytics"])
    degree = st.selectbox("Select your degree", ["None", "Bachelor's", "Master's", "PhD"])

    if st.button("Get Job Recommendations"):
        recommendations = get_job_recommendations(skill, certificate, degree)
        if recommendations:
            st.success(f"Recommended Jobs:\n" + "\n".join(recommendations))
        else:
            st.error("No recommendations found.")

    if st.button("Logout"):
        session_state["logged_in_user"] = None
        login_page()

def get_job_recommendations(skill, certificate, degree):
    job_recommendations = {
        "Programming": [
            {"job": "Software Developer", "certificates": ["None"], "degrees": ["Bachelor's", "Master's"]},
            {"job": "Web Developer", "certificates": ["None"], "degrees": ["Bachelor's"]},
            {"job": "Backend Developer", "certificates": ["AWS Certified"], "degrees": ["Bachelor's", "Master's"]},
            {"job": "Mobile App Developer", "certificates": ["None"], "degrees": ["Bachelor's"]}
        ],
        "Data Analysis": [
            {"job": "Data Scientist", "certificates": ["None"], "degrees": ["Master's", "PhD"]},
            {"job": "Data Analyst", "certificates": ["Google Analytics"], "degrees": ["Bachelor's"]},
            {"job": "Business Analyst", "certificates": ["None"], "degrees": ["Bachelor's", "Master's"]},
            {"job": "Data Engineer", "certificates": ["AWS Certified"], "degrees": ["Bachelor's"]}
        ],
        "Design": [
            {"job": "Graphic Designer", "certificates": ["None"], "degrees": ["None", "Bachelor's"]},
            {"job": "UX/UI Designer", "certificates": ["None"], "degrees": ["Bachelor's"]},
            {"job": "Product Designer", "certificates": ["None"], "degrees": ["Bachelor's"]},
            {"job": "Web Designer", "certificates": ["None"], "degrees": ["None", "Bachelor's"]}
        ],
        "Marketing": [
            {"job": "Marketing Specialist", "certificates": ["Google Analytics"], "degrees": ["Bachelor's"]},
            {"job": "Social Media Manager", "certificates": ["None"], "degrees": ["None", "Bachelor's"]},
            {"job": "Content Strategist", "certificates": ["None"], "degrees": ["Bachelor's"]},
            {"job": "SEO Specialist", "certificates": ["Google Analytics"], "degrees": ["None", "Bachelor's"]}
        ],
        "Management": [
            {"job": "Project Manager", "certificates": ["PMP"], "degrees": ["Bachelor's", "Master's"]},
            {"job": "Product Manager", "certificates": ["None"], "degrees": ["Bachelor's", "Master's"]},
            {"job": "Operations Manager", "certificates": ["None"], "degrees": ["Bachelor's", "Master's"]},
            {"job": "Team Leader", "certificates": ["None"], "degrees": ["None", "Bachelor's"]}
        ],
        "Engineering": [
            {"job": "Mechanical Engineer", "certificates": ["None"], "degrees": ["Bachelor's", "Master's"]},
            {"job": "Civil Engineer", "certificates": ["None"], "degrees": ["Bachelor's", "Master's"]},
            {"job": "Electrical Engineer", "certificates": ["None"], "degrees": ["Bachelor's", "Master's"]},
            {"job": "Structural Engineer", "certificates": ["None"], "degrees": ["Bachelor's", "Master's"]}
        ]
    }

    matched_jobs = []
    for job in job_recommendations.get(skill, []):
        if certificate in job["certificates"] and degree in job["degrees"]:
            matched_jobs.append(job["job"])

    return matched_jobs

if __name__ == "__main__":
    if session_state["logged_in_user"]:
        main_page()
    else:
        login_page()

