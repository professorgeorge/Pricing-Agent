# GitHub Pages Setup Instructions

This repository now includes a landing page that can be deployed to GitHub Pages.

## Files

- **index.html** - Main landing page
- **styles.css** - Styling for the landing page
- **.github/workflows/pages.yml** - GitHub Actions workflow for deployment

## Enabling GitHub Pages

To enable GitHub Pages and deploy the landing page:

1. Go to your repository on GitHub
2. Click on **Settings**
3. In the left sidebar, click on **Pages**
4. Under **Source**, select **GitHub Actions**
5. The workflow will automatically deploy your page on the next push to the `main` branch

## Viewing Your Site

Once deployed, your site will be available at:
```
https://professorgeorge.github.io/pricingagent/
```

## Workflow Details

The GitHub Actions workflow (`.github/workflows/pages.yml`) will:
- Automatically trigger on every push to the `main` branch
- Can also be manually triggered from the Actions tab
- Deploy the entire repository root (including index.html) to GitHub Pages
- Provide the deployment URL in the workflow output

## Local Development

To test the landing page locally:

```bash
# Start a simple HTTP server
python -m http.server 8000

# Open your browser to:
# http://localhost:8000/index.html
```

## Customization

You can customize the landing page by editing:
- **index.html** - Update content, sections, links
- **styles.css** - Modify colors, fonts, layout
- Update the color scheme by changing CSS variables in `:root`
