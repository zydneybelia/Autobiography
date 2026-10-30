import io
from datetime import date

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

MSG_FILE = "messages.csv"


def load_messages():
    try:
        return pd.read_csv(MSG_FILE).to_dict("records")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []


def save_messages(msgs):
    pd.DataFrame(msgs).to_csv(MSG_FILE, index=False)

# ------------------------------------------------------------------
# EDIT THESE FIRST  (everything marked "EDIT" is a stand-in for you)
# ------------------------------------------------------------------
NAME = "Jhon Zydney T. Belia"                     
SECTION = "CSIT 349 · Section G01"  
PROGRAM = "BS Information Technology · Year 4"  
GITHUB = "https://github.com/zydneybelia"
EMAIL = "zydneybelia@gmail.com"

st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------
# Styling
# ------------------------------------------------------------------
st.markdown(
    """
    
    <style>
   .hero {
    padding: .5rem 0 .5rem 1.4rem;
    background: transparent;
    border: none;
    border-left: 4px solid #6366f1;
    margin-bottom: 1rem;
}
.hero h1 { margin: 0; font-size: 2.6rem; }
.hero p  { margin: .3rem 0 0 0; font-size: 1.1rem; opacity: .8; }
.pill {
    display:inline-block; padding: 2px 12px; margin: 2px 4px 2px 0;
    border-radius: 999px; background: rgba(99,102,241,.15);
    border: 1px solid rgba(99,102,241,.45);
    font-size: .82rem; font-weight: 600;
}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# Data (EDIT the numbers to be honest about your own skills)
# ------------------------------------------------------------------
SKILLS = pd.DataFrame(
    {
        "Skill": ["Python", "JavaScript / React", "Java / Spring Boot",
                  "SQL / Supabase", "GitHub", "UI / Canva design"],
        "Category": ["Language", "Frontend", "Backend",
                     "Database", "Tools", "Design"],
        "Level": [75, 80, 70, 70, 80, 90],
        "Years": [2, 2, 2, 2, 2, 2],
    }
)

PROJECTS = [
    {
        "title": "QuickBite",
        "type": "Web + Mobile",
        "role": "Full-stack developer (group project, IT342_G5)",
        "tools": ["Spring Boot", "React", "Kotlin", "Supabase", "MySQL"],
        "desc": "A food ordering app with a web client and an Android client that share one backend API.",
        "outcome": "Working ordering flow across web and mobile for the course subject IT342 requirement.",
        "link": "https://github.com/zydneybelia/QuickBite_Belia",
        "progress": 90,
    },
    {
        "title": "JapLearn 2.0",
        "type": "Application",
        "role": "Developer/ Documentation(Capstone 2)",
        "tools": ["React", "JavaScript", "REST API"],
        "desc": "A learning system for Japanese: Hiragana, Katakana and basic vocabulary with practice activities.",
        "outcome": "Capstone prototype covering the kana charts and vocabulary practice.",
        "link": "https://github.com/rychfghg/JapLearn-2.0",
        "progress": 70,
    },
    {
        "title": "Notes Application",
        "type": "Web",
        "role": "Solo full-stack developer",
        "tools": ["React", "Vite", "Express.js", "Supabase"],
        "desc": "A notes app where users create, edit and delete notes, backed by an Express API.",
        "outcome": "Complete CRUD app with a React + Vite frontend and a hosted database.",
        "link": "https://github.com/zydneybelia/NotesApplication",
        "progress": 100,
    },
    {
        "title": "Loaner Request",
        "type": "Low-code",
        "role": "Developer",
        "tools": ["ServiceNow Studio", "GitHub"],
        "desc": "A custom ServiceNow application for requesting loaner equipment, linked to a GitHub repo.",
        "outcome": "Custom app built in ServiceNow Studio and version-controlled in Module4--AppDev.",
        "link": "https://github.com/zydneybelia/Module4--AppDev",
        "progress": 95,
    },

     {
        "title": "Wildcat-Watch",
        "type": "Web Application",
        "role": "Full-stack developer (Group Project)",
        "tools": ["Python", "Django", "Supabase", "PostgreSQL", "Render"],
        "desc": "A web-based security monitoring system with role-based access for administrators, security officers, and supervisors.",
        "outcome": "Developed a role-based security management application with a Django backend and Supabase database, deployed using Render.",
        "link": "https://github.com/WildcatWatch/Wildcat-Watch",
        "progress": 100,
    },
     
]

MILESTONES = pd.DataFrame(
    {
        "Year": [2022, 2023, 2024, 2025, 2026],
        "Milestone": [
            "Started my IT degree",              
            "Learned OOP in Java",       
            "Learned React and Express",         
            "Built QuickBite App for school project",
            "Capstone 2: JapLearn 2.0",
        ],
        "Impact": [20, 40, 55, 75, 90],
    }
)

# ------------------------------------------------------------------
# Session state
# ------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = load_messages()
if "visits" not in st.session_state:
    st.session_state.visits = 0
st.session_state.visits += 1


def make_avatar(initials: str, size: int = 400) -> Image.Image:
    """Clearly labeled stand-in photo. Replace with st.image('me.jpg')."""
    img = Image.new("RGB", (size, size))
    px = img.load()
    for y in range(size):
        for x in range(size):
            t = (x + y) / (2 * size)
            px[x, y] = (int(79 + 157 * t), int(70 + 20 * t), int(229 - 80 * t))
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", size // 3)
    except Exception:
        font = ImageFont.load_default()
    draw.text((size / 2, size / 2), initials, fill="white", font=font, anchor="mm")
    return img


# ------------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------------
with st.sidebar:
    st.image("me.jpg", width="stretch")
    st.markdown(f"### {NAME}")
    st.caption(f"{PROGRAM}\n\n{SECTION}")
    st.divider()

    st.subheader("⚙️ Customize the page")
    accent = st.color_picker("Chart accent color", "#6366f1")
    show_table = st.checkbox("Show raw data tables", value=True)
    skill_filter = st.multiselect(
        "Filter skill categories",
        options=sorted(SKILLS["Category"].unique()),
        default=sorted(SKILLS["Category"].unique()),
    )
    min_level = st.slider("Minimum skill level", 0, 100, 0, step=5)
    chart_kind = st.radio("Skills chart type", ["Bar", "Area", "Line"], horizontal=True)

    st.divider()
    st.link_button("🐙 My GitHub", GITHUB, width="stretch")
    st.caption(f"Page views this session: {st.session_state.visits}")

# ------------------------------------------------------------------
# Hero
# ------------------------------------------------------------------
st.markdown(
    f"""
    <div class="hero">
      <h1>👋 Hi, I'm {NAME}</h1>
      <p>Aspiring full-stack developer · web &amp; mobile · learner for life</p>
      <p style="font-size:.95rem; opacity:.85;">{PROGRAM} &nbsp;|&nbsp; {SECTION}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Projects", len(PROJECTS), "+2 this year")
m2.metric("Skills tracked", len(SKILLS))
m3.metric("Avg. skill level", f"{SKILLS['Level'].mean():.0f}%", "+8%")
m4.metric("Languages used", 4)

tab_about, tab_skills, tab_projects, tab_contact = st.tabs(
    ["📖 Autobiography", "📊 Skills", "💼 Portfolio", "✉️ Contact"]
)

# ------------------------------------------------------------------
# Tab 1: Autobiography
# ------------------------------------------------------------------
with tab_about:
    left, right = st.columns([2, 1], gap="large")
    with left:
        st.header("About Me")
        st.markdown(
            f"""
            I'm **{NAME}**, an IT student who likes to explore new ideas, and turn them into working apps.
            I mostly build **full-stack web** projects just like my QuickBite App. I usually work with a team or group,
            and I like the moment a feature that I'm working on finally runs.

            I live here in Cebu City where I most grew up. I knew about computers when I was a kid, but only the parts of it
            such as the keyboard, mouse, and monitor. I started learning programming when I was alreay in college.
            Until now, I still want to learn more about programming and how to make apps that can help people in their daily lives.
            """
        )
        st.subheader("Education")
        st.markdown(
            "- Cebu Institute of Technology (BSIT) — present\n"
            "- Cebu Institution of Technology (STEM) — 2020-2022\n"
            "- St. Paul College Foundation Inc. — 2016-2020"
        )
        st.subheader("Milestones")
        for _, r in MILESTONES.iterrows():
            st.markdown(f"**{r.Year}** — {r.Milestone}")
    with right:
        st.subheader("Quick facts")
        st.info(f"🎓 {PROGRAM}")
        st.success("💻 Full-stack Web Developer")
        st.warning("😎 VIBE CODER")
        st.subheader("Interests")
        for tag in ["Playing online games", "sleeping", "learning new things", "UI design", "vibe coding"]:
            st.markdown(f'<span class="pill">{tag}</span>', unsafe_allow_html=True)

        st.subheader("Favorite part of coding")
        mood = st.select_slider(
            "Pick one",
            options=["Debugging", "Designing", "Planning", "Shipping", "vibe coding"],
            value="Shipping",
        )
        st.write(f"You picked **{mood}**. Mine changes by the day 😄")

    st.subheader("My growth over the years")
    st.line_chart(MILESTONES.set_index("Year")["Impact"], color=accent)
    if show_table:
        st.dataframe(MILESTONES, hide_index=True, width="stretch")

# ------------------------------------------------------------------
# Tab 2: Skills
# ------------------------------------------------------------------
with tab_skills:
    st.header("Skills")
    st.write(
        "I'm strongest on the frontend and in Git workflows, and I'm still growing "
        "on backend and data analysis. Use the sidebar to filter."
    )
    view = SKILLS[SKILLS["Category"].isin(skill_filter) & (SKILLS["Level"] >= min_level)]

    c1, c2 = st.columns([3, 2], gap="large")
    with c1:
        if view.empty:
            st.warning("No skills match the current filters.")
        else:
            chart_df = view.set_index("Skill")[["Level"]]
            if chart_kind == "Bar":
                st.bar_chart(chart_df, color=accent)
            elif chart_kind == "Area":
                st.area_chart(chart_df, color=accent)
            else:
                st.line_chart(chart_df, color=accent)
    with c2:
        if show_table:
            st.dataframe(
                view,
                hide_index=True,
                width="stretch",
                column_config={
                    "Level": st.column_config.ProgressColumn("Level", min_value=0, max_value=100, format="%d%%"),
                    "Years": st.column_config.NumberColumn("Years", format="%d yr"),
                },
            )
        st.download_button(
            "⬇️ Download skills (CSV)",
            SKILLS.to_csv(index=False).encode("utf-8"),
            file_name="zyd_skills.csv",
            mime="text/csv",
        )

    st.subheader("Skill explorer")
    pick = st.selectbox("Choose a skill", SKILLS["Skill"])
    row = SKILLS[SKILLS["Skill"] == pick].iloc[0]
    st.progress(int(row.Level) / 100, text=f"{pick}: {row.Level}% · {row.Years} yr · {row.Category}")

    st.subheader("Weekly practice (sample hours)")
    rng = np.random.default_rng(7)
    hours = pd.DataFrame(
        rng.integers(1, 6, size=(7, 3)),
        index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        columns=["Coding", "Exploring", "Reading"],
    )
    st.bar_chart(hours)

# ------------------------------------------------------------------
# Tab 3: Portfolio
# ------------------------------------------------------------------
with tab_projects:
    st.header("Portfolio")
    f1, f2 = st.columns([1, 2])
    types = ["All"] + sorted({p["type"] for p in PROJECTS})
    sel_type = f1.selectbox("Project type", types)
    query = f2.text_input("Search by title or tool", placeholder="e.g. React")

    shown = [
        p for p in PROJECTS
        if (sel_type == "All" or p["type"] == sel_type)
        and (not query or query.lower() in (p["title"] + " " + " ".join(p["tools"])).lower())
    ]
    st.caption(f"Showing {len(shown)} of {len(PROJECTS)} projects")

    cols = st.columns(2, gap="large")
    for i, p in enumerate(shown):
        with cols[i % 2].container(border=True):
            st.subheader(p["title"])
            st.markdown(f"**Role:** {p['role']}")
            st.write(p["desc"])
            st.markdown(
                "".join(f'<span class="pill">{t}</span>' for t in p["tools"]),
                unsafe_allow_html=True,
            )
            st.progress(p["progress"] / 100, text=f"Completion: {p['progress']}%")
            with st.expander("Outcome"):
                st.write(p["outcome"])
            st.link_button("View on GitHub", p["link"])

    if not shown:
        st.info("No projects match your search. Try another keyword.")

    st.subheader("Tools across projects")
    tool_counts = pd.Series([t for p in PROJECTS for t in p["tools"]]).value_counts()
    st.bar_chart(tool_counts, color=accent)

# ------------------------------------------------------------------
# Tab 4: Contact / feedback
# ------------------------------------------------------------------
with tab_contact:
    st.header("Contact & Feedback")
    a, b = st.columns([3, 2], gap="large")
    with a:
        with st.form("feedback_form", clear_on_submit=True):
            who = st.text_input("Your name")
            mail = st.text_input("Your email")
            reason = st.selectbox("Reason", ["Say hi", "Feedback on this site", "Collaboration", "Other"])
            rating = st.slider("Rate this site", 1, 5, 4)
            msg = st.text_area("Message", height=120)
            agree = st.checkbox("I'm okay with being contacted back")
            sent = st.form_submit_button("Send message 🚀")
        if sent:
            if not who or not msg:
                st.error("Please enter your name and a message.")
            else:
                st.session_state.messages.append(
                    {"name": who, "reason": reason, "rating": rating, "message": msg,
                     "date": date.today().isoformat()}
                )
                save_messages(st.session_state.messages)
                st.success(f"Thanks, {who}! Your message was received.")
                st.toast("Message sent!", icon="✅")
                if rating >= 4:
                    st.balloons()
                if agree:
                    st.info("I'll reply to the email you provided.")
    with b:
        st.subheader("Find me")
        st.markdown(f"- 📧 {EMAIL}\n- 🐙 [github.com/zydneybelia]({GITHUB})")
        st.subheader("Messages this session")
        if st.session_state.messages:
            st.dataframe(pd.DataFrame(st.session_state.messages), hide_index=True)
            if st.button("Clear messages"):
                st.session_state.messages = []
                save_messages([])
                st.rerun()
        else:
            st.caption("Nothing yet. Be the first!")

    st.divider()
    st.subheader("Download my one-page profile")
    profile_txt = (
        f"{NAME}\n{PROGRAM}\n{SECTION}\nGitHub: {GITHUB}\n\nProjects:\n"
        + "\n".join(f"- {p['title']} ({', '.join(p['tools'])})" for p in PROJECTS)
    )
    st.download_button("⬇️ Download profile (.txt)", profile_txt, file_name="profile.txt")

st.divider()
st.caption(f"Built with Streamlit · {NAME} · {SECTION}")
