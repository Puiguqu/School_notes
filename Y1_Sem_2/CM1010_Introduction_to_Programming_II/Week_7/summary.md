# Week 7 - CM1010 Introduction to Programming II - Topic 1 Object orientation in practice - Week 1

## Introduction to case study 3: data visualisation Video• . Duration: 42 seconds 42 sec

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/H7gHr/introduction-to-case-study-3-data-visualisation)

There is no text provided for me to summarize. The given text appears to be a transcription of a video presentation, likely from an educational platform or tutorial series, and does not contain any specific data, formulae, links, or technical details to summarize. 

However, I can provide some general information about the context:

This text is likely from an introductory course or tutorial on programming, specifically focusing on p5.js, a JavaScript library for creative coding. The transcript appears to be from a video presentation that provides an overview of data visualization using p5's tools. The content suggests that the video will guide viewers through the code and structure of a data visualization app, with some features intentionally left incomplete for completion in future lessons.

---

## Introducing P5 data Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/meXhl/introducing-p5-data)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The Toolkit of Data Visualizations case study requires importing the table object from the pm library to construct an application. The table object can be used to store and manipulate quantitative data, including numbers, strings, and categorizable data, which are organized into rows and columns. Qualitative data, such as text and images, is not a focus of this case study. To load external data, a CSV file (Comma Separated Values) can be used, which stores the data without formatting. The `loadTable()` command is used to load the CSV file, and the `preload` function ensures that the data is ready for use when needed. The table object provides methods for accessing rows and columns, including searching for specific values, setting and removing rows, and accessing data by column. For example, `getColumn()` can be used to retrieve all values in a particular column as an array of strings, which may need to be converted to numbers. The documentation provides additional information on the methods available for manipulating tabulated data using the table object.

---

## Accessing external data Video• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/5WdJy/accessing-external-data)

This transcript appears to be from a video lecture on using the P5.js library for data visualization. The speaker is walking through the process of loading and manipulating a dataset, creating a scatterplot, and adding additional visual elements such as a line of best fit.

Here are some key points that can be inferred from the transcript:

1. The speaker starts by introducing the P5.js library and its table object, which allows for easy access to data.
2. They demonstrate how to load external data into the table object and manipulate it using various functions such as `parsefloat` and `sin`.
3. The speaker creates a scatterplot using the `scatterplot()` function and adds data points to it by calling `myScatter.plot()`.
4. They add additional visual elements, such as lines of best fit, by creating new functions that access the underlying data.
5. Throughout the video, the speaker emphasizes the importance of parsing data types and ensuring that numerical values are used correctly in mathematical operations.

The final section of the transcript mentions a case study 3, which suggests that this video is part of a larger course or tutorial series on using P5.js for data visualization. The accompanying practice assignments and additional page content suggest that the speaker provides hands-on exercises and resources to support learning.

Overall, this transcript appears to be a comprehensive introduction to using P5.js for data visualization, covering key concepts such as loading data, creating scatterplots, and adding visual elements like lines of best fit.

---

## Data visualisation application: under the hood Video• . Duration: 42 minutes 42 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/Ta3uA/data-visualisation-application-under-the-hood)

This is a transcript of a video lecture on P5.js, a JavaScript library for creating interactive graphics and animations. The lecture is part of an introductory course on P5.js.

The lecturer introduces the concept of data visualization and explains how P5.js can be used to create interactive visualizations. They demonstrate how to access external data using APIs and show examples of different types of visualizations, including bar charts, pie charts, and scatter plots.

The lecturer then focuses on a specific case study, "TechDiversityRace", which is an object that displays a pie chart. They walk the audience through the code, explaining each part and how it works together to create the visualization.

They highlight key concepts such as constructors, methods, and layouts, and demonstrate how these are used in P5.js to create interactive visualizations.

The lecture also covers other topics, including accessing external data, preparing for a case study, and practice assignments. The lecturer encourages the audience to explore the code and learn more about the underlying mechanics of the visualization app.

Key takeaways from this transcript include:

* Understanding how to access external data using APIs
* Familiarity with P5.js constructors, methods, and layouts
* Ability to create interactive visualizations using P5.js
* Understanding of how to break down complex code into smaller parts

Overall, this lecture aims to provide a foundational understanding of P5.js and its capabilities for creating interactive visualizations.

---

## Case study 3: data visualisation Reading• . Duration: 3 hours 3h

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/supplement/nW6GE/case-study-3-data-visualisation)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

The task involves completing visualizations in a data visualization project template, starting with stekch.js. The goal is to create stacked bar charts for tech diversity by gender, line graphs for pay gap between female and male employees over time, and pie charts for racial diversity of prominent tech companies. The raw data for the first visualization is stored in ./data/tech-diversity/gender-2018.csv, while the raw data for the second and third visualizations are stored in ./data/pay-gap/all-employees-hourly-pay-by-gender-1997-2017.csv and ./data/tech-diversity/race-2018.csv, respectively. The project uses the p5.js library and assumes knowledge of JavaScript programming. To complete the first visualization, the code needs to be modified to extract relevant data from each table row and store it in a company object using methods such as getString() and getNum(). Similarly, the second and third visualizations require completing the mapPayGapToHeight(), rect(), and line() functions, respectively, by utilizing the mapYearToWidth() method and accessing values within the visualization object. The project also includes instructions for creating a select DOM element to populate options programmatically using company names from the data.

---

