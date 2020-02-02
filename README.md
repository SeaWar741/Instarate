# **Instarate**
Web application for intrinsic image popularity score on instagram images

## Instructions

1) Install dependencies
2) Run flask server
3) Upload image
4) Receive popularity score

### **Dependencies**

* Python **3.7** or above

* GTX 1050 or above

* CuDNN is required

```python
    pip install flask
    pip install numpy
    pip install Torch
    pip install Torchvision
    pip install pillow
    pip install gunicorn
```

## **Try it**

Web app: https://instarate-beta.herokuapp.com/

### **References**

This proyect is based on [Intrinsic Image Popularity Assessment](https://arxiv.org/abs/1907.01985)

@inproceedings{ding2019intrinsic,
  title={Intrinsic Image Popularity Assessment},
  author={Ding, Keyan and Ma, Kede and Wang, Shiqi},
  booktitle={ACM International Conference on Multimedia},
  pages={1979--1987},
  year={2019},
  publisher={ACM}
}