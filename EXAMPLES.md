# Pricing Agent Examples

This file contains example scenarios demonstrating how the Pricing Agent recommends prices for different types of products and services.

## Example 1: SaaS Product (B2B)

**Input:**
- Product: Cloud Analytics Platform
- Type: Software/Digital product
- Customer Type: B2B (Other businesses)
- Industry: SaaS
- Unit Cost: $5 (per user per month)
- Market Position: Established competitor
- Uniqueness: Somewhat differentiated
- Competitor Price: $49
- Expected Volume: 500 users/month
- Customer LTV: $2400

**Expected Recommendation:**
- Strategy: Subscription pricing
- Price Range: $120-$360/month (based on LTV)
- Or competitive pricing: $44-$54/month (based on competitors)
- Suggested approach: Tiered pricing (Basic $39, Pro $79, Enterprise $149)

---

## Example 2: Physical Product (B2C)

**Input:**
- Product: Handcrafted Leather Wallet
- Type: Product (physical good)
- Customer Type: B2C (Individual consumers)
- Industry: Retail
- Unit Cost: $30
- Market Position: Niche player
- Uniqueness: Highly innovative/unique
- Competitor Price: Unknown
- Expected Volume: 100 units/month

**Expected Recommendation:**
- Strategy: Value-based pricing
- Price Range: $36-$90 (20-200% premium over cost)
- Suggested Target: $63
- Profit Margin: 52%
- Monthly Revenue: $6,300
- Monthly Profit: $3,300

---

## Example 3: Consulting Service (B2B)

**Input:**
- Product: Digital Marketing Consulting
- Type: Service
- Customer Type: B2B (Other businesses)
- Industry: Consulting
- Unit Cost: $100/hour (including overhead)
- Market Position: Established competitor
- Uniqueness: Somewhat differentiated
- Competitor Price: $150/hour
- Expected Volume: 80 hours/month
- Customer LTV: $50,000

**Expected Recommendation:**
- Strategy: Value-based pricing
- Price Range: $120-$300/hour
- Suggested Target: $210/hour
- Profit Margin: 52%
- Monthly Revenue: $16,800
- Monthly Profit: $8,800

---

## Example 4: New Market Entry Product

**Input:**
- Product: Smart Home Device
- Type: Product (physical good)
- Customer Type: B2C (Individual consumers)
- Industry: Retail
- Unit Cost: $25
- Market Position: New market entry
- Uniqueness: Similar to competitors
- Competitor Price: $79
- Expected Volume: 200 units/month

**Expected Recommendation:**
- Strategy: Penetration pricing
- Price Range: $47-$67 (60-85% of competitor price)
- Suggested Target: $57
- Comparison: 28% lower than competitors
- Monthly Revenue: $11,400
- Monthly Profit: $6,400
- Tips: Focus on customer acquisition, plan to increase prices after gaining market share

---

## Example 5: Premium/Luxury Product

**Input:**
- Product: Limited Edition Watch
- Type: Product (physical good)
- Customer Type: B2C (Individual consumers)
- Industry: Luxury
- Unit Cost: $200
- Market Position: Market leader
- Uniqueness: Highly innovative/unique
- Competitor Price: $800
- Expected Volume: 20 units/month

**Expected Recommendation:**
- Strategy: Price skimming
- Price Range: $260-$500
- Suggested Target: $380
- Profit Margin: 47%
- Monthly Revenue: $7,600
- Monthly Profit: $3,600
- Tips: Emphasize exclusivity, target early adopters, maintain premium positioning

---

## Example 6: Manufacturing Component (B2B)

**Input:**
- Product: Industrial Bearing
- Type: Product (physical good)
- Customer Type: B2B (Other businesses)
- Industry: Manufacturing
- Unit Cost: $15
- Market Position: Established competitor
- Uniqueness: Commodity
- Competitor Price: $22
- Expected Volume: 1000 units/month

**Expected Recommendation:**
- Strategy: Competitive pricing
- Price Range: $19.80-$24.20 (90-110% of competitor price)
- Suggested Target: $22
- Profit Margin: 32%
- Monthly Revenue: $22,000
- Monthly Profit: $7,000
- Tips: Monitor competitor prices, differentiate on service/delivery

---

## Example 7: Subscription Box Service

**Input:**
- Product: Monthly Snack Box
- Type: Subscription/Membership
- Customer Type: B2C (Individual consumers)
- Industry: E-commerce
- Unit Cost: $12 (cost of goods + shipping)
- Market Position: Niche player
- Uniqueness: Somewhat differentiated
- Competitor Price: $29.99
- Expected Volume: 300 subscribers
- Customer LTV: $500

**Expected Recommendation:**
- Strategy: Subscription pricing
- Price Range: $25-$75/month (5-15% of LTV)
- Competitive check: $27-$33/month
- Suggested Target: $29.99 (match competition)
- Profit Margin: 60%
- Monthly Revenue: $8,997
- Monthly Profit: $5,397
- Tips: Offer annual discount (15% off), focus on retention

---

## Key Takeaways

1. **Cost-Plus** works well for commodities and manufacturing with predictable costs
2. **Value-Based** maximizes profit for differentiated products and services
3. **Competitive** is essential when entering established markets
4. **Penetration** helps gain market share but requires volume to be profitable
5. **Skimming** works for innovative products but requires strong differentiation
6. **Subscription** should balance LTV with competitive market rates

## Testing Your Pricing

After getting a recommendation:
1. Start with the suggested target price
2. Test with a small customer segment
3. Monitor conversion rates and customer feedback
4. Adjust based on data
5. Re-run the agent as market conditions change
