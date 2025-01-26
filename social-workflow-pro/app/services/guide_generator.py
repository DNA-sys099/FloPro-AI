from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
import os
from datetime import datetime
from typing import Dict, List

class GuideGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        
        # Free tools recommendations
        self.free_tools = {
            'photo_editing': [
                'GIMP - Professional photo editing',
                'Canva - Free design templates',
                'Snapseed - Mobile photo editing'
            ],
            'scheduling': [
                'Later - Free social media scheduling',
                'Buffer - Free plan available',
                'Facebook Creator Studio - Free scheduling'
            ],
            'analytics': [
                'Google Analytics - Free website tracking',
                'Facebook Insights - Free social analytics',
                'Instagram Insights - Free performance metrics'
            ]
        }
        
        # Business templates
        self.business_templates = {
            'restaurant': {
                'content_ideas': [
                    'Daily specials and menu highlights',
                    'Behind-the-scenes kitchen preparation',
                    'Chef spotlights and cooking tips',
                    'Customer reviews and testimonials',
                    'Food plating and presentation tips'
                ],
                'posting_schedule': [
                    'Monday: Week\'s specials preview',
                    'Wednesday: Chef\'s special feature',
                    'Friday: Weekend menu highlights',
                    'Saturday: Customer spotlight',
                    'Sunday: Weekly recap'
                ],
                'hashtags': [
                    '#FoodLover', '#LocalRestaurant', '#FoodieLife',
                    '#ChefLife', '#FoodPhotography', '#RestaurantLife'
                ]
            },
            'retail': {
                'content_ideas': [
                    'New product announcements',
                    'Styling tips and combinations',
                    'Customer success stories',
                    'Behind-the-scenes store operations',
                    'Product care guides'
                ],
                'posting_schedule': [
                    'Monday: New arrivals',
                    'Wednesday: Style guide',
                    'Friday: Weekend promotions',
                    'Saturday: Customer features',
                    'Sunday: Week ahead preview'
                ],
                'hashtags': [
                    '#ShopLocal', '#RetailTherapy', '#NewArrivals',
                    '#ShopSmall', '#StyleGuide', '#RetailLife'
                ]
            },
            'fitness': {
                'content_ideas': [
                    'Workout of the day',
                    'Form and technique tips',
                    'Member transformation stories',
                    'Nutrition and recipe ideas',
                    'Motivation and mindset tips'
                ],
                'posting_schedule': [
                    'Monday: Motivation Monday',
                    'Wednesday: Workout tips',
                    'Friday: Member spotlight',
                    'Saturday: Weekend warrior',
                    'Sunday: Week preparation'
                ],
                'hashtags': [
                    '#FitnessGoals', '#WorkoutMotivation', '#FitLife',
                    '#HealthyLifestyle', '#FitnessJourney', '#GymLife'
                ]
            }
        }
        
    def create_business_guide(self, business_name: str, business_type: str, target_audience: str) -> str:
        """Create a guide using free ReportLab library"""
        filename = f"{business_type}_growth_guide_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = os.path.join('guides', filename)
        os.makedirs('guides', exist_ok=True)
        
        # Create PDF
        doc = SimpleDocTemplate(
            filepath,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        # Build content
        story = []
        
        # Add cover
        self.add_cover(story, business_name, business_type)
        
        # Add free tools section
        self.add_free_tools_section(story)
        
        # Add business-specific content
        self.add_business_content(story, business_type, target_audience)
        
        # Generate PDF
        doc.build(story)
        return filepath
    
    def add_cover(self, story, business_name: str, business_type: str):
        """Add cover page using free styling"""
        title = Paragraph(
            f"Growth Strategy Guide for {business_name}",
            self.styles['Title']
        )
        subtitle = Paragraph(
            f"Specialized for {business_type.title()} Business Growth",
            self.styles['Heading1']
        )
        date = Paragraph(
            f"Created: {datetime.now().strftime('%B %d, %Y')}",
            self.styles['Normal']
        )
        
        story.extend([title, Spacer(1, 30), subtitle, Spacer(1, 20), date, Spacer(1, 60)])
    
    def add_free_tools_section(self, story):
        """Add section about free tools"""
        title = Paragraph("Free Tools for Your Business", self.styles['Heading1'])
        story.extend([title, Spacer(1, 20)])
        
        for category, tools in self.free_tools.items():
            subtitle = Paragraph(category.replace('_', ' ').title(), self.styles['Heading2'])
            story.extend([subtitle, Spacer(1, 10)])
            
            for tool in tools:
                tool_p = Paragraph(f"• {tool}", self.styles['Normal'])
                story.extend([tool_p, Spacer(1, 5)])
            
            story.append(Spacer(1, 20))
    
    def add_business_content(self, story, business_type: str, target_audience: str):
        """Add business-specific content"""
        templates = self.business_templates.get(business_type.lower(), self.get_generic_templates())
        
        # Add content strategy
        title = Paragraph(f"Content Strategy for {business_type.title()}", self.styles['Heading1'])
        story.extend([title, Spacer(1, 20)])
        
        for idea in templates['content_ideas']:
            idea_p = Paragraph(f"• {idea}", self.styles['Normal'])
            story.extend([idea_p, Spacer(1, 5)])
        
        # Add posting schedule
        schedule_title = Paragraph("Posting Schedule", self.styles['Heading2'])
        story.extend([Spacer(1, 20), schedule_title, Spacer(1, 10)])
        
        for time in templates['posting_schedule']:
            time_p = Paragraph(f"• {time}", self.styles['Normal'])
            story.extend([time_p, Spacer(1, 5)])
        
        # Add hashtags
        hashtag_title = Paragraph("Recommended Hashtags", self.styles['Heading2'])
        story.extend([Spacer(1, 20), hashtag_title, Spacer(1, 10)])
        
        hashtags = Paragraph(", ".join(templates['hashtags']), self.styles['Normal'])
        story.extend([hashtags, Spacer(1, 20)])
    
    def get_generic_templates(self) -> Dict:
        """Get generic templates"""
        return self.business_templates.get('retail', {})
