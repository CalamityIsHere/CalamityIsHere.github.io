# Signal Bench on GitHub Pages

Signal Bench is a four-page electrical engineering portfolio. The welcome page introduces your work, About me holds your background, Projects gathers your case studies, and Contact displays your public email once you add it. One clearly labeled illustrative waveform study shows how a case study looks.

## 1. Create a home for the website

1. Sign in to GitHub and create a **public repository**. GitHub Free includes Pages hosting for public repositories.
2. For a personal homepage, name the repository **YOUR-USERNAME.github.io**, replacing YOUR-USERNAME with your GitHub username. If you already use that repository, create a new one named **portfolio** to host this design at **https://YOUR-USERNAME.github.io/portfolio/**.
3. Select **Add a README file** when creating the repository so it has a branch. The supplied publishing workflow uses **main**. If your default branch has a different name, change the branch under `push` in `.github/workflows/pages.yml` to match.
4. Open the repository’s **Settings → Pages → Build and deployment**. Choose **GitHub Actions** as the source. The package includes the workflow.

[GitHub Pages site types and free hosting](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) · [Publishing source settings](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

## 2. Import the design and publish

1. **Unzip** the starter kit on your computer. Open the folder that contains `build.py`, `assets`, `content`, and `uploads`.
2. Make hidden files visible. On macOS press **Command + Shift + period** in Finder. On Windows select **View → Show → Hidden items** in File Explorer.
3. In the new GitHub repository, choose **Add file → Upload files**. Drag the **contents** of the extracted folder onto the upload area. Keep the folders intact. The root of the repository should contain the following:

   ```text
   .github/workflows/pages.yml   automatic publishing
   .pages.yml                    visual editor configuration
   .gitignore                    excludes local previews
   assets/                       design and welcome-page waveform
   content/                      profile and project write-ups
   uploads/                      project images
   build.py                      generates the website
   README.md                     this guide
   ```

4. Choose **Commit changes** to save the files on **main**. Check that `.pages.yml` and `.github/workflows/pages.yml` reached GitHub. If your browser skipped either hidden item, choose **Add file → Create new file**, enter its exact path, copy in its contents from the extracted kit, and commit. A slash in the filename creates a directory.
5. Open **Actions → Publish portfolio**. When the **deploy** job succeeds, follow the website link on the run, or open **Settings → Pages → Visit site**. Open each navigation link and the example project.

This first deployment displays the sample study and a neutral contact message. To personalize before your first public deployment, edit the content JSON files locally before uploading. All committed source files in a public repository are publicly readable, including projects you hide from the website.

## 3. Edit through a graphical dashboard

**Pages CMS is the recommended free editor for this kit.** Its browser forms cover personal details, project descriptions, the publish switch, and image uploads. Design and typography are controlled by the shared stylesheet.

1. Sign in with GitHub at [Pages CMS](https://app.pagescms.org/). Install its GitHub App and select your portfolio repository when choosing repository access.
2. Open that repository and the **main** branch in Pages CMS. The supplied `.pages.yml` defines **Portfolio settings** and **Projects**. If the app asks you to build a configuration, confirm that this file is at the repository root on the selected branch.
3. Open **Portfolio settings** to change Signal Bench to your name, edit your introductions and biography, and enter your public contact email. Save. The Contact page will display a clickable email address that opens the visitor’s email app.
4. Open **Projects**, create an entry, and give it a unique title and short summary. Add the design brief, circuit decisions, and measured results. Upload an optional schematic or bench photo and write a short image description. Switch **Show on website** on and save.
5. After the publishing run finishes, the new project appears alphabetically by filename in the archive, with a link to its full write-up. To remove the illustrative example from the website, open **Reading a damped oscillation**, turn **Show on website** off, and save.

[Pages CMS features and pricing](https://pagescms.org/) · [Connecting a GitHub repository](https://pagescms.org/docs/quick-start/)

## 4. Change the design or preview locally

**Visual Studio Code** is a free desktop option for editing the layout and colors directly. Open the extracted or cloned repository with **File → Open Folder**. Change `assets/style.css` for colors, type, spacing, and mobile layout. The variables at the top control the ink, paper, and rule colors. Page layouts live in `build.py`. For routine content changes, Pages CMS offers the simpler interface. [Visual Studio Code](https://code.visualstudio.com/)

To preview local edits, install Python 3 if needed. In the project folder, run `python3 build.py` on macOS/Linux or `py -3 build.py` on Windows. Open `_site/index.html` in a browser. Run the same command after each local edit and refresh. The build uses Python’s standard library. Upload changed source files or commit and push them to main. GitHub builds the public copy automatically.

## If a change does not appear

- **No publishing run** — Check the branch name and the workflow file path. Open the Actions tab and confirm workflows are enabled. You can start **Publish portfolio → Run workflow** manually.
- **First run failed** — Confirm Settings → Pages uses GitHub Actions, then rerun the failed job. The build log identifies a missing image or invalid JSON file by name or location.
- **Sample shows, new project missing** — Open the project in Pages CMS, turn on Show on website, save on main, and check that the newest deployment finished.
- **404** — Open the URL shown under Settings → Pages. A repository named portfolio includes /portfolio/ in its address. The site uses relative links, so both personal and project addresses work.

[GitHub Pages deployment workflow reference](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
