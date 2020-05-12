import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

## Prepare model
proto = './models/colorization_deploy_v2.prototxt'
weights = './models/colorization_release_v2.caffemodel'
# colorization_release_v2_norebal.caffemodel은 클래스 재조정 기간없이 분류 손실로 훈련됨
# 결과는 더 흐리지 만 더 "안전한" 채색
# weights = './models/colorization_release_v2_norebal.caffemodel' 

# load cluster centers
pts_in_hull = np.load('./models/pts_in_hull.npy')
pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1).astype(np.float32)

# load model
net = cv2.dnn.readNetFromCaffe(proto, weights)
# net.getLayerNames()

# populate cluster centers as 1x1 convolution kernel
# 클러스터 센터를 1x1 컨볼루션 커널로 채우기
net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull]
# 스케일 레이어가 OpenCV dnn 모듈에서 작동하지 않는 듯.. conv8_313_rh 레이어에 2.606을 수동으로 채워야 함
net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full((1, 313), 2.606, np.float32)]

img_path = './img/parasite_01.jpg'
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
img_input = img.copy()

# convert BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

img_rgb = img.copy()

# 입력 표준화
img_rgb = (img_rgb / 255.).astype(np.float32)

# convert RGB to LAB
img_lab = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2Lab)
# L 채널 만 사용
img_l = img_lab[:, :, 0]

input_img = cv2.resize(img_l, (224, 224))
input_img -= 50 # 평균 센터링의 경우 50 빼기

# 플롯 이미지
# fig = plt.figure(figsize=(10, 5))
# fig.add_subplot(1, 2, 1)
# plt.imshow(img_rgb)
# fig.add_subplot(1, 2, 2)
plt.axis('off')
plt.imshow(input_img, cmap='gray')

net.setInput(cv2.dnn.blobFromImage(input_img))
pred = net.forward()[0,:,:,:].transpose((1, 2, 0))

# 원래 이미지 모양으로 크기 조정
pred_resize = cv2.resize(pred, (img.shape[1], img.shape[0]))

# 원본 이미지 L과 연결
pred_lab = np.concatenate([img_l[:, :, np.newaxis], pred_resize], axis=2)

# convert LAB to RGB
pred_rgb = cv2.cvtColor(pred_lab, cv2.COLOR_Lab2RGB)
pred_rgb = np.clip(pred_rgb, 0, 1) * 255
pred_rgb = pred_rgb.astype(np.uint8)

# 플롯 예측 결과
fig = plt.figure(figsize=(20, 10))
fig.add_subplot(1, 2, 1).axis('off')
plt.imshow(img_l, cmap='gray')
fig.add_subplot(1, 2, 2).axis('off')
plt.imshow(pred_rgb)
# plt.savefig(output_filename)

# 결과 이미지 파일 저장
filename, ext = os.path.splitext(img_path)
input_filename = '%s_input%s' % (filename, ext)
output_filename = '%s_output%s' % (filename, ext)

pred_rgb_output = cv2.cvtColor(pred_rgb, cv2.COLOR_RGB2BGR)

cv2.imwrite(input_filename, img_input)
cv2.imwrite(output_filename, np.concatenate([img, pred_rgb_output], axis=1))