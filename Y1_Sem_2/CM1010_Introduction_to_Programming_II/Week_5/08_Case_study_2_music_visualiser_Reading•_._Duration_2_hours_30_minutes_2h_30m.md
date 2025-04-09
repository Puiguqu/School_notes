# Case study 2: music visualiser Reading• . Duration: 2 hours 30 minutes 2h 30m

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

