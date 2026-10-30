Autobiography & Portfolio App

A personal autobiography and portfolio website built with Streamlit for CSIT 349 · Applied AI.

Author: Jhon Zydney T. Belia Program: BS Information Technology · Year 4 Section: CSIT 349 · Section G01 GitHub: zydneybelia

Live app: add your Streamlit Community Cloud link here

Features
Autobiography: background, education, interests, milestones, and a growth chart.
Skills: a chart and table of my skills with sidebar filters and a CSV download.
Portfolio: project cards with role, tools, outcome, progress, and a GitHub link, plus search and filter.
Contact & Feedback: a form that responds after submission, with saved messages.
Sidebar controls: accent color, skill category filter, minimum skill level, and chart type.
Streamlit components used

st.set_page_config, st.title/header/subheader, st.markdown, st.columns, st.tabs, st.sidebar, st.container, st.expander, st.metric, st.dataframe, st.bar_chart, st.line_chart, st.area_chart, st.image, st.progress, st.slider, st.select_slider, st.selectbox, st.multiselect, st.radio, st.checkbox, st.text_input, st.text_area, st.color_picker, st.form, st.button, st.link_button, st.download_button, st.toast, st.balloons, and st.session_state.

Run locally
bash
pip install -r requirements.txt
python -m streamlit run app.py

Then open http://localhost:8501 in your browser.

Project structure
.
├── app.py             # the Streamlit app
├── requirements.txt   # Python dependencies
├── me.jpg             # profile photo
└── README.md
Tech

Python · Streamlit · pandas · NumPy · Pillow

Notes

Contact form messages are saved to messages.csv while the app runs. On Streamlit Community Cloud this file resets when the app restarts.
