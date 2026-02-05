import json
import os
from typing import List, Optional
from backend.models.schemas import Topic, Quiz, Flashcard, UserProgress
from datetime import datetime


class DataService:
    def __init__(self):
        self.data_dir = "data"
        self.topics_file = os.path.join(self.data_dir, "topics.json")
        self.quizzes_file = os.path.join(self.data_dir, "quizzes.json")
        self.flashcards_file = os.path.join(self.data_dir, "flashcards.json")
        self.mastery_file = os.path.join(self.data_dir, "mastery.json")
    
    def _load_json(self, filepath: str) -> dict:
        """Load JSON file"""
        if not os.path.exists(filepath):
            return {}
        with open(filepath, 'r') as f:
            return json.load(f)
    
    def _save_json(self, filepath: str, data: dict):
        """Save data to JSON file"""
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    def get_topics(self) -> List[Topic]:
        """Get all topics"""
        data = self._load_json(self.topics_file)
        return [Topic(**topic) for topic in data.get("topics", [])]
    
    def get_topic_by_id(self, topic_id: str) -> Optional[Topic]:
        """Get a specific topic"""
        topics = self.get_topics()
        for topic in topics:
            if topic.id == topic_id:
                return topic
        return None
    
    def get_quizzes(self, topic_id: Optional[str] = None) -> List[Quiz]:
        """Get quizzes, optionally filtered by topic"""
        data = self._load_json(self.quizzes_file)
        quizzes = [Quiz(**quiz) for quiz in data.get("quizzes", [])]
        
        if topic_id:
            quizzes = [q for q in quizzes if q.topic_id == topic_id]
        
        return quizzes
    
    def get_flashcards(self, topic_id: Optional[str] = None) -> List[Flashcard]:
        """Get flashcards, optionally filtered by topic"""
        data = self._load_json(self.flashcards_file)
        flashcards = [Flashcard(**card) for card in data.get("flashcards", [])]
        
        if topic_id:
            flashcards = [f for f in flashcards if f.topic_id == topic_id]
        
        return flashcards
    
    def get_user_progress(self, user_id: str = "default_user") -> List[UserProgress]:
        """Get user progress for all topics"""
        data = self._load_json(self.mastery_file)
        progress_list = data.get("progress", [])
        return [UserProgress(**p) for p in progress_list if p.get("user_id", "default_user") == user_id]
    
    def get_topic_progress(self, topic_id: str, user_id: str = "default_user") -> Optional[UserProgress]:
        """Get user progress for a specific topic"""
        progress_list = self.get_user_progress(user_id)
        for progress in progress_list:
            if progress.topic_id == topic_id:
                return progress
        return None
    
    def update_progress(self, progress: UserProgress):
        """Update user progress for a topic"""
        data = self._load_json(self.mastery_file)
        progress_list = data.get("progress", [])
        
        # Find and update existing progress
        found = False
        for i, p in enumerate(progress_list):
            if p.get("topic_id") == progress.topic_id and p.get("user_id", "default_user") == progress.user_id:
                progress_list[i] = progress.dict()
                found = True
                break
        
        # Add new progress if not found
        if not found:
            progress_list.append(progress.dict())
        
        data["progress"] = progress_list
        self._save_json(self.mastery_file, data)
    
    def calculate_overall_progress(self, user_id: str = "default_user") -> dict:
        """Calculate overall learning progress"""
        topics = self.get_topics()
        progress_list = self.get_user_progress(user_id)
        
        if not topics:
            return {"total_topics": 0, "completed_topics": 0, "average_mastery": 0.0}
        
        total_topics = len(topics)
        total_mastery = 0.0
        completed_topics = 0
        
        progress_dict = {p.topic_id: p for p in progress_list}
        
        for topic in topics:
            if topic.id in progress_dict:
                mastery = progress_dict[topic.id].mastery_level
                total_mastery += mastery
                if mastery >= 80:  # Consider 80% as completed
                    completed_topics += 1
        
        average_mastery = total_mastery / total_topics if total_topics > 0 else 0.0
        
        return {
            "total_topics": total_topics,
            "completed_topics": completed_topics,
            "average_mastery": round(average_mastery, 2),
            "completion_percentage": round((completed_topics / total_topics) * 100, 2) if total_topics > 0 else 0.0
        }


data_service = DataService()
