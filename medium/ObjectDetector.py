# Imports we will need to run the code

from PIL import Image
import torch 
print('torch version : {torch.__version__}')

import torchvision
print(f'torchvision version : {torchvision.__version__}')
from torchvision.transforms.functional import pil_to_tensor
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.utils import draw_bounding_boxes
from torchvision.transforms.functional import to_pil_image

import pycocotools
from pycocotools.coco import COCO

import numpy as np
import matplotlib.pyplot as plt
import os


# Orchestrating cells
MODEL_RESERVE = fasterrcnn_resnet50_fpn(pretrained=True, progress=False)

# here we are to implement the main process class

class ObjectDetector:
  """
    Args:
      path_img - an absolute path to the image(s) we are to process
  """

  def __init__(self, img_path=None, model=MODEL_RESERVE, threshold = None):
    # main parameters and containers
    self.img_path = img_path
    self.images = {}
    self.formats = ['jpg', 'jpeg', 'JPG', 'JPEG', 'PNG', 'png']

    # model-related attributes
    self.model = model
    self.model.eval() 
    self.threshold = threshold

    # if file, append
    if os.path.isfile(self.img_path):
      key = self.img_path.split('/')[-1]
      self.images[key] = {}
      self.images[key]['image'] = Image.open(img_path)

    # if dir, iterate
    elif os.path.isdir(self.img_path):
      for f in os.listdir(self.img_path):
        if f.split('.')[-1] in self.formats:
          self.images[f] = {}
          self.images[f]['image'] = Image.open(f)

    print(f'Read and processed {len(self.images)} files.')


    # put the sequence of actions needed here
    self._get_tensors()
    self.get_predictions()
    self._apply_threshold()
    self._load_labels()


  def _get_tensors(self):
    for i, k in enumerate(self.images):
      image_tensor_int = pil_to_tensor(self.images[k]['image'])
      image_tensor_int = image_tensor_int.unsqueeze(dim=0)
      image_tensor_float = image_tensor_int / 255.0
      self.images[k]['float_tensor'] = image_tensor_float
      print(f'Processed {i + 1} / {len(self.images)} images to tensors.', end = '\r')


  def get_predictions(self):
    N = len(self.images)
    for i, k in enumerate(self.images):
      print(f'Processing image {i + 1} / {N}.')
      img_prediction = self.model(self.images[k]['float_tensor'])
      self.images[k]['prediction'] = img_prediction
    print('Processing done.')


  def _apply_threshold(self):
    N = len(self.images)
    for i, k in enumerate(self.images):
      mask = self.images[k]['prediction'][0]['scores'] > self.threshold
      self.images[k]['prediction'][0]["boxes"] = self.images[k]['prediction'][0]["boxes"][mask]
      self.images[k]['prediction'][0]["labels"] = self.images[k]['prediction'][0]["labels"][mask]
      self.images[k]['prediction'][0]["scores"] = self.images[k]['prediction'][0]["scores"][mask] 
      print(f'Cut {i + 1} / {N} via threshold.', end = '\r')

  def _load_labels(self):
    # get the indices
    coco_url = 'http://images.cocodataset.org/annotations/annotations_trainval2017.zip'
    if not os.path.exists('annotations/instances_val2017.json'):
      os.system(f'wget {coco_url}')
      os.system('unzip /content/annotations_trainval2017.zip -d ./')
    annFile='annotations/instances_val2017.json'

    # get the object from the file
    coco=COCO(annFile)

    # iterate and mark the objects found
    N = len(self.images) 
    for i, k in enumerate(self.images):
      labels = coco.loadCats(self.images[k]['prediction'][0]["labels"].numpy())
      self.images[k]['objects'] = labels
      print(f'Objects separated for {i + 1} / {N} images.', end = '\r')




