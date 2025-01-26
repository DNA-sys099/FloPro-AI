import nltk
from textblob import TextBlob
import re
from collections import defaultdict
from typing import List, Dict
import random

class ViralContentGenerator:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        
        self.viral_hooks = {
            'curiosity': [
                "The secret behind [topic]",
                "You won't believe what happens when [action]",
                "How we discovered [revelation]",
                "The truth about [topic]",
                "What nobody tells you about [topic]"
            ],
            'value': [
                "X essential tips for [goal]",
                "The ultimate guide to [topic]",
                "How to [action] in X simple steps",
                "X ways to improve your [topic]",
                "Transform your [topic] with these tricks"
            ],
            'emotional': [
                "Why this [topic] will make you [emotion]",
                "The inspiring story of [topic]",
                "How [topic] changed everything",
                "This [topic] will restore your faith in [concept]",
                "The most amazing [topic] you'll see today"
            ]
        }
        
        self.content_templates = {
            'restaurant': {
                'behind_scenes': [
                    "Watch our chef create [dish] from scratch 👨‍🍳",
                    "The secret ingredients in our famous [dish] 🤫",
                    "How we perfect each [dish] before serving 🔥",
                    "Early morning prep: Making fresh [dish] 🌅",
                    "Kitchen secrets: The making of [dish] 🏆"
                ],
                'special_offers': [
                    "Today only: [discount]% off our signature [dish] 🎉",
                    "Happy hour special: [dish] + [drink] combo 🍷",
                    "Weekend feast: All-you-can-eat [dish] 🍽️",
                    "Early bird special: Free [side] with any [dish] 🌟",
                    "Group dining deal: [dish] platter for [price] 👥"
                ],
                'customer_features': [
                    "Meet [name], our regular who loves our [dish] ❤️",
                    "Why [name] drives 2 hours for our [dish] 🚗",
                    "Customer spotlight: [name]'s favorite [dish] ⭐",
                    "[name]'s reaction to trying our new [dish] 😍",
                    "Family tradition: [name]'s weekly [dish] ritual 🏆"
                ]
            },
            'retail': {
                'product_launches': [
                    "Just dropped: The all-new [product] collection 🎉",
                    "Introducing our limited edition [product] ✨",
                    "New arrival alert: [product] now in stock 🛍️",
                    "First look: [product] in [color] 👀",
                    "Exclusive release: [product] [feature] edition 🌟"
                ],
                'styling_tips': [
                    "X ways to style your [product] 💫",
                    "From day to night: Styling [product] 🌙",
                    "Perfect pairs: [product] + [product] combo 👌",
                    "Seasonal styling: [product] for [season] 🍁",
                    "Style hack: Transform your [product] look 💭"
                ],
                'customer_features': [
                    "[name]'s [product] transformation ✨",
                    "Customer spotlight: [name] in [product] 🌟",
                    "Style story: How [name] rocks our [product] 💃",
                    "Before & After: [name]'s [product] journey 📸",
                    "Real customer review: [product] magic ⭐"
                ]
            },
            'fitness': {
                'workouts': [
                    "X-minute [body_part] workout 💪",
                    "Quick [intensity] [type] session 🔥",
                    "Full body burn: [duration] challenge 🏋️‍♀️",
                    "No equipment needed: [focus] workout 🎯",
                    "[body_part] transformation routine 💫"
                ],
                'transformations': [
                    "[name]'s X-week transformation story 🎉",
                    "Before & After: [name]'s [goal] journey 📸",
                    "How [name] lost X pounds in [timeframe] 💪",
                    "Member spotlight: [name]'s success story ⭐",
                    "Transformation Tuesday: [name]'s progress 🔄"
                ],
                'tips': [
                    "X essential tips for [goal] 📝",
                    "Nutrition hack: [tip] for better results 🥗",
                    "Form check: Perfect your [exercise] 🎯",
                    "Recovery tips for [body_part] training 🧘‍♀️",
                    "Pre-workout routine for maximum gains 💪"
                ]
            }
        }
        
    def generate_viral_content(self, industry: str, topic: str, hook_type: str) -> List[Dict]:
        """Generate viral content ideas"""
        # Get relevant templates
        industry_templates = self.content_templates.get(industry, {})
        hooks = self.viral_hooks.get(hook_type, [])
        
        content_ideas = []
        
        for category, templates in industry_templates.items():
            for template in templates:
                # Apply viral hooks
                for hook in hooks:
                    content = self._apply_hook(hook, template, topic)
                    
                    # Add engagement elements
                    content = self._add_engagement_elements(content)
                    
                    content_ideas.append({
                        'content': content,
                        'category': category,
                        'hook_type': hook_type,
                        'engagement_elements': self._analyze_engagement_elements(content)
                    })
        
        return content_ideas
    
    def _apply_hook(self, hook: str, template: str, topic: str) -> str:
        """Apply viral hook to template"""
        # Replace placeholders
        content = hook.replace('[topic]', topic)
        content = content + "\n\n" + template
        
        return content
    
    def _add_engagement_elements(self, content: str) -> str:
        """Add engagement-boosting elements"""
        elements = {
            'questions': [
                "What do you think?",
                "Have you tried this?",
                "Can you relate?",
                "What's your experience?",
                "Would you try this?"
            ],
            'calls_to_action': [
                "Double tap if you agree! ❤️",
                "Share this with someone who needs to see it 🙌",
                "Save this for later 🔖",
                "Drop a 👋 if you're trying this",
                "Tag your friends below 👇"
            ],
            'emojis': ["✨", "🔥", "💫", "⭐", "🎯", "💪", "🎉", "🌟"]
        }
        
        # Add question
        content += f"\n\n{random.choice(elements['questions'])}"
        
        # Add call-to-action
        content += f"\n\n{random.choice(elements['calls_to_action'])}"
        
        # Add emojis if not present
        if len(re.findall(r'[\U0001F300-\U0001F999]', content)) < 3:
            content = content + " " + " ".join(random.sample(elements['emojis'], 2))
        
        return content
    
    def _analyze_engagement_elements(self, content: str) -> Dict:
        """Analyze engagement elements in content"""
        return {
            'questions': len(re.findall(r'\?', content)),
            'calls_to_action': len(re.findall(r'(like|comment|share|save|tag|try)', content.lower())),
            'emojis': len(re.findall(r'[\U0001F300-\U0001F999]', content)),
            'sentiment': TextBlob(content).sentiment.polarity,
            'length': len(content)
        }
    
    def generate_hashtag_groups(self, industry: str, content: str) -> Dict[str, List[str]]:
        """Generate grouped hashtags for the content"""
        # Extract keywords
        words = nltk.word_tokenize(content.lower())
        keywords = [word for word, tag in nltk.pos_tag(words) 
                   if tag in ['NN', 'NNS', 'JJ', 'VB']]
        
        # Industry-specific hashtags
        industry_hashtags = {
            'restaurant': {
                'general': ['#foodie', '#instafood', '#foodstagram'],
                'quality': ['#homemade', '#fresh', '#delicious'],
                'experience': ['#foodlover', '#foodphotography', '#yummy']
            },
            'retail': {
                'general': ['#fashion', '#style', '#shopping'],
                'quality': ['#trendy', '#luxury', '#quality'],
                'experience': ['#shoplocal', '#boutique', '#musthave']
            },
            'fitness': {
                'general': ['#fitness', '#workout', '#gym'],
                'quality': ['#strong', '#healthy', '#fit'],
                'experience': ['#motivation', '#fitnessmotivation', '#lifestyle']
            }
        }
        
        # Get industry hashtags
        hashtag_groups = industry_hashtags.get(industry, {})
        
        # Add content-specific hashtags
        content_hashtags = [f"#{keyword}" for keyword in set(keywords) 
                          if len(keyword) > 3][:5]
        hashtag_groups['content'] = content_hashtags
        
        return hashtag_groups
    
    def generate_content_series(self, industry: str, topic: str, duration: int) -> List[Dict]:
        """Generate a series of related content posts"""
        series = []
        
        # Series templates
        series_templates = {
            'restaurant': {
                'behind_the_menu': [
                    "The inspiration behind [dish]",
                    "How we source ingredients for [dish]",
                    "Chef's special technique for [dish]",
                    "The story of [dish]",
                    "Customer favorites: Why [dish] is special"
                ],
                'cooking_journey': [
                    "Morning prep: Fresh ingredients",
                    "Afternoon skills: Perfecting [technique]",
                    "Evening service: Plating [dish]",
                    "Late night: Chef's tasting",
                    "Weekend special: Creating [dish]"
                ]
            },
            'retail': {
                'style_guide': [
                    "Essential pieces for [season]",
                    "How to mix and match [items]",
                    "Accessorizing your [item]",
                    "Color combinations for [item]",
                    "Dress up or down: [item] versatility"
                ],
                'collection_story': [
                    "Design inspiration",
                    "Material selection",
                    "Production process",
                    "Styling options",
                    "Customer stories"
                ]
            },
            'fitness': {
                'transformation': [
                    "Starting point: Assessment",
                    "Week 1: Foundation building",
                    "Week 2: Increasing intensity",
                    "Week 3: Breaking plateaus",
                    "Final results and tips"
                ],
                'technique_mastery': [
                    "Basic form guide",
                    "Common mistakes to avoid",
                    "Advanced variations",
                    "Progress tracking",
                    "Success stories"
                ]
            }
        }
        
        # Get relevant templates
        industry_series = series_templates.get(industry, {})
        series_type = random.choice(list(industry_series.keys()))
        templates = industry_series[series_type]
        
        # Generate series
        for i, template in enumerate(templates[:duration]):
            content = self._apply_hook(
                random.choice(self.viral_hooks['value']),
                template,
                topic
            )
            content = self._add_engagement_elements(content)
            
            series.append({
                'day': i + 1,
                'content': content,
                'type': series_type,
                'hashtags': self.generate_hashtag_groups(industry, content)
            })
        
        return series
