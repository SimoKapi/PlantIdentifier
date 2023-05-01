# PlantIdentifier
<!-- ##Creates a PowerPoint presentation from an input sequence of images
Each slide of the PowerPoint will contain one image and its matching plant name -->
## Creates a phylogenetic tree

**Dependencies:**
```
tkinter, python-pptx, numpy, PIL, requests, json, csv, selenium, webdriver_manager, bs4
```
##Instructions:

<!-- - Drag all your photos into the **id_dir** directory (regardless of the image format)
- Download this dataset: (https://zenodo.org/record/4726653#.ZE5bJC9BxQK) and drag it into the main directory. **Caution: 31.65 GB**
- Open a terminal window in the main directory, run **python main.py true** to train the model, then **python main.py false** to evaluate your images and create the resulting PowerPoint
- All photos will be converted to Portable Pixmap Format (.ppm), original format moved to **wrong_formats** -->

- If using just the plant names, a.k.a. to only create a phylogenetic tree, write the latin names of your plants into the **plants.csv** file, separated by commas (Example: muscari neglectum,taraxacum officinale,erica carnea,iberis sempervirens). -> Open a terminal window in the main directory and run **python value_getter.py true true**
- If using images, name each image by the corresponding latin name, replacing spaces with underscores (Example: muscar_neglectum) -> Open a terminal window in the main directory and run **python value_getter.py true false**
- Sit back, relax, and let the magic happen
- Take a screenshot of the resulting phylogenetic tree and find the PowerPoint in the main directory (Keep in mind using just the plant names does **not** yield a PowerPoint presentation)

![Phylogenetic tree example]/Photos/tree.png "Example of a tree created by this program"
![Powerpoint slide example]/Photos/powerpoint.png "Example of a powerpoint slide created by this program"