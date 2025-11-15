# GitHub Pages Deployment Guide

Your website is now ready to be deployed to GitHub Pages! Follow these steps:

## Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Repository name: `bhardwaj-hospital-website` (or any name you prefer)
5. Make sure it's set to **Public** (required for free GitHub Pages)
6. **Do NOT** initialize with README, .gitignore, or license (we already have files)
7. Click "Create repository"

## Step 2: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Run these in your terminal:

```bash
cd /home/nishv/projects/bhardwaj-hospital-website
git remote add origin https://github.com/YOUR_USERNAME/bhardwaj-hospital-website.git
git push -u origin main
```

**Note:** Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** tab
3. Scroll down to **Pages** in the left sidebar
4. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **Save**

## Step 4: Wait for Deployment

- GitHub Pages will take 1-2 minutes to build your site
- You'll see a green checkmark when it's ready
- Your site will be available at: `https://YOUR_USERNAME.github.io/bhardwaj-hospital-website/`

## Quick Commands Reference

```bash
# Navigate to project
cd /home/nishv/projects/bhardwaj-hospital-website

# Check status
git status

# Add changes
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push origin main
```

## Updating Your Website

Whenever you make changes:
1. Make your edits
2. Run: `git add .`
3. Run: `git commit -m "Description of changes"`
4. Run: `git push origin main`
5. GitHub Pages will automatically update in 1-2 minutes

## Custom Domain (Optional)

If you have a custom domain:
1. Go to repository Settings > Pages
2. Under "Custom domain", enter your domain
3. Update your domain's DNS records as instructed by GitHub

## Troubleshooting

- **404 Error**: Make sure `index.html` is in the root folder
- **Styles not loading**: Check that all CSS files are referenced correctly
- **Images not showing**: Verify image paths are relative (not absolute URLs)
- **Site not updating**: Wait 1-2 minutes and clear browser cache

## Repository Structure

Your website structure:
```
bhardwaj-hospital-website/
├── index.html          (Main page)
├── styles.css          (Styles)
├── script.js           (JavaScript)
├── Gemini_Generated_Image_dhpr2bdhpr2bdhpr.png
└── README.md
```

