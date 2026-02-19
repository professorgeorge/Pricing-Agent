# Pricing Agent

An intelligent pricing recommendation system that helps you determine optimal prices for your goods or services based on industry best practices, market positioning, and competitive analysis.

## Overview

The Pricing Agent is an interactive tool that:
- Asks targeted questions about your product/service
- Analyzes pricing strategies from B2B and B2C perspectives
- Recommends optimal price ranges based on proven methodologies
- Provides strategic insights and actionable pricing tips

## Features

### Comprehensive Pricing Strategies

The agent employs multiple pricing strategies:

1. **Cost-Plus Pricing**: Adds appropriate markup to your costs
   - B2C: 30-50% markup
   - B2B: 15-30% markup

2. **Value-Based Pricing**: Prices based on customer perceived value
   - Best for unique or innovative products
   - Premium pricing for differentiated offerings

3. **Competitive Pricing**: Positions price relative to competitors
   - Market-aware pricing
   - Strategic positioning (90-110% of competitor prices)

4. **Penetration Pricing**: Lower prices to gain market share
   - Ideal for new market entry
   - 60-85% of typical market price

5. **Price Skimming**: Premium pricing for innovative products
   - First-to-market advantage
   - 130-250% premium pricing

6. **Subscription Pricing**: Recurring revenue models
   - Based on customer lifetime value
   - 5-15% of LTV per month

### Industry-Specific Knowledge

Built-in expertise for multiple industries:
- Software/SaaS (80% margins)
- Retail (40% margins)
- Consulting (50% margins)
- Manufacturing (25% margins)
- E-commerce (35% margins)
- Luxury goods (60% margins)
- Food & Beverage (30% margins)

## Installation

No external dependencies required! Uses only Python standard library.

```bash
git clone https://github.com/professorgeorge/pricingagent.git
cd pricingagent
```

## Usage

Run the pricing agent:

```bash
python pricing_agent.py
```

The agent will guide you through a series of questions:

1. Product/service name
2. Type (product, service, software, subscription)
3. Customer type (B2C, B2B, or both)
4. Industry category
5. Unit cost
6. Market position
7. Product uniqueness
8. Competitor pricing (if known)
9. Expected sales volume
10. Customer lifetime value (for services/subscriptions)

### Example Session

```
======================================================================
PRICING AGENT - Let's find the right price for your product/service
======================================================================

What is the name of your product or service?
Your answer: Premium Widget Pro

Is this a product or service?
  1. Product (physical good)
  2. Service
  3. Software/Digital product
  4. Subscription/Membership
Enter your choice (number): 1

Who are your primary customers?
  1. B2C (Individual consumers)
  2. B2B (Other businesses)
  3. Both B2B and B2C
Enter your choice (number): 2

...

======================================================================
PRICING RECOMMENDATION
======================================================================

Product/Service: Premium Widget Pro
Unit Cost: $25.00

Recommended Price Range:        $28.75 - $32.50
Suggested Target Price:         $30.62
Target Profit Margin:           18.4%
Target Markup:                  22.5%

Recommended Strategy:           Cost Plus
Strategy Description:           Cost-plus pricing adds a markup percentage to the cost of goods
Best For:                       Commodity products, manufacturing, retail
```

## Pricing Strategies Explained

### When to Use Each Strategy

**Cost-Plus**: 
- Manufacturing and production businesses
- Retail with consistent costs
- Commoditized products

**Value-Based**:
- Unique or patented products
- Professional services
- High-end consulting

**Competitive**:
- Crowded markets
- Similar product offerings
- Price-sensitive customers

**Penetration**:
- New market entry
- Building customer base
- High customer acquisition focus

**Skimming**:
- Innovative new products
- Limited competition
- Early adopter targeting

**Subscription**:
- SaaS products
- Membership programs
- Ongoing services

## How It Works

1. **Information Gathering**: Interactive Q&A session collects product details
2. **Strategy Selection**: AI-driven algorithm selects optimal pricing strategy
3. **Price Calculation**: Applies industry benchmarks and best practices
4. **Recommendation**: Provides price range with detailed analysis
5. **Insights**: Offers strategic tips and profitability projections

## Best Practices

- **Test Multiple Price Points**: Use the recommendations as a starting point
- **Monitor Competitors**: Keep pricing data current
- **Track Metrics**: Monitor conversion rates at different price points
- **Customer Feedback**: Validate perceived value with customers
- **Adjust Over Time**: Revisit pricing as market conditions change

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

See LICENSE file for details.

## Acknowledgments

Built with best practices from:
- Harvard Business Review pricing research
- B2B and B2C pricing strategies
- Industry-standard margin benchmarks
- Competitive positioning theory
