
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

![test_res_AdobeExpress](https://user-images.githubusercontent.com/110551998/190914264-4fd48d7a-0cee-4db0-8ec5-da524381f0fd.gif)

### Distinguishing whether a pet is on the couch or by the couch:

![near_couch_res_AdobeExpress](https://user-images.githubusercontent.com/110551998/190914243-10098c58-109c-4f6c-b63c-eceedfe432bf.gif)

### Detecting from different angels:

![output_AdobeExpress](https://user-images.githubusercontent.com/110551998/190914279-d0d09f0f-3682-480b-ab18-07a0ed3e0e14.gif)
