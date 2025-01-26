from typing import List, Dict
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import random
import spacy
from ..models.workflow import ContentType, Platform

class AIContentService:
    def __init__(self):
        # Download required NLTK data
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('vader_lexicon')
        nltk.download('stopwords')
        
        # Initialize free NLP tools
        self.nlp = spacy.load('en_core_web_sm')
        self.sia = SentimentIntensityAnalyzer()
        
        # Load pre-made templates
        self.templates = {
            'product': [
                "🎉 Exciting news! Check out our {product} - perfect for {audience} who want {benefit}! #MustHave",
                "💡 Did you know? Our {product} helps {audience} achieve {benefit}. Try it today! #Innovation",
                "✨ Transform your {topic} with our amazing {product}! Perfect for {audience}. #GameChanger"
            ],
            'update': [
                "📢 Big news! We're excited to announce {update}! Stay tuned for more. #Announcement",
                "🚀 We're leveling up! {update} is now available for all our amazing customers! #Growth",
                "📈 Guess what? {update} has just landed! Check it out now! #Update"
            ],
            'event': [
                "🎯 Join us for {event}! Perfect for {audience} looking to {benefit}. #Event",
                "📅 Mark your calendars! {event} is happening soon. Don't miss out! #SaveTheDate",
                "🌟 Ready for something amazing? Join us at {event}! #Exclusive"
            ]
        }
        
        # Load engagement patterns
        self.engagement_patterns = {
            'hashtags': ['#trending', '#viral', '#success', '#business', '#growth'],
            'emojis': ['✨', '🚀', '💡', '🎯', '🌟', '💪', '🔥', '📈'],
            'call_to_actions': ['Try now!', 'Learn more!', 'Join us!', 'Get started!', 'Discover more!']
        }
    
    async def generate_content(
        self,
        brand_voice: str,
        target_audience: str,
        content_type: ContentType,
        platform: Platform,
        keywords: List[str],
        campaign_goals: str
    ) -> Dict:
        """Generate engaging content using templates and NLP"""
        
        # Select template based on content type
        template = random.choice(self.templates.get(content_type.lower(), self.templates['update']))
        
        # Fill in template with relevant information
        content = template.format(
            product=random.choice(keywords),
            audience=target_audience,
            benefit=campaign_goals,
            update=campaign_goals,
            event=campaign_goals,
            topic=random.choice(keywords)
        )
        
        # Add engagement elements
        content = self._enhance_content(content, platform)
        
        return {
            "content": content,
            "suggestions": self._analyze_content_performance(content, platform)
        }
    
    def _enhance_content(self, content: str, platform: Platform) -> str:
        """Enhance content with platform-specific elements"""
        
        # Add relevant hashtags
        hashtags = ' '.join(random.sample(self.engagement_patterns['hashtags'], 2))
        
        # Add emojis
        emojis = random.sample(self.engagement_patterns['emojis'], 2)
        
        # Add call to action
        cta = random.choice(self.engagement_patterns['call_to_actions'])
        
        # Combine elements based on platform
        if platform == Platform.INSTAGRAM:
            content = f"{emojis[0]} {content} {emojis[1]}\n\n{cta}\n\n{hashtags}"
        elif platform == Platform.TWITTER:
            content = f"{emojis[0]} {content}\n{cta} {hashtags}"
        else:
            content = f"{content}\n\n{cta} {hashtags}"
            
        return content
    
    async def analyze_trends(self, industry: str, timeframe: str = "week") -> Dict:
        """Analyze trends using pre-defined patterns"""
        trends = [
            f"Growing interest in {industry} innovation",
            f"Rising demand for sustainable {industry} solutions",
            f"Digital transformation in {industry}",
            f"Customer-centric approaches in {industry}",
            f"{industry} automation and efficiency"
        ]
        
        return {
            "trends": trends,
            "opportunities": self._extract_opportunities(trends)
        }
    
    def _analyze_content_performance(self, content: str, platform: Platform) -> List[str]:
        """Analyze content using free NLP tools"""
        
        # Analyze sentiment
        sentiment = self.sia.polarity_scores(content)
        
        # Analyze readability
        doc = self.nlp(content)
        words = len([token for token in doc if not token.is_punct])
        sentences = len(list(doc.sents))
        readability = words / max(sentences, 1)
        
        suggestions = []
        
        # Generate suggestions based on analysis
        if sentiment['compound'] < 0:
            suggestions.append("Consider using more positive language")
        
        if readability > 20:
            suggestions.append("Try shorter, more concise sentences")
            
        if len(content.split()) < 10:
            suggestions.append("Consider adding more detail to engage your audience")
            
        if platform == Platform.INSTAGRAM and '#' not in content:
            suggestions.append("Add relevant hashtags for better reach")
            
        return suggestions or ["Content looks good! Ready to post!"]
    
    def _extract_opportunities(self, trends: List[str]) -> List[str]:
        """Extract opportunities from trends"""
        opportunities = []
        for trend in trends:
            opportunities.append(f"Capitalize on {trend.lower()} with targeted content")
        return opportunities
