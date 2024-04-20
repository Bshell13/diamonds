# Data analysis of Diamonds Dataset
This repo will make a dashboard over the analysis of the diamonds dataset from the seaborn module.

## Volume of a Diamond
In this dataset, I added a column that estimates the volume of a diamond by using the cone formula:<br>
$`V = \pi * r^2 * \frac{h}{3}`$<br>
r = radius<br>
h = height<br>

## Virtual Environment
Creating a virtual environment to install external modules to the environment.
```shell
py -m venv .venv
.venv\Scripts\activate
```

## External Libraries
List of libraries to install into the .venv
-  pandas
-  seaborn
-  shiny
-  shinylive
-  shinywidgets
-  shinyswatch
-  plotly
```shell
py -m pip install "list of external libraries"
py -m pip freeze > requirements.txt
```

## Run app.py Locally
Run this code in the terminal to run the app locally with quick changes.
```shell
shiny run --reload --launch-browser dashboard/app.py
```

# Push changes to docs folder in GitHub
Run this code in your terminal to report changes to Github.
```shell
shiny static-assets remove
shinylive export dashboard docs
py -m http.server --directory docs --bind localhost 8008
```