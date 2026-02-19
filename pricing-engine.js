/**
 * Pricing Agent - JavaScript Implementation
 * Pricing calculation engine for web application
 */

class PricingKnowledgeBase {
    constructor() {
        this.pricingStrategies = {
            'cost_plus': {
                'description': 'Cost-plus pricing adds a markup percentage to the cost of goods',
                'typical_markup_b2c': [0.30, 0.50],  // 30-50% markup
                'typical_markup_b2b': [0.15, 0.30],  // 15-30% markup
                'best_for': 'Commodity products, manufacturing, retail'
            },
            'value_based': {
                'description': 'Price based on perceived customer value rather than cost',
                'typical_premium': [0.20, 2.00],  // 20-200% over cost
                'best_for': 'Unique products, innovative solutions, premium brands'
            },
            'competitive': {
                'description': 'Price relative to competitors',
                'typical_range': [0.90, 1.10],  // 90-110% of competitor price
                'best_for': 'Commoditized markets, high competition'
            },
            'penetration': {
                'description': 'Low initial price to gain market share',
                'typical_discount': [0.60, 0.85],  // 60-85% of market price
                'best_for': 'New market entry, building customer base'
            },
            'skimming': {
                'description': 'High initial price for innovative/unique products',
                'typical_premium': [1.30, 2.50],  // 130-250% of typical market price
                'best_for': 'Innovative products, first-to-market, luxury goods'
            },
            'subscription': {
                'description': 'Recurring pricing model',
                'ltv_multiplier': [0.05, 0.15],  // 5-15% of customer lifetime value per month
                'best_for': 'Software, services, content, membership models'
            }
        };
        
        this.industryFactors = {
            'software': {'typical_margin': 0.80, 'pricing_model': 'subscription'},
            'retail': {'typical_margin': 0.40, 'pricing_model': 'cost_plus'},
            'consulting': {'typical_margin': 0.50, 'pricing_model': 'value_based'},
            'manufacturing': {'typical_margin': 0.25, 'pricing_model': 'cost_plus'},
            'saas': {'typical_margin': 0.75, 'pricing_model': 'subscription'},
            'ecommerce': {'typical_margin': 0.35, 'pricing_model': 'competitive'},
            'luxury': {'typical_margin': 0.60, 'pricing_model': 'skimming'},
            'food_beverage': {'typical_margin': 0.30, 'pricing_model': 'cost_plus'},
        };
    }
    
    getStrategyRecommendation(productType, marketPosition, customerType) {
        if (marketPosition === 'new_market' || marketPosition === 'entry') {
            return 'penetration';
        } else if (productType === 'innovative' || marketPosition === 'leader') {
            return 'skimming';
        } else if (productType === 'commodity') {
            return 'competitive';
        } else if (customerType === 'b2b' && productType === 'service') {
            return 'value_based';
        } else if (productType === 'subscription') {
            return 'subscription';
        } else {
            return 'cost_plus';
        }
    }
}

class PricingCalculator {
    constructor() {
        this.kb = new PricingKnowledgeBase();
    }
    
    calculatePriceRecommendation(productInfo) {
        const unitCost = parseFloat(productInfo.unitCost) || 0;
        
        // Determine customer type
        let customerType = 'b2c';
        if (productInfo.customerType && productInfo.customerType.toLowerCase().includes('b2b')) {
            customerType = 'b2b';
        }
        
        // Determine product type for strategy
        let productType = 'product';
        if (productInfo.uniqueness && productInfo.uniqueness.toLowerCase().includes('innovative')) {
            productType = 'innovative';
        } else if (productInfo.uniqueness && productInfo.uniqueness.toLowerCase().includes('commodity')) {
            productType = 'commodity';
        } else if (productInfo.type && productInfo.type.toLowerCase().includes('subscription')) {
            productType = 'subscription';
        } else if (productInfo.type && productInfo.type.toLowerCase().includes('service')) {
            productType = 'service';
        }
        
        // Determine market position
        let marketPosition = 'established';
        if (productInfo.marketPosition && productInfo.marketPosition.toLowerCase().includes('new')) {
            marketPosition = 'entry';
        } else if (productInfo.marketPosition && productInfo.marketPosition.toLowerCase().includes('leader')) {
            marketPosition = 'leader';
        }
        
        // Get recommended strategy
        const strategy = this.kb.getStrategyRecommendation(productType, marketPosition, customerType);
        const strategyInfo = this.kb.pricingStrategies[strategy];
        
        // Calculate price range based on strategy
        let minPrice = unitCost;
        let maxPrice = unitCost;
        
        if (strategy === 'cost_plus') {
            const markupRange = strategyInfo[`typical_markup_${customerType}`];
            minPrice = unitCost * (1 + markupRange[0]);
            maxPrice = unitCost * (1 + markupRange[1]);
            
        } else if (strategy === 'value_based') {
            const premiumRange = strategyInfo['typical_premium'];
            minPrice = unitCost * (1 + premiumRange[0]);
            maxPrice = unitCost * (1 + premiumRange[1]);
            
        } else if (strategy === 'competitive') {
            const competitorPrice = parseFloat(productInfo.competitorPrice);
            if (competitorPrice && competitorPrice > 0) {
                const rangeMultiplier = strategyInfo['typical_range'];
                minPrice = competitorPrice * rangeMultiplier[0];
                maxPrice = competitorPrice * rangeMultiplier[1];
            } else {
                // Fallback to cost-plus if no competitor price
                minPrice = unitCost * 1.3;
                maxPrice = unitCost * 1.5;
            }
            
        } else if (strategy === 'penetration') {
            const competitorPrice = parseFloat(productInfo.competitorPrice);
            if (competitorPrice && competitorPrice > 0) {
                const discountRange = strategyInfo['typical_discount'];
                minPrice = competitorPrice * discountRange[0];
                maxPrice = competitorPrice * discountRange[1];
            } else {
                minPrice = unitCost * 1.1;
                maxPrice = unitCost * 1.3;
            }
            
        } else if (strategy === 'skimming') {
            const premiumRange = strategyInfo['typical_premium'];
            minPrice = unitCost * premiumRange[0];
            maxPrice = unitCost * premiumRange[1];
            
        } else if (strategy === 'subscription') {
            const customerLTV = parseFloat(productInfo.customerLTV);
            if (customerLTV && customerLTV > 0) {
                const ltvMult = strategyInfo['ltv_multiplier'];
                minPrice = customerLTV * ltvMult[0];
                maxPrice = customerLTV * ltvMult[1];
            } else {
                // Fallback to cost-plus
                minPrice = unitCost * 1.3;
                maxPrice = unitCost * 1.5;
            }
        }
        
        // Apply industry adjustments if available
        const industry = (productInfo.industry || '').toLowerCase().replace(/\s+/g, '_').replace(/\//g, '_');
        if (this.kb.industryFactors[industry]) {
            const industryInfo = this.kb.industryFactors[industry];
            const targetMargin = industryInfo['typical_margin'];
            // Adjust prices to meet industry margin
            const industryPrice = unitCost / (1 - targetMargin);
            // Blend with strategy-based price
            minPrice = (minPrice + industryPrice * 0.9) / 2;
            maxPrice = (maxPrice + industryPrice * 1.1) / 2;
        }
        
        // Ensure minimum profitability
        minPrice = Math.max(minPrice, unitCost * 1.05);  // At least 5% margin
        
        const recommendationDetails = {
            strategy: strategy,
            strategyDescription: strategyInfo['description'],
            bestFor: strategyInfo['best_for'],
            customerType: customerType,
            productType: productType,
            marketPosition: marketPosition
        };
        
        return {
            minPrice: minPrice,
            maxPrice: maxPrice,
            targetPrice: (minPrice + maxPrice) / 2,
            details: recommendationDetails,
            productInfo: productInfo
        };
    }
    
    getStrategyTips(strategy) {
        const tips = {
            'cost_plus': [
                'Ensure all costs are accurately captured (materials, labor, overhead)',
                'Consider volume discounts for larger orders',
                'Monitor costs regularly and adjust prices accordingly'
            ],
            'value_based': [
                'Focus on communicating unique value propositions',
                'Gather customer feedback on perceived value',
                'Consider premium packaging or service bundles'
            ],
            'competitive': [
                'Regularly monitor competitor pricing changes',
                'Differentiate on service, quality, or features to justify premium',
                'Consider price matching guarantees'
            ],
            'penetration': [
                'Plan timeline to gradually increase prices as you gain market share',
                'Focus on customer acquisition and retention',
                'Ensure you can sustain lower margins initially'
            ],
            'skimming': [
                'Emphasize innovation and unique features',
                'Target early adopters willing to pay premium',
                'Plan to lower prices as market matures and competition increases'
            ],
            'subscription': [
                'Offer multiple tiers (basic, pro, enterprise)',
                'Consider annual discounts (10-20% off monthly price)',
                'Focus on reducing churn to maximize lifetime value'
            ]
        };
        
        return tips[strategy] || [];
    }
}
