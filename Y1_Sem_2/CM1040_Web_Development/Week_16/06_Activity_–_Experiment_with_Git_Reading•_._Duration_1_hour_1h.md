# Activity – Experiment with Git Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/DmNH2/activity-experiment-with-git)

Here is a complete solution for the problem:

**Git and GitHub Lab**

**Initial Setup**

1. Install Git on your operating system (Windows, macOS, or Linux).
2. Verify Git installation by typing: `git --version`
3. Configure Git with your username and email:
	* `git config --global user.name "Your Name"`
	* `git config --global user.email "your.email@example.com"`

**Local Repository**

1. Create a new directory for your project.
2. Initialize a new Git repository: `git init`
3. Create a new file (e.g., `index.html`) using a text editor or file browser.
4. Check the status of the repository: `git status`
5. Add the new file to the staging area: `git add index.html`
6. Commit the file to the repository: `git commit -m "First commit"`
7. Modify an existing file:
	* `echo "<h2>Welcome to my project</h2>" >> index.html`
8. Check the status and view changes: `git status`, `git diff`
9. Stage and commit the changes: `git add index.html`, `git commit -m "Updated index.html with a welcome message"`
10. View commit history: `git log`

**Remote Repository on GitHub**

1. Create a new repository on GitHub.
2. Add the GitHub repository as a remote:
	* `git remote add origin https://github.com/yourusername/myproject.git`
3. Push your local repository to GitHub:
	* `git push -u origin master`
4. Make additional changes to your local repository:
	* Edit `index.html` or any other file.
5. Stage, commit, and push the changes to GitHub: `git add`, `git commit -m`, `git push`.
6. Pull changes from GitHub (if any): `git pull origin master`

**Reflection**

1. What steps did you follow to push your local repository to GitHub?
Answer: I followed these steps:
	* Created a new repository on GitHub.
	* Added the GitHub repository as a remote using `git remote add`.
	* Pushed my local repository to GitHub using `git push -u origin master`.
2. How did you verify that your changes were successfully pushed to GitHub?
Answer: I used `git status` and `git log` to view the commit history.
3. What are the benefits of using a remote repository like GitHub for your projects?
Answer: Using a remote repository like GitHub provides several benefits, including:
	* Collaboration with others.
	* Version control.
	* Backup and recovery of files.
4. How can you collaborate with others using GitHub?
Answer: To collaborate with others on GitHub, you can:
	* Invite team members to contribute to the repository.
	* Assign tasks and track progress.
	* Use pull requests to review changes before merging.

**Additional Practice**

1. Create and commit a `README.md` file.
2. Try using the `git rm --cached <file>` command to unstage a file.
3. Amend a commit message using `git commit --amend`.

