/**
 * Pricing Agent Web Application
 * Handles form interactions and displays results
 */

// Initialize calculator
const calculator = new PricingCalculator();

// Get form elements
const form = document.getElementById('pricingForm');
const resultsDiv = document.getElementById('results');
const resultsContent = document.getElementById('resultsContent');
const newCalculationBtn = document.getElementById('newCalculation');
const productTypeSelect = document.getElementById('productType');
const ltvGroup = document.getElementById('ltvGroup');

// Show/hide LTV field based on product type
productTypeSelect.addEventListener('change', function() {
    const type = this.value.toLowerCase();
    if (type.includes('subscription') || type.includes('service')) {
        ltvGroup.style.display = 'block';
    } else {
        ltvGroup.style.display = 'none';
    }
});

// Handle form submission
form.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Collect form data
    const formData = new FormData(form);
    const productInfo = {
        name: formData.get('productName'),
        type: formData.get('productType'),
        industry: formData.get('industry'),
        customerType: formData.get('customerType'),
        marketPosition: formData.get('marketPosition'),
        uniqueness: formData.get('uniqueness'),
        unitCost: formData.get('unitCost'),
        competitorPrice: formData.get('competitorPrice') || null,
        expectedVolume: formData.get('expectedVolume') || null,
        customerLTV: formData.get('customerLTV') || null
    };
    
    // Calculate recommendation
    const recommendation = calculator.calculatePriceRecommendation(productInfo);
    
    // Display results
    displayResults(recommendation);
    
    // Scroll to results
    resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });
});

// Handle form reset
form.addEventListener('reset', function() {
    resultsDiv.style.display = 'none';
    ltvGroup.style.display = 'none';
});

// Handle new calculation button
newCalculationBtn.addEventListener('click', function() {
    resultsDiv.style.display = 'none';
    form.reset();
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Display results function
function displayResults(recommendation) {
    const { minPrice, maxPrice, targetPrice, details, productInfo } = recommendation;
    const unitCost = parseFloat(productInfo.unitCost) || 0;
    
    // Calculate margins
    let marginPercent = 0;
    let markupPercent = 0;
    if (unitCost > 0 && targetPrice > 0) {
        marginPercent = ((targetPrice - unitCost) / targetPrice) * 100;
        markupPercent = ((targetPrice - unitCost) / unitCost) * 100;
    }
    
    // Build results HTML
    let html = `
        <div class="result-summary">
            <div class="result-product">
                <h4>${escapeHtml(productInfo.name)}</h4>
                <p class="product-meta">Unit Cost: <strong>$${formatNumber(unitCost)}</strong></p>
            </div>
            
            <div class="result-pricing">
                <div class="price-range">
                    <span class="label">Recommended Price Range</span>
                    <span class="range">$${formatNumber(minPrice)} - $${formatNumber(maxPrice)}</span>
                </div>
                <div class="target-price">
                    <span class="label">Target Price</span>
                    <span class="price">$${formatNumber(targetPrice)}</span>
                </div>
            </div>
            
            <div class="result-metrics">
                <div class="metric">
                    <span class="metric-label">Profit Margin</span>
                    <span class="metric-value">${formatNumber(marginPercent)}%</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Markup</span>
                    <span class="metric-value">${formatNumber(markupPercent)}%</span>
                </div>
            </div>
        </div>
        
        <div class="result-strategy">
            <h4>Recommended Strategy</h4>
            <div class="strategy-info">
                <div class="strategy-name">${formatStrategyName(details.strategy)}</div>
                <p class="strategy-description">${escapeHtml(details.strategyDescription)}</p>
                <p class="strategy-best-for"><strong>Best for:</strong> ${escapeHtml(details.bestFor)}</p>
            </div>
        </div>
    `;
    
    // Add insights section
    html += '<div class="result-insights"><h4>Pricing Insights</h4><ul>';
    
    if (productInfo.competitorPrice && parseFloat(productInfo.competitorPrice) > 0) {
        const compPrice = parseFloat(productInfo.competitorPrice);
        const diffPercent = ((targetPrice - compPrice) / compPrice) * 100;
        const comparison = diffPercent > 0 ? 'higher' : 'lower';
        html += `<li>Your target price is ${formatNumber(Math.abs(diffPercent))}% ${comparison} than competitors</li>`;
    }
    
    if (productInfo.expectedVolume && parseInt(productInfo.expectedVolume) > 0) {
        const volume = parseInt(productInfo.expectedVolume);
        const monthlyRevenue = volume * targetPrice;
        const monthlyProfit = volume * (targetPrice - unitCost);
        html += `<li>Expected monthly revenue: $${formatNumber(monthlyRevenue)}</li>`;
        html += `<li>Expected monthly profit: $${formatNumber(monthlyProfit)}</li>`;
    }
    
    html += '</ul></div>';
    
    // Add strategy tips
    const tips = calculator.getStrategyTips(details.strategy);
    if (tips.length > 0) {
        html += `<div class="result-tips">
            <h4>Tips for ${formatStrategyName(details.strategy)}</h4>
            <ul>`;
        tips.forEach(tip => {
            html += `<li>${escapeHtml(tip)}</li>`;
        });
        html += '</ul></div>';
    }
    
    // Add best practices
    html += `
        <div class="result-footer">
            <p><strong>Remember:</strong> Pricing is both art and science. Test different price points and gather customer feedback to optimize your pricing strategy.</p>
        </div>
    `;
    
    resultsContent.innerHTML = html;
    resultsDiv.style.display = 'block';
}

// Helper functions
function formatNumber(num) {
    if (num === null || num === undefined || isNaN(num)) {
        return '0.00';
    }
    return Number(num).toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

function formatStrategyName(strategy) {
    return strategy.split('_').map(word => 
        word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ');
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}
