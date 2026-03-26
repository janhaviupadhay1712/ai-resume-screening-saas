import streamlit as st
import requests


if "scores" not in st.session_state:
    st.session_state.scores = []

st.set_page_config(page_title="HireAI", layout="wide")

# ---------------------------
# CUSTOM CSS (DARK UI)
# ---------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0a0f2c, #12194a);
    color: white;
}

/* Sidebar text */
section[data-testid="stSidebar"] label {
    color: #ffffff !important;
    font-weight: 500;
}

/* Radio buttons text */
section[data-testid="stSidebar"] .stRadio label {
    color: #ffffff !important;
    font-size: 16px;
}

/* Selected item (Analytics etc.) */
section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label[data-checked="true"] {
    color: #00ffcc !important;
    font-weight: bold;
    text-shadow: 0 0 10px #00ffcc;
}

/* Hover effect */
section[data-testid="stSidebar"] .stRadio label:hover {
    color: #00ffcc !important;
    transition: 0.3s;

}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.markdown("## 🚀 AI Screener")

menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Match Resume", "Rank Candidates", "Analytics"],
    label_visibility="collapsed"
)

# ---------------------------
# DASHBOARD
# ---------------------------
if menu == "Dashboard":
    st.markdown("""
    <h1 style='
        font-size: 48px;
        font-weight: 800;
        color: ##0000cd;
        margin-bottom: 5px;
    '>
        🚀 HireAI
    </h1>

    <p style='
        font-size: 18px;
        color: #100c08;
        margin-bottom: 30px;
    '>
        Smart AI-powered Resume Screening Dashboard
    </p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    col1.metric("Resumes Processed", "2")
    col2.metric("Avg Match Score", "49%")
    col3.metric("Top Candidate Score", "47%")

# ---------------------------
# MATCH RESUME
# ---------------------------
elif menu == "Match Resume":

    st.markdown("## 📄 Match Resume")

    uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])
    job_desc = st.text_area("Job Description")

    if st.button("🚀 Analyze Match"):
        if uploaded_file and job_desc:

            with st.spinner("Analyzing..."):

                files = {"file": uploaded_file}
                data = {"job_description": job_desc}

                response = requests.post(
                    "http://127.0.0.1:8000/match-resume/",
                    files=files,
                    data=data
                )

                result = response.json()
                score = result["match_score_percent"]

                st.success(f"Match Score: {score}%")
                st.progress(int(score))

# ---------------------------
# RANK CANDIDATES
# ---------------------------
elif menu == "Rank Candidates":

    st.markdown("## 🏆 Rank Candidates")
    st.write("Upload resumes and rank them")

    uploaded_files = st.file_uploader(
        "Upload Resumes",
        type=["pdf"],
        accept_multiple_files=True
    )

    job_desc = st.text_area("Job Description")

    if st.button("⚡ Rank Candidates"):

        if uploaded_files and job_desc:

            with st.spinner("Ranking..."):

                files = [("files", f) for f in uploaded_files]
                data = {"job_description": job_desc}

                response = requests.post(
                    "http://127.0.0.1:8000/rank-resumes/",
                    files=files,
                    data=data
                )

                result = response.json()

                # ✅ STORE SCORES
                st.session_state.scores = [
                    round(item["score"], 2) for item in result["ranked_candidates"]
                ]
                st.write("Stored Scores:", st.session_state.scores)

                cols = st.columns(3)

                for i, item in enumerate(result["ranked_candidates"][:3]):
                    rank = ["1st", "2nd", "3rd"][i] if i < 3 else f"{i + 1}th"
                    with cols[i]:
                        st.markdown(f"""
                        <div style="background:#1b214f;padding:15px;border-radius:10px;text-align:center">
                            <h3><h3 style="
    color:#00ffcc;
    text-shadow: 0 0 10px #00ffcc, 0 0 20px #00ffcc;
">
    {rank}
</h3></h3>
                            <h4 style="
    color:#00ffcc;
    text-shadow: 0 0 8px #00ffcc;
">
    Candidate {i+1}
</h4>
                            <p style="color:#00ffcc;font-size:18px;">
                                {item['score']}%
                            </p>
                        </div>
                        """, unsafe_allow_html=True)
# ---------------------------
# ANALYTICS
# ---------------------------
elif menu == "Analytics":

    st.markdown("## 📈 Analytics Dashboard")

    scores = st.session_state.scores

    if not scores:
        st.warning("No data yet. Upload resumes first.")
    else:

        # ---------------------------
        # METRICS
        # ---------------------------
        col1, col2, col3 = st.columns(3)

        col1.metric("Total Candidates", len(scores))
        col2.metric("Average Score", f"{round(sum(scores)/len(scores), 2)}%")
        col3.metric("Top Score", f"{max(scores)}%")

        # ---------------------------
        # BAR CHART
        # ---------------------------
        st.markdown("### 📊 Candidate Scores")

        chart_data = {
            "Candidates": [f"C{i+1}" for i in range(len(scores))],
            "Scores": scores
        }

        st.bar_chart(chart_data, x="Candidates", y="Scores")

        # ---------------------------
        # PROGRESS BARS
        # ---------------------------
        st.markdown("### 🏆 Individual Performance")

        for i, score in enumerate(scores):
            st.write(f"Candidate {i+1}")
            st.progress(int(score))

        # ---------------------------
        # INSIGHTS
        # ---------------------------
        st.markdown("### 💡 Insights")

        avg = sum(scores)/len(scores)

        if max(scores) > 80:
            st.success("Top candidate is highly relevant 🎯")
        elif max(scores) > 60:
            st.info("Good candidates available 👍")
        else:
            st.warning("Low match candidates ⚠️")

        if avg < 50:
            st.warning("Average score is low — refine job description")