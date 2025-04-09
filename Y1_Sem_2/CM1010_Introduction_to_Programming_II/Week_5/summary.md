# Week 5 - CM1010 Introduction to Programming II - Topic 1 Object orientation in practice - Week 1

## Introduction to case study 2: music visualiser Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/lwvMA/introduction-to-case-study-2-music-visualiser)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

Music visualization has been used to enhance the listening experience of music for nearly five decades, dating back to the Atari video music system in 1977. Recent advancements have led to the development of in-built visualization features in music playback software such as Winamp, Windows Media Player, and iTunes. The current trend for VJing (Visual Jamming) involves performers creating arresting visual output in front of a live audience, while the demo scene has pushed computing platforms to produce graphical output beyond their processing power capabilities. This case study aims to build upon a basic music visualization program and create out-of-this-world visualizations that reflect the tone, energy, and time signature of music. The application allows for full-screen mode and resizing, with a Play button that springs into life and plays the first visualization, such as an old-fashioned Spectrum display showing different colors for diverse sound amplitudes. Users can choose from various visualizations, including a wave pattern and "needles" displaying amplitude in four frequency bands (bass, low-mids, high-mids, and treble). The application has limitations, such as responsiveness issues when resizing the screen or window. Future videos will delve into the technical details of how this application works under the hood.

---

## P5.js sound: loading and playing a sound Video• . Duration: 16 minutes 16 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/DpA0T/p5-js-sound-loading-and-playing-a-sound)

Based on the provided transcript, here is an outline of the key points covered in Lesson 3.1 Introduction to P5 Sounds:

I. Introduction
- Brief overview of P5 sounds and its capabilities.

II. Preparing for Case Study 2
- Overview of case study 2 and what it entails.
- Importance of understanding how to work with sound in programming.

III. Loading and Playing a Sound
- Explanation of the `loadSound()` function and its parameters.
- Discussion of callbacks (success, error, and while loading) used when loading large sounds.
- Example code that demonstrates using success callback to verify if the sound has loaded.

IV. Making Your Own Sound Composition
- Encouragement for students to explore P5 Sounds further by checking out freesound.org or similar resources.
- Suggestion to experiment with different methods (amplitude, frequency) and techniques in creating unique sounds.

Key Takeaways:

- Understanding how to load and play sounds using the `loadSound()` function and its callbacks.
- Familiarity with basic sound manipulation techniques like amplitude and frequency modification.
- The importance of testing and experimentation when working with audio files in programming.

---

## P5.js sound: amplitude Video• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/zvamN/p5-js-sound-amplitude)

Based on the provided transcript, I will summarize the main points of Lesson 3.1 Introduction to amplitude analysis in P5.js.

**Summary**

In this lesson, students learn how to analyze sound using P5.js. The first step is to create a simple program that loads and plays a sound file using the `loadSound()` function. Once the sound is loaded, students can measure its amplitude using the `amplitude()` function. Amplitude represents the magnitude of the sound wave at any given time.

**Key Concepts**

1. **Amplitude analysis**: Measuring the magnitude of a sound wave over time.
2. **P5.js sound functions**: `loadSound()`, `play()`, and `amp()` (short for amplitude).
3. **Visualizing amplitude**: Using the `beginShape()`, `vertex()`, and `endShape()` functions to create visual representations of amplitude.

**Practical Exercise**

Students are encouraged to:

1. Experiment with different sound files to observe changes in amplitude.
2. Create animations using amplitude, such as changing the size or rotation of graphics.
3. Explore how amplitude affects musical composition.

By analyzing amplitude, students can gain insights into the properties of sound waves and create interactive visualizations that respond to audio input. This skill is essential for creating engaging music visualizations and understanding the relationship between sound and visuals.

---

## P5.js sound: frequency, part 1 Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/yuHQf/p5-js-sound-frequency-part-1)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

The concept of frequency is an important aspect of sound quality, where pitch is directly related to frequency. Human hearing range spans from 20 Hz to 20,000 Hz, but factors like amplitude and listener age can affect audibility. Certain sounds, such as the triangle and kettledrum, cannot be precisely measured due to their complex composition of multiple frequencies. In contrast, single notes on a piano can be described using a single frequency, while chords require considering multiple frequencies and amplitudes. To accurately describe a sound digitally, one must measure every possible frequency from 20 Hz to 20,000 Hz and record its amplitude, resulting in a frequency spectrum. Frequency bands are used to group together too many frequencies, making it impractical to consider all 18,980 possible frequencies simultaneously. The Fast Fourier Transform (FFT) objects in p5.js can be used to create a rolling frequency spectrum for music tracks, allowing for the analysis of sound properties like amplitude and pitch over time. By understanding frequency spectra and their applications, one can gain insight into the complex nature of sound and develop skills for analyzing and manipulating audio signals.

---

## P5.js sound: frequency, part 2 Video• . Duration: 13 minutes 13 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/Bo3uf/p5-js-sound-frequency-part-2)

Based on the provided transcript, here's a summary of the lesson:

**Lesson Topic:** Analyzing Sound using P5.js

**Key Concepts:**

1. Introduction to P5.js sound functionality
2. Loading and playing sounds in P5.js
3. Amplitude analysis (making music compositions)
4. Frequency analysis (playing with frequency bands)

**Learning Objectives:**

* Understand how to load and play sounds in P5.js
* Learn about amplitude analysis for making music compositions
* Discover how to analyze sound using frequency bands

**Practice Assignments:**

1. Analyzing sound (30 minutes): Students are asked to experiment with analyzing sound in P5.js.
2. Exploring a music visualisation app (30 minutes): Students learn about a specific music visualisation application and its underlying technology.

**Additional Resources:**

* Videos: tutorials on loading sounds, amplitude analysis, frequency analysis, and creating music compositions.
* Reading materials: articles on reading sound data and playing with amplitude.
* Interviews: an interview with a student who has experience with music visualisation applications.

This lesson provides students with hands-on experience in analyzing sound using P5.js, which is essential for creating interactive audio-visual experiences. By exploring the concepts of amplitude analysis and frequency bands, students can develop their skills in understanding and manipulating sound data.

---

## Music visualisation application: under the hood Video• . Duration: 29 minutes 29 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/spnED/music-visualisation-application-under-the-hood)

The provided transcript appears to be a lesson plan or lecture notes for a programming course, specifically focused on the P5.js library. The content is divided into several sections:

1. Introduction
2. Preparing for case study 2
3. Video and reading materials related to sound in P5.js (loading and playing sounds, making your own sound composition, playing with amplitude, frequency, etc.)
4. Practice assignments related to analyzing sound and understanding the music visualisation app

The transcript includes code examples and diagrams, but they are not directly transcribed here.

The main topics covered in this lesson appear to be:

* Understanding the P5.js library and its capabilities
* Creating interactive applications with sound using P5.js
* Analyzing sound waves and understanding amplitude, frequency, etc.
* Building a music visualisation app using P5.js

Overall, this lesson seems to be part of a larger course on programming, specifically focused on web development and interactive applications.

---

## Interview with a student: Taylor Millin Read Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/hZj2o/interview-with-a-student-taylor-millin-read)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Taylor, a first-year computer science student at Goldsmiths, built an application for his Introduction to Programming project based on the music visualization app. The application features four different visualizations: Spin, which reacts to waveform and spectrum analysis of the FFT algorithm; Video, which uses the pixel array to change colors in real-time; Store Waveform, which moves when clicked; and a third visualization that Taylor did not explain further. Taylor's favorite visualization is Video, which uses the pixel array to edit RGB values depending on the volume or amplitude of certain frequencies. This was achieved by using the p5 library and filling the pixel array with new colors in the draw function. The application also features simple controls, including a play button, dial key presses, and a beat analyzer that Taylor wanted to implement but did not have time for. Taylor's inspiration for the Video app came from wanting to use video from the computer's camera and react it fluidly with music. The application was built using p5.js, which allows for easy manipulation of colors and pixels. Taylor would recommend using other color systems, such as HSB or HSV, in future projects.

---

## Case study 2: music visualiser Reading• . Duration: 2 hours 30 minutes 2h 30m

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/supplement/06kJT/case-study-2-music-visualiser)

I'll provide a step-by-step solution to complete the music visualizer project.

**Step 1: Complete the `mousePressed()` function in `controlsAndInput.js`**

In the `ControlsAndInput` constructor function, add the following code to check if the mouse click is on the play button:
```javascript
playButton.addEventListener('click', () => {
  music.play();
});
```
This will start the music when the play button is clicked.

**Step 2: Complete the visualization menu in `controlsAndInput.js`**

Add the following code to display the visualization menu:
```javascript
menu = document.getElementById('menu');

function showMenu() {
  menu.style.display = 'block';
}

function hideMenu() {
  menu.style.display = 'none';
}

showMenu();
```
This will display the menu when the page loads and toggle it off when another element is clicked.

**Step 3: Complete the `Spectrum()` constructor function in `spectrum.js`**

Modify the `Spectrum` constructor function to draw horizontal bars instead of vertical ones:
```javascript
function Spectrum() {
  // ...

  barWidth = 10;
  barHeight = height / fft.length;

  for (let i = 0; i < fft.length; i++) {
    const amplitude = fft[i] * 255;
    const x = i * barWidth;
    const y = height - (amplitude * barHeight);
    const color = `rgb(${Math.floor(128 + (127 * amplitude))}, 255, ${Math.floor(128 + (128 * amplitude))})`;

    ctx.fillStyle = color;
    ctx.fillRect(x, y, barWidth, barHeight);
  }
}
```
This will draw horizontal bars with a gradual transition from green to red based on the amplitude value.

**Step 4: Complete the `Needles()` constructor function in `needles.js`**

Modify the `Needles` constructor function to draw the frequency bands:
```javascript
function Needles() {
  // ...

  for (let i = 0; i < fft.length; i++) {
    const amplitude = fft[i] * 255;
    const x = i * barWidth;
    const y = height - (amplitude * barHeight);
    const color = `rgb(${Math.floor(128 + (127 * amplitude))}, 255, ${Math.floor(128 + (128 * amplitude))})`;

    ctx.fillStyle = color;
    ctx.fillRect(x, y, barWidth, barHeight);

    if (i < fft.length / 2) {
      const frequency = i / fft.length * 200; // adjust this value to change the frequency range
      ctx.beginPath();
      ctx.moveTo(frequency, height);
      ctx.lineTo(frequency, 0);
      ctx.stroke();
    }
  }
}
```
This will draw horizontal bars with a gradual transition from green to red based on the amplitude value and also add vertical lines for the frequency bands.

**Step 5: Update the `draw()` function in `index.js`**

Modify the `draw()` function to call the `Spectrum` and `Needles` constructors:
```javascript
function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  spectrum.draw();
  needles.draw();
}
```
This will update the visualization when the `draw()` function is called.

**Step 6: Upload your completed drawing app sketch for peer review**

Once you've completed all the steps, upload your sketch to a platform like GitHub or GitLab and share it with your peers. This will allow them to provide feedback on your progress and help you identify areas for improvement.

---

## Making your own sound composition Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/supplement/DRu7H/making-your-own-sound-composition)

Here is a summary of the text in 8 sentences:

To complete this p5.js sketch, create an initial global variable "isInitialised" and set it to false initially. Draw a message on the screen when "isInitialised" is false and start playback on the first key press when the sketch is run. Alter the rate argument of the loop method and set a start time by setting it to zero. Use the mouse x position and the map function to change the playback rate based on the mouse position when playback is started. Pause the sound when the space button is pressed, which requires adding a condition to the keyPressed function that checks for the space button. To allow for playback to be restarted, nest another conditional as shown in Simon's video. Add an anonymous function to the call to loadSound which stops playback until the file is fully loaded. Explore other methods provided by the sound library and search for freely available sounds if needed.

---

## Playing with amplitude Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/supplement/evKIR/playing-with-amplitude)

Here is a summary of the text in 8 sentences:

The video tutorial demonstrates how to use amplitude to alter the volume of p5.js sketches. To complete the exercise, follow these steps: create a global variable "amplitude" with an initial value of a new p5 Amplitude object in setup. In the draw function, calculate the current level of amplitude and display it on the screen using text() or an ellipse that changes size based on the amplitude. Use the map function to scale the ellipse and the array amplitudes to display as a series of ellipses across the screen. Push the current amplitude to the end of the amplitudes array in draw, and remove the first value using shift. This will create an animation of ellipses changing size based on the amplitude of the sound file. The exercise encourages thinking about other forms of animation that could be designed using amplitude. To complete the exercise, download the ZIP file from the video resources or link provided.

---

## Playing with frequency Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/supplement/H6Qu2/playing-with-frequency)

Here is a summary of the text in 8 sentences, preserving key information:

The video tutorial by Simon covers the basics of frequency and volume alteration in p5.js sketches. To complete the template, download the ZIP file or access it from the provided link. In the sketch, create a global variable "fft" and set it to an FFT object in the setup function. In the draw function, analyze the FFT using its "analyse" method, storing the result in a new variable called "freqs". The resulting array should have 1024 elements; draw the values using a for loop. Use the "getEnergy" method from the FFT to calculate energy bands (e.g., "bass", "highMid"), and use these values to set ellipse dimensions. Replicate this process for each energy band, experimenting with different tracks and animations. This tutorial is part of Lesson 3.1-3.5 in the course, covering topics such as sound composition, frequency analysis, and music visualization applications.

---

## Reflection on interview with the student Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/supplement/O9Lwq/reflection-on-interview-with-the-student)

Here is a summary of the text in 8 sentences, preserving key information:

The interview with Taylor has prompted reflection on the progress made with the drawing application project. Features such as adding controls to the music visualiser and manipulating the waveform have been inspiring and worth considering for implementation. The use of camera and microphone features in Taylor's application could also be incorporated into the project, but handling their absence would need to be addressed. Planning techniques such as brainstorming, iterating different designs, and regular progress logging will be essential for the midterm assignment. The assessment of current progress will help determine if the project is on target to complete on time and meet the required standard. Taylor's reflective thoughts on his project and potential improvements can serve as a model for the final application submission. To prepare for this, it is recommended to start keeping track of designs, sketches, sources of inspiration, technical help, and regular progress updates. These will be essential components for the midterm or end-of-term assessments.

---

