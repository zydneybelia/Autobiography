# 👋 Autobiography & Portfolio App

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B?logo=streamlit&logoColor=white)

A personal autobiography and portfolio website built with [Streamlit](https://streamlit.io) for **CSIT 349 · Applied AI**.

🔗 **Live app:** [](https://autobiography-ycjisfjeeb3eoksrdtzkyo.streamlit.app/)

## 👤 About the author

| | |
|---|---|
| **Name** | Jhon Zydney T. Belia |
| **Program** | BS Information Technology · Year 4 |
| **Course / Section** | CSIT 349 · Section G01 |
| **GitHub** | [@zydneybelia](https://github.com/zydneybelia) |

## ✨ Features

| Tab | What it shows |
|---|---|
| 📖 **Autobiography** | Background, education, interests, milestones, and a growth chart |
| 📊 **Skills** | Skill chart and table with sidebar filters and a CSV download |
| 💼 **Portfolio** | Project cards (role, tools, outcome, progress, GitHub link) with search and filter |
| ✉️ **Contact** | Feedback form that responds after submission, with saved messages |

The sidebar lets visitors change the chart accent color, filter skill categories, set a minimum skill level, and switch the chart type.

## 🧩 Streamlit components used

- **Layout:** `set_page_config`, `columns`, `tabs`, `sidebar`, `container`, `expander`
- **Text and media:** `title`, `header`, `subheader`, `markdown`, `image`
- **Data display:** `metric`, `dataframe`, `progress`, `bar_chart`, `line_chart`, `area_chart`
- **Inputs:** `slider`, `select_slider`, `selectbox`, `multiselect`, `radio`, `checkbox`, `text_input`, `text_area`, `color_picker`, `form`
- **Actions and feedback:** `button`, `link_button`, `download_button`, `toast`, `balloons`
- **State:** `session_state`

## 🚀 Run locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

Then open <http://localhost:8501> in your browser.

## 📁 Project structure

```
.
├── app.py             # the Streamlit app
├── requirements.txt   # Python dependencies
├── me.jpg             # profile photo
└── README.md
```

## 🛠️ Built with

Python · Streamlit · pandas · NumPy · Pillow

## 📝 Notes

Contact form messages are saved to `messages.csv` while the app runs. On Streamlit Community Cloud this file resets when the app restarts.
