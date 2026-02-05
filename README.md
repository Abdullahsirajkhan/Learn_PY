# Learn_Py 🐍

A comprehensive web application designed to teach Python programming from zero to Object-Oriented Programming (OOP). Features a modern dashboard-style interface with interactive learning tools including quizzes, flashcards, mind maps, progress tracking, and a structured learning path.

## Features

### 🎯 Dashboard Interface
- Clean, intuitive dashboard with quick access to all learning modules
- Real-time statistics showing overall progress and mastery levels
- Modern, responsive design that works on desktop and mobile

### 📝 Interactive Quizzes
- Topic-based quizzes covering all Python concepts
- Instant feedback with explanations
- Automatic progress tracking and mastery calculation
- Difficulty levels: Beginner, Intermediate, Advanced

### 🎴 Flashcards with Spaced Repetition
- Learn key concepts through active recall
- Rate your understanding (1-5 scale) for spaced repetition
- Topic filtering for focused study sessions
- Tracks review frequency and performance

### 🗺️ Visual Mind Map
- Interactive visualization of the entire Python curriculum
- Color-coded nodes showing mastery levels
- Radial tree layout for easy navigation
- Visual representation of learning progress

### 📊 Progress Tracking
- Detailed topic-wise progress metrics
- Overall completion percentage
- Average mastery levels across all topics
- Review history and last studied dates

### 🎯 Structured Learning Path
- Curated sequence of topics from basics to OOP
- Subtopics breakdown for each major topic
- Progress indicators (completed, in-progress, not started)
- Quick links to quizzes and flashcards

## Technology Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: Lightning-fast ASGI server

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with CSS variables and flexbox/grid
- **JavaScript (ES6+)**: Vanilla JS for interactivity
- **D3.js**: Data visualization for mind map

### Data Storage
- **JSON**: Lightweight file-based storage for:
  - Topics and curriculum structure
  - Quizzes with questions and answers
  - Flashcards content
  - User progress and mastery tracking

## Project Structure

```
Learn_PY/
├── backend/
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py          # Pydantic models
│   ├── routes/
│   │   ├── __init__.py
│   │   └── api.py              # API endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   └── data_service.py     # Business logic
│   └── __init__.py
├── data/
│   ├── topics.json             # Python topics curriculum
│   ├── quizzes.json            # Quiz questions
│   ├── flashcards.json         # Flashcard content
│   └── mastery.json            # User progress data
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css       # Application styles
│   │   └── js/
│   │       └── api.js          # API client
│   └── templates/
│       ├── index.html          # Dashboard
│       ├── quizzes.html        # Quiz interface
│       ├── flashcards.html     # Flashcard interface
│       ├── mindmap.html        # Mind map visualization
│       ├── progress.html       # Progress tracking
│       └── learning_path.html  # Learning path
├── main.py                     # FastAPI application entry point
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abdullahsirajkhan/Learn_PY.git
   cd Learn_PY
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Access the application**
   Open your browser and navigate to:
   ```
   http://localhost:8000
   ```

3. **Explore the features**
   - Visit the dashboard to see your progress
   - Take quizzes to test your knowledge
   - Use flashcards for active recall
   - Visualize your learning journey with the mind map
   - Track your progress across all topics
   - Follow the structured learning path

## API Endpoints

### Topics
- `GET /api/topics` - Get all Python topics
- `GET /api/topics/{topic_id}` - Get specific topic details

### Quizzes
- `GET /api/quizzes` - Get all quizzes (optional: filter by topic_id)
- `POST /api/quizzes/submit` - Submit quiz answer and update progress

### Flashcards
- `GET /api/flashcards` - Get all flashcards (optional: filter by topic_id)
- `POST /api/flashcards/review` - Submit flashcard review and update progress

### Progress
- `GET /api/progress` - Get user progress for all topics
- `GET /api/progress/{topic_id}` - Get progress for specific topic

## Data Models

### Topic
- `id`: Unique identifier
- `title`: Topic name
- `description`: Brief description
- `order`: Learning sequence
- `subtopics`: List of subtopics
- `difficulty`: beginner/intermediate/advanced

### Quiz
- `id`: Unique identifier
- `topic_id`: Associated topic
- `question`: Question text
- `options`: List of answer choices
- `correct_answer`: Index of correct option
- `explanation`: Detailed explanation
- `difficulty`: Difficulty level

### Flashcard
- `id`: Unique identifier
- `topic_id`: Associated topic
- `front`: Question/prompt
- `back`: Answer/explanation
- `difficulty`: Difficulty level

### User Progress
- `user_id`: User identifier (default: "default_user")
- `topic_id`: Associated topic
- `mastery_level`: Percentage (0-100)
- `last_reviewed`: ISO timestamp
- `times_reviewed`: Review count
- `correct_answers`: Number of correct answers
- `total_attempts`: Total attempts

## Extensibility & AI Integration

The application is designed with clean architecture principles for easy extension:

### Current Structure
- **Separation of Concerns**: Models, routes, and services are cleanly separated
- **RESTful API**: Well-defined API endpoints for all operations
- **JSON Data Storage**: Easy to migrate to databases (SQLite, PostgreSQL, etc.)
- **Modular Frontend**: Each feature has its own page and can be enhanced independently

### Future AI Integration Points
1. **Adaptive Learning**
   - AI can analyze user progress and recommend personalized learning paths
   - Predict optimal review times based on spaced repetition algorithms

2. **Content Generation**
   - Generate additional quizzes and flashcards using AI
   - Create personalized examples based on user's interests

3. **Intelligent Tutoring**
   - Add chatbot for answering Python questions
   - Provide contextual hints during quizzes

4. **Code Practice**
   - Integrate code editor with AI-powered feedback
   - Automated code review and suggestions

5. **Natural Language Processing**
   - Analyze user's answers in open-ended questions
   - Provide detailed feedback on code explanations

### Adding New Features
To add new features:
1. Add new models in `backend/models/schemas.py`
2. Create service methods in `backend/services/`
3. Add API routes in `backend/routes/api.py`
4. Create frontend templates in `frontend/templates/`
5. Add styling in `frontend/static/css/style.css`
6. Implement client-side logic in JavaScript

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Abdullah Siraj Khan

## Acknowledgments

- Built with FastAPI for high performance
- Styled with modern CSS3 features
- Visualizations powered by D3.js 
