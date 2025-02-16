# Nihongo Quest  

Nihongo Quest is a Flask-based web application designed to help users learn Japanese vocabulary through interactive quizzes. Users can log in, take quizzes, and test their knowledge by answering questions about Japanese words.

## Objective and Next Steps  

### Objective  
The goal of Nihongo Quest is to provide an engaging platform for learning Japanese vocabulary. The app allows users to take quizzes, track their progress, and improve their understanding of the language through repetition and interaction.

### Next Steps  
- Implement user-specific progress tracking and scores.  
- Improve the UI/UX for a better learning experience.  
- Add more quiz categories and difficulty levels.  
- Deploy the application online for wider accessibility.  

## Problems and Solutions  

### ❌ **Problem: CSRF Token Errors in Quiz Form**  
- **Issue:** The CSRF token was missing or not being validated correctly in the form submission.  
- **Solution:**  
  - Ensured that `CSRFProtect(app)` was correctly initialized in `app.py`.  
  - Passed the CSRF token explicitly in `render_template()`.  
  - Added a hidden input field in `quiz.html` to include the CSRF token in the form.  

### ❌ **Problem: Understanding Mako Templates**  
- **What is Mako?**  
  Mako is a templating engine for Python, similar to Jinja2 but with a syntax closer to standard Python expressions.  
  - **Why is it relevant?** Mako is sometimes used in Flask applications when working with certain frameworks or plugins that require an alternative template engine.  
  - **In Nihongo Quest:** We are using Jinja2 (Flask's default template engine), so Mako is not needed for now. However, understanding Mako can be useful for other Python projects.  

## Installation  

1. Clone the repository:  
   ```sh
   git clone https://github.com/your-username/nihongo-quest.git
   cd nihongo-quest
   ```

2. Create and activate a virtual envionment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   ```

3. Install independecies:
   ```sh
   pip install -r requirements.txt

   ```
4. Run the application
   ```sh
   flask run

   ```

## Technologies Used  

- **Flask** – Backend framework  
- **SQLAlchemy** – Database ORM  
- **Flask-Login** – User authentication  
- **Flask-WTF** – Forms and CSRF protection  
- **Jinja2** – Template rendering  

## Contributing  

Feel free to open issues or submit pull requests to improve Nihongo Quest!  

