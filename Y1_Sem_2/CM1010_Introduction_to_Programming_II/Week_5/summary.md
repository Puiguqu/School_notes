# Week 5 - CM1010 Introduction to Programming II - Topic 1 Object orientation in practice - Week 1

## Introduction to case study 2: music visualiser Video• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/lwvMA/introduction-to-case-study-2-music-visualiser)

Here is a summary of the text in 8 sentences, preserving key information, formulae, links, and technical details:

Music visualization has been used to enhance music listening experiences for almost five decades, dating back to the Atari video music system in 1977. Recently, music playback software such as Winamp, Windows Media Player, and iTunes have included in-built visualization features. The demo scene and VJing art forms also explore music visualization, where performers create visual output in front of a live audience. This case study aims to build upon a basic music visualization program, creating out-of-this-world visualizations that reflect the tone, energy, and time signature of music. The application allows users to choose between different visualizations, including an old-fashioned Spectrum display for sound amplitudes, a wave pattern responding to FFT output, and "needles" displaying amplitude in four frequency bands. The application is responsive, resizing with screen changes and allowing full-screen mode with a Play button. However, there are limitations, such as a bug that needs to be fixed and the lack of perfect scaling. A future video will delve into the technical details of how the music visualization program works under the hood.

---

## P5.js sound: loading and playing a sound Video• . Duration: 16 minutes 16 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/DpA0T/p5-js-sound-loading-and-playing-a-sound)

Here is a written summary of the video transcript:

The video introduces the P5.js sound library and shows how to play sounds in an interactive program. The speaker explains that the sound library provides objects called "sound files" which can be used to create music.

The speaker then demonstrates how to load and play a sound file using the `loadSound()` function, which returns a promise when the sound is loaded. They use the `successCallback` callback to execute code when the sound is loaded, in this case logging a message to the console.

Next, the speaker shows how to pause and resume playback of a sound file using the `pause()` and `play()` functions. They demonstrate how to check if a sound file has been paused or not using the `isPaused` method.

The speaker also discusses how to load large sound files, which can take several seconds to load. To handle this situation, they use the `successCallback` callback to execute code when the sound is loaded, and only play the sound file if it has actually finished loading (i.e., the `isLoaded` variable is set to true).

Throughout the video, the speaker uses examples to illustrate each concept, such as playing a single beep sound or creating a short melody using multiple sounds. They also encourage viewers to try out different sounds and experiments with the P5.js sound library.

Overall, the video provides a comprehensive introduction to the basics of working with audio in P5.js, including loading and playing sounds, pausing and resuming playback, and handling large sound files.

---

## P5.js sound: amplitude Video• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/zvamN/p5-js-sound-amplitude)

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

## P5.js sound: frequency, part 1 Video• . Duration: 4 minutes 4 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/yuHQf/p5-js-sound-frequency-part-1)

Here is a summary of the text in 8 sentences, preserving key information and concepts:

The concept of frequency is an important aspect of sound, where pitch is measured in hertz (Hz). The human hearing range spans from 20 Hz to 20,000 Hz. Sounds can be either pitched or unpitched, with pitched sounds having a dominant frequency that can be described digitally using frequency spectra. To accurately describe a sound digitally, every possible frequency within the hearing range must be considered and its amplitude measured, resulting in a complex bar chart known as a frequency spectrum. However, this is impractical due to the vast number of frequencies (18,980) involved, so they are grouped into bands for easier analysis. A graphic equalizer display can provide an idea of how these frequency bands shift over time as the sound changes. To analyze sound in p5.js, a rolling frequency spectrum can be created using FFT objects, allowing for a dynamic representation of music tracks. The process involves taking multiple frequency spectra to capture the changing characteristics of the sound over time.

---

## P5.js sound: frequency, part 2 Video• . Duration: 13 minutes 13 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/Bo3uf/p5-js-sound-frequency-part-2)

This is a transcript of an online lesson or tutorial on using P5.js, a JavaScript library for creating visualizations. The lesson covers various topics related to sound and music visualization in P5.js.

The transcript begins by introducing the concept of frequency analysis in music, which involves breaking down a musical signal into its component frequencies. It then moves on to using P5.js to load and play sounds, manipulate amplitude (the loudness or volume of a sound), and analyze frequency.

The lesson also covers how to use P5.js to create simple music visualizations, such as isolating different parts of a track by grouping together different frequency bands. The transcript includes tips and advice on how to experiment with different visualization techniques and create more complex music visualizations.

Throughout the lesson, there are links to additional resources, including videos and readings that provide further information and practice assignments for students to complete.

The final section includes a video interview with a student who created a music visualization application, as well as some reflection on the process of creating such an application.

Overall, this transcript appears to be part of a larger lesson or course on using P5.js for music visualization and sound analysis.

---

## Music visualisation application: under the hood Video• . Duration: 29 minutes 29 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/spnED/music-visualisation-application-under-the-hood)

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

## Interview with a student: Taylor Millin Read Video• . Duration: 6 minutes 6 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/lecture/hZj2o/interview-with-a-student-taylor-millin-read)

The video transcript is about an Introduction to Programming project at Goldsmiths University, where a first-year computer science student, Taylor, built an application using the P5.js library. The application has four different visualizations that react to the waveform and spectrum analysis of the FFT algorithm: Spin, which spins in response to the waveform; a store waveform that moves from the center point when clicked; and a video visualization that uses the pixel array to change colors based on frequency amplitudes. Taylor's favorite visualization is the video one, which he created using the pixel array to edit red, green, blue, and alpha values depending on the volume of certain frequencies.

The application was built using P5.js, and Taylor used a function to update pixels by editing their RGB values. He also used the FFT algorithm to analyze the music signal and generate visualizations that react to it. The video app uses the pixel array to change colors as the music plays, and Taylor created this effect by making edits to the red, green, blue, and alpha values of each individual pixel.

Taylor's inspiration for the video app was to use video from the computer camera and the pixel array to create a fluid reaction with the music. He also wanted to explore alternative color systems beyond RGB, but ultimately used RGB throughout his project. Taylor faced challenges in finding better ways to manipulate colors and editing code, but he created a simple yet effective solution using the angle parameter to rotate pixels.

Overall, Taylor's project demonstrates the capabilities of P5.js for building interactive music visualizations that react to audio signals. The video app is an example of how this library can be used to create engaging and dynamic visuals that respond to sound waves.

---

## Case study 2: music visualiser Reading• . Duration: 2 hours 30 minutes 2h 30m

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/supplement/06kJT/case-study-2-music-visualiser)

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

## Making your own sound composition Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/supplement/DRu7H/making-your-own-sound-composition)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

To complete this sketch, create an `initialized` global variable with a value of `false` initially. When `initialized` is `false`, draw a message on the screen. The loop method's `rate` argument can be altered to explore sound playback effects, including setting a start time (currently set to 0). Use the `map` function and mouse x position to change playback rate when playback starts. Pause sound playback when the space button is pressed by adding a condition to the `keyPressed` function that checks for the space button. To allow for playback restarts, nest a further conditional as Simon shows in the previous video. An anonymous function can be added to the `loadSound` call to stop playback until the file is fully loaded. Explore other sound library methods and search for freely available sounds if needed.

---

## Playing with amplitude Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/supplement/evKIR/playing-with-amplitude)

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

## Playing with frequency Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/supplement/H6Qu2/playing-with-frequency)

There is no text provided for me to summarize. The text appears to be a description of a video tutorial on using p5.js with sound, specifically frequency analysis and music visualization. 

If you provide the actual text or context, I can help you summarize it in 8 sentences while preserving key information, formulae, links, and technical details.

---

## Reflection on interview with the student Reading• . Duration: 30 minutes 30 min

[Original lesson](https://www.coursera.org/learn/uol-introduction-to-programming-2/supplement/O9Lwq/reflection-on-interview-with-the-student)

Here is a summary of the text in 8 sentences, preserving key information:

The interview with Taylor has encouraged reflection on progress made so far with the drawing application project. Key takeaways from the interview include potential features to add or redesign, such as controls for the music visualizer and different waveform manipulation techniques. Incorporating camera and microphone functionality into the application is also an idea worth exploring. The midterm assignment will require a detailed implementation plan, which can be maximized with planning techniques and brainstorming to iterate on designs. Regular progress logging, tracking of design sources and inspiration, and technical help are essential aspects to keep track of for assessment purposes. Taylor's experience has taught him what he would do differently in the future, highlighting the importance of reflection on one's project. To prepare for this self-assessment, students should start keeping a record of their thinking, progress, and brainstorming designs. The assignments and assessments will require students to upload these logs as part of their midterm or end-of-term evaluations.

---

