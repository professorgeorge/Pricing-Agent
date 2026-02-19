#!/usr/bin/env python3
"""
Pricing Agent - Recommend prices for goods or services based on user information.

This agent uses best practices from business-to-business (B2B) and business-to-consumer (B2C)
pricing strategies to recommend optimal prices or price ranges.
"""

import json
from typing import Dict, List, Optional, Tuple


class PricingKnowledgeBase:
    """Knowledge base containing pricing strategies and best practices."""
    
    def __init__(self):
        self.pricing_strategies = {
            'cost_plus': {
                'description': 'Cost-plus pricing adds a markup percentage to the cost of goods',
                'typical_markup_b2c': (0.30, 0.50),  # 30-50% markup
                'typical_markup_b2b': (0.15, 0.30),  # 15-30% markup
                'best_for': 'Commodity products, manufacturing, retail'
            },
            'value_based': {
                'description': 'Price based on perceived customer value rather than cost',
                'typical_premium': (0.20, 2.00),  # 20-200% over cost
                'best_for': 'Unique products, innovative solutions, premium brands'
            },
            'competitive': {
                'description': 'Price relative to competitors',
                'typical_range': (0.90, 1.10),  # 90-110% of competitor price
                'best_for': 'Commoditized markets, high competition'
            },
            'penetration': {
                'description': 'Low initial price to gain market share',
                'typical_discount': (0.60, 0.85),  # 60-85% of market price
                'best_for': 'New market entry, building customer base'
            },
            'skimming': {
                'description': 'High initial price for innovative/unique products',
                'typical_premium': (1.30, 2.50),  # 130-250% of typical market price
                'best_for': 'Innovative products, first-to-market, luxury goods'
            },
            'subscription': {
                'description': 'Recurring pricing model',
                'ltv_multiplier': (0.05, 0.15),  # 5-15% of customer lifetime value per month
                'best_for': 'Software, services, content, membership models'
            }
        }
        
        self.industry_factors = {
            'software': {'typical_margin': 0.80, 'pricing_model': 'subscription'},
            'retail': {'typical_margin': 0.40, 'pricing_model': 'cost_plus'},
            'consulting': {'typical_margin': 0.50, 'pricing_model': 'value_based'},
            'manufacturing': {'typical_margin': 0.25, 'pricing_model': 'cost_plus'},
            'saas': {'typical_margin': 0.75, 'pricing_model': 'subscription'},
            'ecommerce': {'typical_margin': 0.35, 'pricing_model': 'competitive'},
            'luxury': {'typical_margin': 0.60, 'pricing_model': 'skimming'},
            'food_beverage': {'typical_margin': 0.30, 'pricing_model': 'cost_plus'},
        }
    
    def get_strategy_recommendation(self, product_type: str, market_position: str, 
                                   customer_type: str) -> str:
        """Recommend a pricing strategy based on product and market characteristics."""
        if market_position == 'new_market' or market_position == 'entry':
            return 'penetration'
        elif product_type == 'innovative' or market_position == 'leader':
            return 'skimming'
        elif product_type == 'commodity':
            return 'competitive'
        elif customer_type == 'b2b' and product_type == 'service':
            return 'value_based'
        elif product_type == 'subscription':
            return 'subscription'
        else:
            return 'cost_plus'


class PricingAgent:
    """Interactive pricing agent that asks questions and recommends prices."""
    
    def __init__(self):
        self.kb = PricingKnowledgeBase()
        self.product_info: Dict = {}
        
    def ask_question(self, question: str, options: Optional[List[str]] = None) -> str:
        """Ask the user a question and get their response."""
        print(f"\n{question}")
        if options:
            for i, option in enumerate(options, 1):
                print(f"  {i}. {option}")
            while True:
                try:
                    choice = input("Enter your choice (number): ").strip()
                    idx = int(choice) - 1
                    if 0 <= idx < len(options):
                        return options[idx]
                    print("Invalid choice. Please try again.")
                except (ValueError, KeyboardInterrupt):
                    print("Invalid input. Please enter a number.")
        else:
            return input("Your answer: ").strip()
    
    def ask_yes_no(self, question: str) -> bool:
        """Ask a yes/no question."""
        response = self.ask_question(f"{question} (yes/no)")
        return response.lower() in ['yes', 'y']
    
    def gather_information(self):
        """Gather information about the product/service through questions."""
        print("\n" + "="*70)
        print("PRICING AGENT - Let's find the right price for your product/service")
        print("="*70)
        
        # Basic product information
        self.product_info['name'] = self.ask_question(
            "What is the name of your product or service?"
        )
        
        self.product_info['type'] = self.ask_question(
            "Is this a product or service?",
            ['Product (physical good)', 'Service', 'Software/Digital product', 'Subscription/Membership']
        )
        
        # Customer type
        self.product_info['customer_type'] = self.ask_question(
            "Who are your primary customers?",
            ['B2C (Individual consumers)', 'B2B (Other businesses)', 'Both B2B and B2C']
        )
        
        # Industry
        print("\nWhat industry does this fall under?")
        industries = list(self.kb.industry_factors.keys()) + ['Other']
        self.product_info['industry'] = self.ask_question(
            "Select your industry:",
            industries
        )
        
        # Cost information
        cost_str = self.ask_question(
            "What is your cost to produce/deliver one unit? (Enter number only, e.g., 50)"
        )
        try:
            self.product_info['unit_cost'] = float(cost_str)
        except ValueError:
            print("Invalid cost. Using 0 as default.")
            self.product_info['unit_cost'] = 0.0
        
        # Market position
        self.product_info['market_position'] = self.ask_question(
            "What is your market position?",
            ['New market entry', 'Established competitor', 'Market leader', 'Niche player']
        )
        
        # Product uniqueness
        self.product_info['uniqueness'] = self.ask_question(
            "How unique is your product/service?",
            ['Highly innovative/unique', 'Somewhat differentiated', 'Similar to competitors', 'Commodity']
        )
        
        # Competitor pricing
        has_competitors = self.ask_yes_no(
            "Do you know your competitors' prices?"
        )
        
        if has_competitors:
            comp_price_str = self.ask_question(
                "What is the average competitor price? (Enter number only)"
            )
            try:
                self.product_info['competitor_price'] = float(comp_price_str)
            except ValueError:
                self.product_info['competitor_price'] = None
        else:
            self.product_info['competitor_price'] = None
        
        # Volume expectations
        volume_str = self.ask_question(
            "How many units do you expect to sell per month? (Enter number only)"
        )
        try:
            self.product_info['expected_volume'] = int(volume_str)
        except ValueError:
            self.product_info['expected_volume'] = 0
        
        # Customer lifetime value (for services/subscriptions)
        if 'Subscription' in self.product_info['type'] or 'Service' in self.product_info['type']:
            ltv_str = self.ask_question(
                "What is the expected customer lifetime value? (total revenue per customer over their lifetime, enter number only)"
            )
            try:
                self.product_info['customer_ltv'] = float(ltv_str)
            except ValueError:
                self.product_info['customer_ltv'] = None
        
    def calculate_price_recommendation(self) -> Tuple[float, float, Dict]:
        """Calculate price recommendation based on gathered information."""
        unit_cost = self.product_info.get('unit_cost', 0)
        
        # Determine customer type
        customer_type = 'b2c'
        if 'B2B' in self.product_info.get('customer_type', ''):
            customer_type = 'b2b'
        
        # Determine product type for strategy
        product_type = 'product'
        if 'innovative' in self.product_info.get('uniqueness', '').lower():
            product_type = 'innovative'
        elif 'Commodity' in self.product_info.get('uniqueness', ''):
            product_type = 'commodity'
        elif 'Subscription' in self.product_info.get('type', ''):
            product_type = 'subscription'
        elif 'Service' in self.product_info.get('type', ''):
            product_type = 'service'
        
        # Determine market position
        market_position = 'established'
        if 'New' in self.product_info.get('market_position', ''):
            market_position = 'entry'
        elif 'leader' in self.product_info.get('market_position', '').lower():
            market_position = 'leader'
        
        # Get recommended strategy
        strategy = self.kb.get_strategy_recommendation(product_type, market_position, customer_type)
        strategy_info = self.kb.pricing_strategies[strategy]
        
        # Calculate price range based on strategy
        min_price = unit_cost
        max_price = unit_cost
        
        if strategy == 'cost_plus':
            markup_range = strategy_info[f'typical_markup_{customer_type}']
            min_price = unit_cost * (1 + markup_range[0])
            max_price = unit_cost * (1 + markup_range[1])
            
        elif strategy == 'value_based':
            premium_range = strategy_info['typical_premium']
            min_price = unit_cost * (1 + premium_range[0])
            max_price = unit_cost * (1 + premium_range[1])
            
        elif strategy == 'competitive':
            if self.product_info.get('competitor_price'):
                comp_price = self.product_info['competitor_price']
                range_multiplier = strategy_info['typical_range']
                min_price = comp_price * range_multiplier[0]
                max_price = comp_price * range_multiplier[1]
            else:
                # Fallback to cost-plus if no competitor price
                min_price = unit_cost * 1.3
                max_price = unit_cost * 1.5
                
        elif strategy == 'penetration':
            if self.product_info.get('competitor_price'):
                comp_price = self.product_info['competitor_price']
                discount_range = strategy_info['typical_discount']
                min_price = comp_price * discount_range[0]
                max_price = comp_price * discount_range[1]
            else:
                min_price = unit_cost * 1.1
                max_price = unit_cost * 1.3
                
        elif strategy == 'skimming':
            premium_range = strategy_info['typical_premium']
            min_price = unit_cost * premium_range[0]
            max_price = unit_cost * premium_range[1]
            
        elif strategy == 'subscription':
            if self.product_info.get('customer_ltv'):
                ltv = self.product_info['customer_ltv']
                ltv_mult = strategy_info['ltv_multiplier']
                min_price = ltv * ltv_mult[0]
                max_price = ltv * ltv_mult[1]
            else:
                # Fallback to cost-plus
                min_price = unit_cost * 1.3
                max_price = unit_cost * 1.5
        
        # Apply industry adjustments if available
        industry = self.product_info.get('industry', '').lower().replace(' ', '_').replace('/', '_')
        if industry in self.kb.industry_factors:
            industry_info = self.kb.industry_factors[industry]
            target_margin = industry_info['typical_margin']
            # Adjust prices to meet industry margin
            industry_price = unit_cost / (1 - target_margin)
            # Blend with strategy-based price
            min_price = (min_price + industry_price * 0.9) / 2
            max_price = (max_price + industry_price * 1.1) / 2
        
        # Ensure minimum profitability
        min_price = max(min_price, unit_cost * 1.05)  # At least 5% margin
        
        recommendation_details = {
            'strategy': strategy,
            'strategy_description': strategy_info['description'],
            'best_for': strategy_info['best_for'],
            'customer_type': customer_type,
            'product_type': product_type,
            'market_position': market_position
        }
        
        return min_price, max_price, recommendation_details
    
    def display_recommendation(self, min_price: float, max_price: float, details: Dict):
        """Display the pricing recommendation to the user."""
        print("\n" + "="*70)
        print("PRICING RECOMMENDATION")
        print("="*70)
        
        print(f"\nProduct/Service: {self.product_info['name']}")
        print(f"Unit Cost: ${self.product_info['unit_cost']:.2f}")
        
        print(f"\n{'Recommended Price Range:':<30} ${min_price:.2f} - ${max_price:.2f}")
        print(f"{'Suggested Target Price:':<30} ${(min_price + max_price) / 2:.2f}")
        
        # Calculate margins
        target_price = (min_price + max_price) / 2
        if self.product_info['unit_cost'] > 0:
            margin_pct = ((target_price - self.product_info['unit_cost']) / target_price) * 100
            markup_pct = ((target_price - self.product_info['unit_cost']) / self.product_info['unit_cost']) * 100
            print(f"{'Target Profit Margin:':<30} {margin_pct:.1f}%")
            print(f"{'Target Markup:':<30} {markup_pct:.1f}%")
        
        print(f"\n{'Recommended Strategy:':<30} {details['strategy'].replace('_', ' ').title()}")
        print(f"{'Strategy Description:':<30} {details['strategy_description']}")
        print(f"{'Best For:':<30} {details['best_for']}")
        
        # Additional insights
        print("\n" + "-"*70)
        print("PRICING INSIGHTS")
        print("-"*70)
        
        if self.product_info.get('competitor_price'):
            comp_price = self.product_info['competitor_price']
            target_price = (min_price + max_price) / 2
            diff_pct = ((target_price - comp_price) / comp_price) * 100
            print(f"• Your target price is {abs(diff_pct):.1f}% {'higher' if diff_pct > 0 else 'lower'} than competitors")
        
        if self.product_info.get('expected_volume'):
            volume = self.product_info['expected_volume']
            target_price = (min_price + max_price) / 2
            monthly_revenue = volume * target_price
            monthly_profit = volume * (target_price - self.product_info['unit_cost'])
            print(f"• Expected monthly revenue: ${monthly_revenue:,.2f}")
            print(f"• Expected monthly profit: ${monthly_profit:,.2f}")
        
        # Strategy-specific tips
        print(f"\n{'TIPS FOR ' + details['strategy'].upper() + ' PRICING:'}")
        
        if details['strategy'] == 'cost_plus':
            print("• Ensure all costs are accurately captured (materials, labor, overhead)")
            print("• Consider volume discounts for larger orders")
            print("• Monitor costs regularly and adjust prices accordingly")
            
        elif details['strategy'] == 'value_based':
            print("• Focus on communicating unique value propositions")
            print("• Gather customer feedback on perceived value")
            print("• Consider premium packaging or service bundles")
            
        elif details['strategy'] == 'competitive':
            print("• Regularly monitor competitor pricing changes")
            print("• Differentiate on service, quality, or features to justify premium")
            print("• Consider price matching guarantees")
            
        elif details['strategy'] == 'penetration':
            print("• Plan timeline to gradually increase prices as you gain market share")
            print("• Focus on customer acquisition and retention")
            print("• Ensure you can sustain lower margins initially")
            
        elif details['strategy'] == 'skimming':
            print("• Emphasize innovation and unique features")
            print("• Target early adopters willing to pay premium")
            print("• Plan to lower prices as market matures and competition increases")
            
        elif details['strategy'] == 'subscription':
            print("• Offer multiple tiers (basic, pro, enterprise)")
            print("• Consider annual discounts (10-20% off monthly price)")
            print("• Focus on reducing churn to maximize lifetime value")
        
        print("\n" + "="*70)
    
    def run(self):
        """Run the pricing agent interaction."""
        try:
            self.gather_information()
            min_price, max_price, details = self.calculate_price_recommendation()
            self.display_recommendation(min_price, max_price, details)
            
            print("\nThank you for using the Pricing Agent!")
            print("Remember: Pricing is both art and science. Test different price points")
            print("and gather customer feedback to optimize your pricing strategy.")
            
        except KeyboardInterrupt:
            print("\n\nPricing agent interrupted. Goodbye!")
        except Exception as e:
            print(f"\n\nAn error occurred: {e}")
            print("Please try again.")


def main():
    """Main entry point for the pricing agent."""
    agent = PricingAgent()
    agent.run()


if __name__ == "__main__":
    main()
