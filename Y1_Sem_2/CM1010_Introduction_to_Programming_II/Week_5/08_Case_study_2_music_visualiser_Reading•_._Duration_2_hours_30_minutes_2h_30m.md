# Case study 2: music visualiser Reading• . Duration: 2 hours 30 minutes 2h 30m

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

