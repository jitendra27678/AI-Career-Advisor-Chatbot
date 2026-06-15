# 🚀 Career Advisor Chatbot

An AI-powered Career Advisor Chatbot built using **Python**, **Streamlit**, and **Google Gemini API**. The application helps users explore career paths, identify required skills, and receive personalized learning roadmaps based on their interests and goals.

---

## 📌 Overview

Choosing the right career path can be challenging, especially with the rapidly evolving technology landscape. This chatbot acts as a virtual career advisor by providing AI-generated guidance, skill recommendations, and structured learning paths.

The chatbot leverages Google's Gemini model to generate intelligent and contextual career advice through a user-friendly Streamlit interface.

---

## ✨ Features

* 🤖 AI-powered career guidance
* 🛣️ Personalized career roadmaps
* 💬 Interactive chat-based interface
* 📚 Skill recommendations for different career paths
* 🎯 Guidance for Data Science, AI, ML, GenAI, and related domains
* 🔒 Secure API key management using environment variables
* 📝 Logging support for monitoring and debugging
* ⚡ Fast and lightweight Streamlit application

---

## 🛠️ Tech Stack

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| Python                | Backend Development             |
| Streamlit             | User Interface                  |
| Google Gemini API     | AI Response Generation          |
| Logging Module        | Application Monitoring          |
| Environment Variables | Secure Configuration Management |

---

## 📂 Project Structure

```text
Career_Advisor_Chatbot/
│
├── app/
│   └── app.py
│
├── services/
│   └── gemini_service.py
│
├── prompts/
│   └── system_prompt.py
│
├── utils/
│   ├── __init__.py
│   └── logger.py
│
├── logs/
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Career_Advisor_Chatbot.git
cd Career_Advisor_Chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

### 5. Run the Application

```bash
streamlit run app/app.py
```

---

## 📸 Application Preview

Add screenshots of your chatbot interface here.

Example:

* Home Screen
* User Query
* AI Generated Career Roadmap

---

## 🎯 Example Use Cases

* Career exploration for students
* Roadmap generation for aspiring Data Scientists
* Skill gap analysis
* Learning path recommendations
* Career transition guidance

---

## 🔮 Future Enhancements

* Resume Analysis
* Job Recommendation System
* Career Path Visualization
* Multi-Language Support
* User Authentication
* Chat History Persistence
* PDF Report Generation

---

## 🧠 Key Learnings

Through this project, I gained practical experience in:

* Prompt Engineering
* Generative AI Applications
* API Integration
* Streamlit Development
* Project Structuring
* Environment Variable Management
* Logging and Error Handling

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

Feel free to fork the repository and submit a pull request.

---

## Author

**Jitendra Khandelwal**

Aspiring Data Scientist | AI & Generative AI Enthusiast



## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
