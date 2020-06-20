   # UI screenshot to React

This tool converts a given UI screenshot into corresponding React Code with Carbon design.
- The model is a combination of Encoder-Decoder network which is a CNN-LSTM architecture generally used in Image captioning models.
- CNN is used to extract the components in a given screenshot and LSTM network uses this information to predict the DSL code.
- This DSL code (output) is passed to DSL mapper which gives React JS code with carbon design.
## Input is a UI screenshot 

![Image 1](https://github.com/sourabhk19/UI-screenshot-to-React-/blob/master/README_images/z1.png)

## Output is React.JS Code with Carbon Components

![Image 2](https://github.com/sourabhk19/UI-screenshot-to-React-/blob/master/README_images/react_code.PNG)

### Training Procedure:

- Clone the repository.
- Extract the dataset files.
- Run [this](https://github.com/sourabhk19/UI-screenshot-to-React-/blob/master/React_Train.ipynb) code for training the dataset by appropriately changing the directory folder names.
- Once the training is done, model weights will be generated. 

### Testing:

- Run [this](https://github.com/sourabhk19/UI-screenshot-to-React-/blob/master/React_Test.ipynb) code by selecting Test directory and [pretrained model](https://github.com/sourabhk19/UI-screenshot-to-React-/tree/master/pretrained%20models)

### For creating additional dataset:

- To convert images to NPZ array, use [this](https://github.com/sourabhk19/UI-screenshot-to-React-/blob/master/Dsl_to_React.ipynb).
- Write corresponding GUI file (intermediate DSL code) in this way.

![Image 3](https://github.com/sourabhk19/UI-screenshot-to-React-/blob/master/README_images/gui.PNG)



## Acknowledgements

The idea is influenced by Toni Beltramelli's pix2code [paper](https://arxiv.org/abs/1705.07962).
