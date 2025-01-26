from textblob import TextBlob
import cv2
import numpy as np
from typing import List, Dict, Union
import re

class ContentOptimizer:
    def __init__(self):
        # No heavy AI models, just lightweight text processing
        pass
        
    def optimize_image(self, image_path: str) -> Dict:
        """Optimize images for social media using OpenCV"""
        image = cv2.imread(image_path)
        
        # Auto-enhance
        enhanced = self._auto_enhance(image)
        
        # Generate multiple sizes for different platforms
        sizes = {
            'instagram_square': (1080, 1080),
            'instagram_portrait': (1080, 1350),
            'facebook': (1200, 630),
            'twitter': (1200, 675)
        }
        
        optimized = {}
        for platform, size in sizes.items():
            optimized[platform] = cv2.resize(enhanced, size)
            
        return optimized
    
    def _auto_enhance(self, image: np.ndarray) -> np.ndarray:
        """Auto-enhance image quality"""
        # Convert to LAB color space
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        
        # Apply CLAHE to L channel
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        
        # Merge channels
        limg = cv2.merge((cl,a,b))
        
        # Convert back to BGR
        enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        
        return enhanced
    
    def optimize_text(self, text: str, platform: str) -> str:
        """Optimize text content for different platforms"""
        # Simple text optimization without AI
        text = text.strip()
        
        if platform == 'instagram':
            text = self._optimize_for_instagram(text)
        elif platform == 'facebook':
            text = self._optimize_for_facebook(text)
        elif platform == 'twitter':
            text = self._optimize_for_twitter(text)
            
        return text
    
    def _optimize_for_instagram(self, text: str) -> str:
        """Instagram-specific optimizations"""
        # Add line breaks for readability
        text = re.sub(r'([.!?])\s+', r'\1\n\n', text)
        
        # Ensure hashtags are at the end
        parts = text.split('#')
        if len(parts) > 1:
            main_text = parts[0]
            hashtags = ['#' + p for p in parts[1:]]
            text = main_text + '\n.\n.\n.\n' + ' '.join(hashtags)
            
        return text
    
    def _optimize_for_facebook(self, text: str) -> str:
        """Facebook-specific optimizations"""
        # Add paragraph breaks
        text = re.sub(r'([.!?])\s+', r'\1\n\n', text)
        
        # Convert hashtags to natural language
        text = re.sub(r'#(\w+)', r'\1', text)
        
        return text
    
    def _optimize_for_twitter(self, text: str) -> str:
        """Twitter-specific optimizations"""
        # Ensure within character limit
        if len(text) > 280:
            text = text[:277] + '...'
            
        return text
    
    def generate_hashtags(self, content: str, industry: str) -> List[str]:
        """Generate relevant hashtags based on content and industry"""
        # Extract keywords
        keywords = self._extract_keywords(content)
        
        # Combine with industry-specific hashtags
        industry_hashtags = self._get_industry_hashtags(industry)
        
        # Create hashtags from keywords
        content_hashtags = ['#' + re.sub(r'\s+', '', k) for k in keywords]
        
        # Combine and remove duplicates
        all_hashtags = list(set(content_hashtags + industry_hashtags))
        
        # Limit to top 30 most relevant
        return all_hashtags[:30]
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract keywords from text"""
        # Remove special characters and split
        words = re.findall(r'\w+', text.lower())
        
        # Remove common words
        common_words = {'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have'}
        keywords = [w for w in words if w not in common_words]
        
        return list(set(keywords))
    
    def _get_industry_hashtags(self, industry: str) -> List[str]:
        """Get industry-specific hashtags"""
        hashtags = {
            'restaurant': [
                '#foodie', '#instafood', '#foodphotography', 
                '#foodlover', '#chef', '#delicious'
            ],
            'retail': [
                '#shopping', '#fashion', '#style', 
                '#shoplocal', '#newcollection', '#boutique'
            ],
            'fitness': [
                '#fitness', '#workout', '#gym', 
                '#fitnessmotivation', '#health', '#training'
            ]
        }
        return hashtags.get(industry.lower(), [])
    
    def analyze_content(self, content: str) -> Dict:
        """Analyze content quality"""
        # Simple text analysis
        blob = TextBlob(content)
        
        # Basic metrics
        metrics = {
            'length': len(content),
            'hashtags': len(re.findall(r'#\w+', content)),
            'questions': len(re.findall(r'\?', content)),
            'calls_to_action': len(re.findall(r'(click|share|like|comment|follow|check out)', content.lower())),
            'emojis': len(re.findall(r'[\U0001F300-\U0001F999]', content)),
            'sentiment': blob.sentiment.polarity,
            'readability': self._calculate_readability(content)
        }
        
        return {
            'metrics': metrics,
            'improvements': self._suggest_improvements(metrics)
        }
    
    def _calculate_readability(self, text: str) -> float:
        """Calculate text readability score"""
        words = len(text.split())
        sentences = len(re.split(r'[.!?]+', text))
        syllables = len(re.findall(r'[aeiou]+', text.lower()))
        
        if sentences == 0:
            return 0
            
        return 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)
    
    def _suggest_improvements(self, metrics: Dict) -> List[str]:
        """Suggest content improvements"""
        suggestions = []
        
        # Length check
        if metrics['length'] < 50:
            suggestions.append("Add more detail to increase engagement")
        elif metrics['length'] > 300:
            suggestions.append("Consider shortening for better readability")
            
        # Hashtag check
        if metrics['hashtags'] < 5:
            suggestions.append("Add more relevant hashtags")
        elif metrics['hashtags'] > 30:
            suggestions.append("Reduce number of hashtags")
            
        # Call-to-action check
        if metrics['calls_to_action'] == 0:
            suggestions.append("Add a clear call-to-action")
            
        # Question check
        if metrics['questions'] == 0:
            suggestions.append("Consider adding a question to increase engagement")
            
        return suggestions
