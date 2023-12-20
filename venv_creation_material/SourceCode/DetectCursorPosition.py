#from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

#keyboard = KeyboardController()
mouse = MouseController()


# Move pointer relative to current position

while True:
    time.sleep(0.5)
    print('The current pointer position is {0}'.format(mouse.position))




# # 開始測量
# start = time.time()

# time.sleep(2)

# print('The current pointer position is {0}'.format(
#     mouse.position))

# # Set pointer position
# mouse.position = (10, 20)
# print('Now we have moved it to {0}'.format(
#     mouse.position))

# # Move pointer relative to current position
# mouse.move(5, -5)

# # Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)

# # Double click; this is different from pressing and releasing
# # twice on macOS
# mouse.click(Button.left, 2)

# # Scroll two steps down
# mouse.scroll(0, 2)

# keyboard.press('A')
# keyboard.release('A')
# with keyboard.pressed(Key.shift):
#     keyboard.press('a')
#     keyboard.release('a')

# # 結束測量
# end = time.time()
# # 輸出結果
# print("執行時間：%f 秒" % (end - start))
