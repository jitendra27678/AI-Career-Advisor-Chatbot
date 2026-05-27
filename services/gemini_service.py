def generate_response(user_input, system_prompt, chat_history):

    user_input = user_input.lower()

    if "data scientist" in user_input:

        return """
## Roadmap to Become a Data Scientist

1. Learn Python
2. Learn Statistics and Mathematics
3. Learn Machine Learning
4. Practice SQL
5. Build Projects
6. Learn Deep Learning
7. Create a GitHub Portfolio

Recommended Tools:
- Python
- Pandas
- NumPy
- Scikit-learn
- TensorFlow
"""

    elif "full stack" in user_input:

        return """
## Roadmap to Become a Full Stack Developer

1. Learn HTML, CSS, JavaScript
2. Learn React.js
3. Learn Backend Development
4. Learn Node.js and Express
5. Learn Databases
6. Build Projects
7. Deploy Applications

Recommended Technologies:
- React
- Node.js
- MongoDB
- Express.js
"""

    elif "interview" in user_input:

        return """
## Interview Preparation Tips

1. Practice DSA
2. Build strong projects
3. Revise core concepts
4. Practice mock interviews
5. Improve communication skills
"""

    elif "resume" in user_input:

        return """
## Resume Improvement Tips

1. Add strong projects
2. Mention technical skills
3. Use proper formatting
4. Keep resume concise
5. Add GitHub and LinkedIn links
"""

    else:

        return """
I am your AI Career Advisor chatbot.

You can ask me about:
- Data Science
- Full Stack Development
- AI/ML
- Career Roadmaps
- Resume Building
- Interview Preparation
"""