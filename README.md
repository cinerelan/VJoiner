# VidJoiner
A video Concatenation Script that concatenates multiple video files into a single video using the MoviePy library.

## Features
**Concatenation:** Combines multiple video files into a single video.
<br />
**Output:** Exports the concatenated video in MP4 format with the libx264 codec at 24 fps.

## Requirements
<ul>
  <li>Python 3.x</li>
  <li>MoviePy</li>
</ul>


## Installation
<ol>
  <li>Clone this repository to your local machine.</li>
  <li>
    Install the required dependencies using pip:
    <pre><code>pip install moviepy</code></pre>
  </li>
</ol>

## Usage
<ol>
  <li>Place your input video files in the specified paths or update the paths in the script.</li>
  <li>Set the <b>output_directory</b> variable to your desired output folder.</li>
  <li>
    Run the script:
    <pre><code>python vidjoiner.py</code></pre>
  </li>
  <li>The concatenated video will be saved as <b>output.mp4</b> in the specified output directory.</li>
</ol>
