# Deployment Guide for GitHub Pages

## 1. Verify Build
You have successfully generated a static version of your site in the `build/` folder.
This folder contains:
- `index.html` (Home)
- `about`, `projects`, `contact` (HTML files without extensions, will be handled by GitHub Pages)
- `static/` (CSS, Images, JS)

## 2. Push to GitHub
If you haven't already, initialize a git repository and push your code.

1.  **Initialize Git** (if not done):
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
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
    - Folder: **/(root)** (We will deploy the `build` folder content to the root of a separate branch or configure it manually, but the easiest way for manual upload or simple flow is often just pushing the build folder content to a `gh-pages` branch).

**Easiest way for you right now:**
We can use a tool like `gh-pages` or simply push the contents of `build` to a `gh-pages` branch.

**Manual Step:**
1.  Run: `git checkout -b gh-pages`
2.  (We need to only commit the build folder contents, but since `build` is likely ignored or mixed, the cleanest way is often a separate deploy script or using a tool).

**BETTER ALTERNATIVE:**
Since you have the source code, just let GitHub build it? No, because it uses Flask.

**RECOMMENDED: Deploy the `build` folder.**
1.  Run this command to push only the `build` folder to the `gh-pages` branch:
    ```bash
    git add build && git commit -m "Build site"
    git subtree push --prefix build origin gh-pages
    ```
2.  Then in GitHub Pages settings, select `gh-pages` branch as source.

## Summary of Commands to Run Now:
```bash
# 1. Add all changes
git add .
git commit -m "Ready for deployment"

# 2. Push source code to main (optional but good)
# git push origin main

# 3. Push the build folder to gh-pages branch
git subtree push --prefix build origin gh-pages
```
Then go to GitHub -> Settings -> Pages -> Source: `gh-pages` branch.
