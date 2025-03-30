# AI Recipe Generator Using Gemini 2.0 Flash

This project is a **Streamlit-based AI Recipe Generator** that uses Google's **Gemini 2.0 Flash** model to generate personalized recipes based on user preferences and available ingredients. The application is built using Python, Streamlit, and the Gemini API for generating content.

---

## 🚀 Features

- Generate recipes based on user input.
- Provides detailed step-by-step instructions.
- Offers multiple recipe suggestions.
- Simple and interactive user interface using Streamlit.
- Fast and efficient content generation using Gemini 2.0 Flash.

---

## 🛠️ Technologies Used

- **Python 3.9+**
- **Streamlit** for building the web interface
- **Gemini 2.0 Flash** (via `google.generativeai`) for recipe generation
- **LangChain** for managing prompts and responses

---

## 📂 Project Structure

```
/AI-Recipe-Generator
├── /gemini                           # Virtual environment
├── /images                           # Image assets for the project
├── app.py                            # Main Streamlit application file
├── requirements.txt                  # Required packages
└── README.md                         # Project documentation
```

---

## 📥 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-repo/ai-recipe-generator.git
cd ai-recipe-generator
```

2. **Create a virtual environment:**
```bash
python -m venv gemini
```

3. **Activate the virtual environment:**
```bash
# Windows
gemini\Scripts\activate

# macOS/Linux
source gemini/bin/activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## 🔑 API Key Configuration

1. Get your **Gemini API key** from [Google AI Studio](https://aistudio.google.com/).
2. Create a `.env` file in the project directory and add your key:
```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

To run the Streamlit app, use the following command:
```bash
streamlit run app.py
```

The app will be available at [http://localhost:8501](http://localhost:8501).

---

## 📝 Usage

1. Open the application in your browser.
2. Enter the ingredients or preferences in the input field.
3. Click **"Generate Recipe"** to get personalized recipe suggestions.
4. Explore different options and save your favorite recipes.

---

## 🐞 Troubleshooting

- Ensure that the correct version of `google-generativeai` is installed.
- If API errors occur, verify that the API key is valid and has sufficient quota.
- Update dependencies if required using:
```bash
pip install --upgrade -r requirements.txt
```

---




