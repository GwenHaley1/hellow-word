import cv2

# 尝试打开默认摄像头
cap = cv2.VideoCapture(0)

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

# 循环不断地从摄像头捕获帧并显示
while True:
    # 读取一帧。ret是一个布尔值，表示是否成功。frame是捕获到的帧。
    ret, frame = cap.read()

    # 如果帧读取成功，显示它。
    if ret:
        cv2.imshow('Camera Feed', frame)

        # 按'q'键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("无法读取帧")
        break

# 释放摄像头并关闭所有OpenCV窗口
cap.release()
cv2.destroyAllWindows()
