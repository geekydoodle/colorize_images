<div align='center'><h1>Colorize images</h1></div>
<div align='center'>Easy way to colourize old images with python</div>

<div align="center"><img src="https://github.com/geekydoodle/colorize_images/blob/main/file/thumbnail.png" width="800" height="500"></div>

<h2>0. Clone from github</h2>

```
git clone https://github.com/geekydoodle/colorize_images.git
```

<h2>1. Change directory into the folder.</h2>

```
cd colorize_images
```
<div align='center'><h2>MODELS</h2></div>

https://github.com/richzhang/colorization/blob/caffe/colorization/models/colorization_deploy_v2.prototxt
https://github.com/richzhang/colorization/blob/caffe/resources/pts_in_hull.npy

<p>Download the models and save them to the model folder in this repo ☝️</p>

<p>and run these commands</p>

```
cd model
wget http://eecs.berkeley.edu/~rich.zhang/projects/2016_colorization/files/demo_v2/colorization_release_v2.caffemodel
```
<p>Same with this ☝️</p>

<h2>2. Make a venv</h2>

<p>Install venv package</p>
  
```
pip install virtualenv
```

<p>3. Make a venv</p>

```
python -m virtualenv name_of_venv
```

<h2>4. Activate the venv</h2>

```
source name_of_env/bin/activate
```

<h2>5. Install Open-CV</h2>

```
pip install opencv-contrib_python
```
<h2>6. Run!!!!!</h2>

```
python colorize_images.py
```

<p>Easy as that</p>

<p>Happy Computer Visioning!!!!!</p>
