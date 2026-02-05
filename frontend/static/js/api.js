const API_BASE = '/api';

// Fetch topics
async function fetchTopics() {
    try {
        const response = await fetch(`${API_BASE}/topics`);
        const data = await response.json();
        return data.topics;
    } catch (error) {
        console.error('Error fetching topics:', error);
        return [];
    }
}

// Fetch quizzes
async function fetchQuizzes(topicId = null) {
    try {
        const url = topicId ? `${API_BASE}/quizzes?topic_id=${topicId}` : `${API_BASE}/quizzes`;
        const response = await fetch(url);
        const data = await response.json();
        return data.quizzes;
    } catch (error) {
        console.error('Error fetching quizzes:', error);
        return [];
    }
}

// Submit quiz answer
async function submitQuiz(quizId, selectedAnswer, topicId) {
    try {
        const response = await fetch(`${API_BASE}/quizzes/submit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                quiz_id: quizId,
                selected_answer: selectedAnswer,
                topic_id: topicId
            })
        });
        return await response.json();
    } catch (error) {
        console.error('Error submitting quiz:', error);
        return null;
    }
}

// Fetch flashcards
async function fetchFlashcards(topicId = null) {
    try {
        const url = topicId ? `${API_BASE}/flashcards?topic_id=${topicId}` : `${API_BASE}/flashcards`;
        const response = await fetch(url);
        const data = await response.json();
        return data.flashcards;
    } catch (error) {
        console.error('Error fetching flashcards:', error);
        return [];
    }
}

// Review flashcard
async function reviewFlashcard(flashcardId, topicId, rating) {
    try {
        const response = await fetch(`${API_BASE}/flashcards/review`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                flashcard_id: flashcardId,
                topic_id: topicId,
                rating: rating
            })
        });
        return await response.json();
    } catch (error) {
        console.error('Error reviewing flashcard:', error);
        return null;
    }
}

// Fetch progress
async function fetchProgress() {
    try {
        const response = await fetch(`${API_BASE}/progress`);
        return await response.json();
    } catch (error) {
        console.error('Error fetching progress:', error);
        return { progress: [], overall: {} };
    }
}

// Fetch topic progress
async function fetchTopicProgress(topicId) {
    try {
        const response = await fetch(`${API_BASE}/progress/${topicId}`);
        return await response.json();
    } catch (error) {
        console.error('Error fetching topic progress:', error);
        return null;
    }
}

// Helper function to get difficulty badge class
function getDifficultyBadgeClass(difficulty) {
    return `difficulty-badge difficulty-${difficulty}`;
}

// Helper function to format date
function formatDate(dateString) {
    if (!dateString) return 'Never';
    const date = new Date(dateString);
    return date.toLocaleDateString();
}

// Helper function to shuffle array
function shuffleArray(array) {
    const newArray = [...array];
    for (let i = newArray.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
    }
    return newArray;
}
