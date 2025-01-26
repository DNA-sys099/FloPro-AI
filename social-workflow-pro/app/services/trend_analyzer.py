import nltk
from textblob import TextBlob
import re
from collections import Counter, defaultdict
from typing import List, Dict, Tuple
from datetime import datetime, timedelta
import math

class TrendAnalyzer:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        self.viral_patterns = {
            'storytelling': [
                r'(how|why|what).+(changed|learned|discovered)',
                r'(day|week|year) in (my|our) life',
                r'(behind|inside).+scenes'
            ],
            'emotional': [
                r'(never|always|finally|actually).+(believed|thought|expected)',
                r'(shocked|amazed|surprised|blown away)',
                r'(best|worst|craziest|amazing).+(experience|moment|day)'
            ],
            'value_hooks': [
                r'(secret|hidden|unknown).+(tips|tricks|hacks)',
                r'(how to|guide|tutorial)',
                r'(mistakes|errors|problems).+(avoid|solve|fix)'
            ]
        }
        
    def analyze_trends(self, posts: List[Dict]) -> Dict:
        """Analyze content trends and patterns"""
        # Sort posts by engagement
        sorted_posts = sorted(posts, key=lambda x: x['engagement'], reverse=True)
        top_posts = sorted_posts[:int(len(posts) * 0.2)]  # Top 20%
        
        trends = {
            'patterns': self._analyze_viral_patterns(top_posts),
            'timing': self._analyze_timing_patterns(top_posts),
            'content_elements': self._analyze_content_elements(top_posts),
            'engagement_factors': self._analyze_engagement_factors(top_posts),
            'viral_hooks': self._identify_viral_hooks(top_posts)
        }
        
        return trends
    
    def _analyze_viral_patterns(self, posts: List[Dict]) -> Dict:
        """Analyze patterns in viral content"""
        pattern_matches = defaultdict(int)
        total_posts = len(posts)
        
        for post in posts:
            content = post['content'].lower()
            for category, patterns in self.viral_patterns.items():
                for pattern in patterns:
                    if re.search(pattern, content):
                        pattern_matches[category] += 1
        
        # Calculate percentage of posts using each pattern
        pattern_stats = {
            category: (count / total_posts) * 100
            for category, count in pattern_matches.items()
        }
        
        return pattern_stats
    
    def _analyze_timing_patterns(self, posts: List[Dict]) -> Dict:
        """Analyze timing patterns of successful posts"""
        hour_stats = defaultdict(list)
        day_stats = defaultdict(list)
        
        for post in posts:
            timestamp = datetime.fromisoformat(post['timestamp'])
            hour_stats[timestamp.hour].append(post['engagement'])
            day_stats[timestamp.strftime('%A')].append(post['engagement'])
        
        # Calculate average engagement by hour and day
        best_hours = {
            hour: sum(engagements)/len(engagements)
            for hour, engagements in hour_stats.items()
        }
        
        best_days = {
            day: sum(engagements)/len(engagements)
            for day, engagements in day_stats.items()
        }
        
        return {
            'best_hours': dict(sorted(best_hours.items(), 
                                    key=lambda x: x[1], 
                                    reverse=True)[:5]),
            'best_days': dict(sorted(best_days.items(), 
                                   key=lambda x: x[1], 
                                   reverse=True))
        }
    
    def _analyze_content_elements(self, posts: List[Dict]) -> Dict:
        """Analyze successful content elements"""
        elements = defaultdict(list)
        
        for post in posts:
            content = post['content']
            elements['length'].append((len(content), post['engagement']))
            elements['hashtags'].append((len(re.findall(r'#\w+', content)), 
                                      post['engagement']))
            elements['mentions'].append((len(re.findall(r'@\w+', content)), 
                                      post['engagement']))
            elements['emojis'].append((len(re.findall(r'[\U0001F300-\U0001F999]', 
                                                    content)), 
                                    post['engagement']))
            
        # Calculate optimal ranges
        optimal_ranges = {}
        for element, values in elements.items():
            sorted_by_engagement = sorted(values, key=lambda x: x[1], reverse=True)
            top_values = sorted_by_engagement[:int(len(values) * 0.2)]  # Top 20%
            
            element_values = [v[0] for v in top_values]
            optimal_ranges[element] = {
                'min': min(element_values),
                'max': max(element_values),
                'average': sum(element_values) / len(element_values)
            }
            
        return optimal_ranges
    
    def _analyze_engagement_factors(self, posts: List[Dict]) -> Dict:
        """Analyze factors contributing to engagement"""
        factors = defaultdict(float)
        total_posts = len(posts)
        
        for post in posts:
            content = post['content'].lower()
            engagement = post['engagement']
            
            # Analyze question impact
            if '?' in content:
                factors['questions'] += engagement
                
            # Analyze call-to-action impact
            if re.search(r'(click|share|like|comment|follow|check out)', content):
                factors['calls_to_action'] += engagement
                
            # Analyze emotional words impact
            blob = TextBlob(content)
            if abs(blob.sentiment.polarity) > 0.5:
                factors['emotional_content'] += engagement
                
            # Analyze story elements
            if re.search(r'(when|then|after|before|finally)', content):
                factors['storytelling'] += engagement
        
        # Normalize factors
        return {
            factor: value/total_posts
            for factor, value in factors.items()
        }
    
    def _identify_viral_hooks(self, posts: List[Dict]) -> List[Dict]:
        """Identify viral hooks in successful content"""
        hooks = []
        
        for post in posts:
            content = post['content'].lower()
            identified_hooks = []
            
            # Analyze hook types
            if re.search(r'(how|why|what)', content):
                identified_hooks.append('curiosity')
            if re.search(r'(secret|hidden|exclusive)', content):
                identified_hooks.append('exclusivity')
            if re.search(r'(only|limited|last chance)', content):
                identified_hooks.append('urgency')
            if re.search(r'(you won\'t believe|amazing|incredible)', content):
                identified_hooks.append('surprise')
            if re.search(r'(free|win|discount|save)', content):
                identified_hooks.append('value')
                
            if identified_hooks:
                hooks.append({
                    'hooks': identified_hooks,
                    'engagement': post['engagement'],
                    'sample': content[:100] + '...'  # First 100 chars as example
                })
        
        # Sort by engagement and return top examples
        return sorted(hooks, key=lambda x: x['engagement'], reverse=True)[:5]
    
    def generate_content_suggestions(self, trends: Dict, industry: str) -> List[Dict]:
        """Generate content suggestions based on trend analysis"""
        suggestions = []
        
        # Get industry-specific templates
        templates = self._get_industry_templates(industry)
        
        # Generate suggestions using top patterns
        for category, percentage in trends['patterns'].items():
            if percentage > 30:  # If pattern appears in >30% of successful posts
                for template in templates:
                    suggestion = self._apply_pattern_to_template(template, category)
                    if suggestion:
                        suggestions.append({
                            'content': suggestion,
                            'pattern': category,
                            'type': template['type']
                        })
        
        # Add timing recommendations
        best_times = self._get_posting_schedule(trends['timing'])
        for suggestion in suggestions:
            suggestion['recommended_time'] = best_times
            
        return suggestions
    
    def _get_industry_templates(self, industry: str) -> List[Dict]:
        """Get industry-specific content templates"""
        templates = {
            'restaurant': [
                {
                    'type': 'behind_scenes',
                    'template': 'Step into our kitchen and discover [hook] our chefs [action] to create [dish]'
                },
                {
                    'type': 'special_offer',
                    'template': '[hook] this week only: [dish] with a special [offer]'
                },
                {
                    'type': 'customer_story',
                    'template': 'Meet [name], who discovered [hook] about our [dish] and now [result]'
                }
            ],
            'retail': [
                {
                    'type': 'product_launch',
                    'template': '[hook] introducing our new [product] that will [benefit]'
                },
                {
                    'type': 'styling_tip',
                    'template': '[hook] style secret: how to wear [product] for any [occasion]'
                },
                {
                    'type': 'customer_feature',
                    'template': 'See how [name] transformed their [space/look] with our [product]'
                }
            ],
            'fitness': [
                {
                    'type': 'workout_tip',
                    'template': '[hook] transform your [muscle_group] with this [duration] workout'
                },
                {
                    'type': 'success_story',
                    'template': 'From [before] to [after]: How [name] achieved [result] in [timeframe]'
                },
                {
                    'type': 'challenge',
                    'template': 'Join our [duration] [type] challenge and see [benefit]'
                }
            ]
        }
        return templates.get(industry.lower(), [])
    
    def _apply_pattern_to_template(self, template: Dict, pattern: str) -> str:
        """Apply viral pattern to content template"""
        content = template['template']
        
        # Apply pattern-specific modifications
        if pattern == 'storytelling':
            content = content.replace('[hook]', 'the incredible story of how')
        elif pattern == 'emotional':
            content = content.replace('[hook]', 'you won\'t believe')
        elif pattern == 'value_hooks':
            content = content.replace('[hook]', 'the secret to')
            
        return content
    
    def _get_posting_schedule(self, timing_data: Dict) -> List[str]:
        """Generate optimal posting schedule"""
        best_hours = timing_data['best_hours']
        best_days = timing_data['best_days']
        
        schedule = []
        for day in list(best_days.keys())[:3]:  # Top 3 days
            for hour in list(best_hours.keys())[:2]:  # Top 2 hours
                schedule.append(f"{day} at {hour:02d}:00")
                
        return schedule
