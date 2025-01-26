from textblob import TextBlob
import nltk
import re
from collections import Counter
from typing import List, Dict
from datetime import datetime

class MarketAnalyzer:
    def __init__(self):
        # Download required NLTK data
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')

    def analyze_competitors(self, competitor_content: List[str]) -> Dict:
        """Analyze competitor content using basic NLP"""
        # Extract keywords
        all_words = []
        for content in competitor_content:
            words = nltk.word_tokenize(content.lower())
            all_words.extend(words)
            
        # Remove common words
        common_words = set(nltk.corpus.words.words())
        keywords = [w for w in all_words if w not in common_words and w.isalnum()]
        
        # Get keyword frequency
        keyword_freq = Counter(keywords).most_common(20)
        
        # Basic sentiment analysis
        sentiments = []
        for content in competitor_content:
            blob = TextBlob(content)
            sentiments.append(blob.sentiment.polarity)
        
        avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
        
        # Extract themes (most common 2-word phrases)
        themes = self._extract_themes(competitor_content)

        return {
            'keywords': [k[0] for k in keyword_freq],
            'sentiment': avg_sentiment,
            'themes': themes
        }

    def _extract_themes(self, texts: List[str]) -> List[List[str]]:
        """Extract common themes from texts"""
        # Get bigrams (2-word phrases)
        bigrams = []
        for text in texts:
            words = nltk.word_tokenize(text.lower())
            bigrams.extend(list(nltk.bigrams(words)))
        
        # Count frequencies
        bigram_freq = Counter(bigrams).most_common(5)
        
        # Convert to list of word pairs
        themes = [[w1, w2] for (w1, w2), _ in bigram_freq]
        
        return themes

    def generate_content_ideas(self, industry: str, keywords: List[str], themes: List[List[str]]) -> List[str]:
        """Generate content ideas based on analysis"""
        templates = self.get_industry_templates(industry)
        ideas = []
        
        for theme in themes:
            theme_str = ' '.join(theme)
            for template in templates:
                # Replace placeholders with actual content
                idea = template.replace('[THEME]', theme_str)
                if '[KEYWORD]' in template:
                    for keyword in keywords[:3]:  # Use top 3 keywords
                        idea_with_keyword = idea.replace('[KEYWORD]', keyword)
                        ideas.append(idea_with_keyword)
                else:
                    ideas.append(idea)

        return list(set(ideas))  # Remove duplicates

    def get_industry_templates(self, industry: str) -> List[str]:
        """Get industry-specific content templates"""
        templates = {
            'restaurant': [
                'Behind the scenes: How we prepare [THEME]',
                'Chef\'s secret tips for perfect [KEYWORD]',
                'Customer spotlight: Why they love our [THEME]',
                'Quick guide: Pairing [KEYWORD] with our specialties',
                'Weekend special: Featuring [THEME]'
            ],
            'retail': [
                'Style guide: How to rock [THEME]',
                'New arrival spotlight: [KEYWORD] collection',
                'Customer lookbook: [THEME] edition',
                'Quick tips: Maintaining your [KEYWORD]',
                'Seasonal must-haves: [THEME] essentials'
            ],
            'fitness': [
                '[THEME] workout challenge',
                'Form check: Perfect your [KEYWORD] technique',
                'Member transformation: [THEME] journey',
                'Quick tips: Maximizing your [KEYWORD] results',
                'Nutrition guide: Best foods for [THEME]'
            ]
        }
        return templates.get(industry.lower(), [])

    def analyze_engagement_patterns(self, historical_data: List[Dict]) -> Dict:
        """Analyze engagement patterns from historical data"""
        # Process timestamps
        hour_engagement = {}
        content_type_engagement = {}
        hashtags = []
        
        for post in historical_data:
            # Hour analysis
            hour = datetime.fromisoformat(post['timestamp']).hour
            if hour not in hour_engagement:
                hour_engagement[hour] = []
            hour_engagement[hour].append(post['engagement'])
            
            # Content type analysis
            content_type = post['content_type']
            if content_type not in content_type_engagement:
                content_type_engagement[content_type] = []
            content_type_engagement[content_type].append(post['engagement'])
            
            # Hashtag analysis
            hashtags.extend(re.findall(r'#\w+', post['content']))
        
        # Calculate averages
        peak_hours = {
            hour: sum(engagements)/len(engagements)
            for hour, engagements in hour_engagement.items()
        }
        
        content_performance = {
            ctype: {
                'mean': sum(engagements)/len(engagements),
                'count': len(engagements)
            }
            for ctype, engagements in content_type_engagement.items()
        }
        
        hashtag_freq = Counter(hashtags).most_common(10)

        return {
            'peak_hours': peak_hours,
            'content_performance': content_performance,
            'top_hashtags': dict(hashtag_freq)
        }

    def generate_growth_strategy(self, 
                               competitor_analysis: Dict, 
                               engagement_patterns: Dict,
                               industry: str) -> Dict:
        """Generate growth strategy based on analysis"""
        # Sort peak posting times
        peak_times = sorted(
            engagement_patterns['peak_hours'].items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]

        # Sort content types by performance
        content_types = sorted(
            [(ct, data['mean']) for ct, data in engagement_patterns['content_performance'].items()],
            key=lambda x: x[1],
            reverse=True
        )

        strategy = {
            'posting_schedule': [
                f"{hour:02d}:00 - Engagement rate: {rate:.2f}"
                for hour, rate in peak_times
            ],
            'content_mix': [
                f"{content_type}: {rate:.2f} avg engagement"
                for content_type, rate in content_types
            ],
            'recommended_hashtags': list(engagement_patterns['top_hashtags'].keys()),
            'content_themes': competitor_analysis['themes'],
            'tone_guidelines': self._generate_tone_guidelines(competitor_analysis['sentiment']),
            'growth_tactics': self._generate_growth_tactics(industry, competitor_analysis)
        }

        return strategy

    def _generate_tone_guidelines(self, sentiment: float) -> List[str]:
        """Generate content tone guidelines based on sentiment"""
        guidelines = []
        
        if sentiment > 0.3:
            guidelines.append("Maintain a consistently positive and upbeat tone")
        elif sentiment < -0.1:
            guidelines.append("Focus on problem-solving and improvement")
        else:
            guidelines.append("Balance positive content with practical solutions")

        return guidelines

    def _generate_growth_tactics(self, industry: str, competitor_analysis: Dict) -> List[str]:
        """Generate industry-specific growth tactics"""
        # Basic tactics based on themes
        tactics = [
            f"Focus on key theme: {' '.join(theme)}" 
            for theme in competitor_analysis['themes'][:3]
        ]
        
        # Add industry-specific tactics
        industry_tactics = {
            'restaurant': [
                "Create weekly themed menu spotlights",
                "Showcase customer reviews with food photos",
                "Share kitchen preparation process",
                "Feature chef specialties"
            ],
            'retail': [
                "Create seasonal lookbooks",
                "Show multiple styling options",
                "Feature customer outfits",
                "Share product care tips"
            ],
            'fitness': [
                "Create workout challenge series",
                "Share member success stories",
                "Provide form tutorials",
                "Share healthy recipes"
            ]
        }
        
        tactics.extend(industry_tactics.get(industry.lower(), []))
        return tactics
