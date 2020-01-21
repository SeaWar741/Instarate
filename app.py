from flask import Flask, request,render_template
import argparse
import torch
import torchvision.models
import torchvision.transforms as transforms
from PIL import Image

app = Flask(__name__)

def prepare_image(image):
    if image.mode != 'RGB':
        image = image.convert("RGB")
    Transform = transforms.Compose([
            transforms.Resize([224,224]),      
            transforms.ToTensor(),
            ])
    image = Transform(image)   
    image = image.unsqueeze(0)
    return image

def predict(image, model):
    image = prepare_image(image)
    with torch.no_grad():
        preds = model(image)
    score = preds.detach().numpy().item()
    return(str(round(score,2))+"/10")

def predicting(image_in):
    device = torch.device("cpu")
    image = Image.open(image_in)
    model = torchvision.models.resnet50()
    model.to(device)
    model.fc = torch.nn.Linear(in_features=2048, out_features=1)
    model.load_state_dict(torch.load('model/model-resnet50.pth',map_location=torch.device('cpu'))) 
    model.eval()
    return predict(image, model)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('index.html',value ='Hi')
    if request.method == 'POST':
        print(request.files)
        if 'file' not in request.files:
            print('file not uploaded')
            return
        file = request.files['file']
        image = file
        flower_name = predicting(image)
        return render_template('result.html',flower = flower_name)

if __name__ == '__main__':
    app.run(debug=True)
