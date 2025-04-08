# CM1010 Introduction to Programming II - Topic 1 Object orientation in practice - Week 1

## Table of Contents

- [Week 10](#week_10)
- [Week 14](#week_14)
- [Week 15](#week_15)
- [Week 16](#week_16)
- [Week 17](#week_17)
- [Week 18](#week_18)
- [Week 19](#week_19)
- [Week 2](#week_2)
- [Week 20](#week_20)
- [Week 4](#week_4)
- [Week 5](#week_5)
- [Week 6](#week_6)
- [Week 7](#week_7)
- [Week 8](#week_8)

## Week 10

### Interview with the pro: Christophe Rhodes Video• . Duration: 12 minutes 12 min

The transcript provides an interview with Christophe Rhodes, a professional software engineer. The conversation covers various aspects of his job, including:

1. **Coding**: Christophe mentions that coding is not the most time-consuming part of his job, but it's essential. He prioritizes accuracy over speed when writing code.
2. **Reviewing code**: Reviewing other people's code is a substantial part of his work. He emphasizes the importance of reviewing code to ensure its quality and to waste his colleagues' time less.
3. **Debugging**: Debugging is another critical aspect of his job, where he spends a significant amount of time trying to identify problems in the code.
4. **Design documents**: Christophe also works on writing design documents for new features, which requires designing and reviewing them with other specialists.
5. **Flexibility**: He advises students to become proficient in multiple programming languages and tools, as well as having flexibility to learn about other tools and technologies.

**Key Takeaways**

* Accuracy is more important than speed when coding.
* Reviewing code is a crucial part of the job, but it's not about nitpicking; rather, it's about ensuring quality.
* Debugging can be time-consuming, but it's essential to identify problems in the code.
* Writing design documents and reviewing them with specialists is an important aspect of his job.
* Having flexibility and learning about other tools and technologies is essential for a career in software engineering.

**Discussion Questions**

1. What are some common mistakes people make when writing code that can lead to debugging issues?
2. How does Christophe approach reviewing code? What are the key factors he considers when reviewing someone else's work?
3. Can you think of any scenarios where speed might be more important than accuracy when coding? Provide an example.
4. How do you think Christophe's emphasis on accuracy and quality would impact a team's overall performance and productivity?
5. What advice would you give to students who are just starting their journey in computer science, focusing on software engineering?

**Extension Activity**

Create a design document for a new feature that you would like to implement in a project. Write it in a format similar to Christophe's design documents. Consider the following:

* Clearly describe the problem you're trying to solve.
* Explain your design and any relevant trade-offs.
* Outline how the implementation will be done, including any necessary tools or technologies.
* Provide examples and test cases to validate your design.

Share your design document with a partner or in a group discussion to get feedback on clarity, coherence, and overall effectiveness.

---

### Topic 5 evaluation and summary Reading• . Duration: 30 minutes 30 min

There is no text to summarize. The provided text appears to be a instructional message or announcement related to an online course or educational program, and it does not contain any specific information about formulas, links, or technical details.

However, I can provide a summary of the key points in 8 sentences:

You have completed the fifth topic of the module, which covered initial plans for extending your chosen application. You have also learned about brainstorming project ideas and planning your time while working on a project. Before moving forward, review the provided checklist to test your knowledge and experience with the discussed topics. You have carefully reviewed the project reading and taken an initial look at the mark scheme. You have explored example extensions from lesson 5.2 and considered how they could be implemented in a template. Additionally, you have watched a video interview with Christophe Rhodes, a professional in software development, to gain insight into their career. You have selected the application you want to continue working on and are now ready to move forward. To ensure you're happy with your choice, you can also review additional example extensions that will be discussed in future topics.

---

## Week 14

### Activity – progress logs (assessed) Reading• . Duration: 20 minutes 20 min

Here is a summary of the text in 8 sentences:

As your project progresses, it's essential to keep a log of what you've achieved and plan to do next. This will help track your project's progress, allow instructors to see how you approached the topic, and provide evidence of your work. You'll be required to complete a log for each topic in the second half, using the provided template to structure your responses. The log should include: project title, current topic, progress made, problems faced, solutions found, plans for the next few weeks, and whether you're on track to complete the project. If not on target, you'll need to explain how you plan to address the issue. You'll be required to submit all four logs with your final project submission and should keep them safe on your computer. The logs will be compiled into a PDF for submission at the end of the project. You can view the template in rich text format (RTF) or Microsoft Word docx format, and you're advised to convert completed logs to PDF for submission.

---

### Topic 7 summary Reading• . Duration: 10 minutes 10 min

I don't see any text provided for me to summarize. Could you please provide the text you'd like me to summarize, and I'll do my best to preserve all key information, formulae, links, and technical details while condensing it into 8 sentences?

---

## Week 15

### Introduction and progress check Video• . Duration: 1 minute 1 min

There is no text provided for me to summarize. The text appears to be a transcript of a video introduction to Lesson 8, which includes information about upcoming topics and providing assistance with project completion. However, the actual content of Lesson 8 is not provided.

If you provide the text for Lesson 8, I can help you summarize it in 8 sentences, preserving key information, formulae, links, and technical details.

---

### Asynchronous function calls Video• . Duration: 4 minutes 4 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

In JavaScript, function calls can be divided into two categories: synchronous and asynchronous. Synchronous functions execute one after another, causing the code to pause while waiting for the previous function to complete. In contrast, asynchronous functions allow other activities to continue running concurrently with the execution of the function. The `billowed sound` function is an example of an asynchronous function call. When calling an asynchronous function in a preload or callback context, the main function continues executing without waiting for the asynchronous operation to complete. This can lead to issues when trying to access the result of the asynchronous function, such as setting a global variable equal to `sample.duration`. To resolve this issue, developers can use callbacks or other techniques to ensure that the asynchronous operation has completed before accessing its result. Asynchronous programming is useful for efficiently utilizing a computer's processing power and reducing "spinning wheels" in software.

---

### Using Callbacks Video• . Duration: 20 minutes 20 min

This is a transcription of a video lecture on callbacks in audio processing, specifically for an interactive media or audio visualizer app. Here's the content:

**Introduction**

In this lesson, we'll be exploring callbacks and how to use them in our audio visualizer app.

**Callback Basics**

A callback is a function that's passed as an argument to another function, which then calls it back when something happens. In the context of audio processing, callbacks are used to handle events such as when a sample finishes playing or when a cue is triggered.

**Using Callbacks with Samples**

We'll start by looking at how to use callbacks with samples. We'll create a variable for our screen text and then draw it on the screen whenever the sample is playing. We'll also add cues to trigger specific times in the sound file.

**Callbacks with addCue**

We'll explore the `addCue` method, which allows us to specify precise timings for our cues. We'll use Audacity to fine-tune these timings and get a more accurate response from our starting signal.

**Using Callbacks in Practice**

As we go through this lesson, you should think about how you could apply callbacks to your own audio visualizer app. How could you use them to create interactive and responsive effects?

**Additional Resources**

* Lesson 8.1: Introduction and progress check
* Lesson 8.2: Callbacks Video
* Video: Using Callbacks (20 minutes)
* Graded Assignment: Callbacks (15 minutes)

Note that the video lecture is not included in this transcription, but it's assumed to be available separately. The additional resources listed at the end suggest that there may be accompanying materials or activities for students to complete alongside this lesson.

---

### Gantt chart check-in/evaluation Reading• . Duration: 30 minutes 30 min

There is not enough information provided in the text to summarize and preserve all key details. The text appears to be a prompt for a lesson review and does not contain any specific content, formulae, links, or technical details.

However, I can provide a summary of the main points:

The text invites students to review their Gantt chart and reflect on its effectiveness in managing their project time. It emphasizes that a Gantt chart should be updated regularly to show progress and identify problems early. The student is encouraged to consider whether they are on track to meet the final deadline, what adjustments need to be made, and how effective the task breakdown was. They are also asked to think about opportunities for additional functionality or testing if they are running ahead of schedule.

If you could provide more context or content from the text, I would be happy to help with a summary.

---

## Week 16

### Breakpoints and stepping Video• . Duration: 5 minutes 5 min

Unfortunately, I do not have enough information to accurately summarize the text in 8 sentences. The text appears to be a transcript of a video lecture on debugging techniques using the browser's console, specifically focusing on breakpoints and stepping through code. The speaker discusses various controls available in the console, including step over, step into, and step out, which allow users to navigate through their code line by line.

The speaker uses an example script to demonstrate how these controls work, including setting breakpoints at specific lines of code and inspecting variables and functions as they execute. They also discuss the importance of understanding how JavaScript's built-in functions, such as `push`, work in order to debug code effectively.

Without more context or information about the content of the transcript, it is difficult to provide a summary that accurately captures the key points and concepts discussed.

---

### Progress log (assessed) Reading• . Duration: 15 minutes 15 min

There is no text provided to summarize. The given text appears to be a part of a course or educational material related to programming, specifically an "Introduction to Programming II" course. It provides guidance on keeping a project log throughout the course and outlines the template for completing these logs.

Here's a summary based on the information available:

Throughout the "Introduction to Programming II" course, it is essential to maintain a log of progress, challenges, and future plans. This helps keep the project on track, allows instructors to assess progress, and provides valuable insights into the approach taken in tackling larger applications. The log template should include the following details:

1. Project title and current topic.
2. Progress made in the topic.
3. Problems faced and solutions found.
4. Plans for the next few weeks.
5. Target completion status and plan to address any issues.

Upon completing all logs, students will need to compile and submit them as a PDF file. It is crucial to keep these logs safe on their computers and ensure they can be easily converted to a PDF format for submission.

---

### Topic 8 summary Reading• . Duration: 10 minutes 10 min

There is no text provided for me to summarize. The text appears to be a summary of a module's eighth topic, but it does not contain any specific content or information that needs to be summarized. If you provide the actual text, I would be happy to assist you in summarizing it in 8 sentences, preserving key information, formulae, links, and technical details.

---

## Week 17

### Testing for stability Video• . Duration: 16 minutes 16 min

The provided transcript is a lecture on software testing, specifically focusing on testing for stability. The lecturer covers various aspects of software testing, including the importance of testing, types of tests (black box, white box, gray box), and how to identify defects.

Here's a summary of the main points:

1. **Importance of Testing**: Testing is crucial in ensuring the quality and reliability of software.
2. **Types of Tests**:
	* Black Box: Tests the functionality of the software without knowing its internal workings.
	* White Box: Tests the functionality of the software by examining its internal workings.
	* Gray Box: A combination of black box and white box testing, where some internal information is available.
3. **Testing for Stability**: Testing for stability involves identifying defects that can cause the software to fail or behave unexpectedly.
4. **Test Case Development**:
	* Identify areas of concern: Determine which features or functions are most critical to test.
	* Create test cases: Develop test cases that cover various scenarios, including error handling and edge cases.
5. **Testing Techniques**:
	* Exploration testing: Test the software by exploring its functionality and identifying potential defects.
	* Repetition testing: Repeat tests multiple times to ensure consistency and accuracy.
6. **Error Handling**: Testing for error handling involves ensuring that the software can recover from errors and exceptions.

The lecturer provides examples of test cases, including:

1. **Pencil Drawing Test Case**:
	* Selecting different tools
	* Changing line widths
	* Verifying correct behavior when switching between tools
2. **Invalid Input Testing**:
	* Testing with invalid input values (e.g., 0, -1, 51, "a", "@")
3. **Persistence of Line Widths**: Verifying that line widths persist across different tools and actions.

The lecture concludes by emphasizing the importance of testing for stability and providing a framework for developing test cases and identifying defects.

**Key Takeaways**

* Testing is essential for ensuring software quality and reliability.
* Different types of tests can be used depending on the context.
* Testing for stability involves identifying defects that can cause the software to fail or behave unexpectedly.
* Test case development should focus on critical areas and cover various scenarios.
* Error handling is crucial for ensuring the software recovers from errors and exceptions.

---

## Week 18

### Beyond Console.log Video• . Duration: 27 minutes 27 min

This is a transcript of an instructional video on debugging and optimizing code. The instructor discusses the following topics:

1. Introduction to profiling tools
2. Understanding CPU cycles vs. memory usage
3. Identifying performance issues with console.log statements
4. Optimizing code using Big O notation
5. Using memory profilers to diagnose issues

The instructor provides a step-by-step guide on how to use these tools and techniques to debug and optimize the provided code.

**Key takeaways:**

* Use profiling tools to understand the performance bottlenecks in your code.
* Understand the difference between CPU cycles and memory usage.
* Optimize code using Big O notation.
* Use memory profilers to diagnose issues related to memory usage.

**Code snippets:**

The instructor provides several code snippets throughout the video, including:

1. A simple particle generator function
2. An optimized version of the particle generator function using Big O notation
3. Code modifications to use a memory profiler

These code snippets illustrate the concepts discussed in the video and provide examples of how to apply them to real-world coding scenarios.

**Actionable items:**

The instructor suggests several actionable items for viewers to try:

1. Use console.log statements to understand performance bottlenecks.
2. Try optimizing code using Big O notation.
3. Experiment with different profiling tools, such as the memory profiler.

These action items encourage viewers to engage actively with the material and apply the concepts learned in the video to their own coding projects.

**Target audience:**

The instructor appears to be targeting developers who are familiar with JavaScript and have some experience with debugging and optimizing code. The video assumes a certain level of technical knowledge, but provides explanations and examples that should be accessible to viewers with varying levels of expertise.

Overall, this video provides a comprehensive guide to debugging and optimizing code, covering essential topics such as profiling tools, Big O notation, and memory profilers.

---

### Progress log (assessed) Reading• . Duration: 30 minutes 30 min

Here is a summary of the text in 8 sentences:

As your programming project progresses, it's essential to maintain a log of your progress and future plans to stay on track and demonstrate how you've approached the project. This log will also allow instructors to assess your work and provide feedback. The log template should include the project title, current topic, progress made, problems faced, solutions found, upcoming tasks, and whether the project is on target for completion. Students are expected to compile and submit all logs at the end of the project, ensuring they are safely stored on their computers. The logs will be converted to PDF format for submission. To prepare for the discussion prompt, students should read the progress log assessment (30 minutes). Additionally, a separate log is required for the debugging skills topic, also using the same template as before. By maintaining these logs and following the guidelines, students can effectively track their progress and receive feedback on their project management skills.

---

### Topic 9 summary Reading• . Duration: 10 minutes 10 min

There is no text provided for me to summarize. The given text appears to be a summary of a course or module with instructions on what topics have been covered and what students should do next, but it does not contain specific information about code testing, debugging techniques, profilers, or project logs.

If you provide the actual text you'd like me to summarize, I'll be happy to help.

---

## Week 19

### Introduction and progress check Video• . Duration: 1 minute 1 min

There is no text to summarize beyond this point. The provided text appears to be a video transcript and additional page content for a lesson on "Testing with Users" as part of a programming course, specifically CM1010 Introduction to Programming II. It provides instructions on how to navigate through the transcript using keyboard shortcuts and mentions the importance of testing techniques and usability testing in software development.

However, I can provide some key concepts and findings related to user testing and usability:

* User testing involves evaluating an application or software with real users to identify usability issues and gather feedback.
* Usability testing aims to ensure that an application meets the needs and expectations of its target audience.
* Testing techniques for complex elements of a project include identifying pain points, gathering feedback from users, and refining the design based on user input.

If you provide more context or specify which aspects of the text you would like me to focus on, I can attempt to provide further assistance.

---

### Usability testing Video• . Duration: 7 minutes 7 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Usability testing is crucial to ensure an application's effectiveness in achieving human goals, such as facilitating creative or logical thought processes. The goal of user testing is to collect data on users' behavior with the application, gathering both qualitative and quantitative data. A common technique for generating nuanced qualitative data is the think-aloud protocol, where users are asked to verbalize their thoughts while interacting with the application. Another approach is to conduct interviews with participants after they complete tasks to gather feedback about their experiences. When planning a user test, it's essential to consider the target audience and design a structured process to ensure consistency between different users of the application. The structure should include clear steps for users to follow, introducing them to the application and utilizing as much of its functionality as possible. To analyze data, look for convergence between users who have had similar problems, and compare task completion times to identify bottlenecks in the application's design. By conducting usability testing and analyzing the collected data, it's possible to determine areas for improvement and evaluate the success of an application in achieving human goals.

---

### Writing your report Video• . Duration: 5 minutes 5 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The report section of your final project submission should provide a technical summary of what you've achieved, how effectively your plan was implemented, and a critical evaluation of the process. The report will consist of four questions: (1) modifications and extensions to templates, (2) an assessment of the effectiveness of your plan, (3) an evaluation of your project's final product, and (4) external sources used in your project. For each extension, you should include its functionality, how it was implemented, and how object-oriented programming techniques were used. When evaluating your project's effectiveness, consider whether you stuck to the schedule, divided time effectively, and performed user or system testing. The report should be well-structured, readable, and use correct English spelling and grammar. It should also include figures or images that help make your argument and upload project logs produced over the last few weeks. When referencing external sources, provide specific details and links to the projects or questions used. Using third-party libraries can have a negative effect on your work; instead, demonstrate your coding skills by creating an end result from scratch.

---

## Week 2

### Splitting across multiple files Video• . Duration: 4 minutes 4 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The instructor presents a technique for organizing code in larger applications, such as game projects with extensive sketch files. The goal is to split up code into multiple files, including constructor functions, to make it more organized and easier to maintain. The instructor uses a practical example from the previous module, copying and pasting constructor functions into new files (Emitter.js and Particle.js) to demonstrate this technique. Each file has its own name as the constructor function, and the instructor emphasizes the importance of saving with a `.js` extension for syntax highlighting. To load these files in the sketch, a new `scripts` tag is added to the HTML, referencing both `p5`, the constructor functions, and the sketch file itself. The order of the script tags matters, with `p5` first, followed by the constructor functions, and finally the sketch file. A refresh of the live preview feature in the text editor resolves an issue with loading files in the wrong order. By organizing code into multiple files, developers can make their code more manageable, readable, and maintainable for themselves and others.

---

### Case studies overview Video• . Duration: 4 minutes 4 min

Here is a summary of the text in 8 sentences, preserving key information:

In this module on object orientation and code organization, students will apply their knowledge to larger applications. The project involves creating a big application by combining smaller elements, with three case studies to choose from: a simple drawing application using p5.js DOM library, a music visualization app using p5.js sound library, and a data visualization app using p5.js table object. Each case study will explore different techniques and features, such as constructor functions, object orientation, and external libraries. The project requires students to design, implement, test, and evaluate their extensions, with assessments on technical implementation, planning, organization, and evaluative skills. The drawing application uses basic tools for drawing lines and airbrushing, while the music visualization app can create visual patterns from sound wave properties. Students will also learn about debugging techniques and guidance on keeping track of progress. After completing case studies, students will choose one to base their project on, with instructor support and resources provided throughout the process. The module aims to develop not only coding skills but also effective coding practices, such as organization, planning, and evaluation.

---

### Programming exercise: hack it – zombie attack Reading• . Duration: 1 hour 1h

Here's a summary of the text in 8 sentences, preserving key information and details:

The program creates a horde of zombies that cross a canvas. The task is to enhance the code by splitting it into multiple files, each containing a different constructor. Each zombie should have a health property assigned to it. A shovel should be added to the game. When a zombie's head is clicked, its health decreases. If a zombie's health reaches zero, a new zombie should be added to the horde. The ultimate goal of the enhanced program can be made into a game where zombies need to be kept from the right side of the screen for as long as possible. The starter code is provided in a ZIP file.

---

### Topic 1 summary and evaluation Reading• . Duration: 30 minutes 30 min

There is no text provided for me to summarize. The text appears to be a module summary from a programming course, outlining the key concepts and topics covered in the first topic of the module. It provides a checklist for students to review their knowledge and experience with object-oriented programming techniques.

However, I can provide a summary of the content if you would like:

The first topic of the module reviews object orientation techniques introduced at the end of Introduction to Programming I. Students have extended their knowledge with a formal understanding of object orientation and its benefits in making programs more readable and extendable. The topic will build upon this foundation, becoming increasingly important throughout the module. Key concepts covered include abstraction and encapsulation, constructor functions in JavaScript, object literals, converting applications to use multiple files, public and private members, and debugging complex issues. Students are encouraged to implement the zombie horde example and complete the chocolate shop debug challenge to demonstrate their understanding. A checklist is provided for students to review their knowledge and experience. The topic also includes a video on case studies overview and a reading assignment to summarize and evaluate the topic.

Please provide the actual text if you would like me to summarize it in 8 sentences, preserving key information, formulae, links, and technical details.

---

## Week 20

### Summary of the module Video• . Duration: 2 minutes 2 min

Unfortunately, there is no text to summarize beyond the introductory section of a video transcript. The provided text only contains a video transcript and does not include any relevant content or information that could be summarized.

However, I can provide a general summary of what appears to be an introduction to programming course:

The course has covered various topics in programming, including drawing commands, nested looping, complex conditionals, object-oriented programming, arrays, and data structures. Students have also been introduced to the JavaScript syntax and the process of programming, co-design, debugging, and the philosophy of code.

The instructor thanks students for their participation in the course and wishes them the best of luck with their future endeavors in programming. They encourage students to continue exploring programming even if it's not a central part of their career path.

Additionally, there are links to further lessons and resources, including:

* Lesson 10.3: Finishing touches
* Lesson 10.4: Progress log
* Lesson 10.5: Summary Video

These links provide access to more content and summaries of the course material.

---

### Progress log (assessed) Reading• . Duration: 30 minutes 30 min

There is no text provided to summarize. The provided text appears to be instructions or guidelines for a student project, specifically regarding keeping a progress log throughout the project. It outlines the template and format required for the log, as well as the importance of submitting it at the end of the project.

If you would like me to help with summarizing actual text, please provide the relevant text, and I will be happy to assist you in condensing the main points into 8 sentences while preserving key information, formulae, links, and technical details.

---

## Week 4

### Interview with the student: Evan Griffiths Video• . Duration: 9 minutes 9 min

This is a transcript of an interview with a student, Evan Griffiths, who completed a project using the p5.js library. The interview covers various aspects of the project, including the changes Evan made to the original template, the model loading feature, and potential improvements for future projects.

The transcript can be broken down into several sections:

1. Introduction and context: Evan introduces himself and explains that he worked on a project using the p5.js library, which is a popular JavaScript library for creating interactive web-based applications.
2. Changes to the original template: Evan discusses the changes he made to the original template, including adding a 3D drawing area, implementing model loading, and improving user interface elements.
3. Model loading feature: Evan explains how he implemented the model loading feature, which allows users to import 3D objects from OBJ files. He also discusses the challenges he faced while working on this feature, such as handling the complexity of the OBJ file format.
4. User interface improvements: Evan highlights several user interface improvements he made, including adding a red highlight box around the selected model and improving the overall layout of the application.
5. Potential improvements for future projects: Evan reflects on potential improvements for future projects, including updating to the latest version of p5.js if necessary and making code changes to improve readability.

Overall, this transcript provides valuable insights into the process of creating an interactive web-based application using p5.js, as well as tips and advice for students working on similar projects.

---

### Instructions for peer review Reading• . Duration: 15 minutes 15 min

Here is a summary of the text in 8 sentences:

Peer review is a collaborative process where students, scholars, or researchers evaluate each other's work to provide feedback and learn from one another. In an academic setting, peer reviews may be part of required assignments, where students submit their own work for grading by peers, while also grading a minimum number of peers' submissions to receive their own assignment grade. Peer review is not just about critiquing but also offering constructive feedback that can help authors improve their work and develop critical thinking and analytical skills. Participating in peer review fosters a sense of community, improves writing and research skills, and offers new perspectives and ideas, as well as preparing students for future academic and professional endeavors. Peer review enhances learning and retention by reinforcing knowledge and understanding of subject matter, while also developing empathy and communication skills. By engaging in peer review, students can gain insight into the review process, reduce anxiety about submitting work for review, and increase their competence in navigating academic and professional review processes. Additionally, peer review exposes students to diverse research topics and methodologies, sparking interest in interdisciplinary study or collaboration, and boosting confidence in academic abilities through the improvement of peers' work. Overall, peer review is a valuable process that can enhance critical thinking, analytical skills, and academic success.

---

### Reflection on interview with the student Reading• . Duration: 30 minutes 30 min

Here is a summary of the text in 8 sentences, preserving key information:

After watching the interview with Evan, students should reflect on their own project's progress and consider how they can incorporate features from Evan's application into their own implementation. This includes redesigning core functionality, such as the color picker and line tool, which Evan built both simple and advanced tools for. Students should plan how to implement more complex p5.js features like 3D graphics by using planning techniques, brainstorming, and iterating different designs. To support this process, students can use various planning methods and assess their current progress regularly to ensure they are on track to meet the deadline and required standard. The midterm assignment will ask students to detail their implementation plan, which they should maximize by keeping a record of brainstorming designs, sketches, sources of inspiration, technical help, and regular logging of progress. Students can upload these materials at the midterm or end-of-term assignments. Evan's interview highlights the importance of self-reflection and documenting one's thinking and progress to improve project outcomes. By following these guidelines, students will be better prepared for their final application submission, where they will reflect on what they would do differently and assess their current progress.

---

### Topic 2 evaluation and summary Reading• . Duration: 10 minutes 10 min

There is not enough text provided to summarize into 8 sentences. The text appears to be a summary of a course or module, but it lacks specific details about the content, concepts, or findings. Can you provide more context or information about what this text is referring to? I'll be happy to help if I can.

---

## Week 5

### Introduction to case study 2: music visualiser Video• . Duration: 5 minutes 5 min

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Music visualization has been used to enhance music listening experiences for almost five decades, dating back to the Atari video music system in 1977. Recently, music playback software such as Winamp, Windows Media Player, and iTunes have included in-built visualization features. The demo scene and VJing art forms also explore music visualization, where performers create visual output in front of a live audience. This case study aims to build upon a basic music visualization program, creating out-of-this-world visualizations that reflect the tone, energy, and time signature of music. The application allows users to choose between different visualizations, including an old-fashioned Spectrum display for sound amplitudes, a wave pattern responding to FFT output, and "needles" displaying amplitude in four frequency bands. The application is responsive, resizing with screen changes and allowing full-screen mode with a Play button. However, there are limitations, such as a bug that needs to be fixed and the lack of perfect scaling. A future video will delve into the technical details of how the music visualization program works under the hood.

---

### P5.js sound: loading and playing a sound Video• . Duration: 16 minutes 16 min

Here is a written summary of the video transcript:

The video introduces the P5.js sound library and shows how to play sounds in an interactive program. The speaker explains that the sound library provides objects called "sound files" which can be used to create music.

The speaker then demonstrates how to load and play a sound file using the `loadSound()` function, which returns a promise when the sound is loaded. They use the `successCallback` callback to execute code when the sound is loaded, in this case logging a message to the console.

Next, the speaker shows how to pause and resume playback of a sound file using the `pause()` and `play()` functions. They demonstrate how to check if a sound file has been paused or not using the `isPaused` method.

The speaker also discusses how to load large sound files, which can take several seconds to load. To handle this situation, they use the `successCallback` callback to execute code when the sound is loaded, and only play the sound file if it has actually finished loading (i.e., the `isLoaded` variable is set to true).

Throughout the video, the speaker uses examples to illustrate each concept, such as playing a single beep sound or creating a short melody using multiple sounds. They also encourage viewers to try out different sounds and experiments with the P5.js sound library.

Overall, the video provides a comprehensive introduction to the basics of working with audio in P5.js, including loading and playing sounds, pausing and resuming playback, and handling large sound files.

---

### P5.js sound: amplitude Video• . Duration: 15 minutes 15 min

This is a transcript of an audio lecture or tutorial on using the P5.js library to analyze sound and create visualizations. The lecturer discusses various topics related to sound analysis, including:

1. Introduction to sound analysis in P5.js
2. Preparing for case study 2
3. Loading and playing sounds in P5.js
4. Analyzing amplitude (volume) of a sound signal
5. Playing with amplitude and frequency
6. Creating music visualizations using P5.js

The lecturer also mentions some additional resources, including videos and practice assignments, that can be used to learn more about sound analysis and visualization in P5.js.

Some key takeaways from the lecture include:

* How to use P5.js to load and play sounds
* How to analyze the amplitude (volume) of a sound signal using P5.js
* How to create visualizations that respond to changes in amplitude and frequency
* The importance of experimenting with different parameters and techniques to achieve the desired effect

The lecture concludes with some practice assignments and additional resources for further learning.

Note: The transcript appears to be an incomplete or fragmented version of a larger tutorial or lecture. Some sections are missing, and there may be additional content not included in this transcription.

---

### P5.js sound: frequency, part 1 Video• . Duration: 4 minutes 4 min

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The concept of frequency is an important aspect of sound, where pitch is measured in hertz (Hz). The human hearing range spans from 20 Hz to 20,000 Hz. Sounds can be either pitched or unpitched, with pitched sounds having a dominant frequency that can be described digitally using frequency spectra. To accurately describe a sound digitally, every possible frequency within the hearing range must be considered and its amplitude measured, resulting in a complex bar chart known as a frequency spectrum. However, this is impractical due to the vast number of frequencies (18,980) involved, so they are grouped into bands for easier analysis. A graphic equalizer display can provide an idea of how these frequency bands shift over time as the sound changes. To analyze sound in p5.js, a rolling frequency spectrum can be created using FFT objects, allowing for a dynamic representation of music tracks. The process involves taking multiple frequency spectra to capture the changing characteristics of the sound over time.

---

### P5.js sound: frequency, part 2 Video• . Duration: 13 minutes 13 min

This is a transcript of an online lesson or tutorial on using P5.js, a JavaScript library for creating visualizations. The lesson covers various topics related to sound and music visualization in P5.js.

The transcript begins by introducing the concept of frequency analysis in music, which involves breaking down a musical signal into its component frequencies. It then moves on to using P5.js to load and play sounds, manipulate amplitude (the loudness or volume of a sound), and analyze frequency.

The lesson also covers how to use P5.js to create simple music visualizations, such as isolating different parts of a track by grouping together different frequency bands. The transcript includes tips and advice on how to experiment with different visualization techniques and create more complex music visualizations.

Throughout the lesson, there are links to additional resources, including videos and readings that provide further information and practice assignments for students to complete.

The final section includes a video interview with a student who created a music visualization application, as well as some reflection on the process of creating such an application.

Overall, this transcript appears to be part of a larger lesson or course on using P5.js for music visualization and sound analysis.

---

### Music visualisation application: under the hood Video• . Duration: 29 minutes 29 min

Based on the provided transcript, here is an outline of the key points and topics covered:

**Lesson Overview**

* Lesson 3.1: Introduction
* Lesson 3.2: Preparing for case study 2

**Case Study 2 Topics**

* Video: "P5.js sound: loading and playing a sound" (Duration: 16 minutes)
	+ Covers the basics of loading and playing sounds in P5.js
* Reading: "Making your own sound composition" (Duration: 30 minutes)
	+ Provides tips and techniques for creating sound compositions using P5.js
* Video: "P5.js sound: amplitude" (Duration: 15 minutes)
	+ Explores the concept of amplitude in sound waves
* Reading: "Playing with amplitude" (Duration: 30 minutes)
	+ Offers advice on how to manipulate and control amplitude in sound compositions
* Video: "P5.js sound: frequency, part 1" (Duration: 4 minutes)
	+ Introduces the concept of frequency in sound waves
* Video: "P5.js sound: frequency, part 2" (Duration: 13 minutes)
	+ Delves deeper into the concept of frequency and its effects on sound
* Reading: "Playing with frequency" (Duration: 30 minutes)
	+ Provides guidance on how to experiment with different frequencies in sound compositions
* Practice Assignment: Analyzing Sound (Duration: 30 minutes)
	+ Encourages students to analyze and understand sound waves using P5.js

**Additional Resources**

* Video: "Music visualisation application: under the hood" (Duration: 29 minutes)
	+ Provides an in-depth look at the underlying code of a music visualization app
* Video: Interview with a Student (Duration: 6 minutes)
	+ Features a conversation between a student and a teacher about P5.js and its applications
* Reading: Reflection on interview with the student (Duration: 30 minutes)
	+ Offers insights into the importance of collaboration and communication in learning programming

**Prerequisites**

* Students should have basic knowledge of P5.js and its functionality.
* Familiarity with sound waves and audio concepts is recommended but not required.

This outline provides a comprehensive overview of the topics covered in Lesson 3.1 and Lesson 3.2, including case study 2. The practice assignment and additional resources are designed to reinforce students' understanding of P5.js and its applications in music visualization.

---

### Interview with a student: Taylor Millin Read Video• . Duration: 6 minutes 6 min

The video transcript is about an Introduction to Programming project at Goldsmiths University, where a first-year computer science student, Taylor, built an application using the P5.js library. The application has four different visualizations that react to the waveform and spectrum analysis of the FFT algorithm: Spin, which spins in response to the waveform; a store waveform that moves from the center point when clicked; and a video visualization that uses the pixel array to change colors based on frequency amplitudes. Taylor's favorite visualization is the video one, which he created using the pixel array to edit red, green, blue, and alpha values depending on the volume of certain frequencies.

The application was built using P5.js, and Taylor used a function to update pixels by editing their RGB values. He also used the FFT algorithm to analyze the music signal and generate visualizations that react to it. The video app uses the pixel array to change colors as the music plays, and Taylor created this effect by making edits to the red, green, blue, and alpha values of each individual pixel.

Taylor's inspiration for the video app was to use video from the computer camera and the pixel array to create a fluid reaction with the music. He also wanted to explore alternative color systems beyond RGB, but ultimately used RGB throughout his project. Taylor faced challenges in finding better ways to manipulate colors and editing code, but he created a simple yet effective solution using the angle parameter to rotate pixels.

Overall, Taylor's project demonstrates the capabilities of P5.js for building interactive music visualizations that react to audio signals. The video app is an example of how this library can be used to create engaging and dynamic visuals that respond to sound waves.

---

### Case study 2: music visualiser Reading• . Duration: 2 hours 30 minutes 2h 30m

I'll guide you through completing each part of the music visualizer project.

**Part 1: Playback and fullscreen**

In the `controlsAndInput.js` file, find the `mousePressed()` function:
```javascript
function mousePressed() {
  if (playButton instanceof Button) {
    playButton.click();
  }
}
```
 Inside this function, check if the click is on the play button. If not, toggle the display between window and fullscreen.

To do this, you'll need to create a `Fullscreen` class that handles fullscreen mode:
```javascript
class Fullscreen extends Button {
  constructor() {
    super();
    thisfullscreen = false;
  }

  setFullscreen(fullscreen) {
    thisfullscreen = fullscreen;
  }
}

function toggleFullscreen() {
  if (fullscreen instanceof Fullscreen) {
    fullscreen.setFullscreen(!fullscreen fullscreen);
  } else {
    // toggle to window mode
  }
}
```
You'll also need to create a `Button` class:
```javascript
class Button extends SketchElement {
  constructor() {
    super();
    this.click = false;
  }

  setClick(click) {
    this.click = click;
  }
}

function createPlayButton() {
  const playButton = new Button();
  // add button styles and functionality here
  return playButton;
}
```
In the `mousePressed()` function, check if the click is on the play button:
```javascript
function mousePressed() {
  if (playButton instanceof Button) {
    playButton.click();
    toggleFullscreen(playButton);
  }
}
```
**Part 2: Visualisation menu**

In the `controlsAndInput.js` file, find the `menu()` function:
```javascript
function menu() {
  // create menu items here
  const visualizations = [
    { name: 'Spectrum', value: 'spectrum' },
    { name: 'WavePattern', value: 'wavepattern' },
    { name: 'Needles', value: 'needles' },
  ];

  for (const visualization of visualizations) {
    const menuItem = createMenuItem(visualization.name);
    // add click event listener here
  }
}
```
To display the menu items, you'll need to create a `SketchElement` class:
```javascript
class MenuItem extends SketchElement {
  constructor(name) {
    super();
    this.name = name;
  }

  render() {
    // render menu item text and styles here
  }
}

function createMenuItem(name) {
  const menuItem = new MenuItem(name);
  return menuItem;
}
```
In the `menu()` function, create a `for` loop to iterate over the visualizations:
```javascript
function menu() {
  for (const visualization of visualizations) {
    // render menu item here
  }
}
```
**Part 3: Spectrum analyser**

To change the spectrum analyser's orientation from vertical to horizontal, you'll need to modify its rendering code.

Assuming your spectrum analyser is rendered in a `SketchElement` class:
```javascript
class SpectrumAnalysers extends SketchElement {
  constructor() {
    super();
    this.orientation = 'vertical';
  }

  setOrientation(orientation) {
    this.orientation = orientation;
  }
}

function createSpectrumAnalysers() {
  const spectrumAnalysers = new SpectrumAnalysers();
  // add rendering code here
}
```
To change the colour of each bar based on its amplitude value, you'll need to modify the rendering code:
```javascript
function renderBar(value) {
  const color = map(value, 0, 255, [0, 255, 0], [255, 0, 0]);
  // draw bar here with calculated color
}
```
**Part 4: Needles**

To complete the needles visualisation, you'll need to modify its rendering code.

Assuming your needle chart is rendered in a `SketchElement` class:
```javascript
class NeedleCharts extends SketchElement {
  constructor() {
    super();
    this.frequencyBands = ['bass', 'mid-low', 'mid-high'];
  }

  setFrequencyBands(frequencyBands) {
    this.frequencyBands = frequencyBands;
  }
}

function createNeedleCharts() {
  const needleCharts = new NeedleCharts();
  // add rendering code here
}
```
To modify the rendering code, you'll need to calculate the value for each frequency band based on the energy values returned by `FFT.energy()`:
```javascript
function renderValue(value) {
  const energyValues = FFT.energy(1);
  const valueForFrequencyBand = map(energyValues, 0, 255, [value.value], [value.value]);
  return valueForFrequencyBand;
}
```
That's a basic guide to completing the music visualizer project. You'll need to fill in the missing code and modify the existing rendering codes to match your desired output.

Please let me know if you have any further questions or need help with implementing these changes!

---

### Making your own sound composition Reading• . Duration: 30 minutes 30 min

Here is a summary of the text in 8 sentences, preserving key information and technical details:

To complete this sketch, create an `initialized` global variable with a value of `false` initially. When `initialized` is `false`, draw a message on the screen. The loop method's `rate` argument can be altered to explore sound playback effects, including setting a start time (currently set to 0). Use the `map` function and mouse x position to change playback rate when playback starts. Pause sound playback when the space button is pressed by adding a condition to the `keyPressed` function that checks for the space button. To allow for playback restarts, nest a further conditional as Simon shows in the previous video. An anonymous function can be added to the `loadSound` call to stop playback until the file is fully loaded. Explore other sound library methods and search for freely available sounds if needed.

---

### Playing with amplitude Reading• . Duration: 30 minutes 30 min

There is no text provided for me to summarize. The text appears to be a video description and instructions on how to complete a template in p5.js sketches, specifically related to amplitude and sound visualization.

However, I can provide a summary of the concepts and findings based on the general information about amplitude and sound visualization in p5.js:

Amplitude is a fundamental concept in sound visualization that refers to the maximum magnitude or loudness of a sound wave. In p5.js, amplitude can be used to control the volume of sounds and create visualizations that respond to changes in amplitude.

To visualize amplitude in p5.js, developers can use the `p5.Amplitude` object to track changes in amplitude over time. The `map()` function can then be used to scale the amplitude values to a range of values that can be displayed as ellipses or other shapes on the screen.

In this specific template, users are instructed to:

1. Create an amplitude global variable and set its initial value to a new `p5.Amplitude` object in setup.
2. Use the `map()` function to scale the amplitude values to display ellipses that change size based on the amplitude.
3. Create a global array `amplitudes` to store past amplitude values, which can be used to create a visualization of changes in amplitude over time.

Overall, this template demonstrates how to use p5.js's built-in `p5.Amplitude` object and the `map()` function to create an interactive sound visualization that responds to changes in amplitude.

---

### Playing with frequency Reading• . Duration: 30 minutes 30 min

There is no text provided for me to summarize. The text appears to be a description of a video tutorial on using p5.js with sound, specifically frequency analysis and music visualization. 

If you provide the actual text or context, I can help you summarize it in 8 sentences while preserving key information, formulae, links, and technical details.

---

### Reflection on interview with the student Reading• . Duration: 30 minutes 30 min

Here is a summary of the text in 8 sentences, preserving key information:

The interview with Taylor has encouraged reflection on progress made so far with the drawing application project. Key takeaways from the interview include potential features to add or redesign, such as controls for the music visualizer and different waveform manipulation techniques. Incorporating camera and microphone functionality into the application is also an idea worth exploring. The midterm assignment will require a detailed implementation plan, which can be maximized with planning techniques and brainstorming to iterate on designs. Regular progress logging, tracking of design sources and inspiration, and technical help are essential aspects to keep track of for assessment purposes. Taylor's experience has taught him what he would do differently in the future, highlighting the importance of reflection on one's project. To prepare for this self-assessment, students should start keeping a record of their thinking, progress, and brainstorming designs. The assignments and assessments will require students to upload these logs as part of their midterm or end-of-term evaluations.

---

## Week 6

### Topic 3 evaluation and summary Reading• . Duration: 30 minutes 30 min

There is no text to summarize in this prompt. The provided text appears to be a section from a course or tutorial, outlining topics and assignments related to programming and music visualizers using p5.js. It does not contain any specific information that can be summarized into 8 sentences.

However, I can provide a summary of the main concepts and topics discussed:

The third topic of the module introduces the music visualizer application, which is explored in detail through case studies and video content. Students learn about the basics of storing and playing sound using p5.js's sound library. They also review the structure of the music visualizer application and complete a peer-graded assignment to demonstrate their understanding. Additionally, students participate in a discussion on reflection and planning for their applications, which is discussed in the second "interview with the student" video. The module includes various assessment components, including a 1-hour case study, review of peers' work, and a 20-minute discussion on case study 2.

If you provide the actual text to summarize, I will be happy to assist you further.

---

## Week 7

### Introduction to case study 3: data visualisation Video• . Duration: 42 seconds 42 sec

There is no text provided for me to summarize. The provided text appears to be a video transcript and additional page content related to an educational platform, but it does not contain any specific information about data visualization or programming concepts that can be summarized in 8 sentences.

If you could provide the actual text about p5's data tools and the structure of the data visualization app, I would be happy to assist you with summarizing the key information, formulae, links, and technical details.

---

### Introducing P5 data Video• . Duration: 5 minutes 5 min

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The toolkit of data visualizations uses the p5.js library to access and manipulate tabulated data. Data can be either quantitative (e.g., numbers, scales) or qualitative (e.g., text, images). The table object provides methods for accessing and manipulating data, including loading external data from a CSV file. The loadTable command is used with the preload argument to ensure data is ready for use when needed. Methods for accessing rows and columns include getting specific rows by index, searching for values in particular columns, setting and removing rows, and accessing data by column. The getColumn method retrieves an array of values for a particular variable, which may require conversion from strings to numbers. The table object provides many methods for manipulating tabulated data, and users are encouraged to review the documentation to learn more. In the next video, a real code example with a data table will be presented, along with further information on the CSV format used in p5.js.

---

### Accessing external data Video• . Duration: 30 minutes 30 min

This is a transcript of a video lesson on using P5.js, a JavaScript library for creating interactive graphics and data visualization. The lesson covers several topics:

1. Introduction to P5.js and its capabilities
2. Loading and manipulating external data using the `table` object
3. Creating a scatterplot using the `scatterplot` constructor
4. Adding a line of best fit to the scatterplot

The transcript includes code examples and explanations, as well as suggestions for practice assignments.

Some key takeaways from the lesson include:

* The importance of parsing data to ensure it is used correctly in calculations
* The flexibility of P5.js in allowing developers to create custom visualizations
* The benefits of using a library like P5.js to simplify data visualization tasks

Overall, this transcript provides a comprehensive overview of how to use P5.js for data visualization, including loading and manipulating data, creating scatterplots, and adding lines of best fit.

---

### Data visualisation application: under the hood Video• . Duration: 42 minutes 42 min

This text appears to be a transcript of a lesson or tutorial on a programming topic, specifically on the P5.js library for data visualization. The content seems to follow a structured format, starting with an introduction and then diving into detailed explanations and examples.

The lesson begins by introducing the concept of a data visualization app and the importance of understanding how it works under the hood. It explains that the app uses various visualizations, including pie charts, bar charts, and more, to display data in a meaningful way.

The lesson then guides the reader through a case study of one of these visualizations, "Pay Gap By Job." The author walks the reader through the code step by step, explaining each part of the visualization's implementation. This process is repeated for other visualizations, such as "Tech Diversity Race" and "Climate Change."

The lesson concludes with an introduction to a data visualization application built using P5.js, providing an overview of how it works and encouraging the reader to further explore its code.

Some key concepts covered in this transcript include:

1.  **P5.js library**: A popular JavaScript library for creating interactive, web-based graphics.
2.  **Data visualization**: The process of representing data in a graphical format to aid understanding and interpretation.
3.  **Case study**: An in-depth examination of a particular topic or problem, often used to learn from real-world examples.

Overall, this transcript aims to provide a comprehensive introduction to the P5.js library's capabilities for data visualization, encouraging readers to explore its applications and code structure.

Please let me know if I can assist you with anything else.

---

### Case study 3: data visualisation Reading• . Duration: 3 hours 3h

Here is a summary of the text in 8 sentences, preserving key information:

The goal of this case study is to complete various visualizations using the provided data-vis template. The first task is to complete the visualization defined in tech-diversity-gender.js to create a stacked bar chart representing the proportion of men employed at each company. To do this, one needs to extract relevant data from the raw CSV file, parse it correctly, and use the correct methods to ensure accurate data representation on the plot. The ratio of female:male staff at Indiegogo is 0.5, which should be correctly visualized on the plot.

The next task is to complete the visualization defined in pay-gap-1997-2017.js to create a line graph representing the pay gap between female and male employees over time. This requires extracting relevant data from the raw CSV file, completing the mapPayGapToHeight() method, and using both mapYearToWidth() and mapPayGapToHeight() methods to plot the pay gap over time.

The third task is to complete the visualization defined in climate-change.js to create a line graph with gradient fill background representing the change in Earth's surface temperature. This requires completing the rect() function below the fill() method, using the mapYearToWidth() method, and accessing values within the visualization object.

Finally, tasks are completed for tech-diversity-race.js (pie chart representing racial diversity of prominent tech companies), pay-gap-by-job-2017.js (scatter plot representing difference in pay for men and women across different jobs).

---

## Week 8

### Interview with a student: Simas Cesnauskas Video• . Duration: 5 minutes 5 min

Here is a summary of the text in 8 sentences, preserving key information:

Simas, a Goldsmiths computer science student, has expanded on a data visualization app to include multiple interactive sketches. He added features such as a pie chart, donut chart, Internet usage sketch, and immunization map, which allow users to explore data by hovering over colors or clicking on specific groups. Simas is particularly proud of the Internet usage sketch, which uses a constructor template to create circles representing different age and sex groups in the UK. He had not programmed before starting the course but was determined to learn and implement complex concepts like constructors. To work on this project, Simas chose data from male and female percentage of Internet usage in 2012 and 2017. One challenge he faced was getting the map functionality working with Leaflet, but he successfully created a new feature despite some technical issues. In retrospect, Simas thinks he could improve the map's performance or try using an alternative library like DS.js to create a 2D density plot. Overall, Simas is pleased with his project and proud of overcoming technical challenges to bring it to life.

---

### Reflection on interview with the student Reading• . Duration: 10 minutes 10 min

Here is a summary of the text in 8 sentences, preserving key information:

Simas' interview highlights the importance of considering design improvements for your own project, such as incorporating animation and redesigning core functionality. To incorporate animation into your designs, you'll need to understand its effective use in data visualization. Simas' use of constructor functions can be a good starting point for implementing more complex object-oriented structures in your application. When planning your implementation, consider using techniques like brainstorming and iterating different designs to achieve better outcomes. You should also keep track of your thinking and progress through regular logging, including sources of inspiration and technical help. For the midterm assignment, you'll need to detail your implementation plan and assess your current progress. To maximize the benefit of this process, consider what planning techniques can support advanced feature implementation and how to iterate different designs. As part of the assessment, you'll be asked to reflect on what you've achieved with your project, so start keeping track of your thinking and progress now.

---

### Topic 4 evaluation and summary Reading• . Duration: 30 minutes 30 min

There is no text to summarize in this request. The provided text appears to be a module introduction, checklist, and assignment instructions for a course or tutorial on p5.js data visualisation. It does not contain specific information, formulae, links, or technical details to summarize.

If you could provide the actual text you'd like me to summarize, I would be happy to assist you in condensing it into 8 sentences while preserving key information and details.

---

