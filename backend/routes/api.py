from fastapi import APIRouter, HTTPException
from typing import Optional
from backend.models.schemas import QuizSubmission, FlashcardReview, UserProgress
from backend.services.data_service import data_service
from datetime import datetime

router = APIRouter()


@router.get("/topics")
async def get_topics():
    """Get all Python learning topics"""
    topics = data_service.get_topics()
    return {"topics": [topic.dict() for topic in topics]}


@router.get("/topics/{topic_id}")
async def get_topic(topic_id: str):
    """Get a specific topic"""
    topic = data_service.get_topic_by_id(topic_id)
    if not topic:
        raise HTTPException(status_code=404, detail="Topic not found")
    return topic.dict()


@router.get("/quizzes")
async def get_quizzes(topic_id: Optional[str] = None):
    """Get quizzes, optionally filtered by topic"""
    quizzes = data_service.get_quizzes(topic_id)
    return {"quizzes": [quiz.dict() for quiz in quizzes]}


@router.post("/quizzes/submit")
async def submit_quiz(submission: QuizSubmission):
    """Submit a quiz answer and update progress"""
    quizzes = data_service.get_quizzes()
    quiz = next((q for q in quizzes if q.id == submission.quiz_id), None)
    
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    
    is_correct = submission.selected_answer == quiz.correct_answer
    
    # Update progress
    progress = data_service.get_topic_progress(submission.topic_id)
    if not progress:
        progress = UserProgress(
            user_id="default_user",
            topic_id=submission.topic_id,
            mastery_level=0.0,
            last_reviewed=datetime.now().isoformat(),
            times_reviewed=0,
            correct_answers=0,
            total_attempts=0
        )
    
    progress.total_attempts += 1
    progress.times_reviewed += 1
    progress.last_reviewed = datetime.now().isoformat()
    
    if is_correct:
        progress.correct_answers += 1
    
    # Calculate mastery level (percentage of correct answers)
    if progress.total_attempts > 0:
        progress.mastery_level = (progress.correct_answers / progress.total_attempts) * 100
    
    data_service.update_progress(progress)
    
    return {
        "correct": is_correct,
        "explanation": quiz.explanation,
        "mastery_level": round(progress.mastery_level, 2)
    }


@router.get("/flashcards")
async def get_flashcards(topic_id: Optional[str] = None):
    """Get flashcards, optionally filtered by topic"""
    flashcards = data_service.get_flashcards(topic_id)
    return {"flashcards": [card.dict() for card in flashcards]}


@router.post("/flashcards/review")
async def review_flashcard(review: FlashcardReview):
    """Review a flashcard and update progress"""
    # Update progress based on rating (1-5)
    progress = data_service.get_topic_progress(review.topic_id)
    if not progress:
        progress = UserProgress(
            user_id="default_user",
            topic_id=review.topic_id,
            mastery_level=0.0,
            last_reviewed=datetime.now().isoformat(),
            times_reviewed=0,
            correct_answers=0,
            total_attempts=0
        )
    
    progress.times_reviewed += 1
    progress.last_reviewed = datetime.now().isoformat()
    
    # Rating of 4-5 is considered good
    if review.rating >= 4:
        progress.correct_answers += 1
    progress.total_attempts += 1
    
    # Calculate mastery level
    if progress.total_attempts > 0:
        progress.mastery_level = (progress.correct_answers / progress.total_attempts) * 100
    
    data_service.update_progress(progress)
    
    return {
        "mastery_level": round(progress.mastery_level, 2),
        "times_reviewed": progress.times_reviewed
    }


@router.get("/progress")
async def get_progress(user_id: str = "default_user"):
    """Get user progress for all topics"""
    progress = data_service.get_user_progress(user_id)
    overall = data_service.calculate_overall_progress(user_id)
    
    return {
        "progress": [p.dict() for p in progress],
        "overall": overall
    }


@router.get("/progress/{topic_id}")
async def get_topic_progress(topic_id: str, user_id: str = "default_user"):
    """Get user progress for a specific topic"""
    progress = data_service.get_topic_progress(topic_id, user_id)
    if not progress:
        return {
            "topic_id": topic_id,
            "mastery_level": 0.0,
            "times_reviewed": 0,
            "correct_answers": 0,
            "total_attempts": 0
        }
    return progress.dict()
