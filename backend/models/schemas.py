from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Topic(BaseModel):
    id: str
    title: str
    description: str
    order: int
    subtopics: List[str]
    difficulty: str


class Quiz(BaseModel):
    id: str
    topic_id: str
    question: str
    options: List[str]
    correct_answer: int
    explanation: str
    difficulty: str


class Flashcard(BaseModel):
    id: str
    topic_id: str
    front: str
    back: str
    difficulty: str


class UserProgress(BaseModel):
    user_id: str = "default_user"
    topic_id: str
    mastery_level: float
    last_reviewed: Optional[str] = None
    times_reviewed: int = 0
    correct_answers: int = 0
    total_attempts: int = 0


class QuizSubmission(BaseModel):
    quiz_id: str
    selected_answer: int
    topic_id: str


class FlashcardReview(BaseModel):
    flashcard_id: str
    topic_id: str
    rating: int  # 1-5, how well the user knew it
