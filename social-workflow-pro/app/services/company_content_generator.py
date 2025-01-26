from typing import Dict, List
import openai
from ..core.config import settings
from datetime import datetime

class CompanyContentGenerator:
    def __init__(self):
        openai.api_key = settings.OPENAI_API_KEY
        
    async def setup_company_profile(
        self,
        company_name: str,
        industry: str,
        products_services: List[str],
        unique_value_props: List[str],
        target_audience: List[str],
        brand_voice: str,
        company_achievements: List[str]
    ):
        """Set up detailed company profile for content generation"""
        self.company_profile = {
            "name": company_name,
            "industry": industry,
            "products_services": products_services,
            "value_props": unique_value_props,
            "target_audience": target_audience,
            "brand_voice": brand_voice,
            "achievements": company_achievements
        }
        return self.company_profile

    async def generate_product_showcase(self, product: Dict):
        """Generate engaging product-focused content"""
        prompts = [
            f"Highlight how {product['name']} solves customer problems",
            f"Share interesting features of {product['name']} without overselling",
            f"Show {product['name']} in action with real use cases",
            f"Share customer success story with {product['name']}"
        ]
        
        return {
            "content_variations": await self._generate_safe_content(prompts),
            "suggested_visuals": self._suggest_product_visuals(product),
            "hashtags": self._generate_product_hashtags(product),
            "best_posting_times": await self._get_optimal_product_timing(product)
        }

    async def generate_service_highlights(self, service: Dict):
        """Generate content highlighting company services"""
        prompts = [
            f"Explain how {service['name']} helps customers",
            f"Share the process of {service['name']} delivery",
            f"Highlight the expertise behind {service['name']}",
            f"Show the results customers get from {service['name']}"
        ]
        
        return {
            "content_variations": await self._generate_safe_content(prompts),
            "suggested_visuals": self._suggest_service_visuals(service),
            "hashtags": self._generate_service_hashtags(service),
            "best_posting_times": await self._get_optimal_service_timing(service)
        }

    async def generate_company_updates(self, update_type: str):
        """Generate content about company news and achievements"""
        safe_topics = {
            "growth": "Company expansion and new opportunities",
            "innovation": "New features and improvements",
            "community": "Community involvement and giving back",
            "achievement": "Awards and certifications",
            "culture": "Company culture and values"
        }
        
        prompts = self._create_update_prompts(safe_topics[update_type])
        
        return {
            "content_variations": await self._generate_safe_content(prompts),
            "suggested_visuals": self._suggest_update_visuals(update_type),
            "hashtags": self._generate_update_hashtags(update_type),
            "best_posting_times": await self._get_optimal_timing(update_type)
        }

    async def generate_educational_content(self, topic: str):
        """Generate educational content related to company expertise"""
        return {
            "how_to_guides": await self._generate_how_to_content(topic),
            "tips_and_tricks": await self._generate_tips_content(topic),
            "industry_insights": await self._generate_insight_content(topic),
            "best_practices": await self._generate_best_practices(topic)
        }

    async def _generate_safe_content(self, prompts: List[str]) -> List[str]:
        """Generate safe, non-controversial content"""
        system_prompt = """
        Create engaging social media content following these rules:
        1. Focus only on factual information
        2. Avoid opinions or controversial topics
        3. Be positive and solution-focused
        4. Don't compare with competitors
        5. Use clear, professional language
        6. Include specific benefits or value
        7. Be authentic and honest
        """
        
        content_variations = []
        for prompt in prompts:
            response = await openai.ChatCompletion.acreate(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            content_variations.append(response.choices[0].message.content)
            
        return content_variations

    def _suggest_product_visuals(self, product: Dict) -> List[Dict]:
        """Suggest visuals for product content"""
        return [
            {"type": "product_photo", "description": "Product in use"},
            {"type": "feature_showcase", "description": "Key features highlight"},
            {"type": "tutorial", "description": "How-to guide"},
            {"type": "results", "description": "Before/After results"}
        ]

    def _suggest_service_visuals(self, service: Dict) -> List[Dict]:
        """Suggest visuals for service content"""
        return [
            {"type": "process", "description": "Service delivery process"},
            {"type": "team", "description": "Expert team members"},
            {"type": "results", "description": "Client results"},
            {"type": "testimonial", "description": "Client testimonial"}
        ]

    def _generate_product_hashtags(self, product: Dict) -> List[str]:
        """Generate relevant product hashtags"""
        base_hashtags = [
            f"#{self.company_profile['name'].replace(' ', '')}",
            f"#{product['name'].replace(' ', '')}",
            f"#{self.company_profile['industry'].replace(' ', '')}"
        ]
        return base_hashtags + self._generate_safe_hashtags(product)

    def _generate_service_hashtags(self, service: Dict) -> List[str]:
        """Generate relevant service hashtags"""
        base_hashtags = [
            f"#{self.company_profile['name'].replace(' ', '')}",
            f"#{service['name'].replace(' ', '')}",
            f"#{self.company_profile['industry'].replace(' ', '')}"
        ]
        return base_hashtags + self._generate_safe_hashtags(service)

    async def _get_optimal_timing(self, content_type: str) -> Dict:
        """Get optimal posting times based on content type and audience"""
        # Implementation for optimal timing
        pass

    def _create_update_prompts(self, update_topic: str) -> List[str]:
        """Create safe prompts for company updates"""
        # Implementation for update prompts
        pass

    def _suggest_update_visuals(self, update_type: str) -> List[Dict]:
        """Suggest visuals for company updates"""
        # Implementation for update visuals
        pass

    def _generate_update_hashtags(self, update_type: str) -> List[str]:
        """Generate hashtags for company updates"""
        # Implementation for update hashtags
        pass

    def _generate_safe_hashtags(self, item: Dict) -> List[str]:
        """Generate safe, relevant hashtags"""
        # Implementation for safe hashtags
        pass
