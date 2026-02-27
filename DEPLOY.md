# Deployment Guide for GitHub Pages

## 1. Verify Static Files
Your site has been converted to pure HTML/CSS/JS.
The key files are in the root directory:
- `index.html` (Home)
- `projects.html`
- `about.html`
- `contact.html`
- `project-*.html` (Project details)

## 2. Push to GitHub
Since your site is now static, you can simply push these files to your repository.

1.  **Initialize Git** (if not done):
    ```bash
    git init
    git add .
    git commit -m "Converted to static HTML site"
    ```

2.  **Create a Repository on GitHub**:
    - Go to [github.com/new](https://github.com/new)
    - Name it (e.g., `portfolio`)
    - Create repository.

3.  **Link and Push**:
    ```bash
    git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
    git branch -M main
    git push -u origin main
    ```

## 3. Configure GitHub Pages
1.  Go to your repository settings on GitHub.
2.  Click on **Pages** in the left sidebar.
3.  Under **Build and deployment**:
    - Source: **Deploy from a branch**
    - Branch: **main**
    - Folder: **/(root)**
4.  Click **Save**.

Your site will be live at `https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/`.
