
# PetVision

A YOLOv6 based computer vision system to identify whether pets are getting on the couch, 
and if so - commands them to get down.

My dog - Zoe, isn't allowed to be on the couch when we are not present, 
so once again I have decided to use software to find a solution: play "down!" command 
anytime she gets on the couch.






## How Does It Work?
I chose to implement the new [YOLOv6](https://github.com/meituan/YOLOv6) to detect
couches and pets using webcam or video file, and get their surrounding boxes coordiantes.

After getting the coordiantes, the software checks if the pet is on the couch conssidering
edge cases, such as when a pet is higher than the couch or their boxes are overlaping but the
pet is standing by the couch.


## Installation

```
pip3 install -r requirements.txt
```


## Some examples of training with Zoe:

### Detecting and commanding to get down:


https://user-images.githubusercontent.com/110551998/190912843-02e324f9-c861-4ad8-908b-aef1e7b0a64f.mp4

### Distinguishing if the pet is by the couch and not on it:



https://user-images.githubusercontent.com/110551998/190912904-c5a6c568-e695-40e1-b8a3-c672b1e2a654.mp4


### Detecting from different angels:


https://user-images.githubusercontent.com/110551998/190912987-cd47c8b5-5004-4248-9f1d-9a6e042aff67.mp4

