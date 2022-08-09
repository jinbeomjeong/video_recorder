import cv2
import os
import os.path as osp
from tqdm import tqdm

l_img_path = osp.join('d:'+os.sep, 'dataset', 'data_scene_flow_multiview', 'testing', 'image_2')
l_img_list = os.listdir(l_img_path)
l_img_list.sort()
l_img = cv2.imread(l_img_path + os.sep + l_img_list[0])

fps = 10
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer = cv2.VideoWriter('.' + os.sep + 'l_img_video.mp4', fourcc, fps, (l_img.shape[1], l_img.shape[0]))

for l_img_name in tqdm(l_img_list, ncols=100, desc='writing video'):
    frame = cv2.imread(l_img_path + os.sep + l_img_name)
    writer.write(frame)
