import easyocr
import cv2

# 初始化 OCR 阅读器
reader = easyocr.Reader(['ch_tra', 'en'], gpu=True)

# 图像路径和输出路径
image_path = r"C:\Users\syf\Desktop\TEXT\CW61127622.jpg"
temp_path = r"C:\Users\syf\Desktop\TEXT\temp_cropped_image.jpg"

# 读取图像
img = cv2.imread(image_path)

# 裁剪区域
x, y, x2, y2 = 65, 350, 530, 430  # 统编
cropped_img = img[y:y2, x:x2]

# 对比度和亮度调整
alpha = 1.5
beta = 0.2
enhanced_img = cv2.convertScaleAbs(cropped_img, alpha=alpha, beta=beta)

# 转换为灰度图像
gray_img = cv2.cvtColor(enhanced_img, cv2.COLOR_BGR2GRAY)

# 应用高斯模糊以去噪
blurred_img = cv2.GaussianBlur(gray_img, (9, 9), 1)

# 形态学操作
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
dilated_img = cv2.dilate(blurred_img, kernel, iterations=2)         #文字膨脹
eroded_img = cv2.erode(blurred_img, kernel, iterations=1)           #文字腐蝕 erosion 減少噪點

# 边缘检测（可选）
edges = cv2.Canny(eroded_img, 100, 200)

# 保存处理后的图像
cv2.imwrite(temp_path, edges)

# 使用 OCR 识别文本
results = reader.readtext(edges)

# 打印识别结果
for result in results:
    print(f'Text: {result[1]}')
    print(f'Position: {result[0]}')
    print(f'Confidence: {result[2]}')
    print('-' * 40)
