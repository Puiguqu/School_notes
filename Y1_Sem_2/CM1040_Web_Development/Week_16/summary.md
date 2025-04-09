# Week 16 - CM1040 Web Development - Topic 1: HTTP and HTML – The internet and HTTP - Week 1

## Topic 8 Week 2 introduction Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/a4akP/topic-8-week-2-introduction)

There is no text to summarize. The provided text appears to be a video transcript and additional page content related to Lesson 16 of Topic 8, specifically discussing version control and DevOps. However, there is no actual text to extract information from.

If you provide the relevant text, I can assist you in summarizing it in 8 sentences, preserving key information, formulae, links, and technical details.

---

## Introduction to Git: init and commit Video• . Duration: 9 minutes 9 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/coZzT/introduction-to-git-init-and-commit)

This is a transcript of an educational video about Git, a version control system used in software development and DevOps practices. The video provides a step-by-step introduction to Git, covering the basics of setting up a repository, adding files, committing changes, and understanding the commit log.

Here's a summary of the key points covered in the video:

1. **Introduction to Git**: The video explains what Git is, its importance in software development, and how it helps manage changes to code.
2. **Setting up an initial repository**: The video demonstrates how to set up an initial Git repository using the `git init` command.
3. **Adding files to the repository**: The video shows how to add files to the repository using the `git add` command and stage changes using the `git status` command.
4. **Committing changes**: The video explains how to commit changes to the repository using the `git commit` command, including adding a message and committing all staged files.
5. **Understanding the commit log**: The video demonstrates how to view the commit log using the `git log` command, which shows all commits made to the repository, including who made them and when.

The video also touches on some advanced topics, such as:

* **Remote services**: The video mentions that Git can be used with remote services, but it does not provide detailed information about this topic.
* **Branching and merging**: The video briefly mentions branching and merging, but does not provide a comprehensive explanation of these concepts.

Overall, the video provides a solid introduction to Git and its basics, making it suitable for beginners who want to learn about version control systems.

---

## Git: remotes, branching and merging Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/cIT2T/git-remotes-branching-and-merging)

This is a transcript of a video on Git, specifically covering the topics of remotes, branching, and merging.

The video begins by introducing the concept of remotes and how to add a remote repository server like GitLab or GitHub to a local repository. The speaker explains that when you push changes to a remote repository, others can pull those changes down from the remote repository.

Next, the speaker discusses the importance of branching in collaborative development. They explain that when multiple developers are working on different parts of the codebase, it's essential to work in separate branches to avoid conflicts and ensure that any changes made by one developer don't break the other developer's work.

The speaker then walks through the process of creating a new branch, making changes, committing those changes, and pushing them to the remote repository. They demonstrate how to create a new branch, make changes to the code, commit those changes, and push them to the remote repository.

Finally, the speaker discusses merging branches and resolving conflicts that may arise when integrating changes from one branch into another. They explain that using Git's merge feature allows developers to resolve any conflicts that may have arisen during the integration process.

Throughout the video, the speaker provides examples and demonstrations of each concept to help illustrate their explanations. The video concludes with a brief summary of the key takeaways from the video.

Some notable points from the transcript include:

* The importance of remotes in collaborative development
* The benefits of branching in collaborative development
* How to create and manage branches using Git
* How to resolve conflicts when merging branches

Overall, this video provides a comprehensive overview of remotes, branching, and merging in Git, which is essential for anyone working on software projects that involve multiple developers.

---

## DevOps practices Video• . Duration: 12 minutes 12 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/F9SML/devops-practices)

This appears to be a transcript of a video lecture on DevOps, specifically covering the topics of continuous integration, continuous delivery, infrastructure as code, monitoring and logging, and DevSecOps. The lecture is likely part of an online course or training program aimed at introducing students to DevOps practices.

The transcript covers the following topics:

1. Continuous Integration (CI): automation of tasks around improving code quality through testing and automated building.
2. Continuous Delivery: packaging up code into a deployable form for IT teams.
3. Infrastructure as Code (IaC): automating IT teams by turning them into scripts that spin up instances of an app depending on the load.
4. Monitoring and Logging: key to understanding what's going on with automated systems, requiring a good dashboard.
5. DevSecOps: integrating security testing and reporting into the DevOps workflow.

The lecture also mentions additional topics, such as version control (Git), code review, and self-evaluation checklists, but does not delve deeply into these topics.

Overall, this transcript provides a high-level overview of the key concepts and practices in DevOps, with a focus on automation, testing, and security.

---

## Topic 8 summary Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/Z4ZgB/topic-8-summary)

There is no text provided for me to summarize. The provided text appears to be a video transcript and additional page content for a lesson on web development, including version control with Git, DevOps practices, and code review. If you provide the actual text, I would be happy to assist you in summarizing it into 8 sentences while preserving key information, formulae, links, and technical details.

---

## Activity – Experiment with Git Reading• . Duration: 1 hour 1h

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

---

## DevOps practices reading Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/fDeSd/devops-practices-reading)

Unfortunately, there is no text provided for me to summarize. The text appears to be a set of instructions and references related to a lesson on DevOps practices, including links to articles and videos, practice assignments, and readings. There is no actual content or information to summarize.

If you could provide the relevant text, I would be happy to assist you in summarizing it into 8 sentences, preserving key information, formulae, links, and technical details, while focusing on the most important concepts and findings.

---

## Code review reading Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/SNpIn/code-review-reading)

Unfortunately, you didn't provide any text to summarize. The provided text appears to be a table of contents or a lesson plan from an online learning platform, but it does not contain any substantive information about code review.

However, I can tell you that the article "Code reviewing in the trenches: Challenges and best practices" by MacLeod et al., published in IEEE Software in 2017 (pp. 34-42), discusses the challenges of code review and provides best practices for improving the process.

If you could provide the text of the article, I would be happy to assist you in summarizing it in 8 sentences while preserving key information, formulae, links, and technical details.

---

## Lesson 16.1: self-evaluation checklist Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/nDEx6/lesson-16-1-self-evaluation-checklist)

Here is a summary of the text in 8 sentences, preserving key information:

Regularly assessing your understanding against learning outcomes is crucial to improve knowledge and skills. This exercise helps you reflect on your learning journey, identify areas for improvement, and develop a plan to deepen your knowledge. You have demonstrated proficiency in using Git for version control, including initializing repositories, adding, committing, and pushing changes to remote services like GitHub or GitLab. Additionally, you can create branches, merge changes, and connect local repositories to remote services. You also understand the principles of DevOps, including continuous integration (CI) and continuous delivery (CD), which automate software development processes. Furthermore, you comprehend the concept of infrastructure as code and its importance in automating web infrastructure scaling. You are familiar with monitoring, logging, and security testing for maintaining a stable and secure production environment. To evaluate your understanding, use this checklist to identify areas where you need improvement and revisit relevant lecture videos, readings, and activities for consolidation.

I preserved the key information by:

* Summarizing the importance of regular self-assessment
* Reciting specific skills demonstrated in using Git and DevOps concepts
* Highlighting knowledge gaps and areas for improvement
* Preserving technical details such as version control concepts and best practices

Note that I did not include links, formulae, or technical details that were not essential to the main message.

---

