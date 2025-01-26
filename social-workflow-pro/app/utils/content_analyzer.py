from typing import Dict, Any
import aiohttp
from ..core.config import settings

async def analyze_content(content: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyzes content for optimization opportunities and enhancement suggestions.
    
    Features:
    1. Sentiment analysis
    2. Hashtag optimization
    3. Best posting time prediction
    4. Content quality score
    5. Engagement prediction
    """
    
    analyzed_content = content.copy()
    
    # Add content quality metrics
    analyzed_content["metrics"] = {
        "quality_score": calculate_quality_score(content),
        "sentiment_score": analyze_sentiment(content),
        "engagement_prediction": predict_engagement(content),
        "optimal_hashtags": optimize_hashtags(content),
        "best_posting_time": predict_best_posting_time(content)
    }
    
    return analyzed_content

def calculate_quality_score(content: Dict[str, Any]) -> float:
    """Calculate content quality score based on various factors"""
    score = 0.0
    
    if "text" in content:
        # Text analysis
        text = content["text"]
        score += len(text.split()) * 0.1  # Length factor
        score += count_unique_words(text) * 0.2  # Vocabulary diversity
        
    if "media" in content:
        # Media analysis
        score += 2.0  # Bonus for including media
        
    if "hashtags" in content:
        # Hashtag analysis
        score += min(len(content["hashtags"]), 5) * 0.5  # Up to 5 hashtags
        
    return min(score, 10.0)  # Cap at 10

def analyze_sentiment(content: Dict[str, Any]) -> float:
    """Analyze content sentiment (simplified version)"""
    # In a real implementation, this would use a proper NLP model
    positive_words = {"great", "amazing", "awesome", "excellent", "happy"}
    negative_words = {"bad", "poor", "terrible", "awful", "sad"}
    
    if "text" not in content:
        return 0.0
        
    text = content["text"].lower()
    words = set(text.split())
    
    positive_count = len(words.intersection(positive_words))
    negative_count = len(words.intersection(negative_words))
    
    total = positive_count + negative_count
    if total == 0:
        return 0.0
        
    return (positive_count - negative_count) / total

def predict_engagement(content: Dict[str, Any]) -> Dict[str, float]:
    """Predict potential engagement metrics"""
    base_score = calculate_quality_score(content) / 10.0
    
    return {
        "likes_prediction": base_score * 1000,
        "comments_prediction": base_score * 100,
        "shares_prediction": base_score * 50
    }

def optimize_hashtags(content: Dict[str, Any]) -> list:
    """Suggest optimal hashtags based on content"""
    if "text" not in content:
        return []
        
    # Extract key terms (simplified version)
    text = content["text"].lower()
    words = [word for word in text.split() if len(word) > 4]
    
    # In a real implementation, this would use trending hashtag data
    # and relevance analysis
    return [f"#{word}" for word in words[:5]]

def predict_best_posting_time(content: Dict[str, Any]) -> Dict[str, Any]:
    """Predict optimal posting time based on content type and historical data"""
    # In a real implementation, this would analyze historical engagement data
    return {
        "day": "Wednesday",
        "time": "15:00",
        "timezone": "UTC",
        "confidence": 0.85
    }

def count_unique_words(text: str) -> int:
    """Count unique words in text"""
    return len(set(text.lower().split()))
