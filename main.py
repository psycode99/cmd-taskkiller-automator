import pyautogui
import time

# uncomment to find x and y coordinates of your terminal
# while True:
#     print(pyautogui.position())
#     time.sleep(5)


task_list = ['wordpad', 'notepad', 'StikyNot', 'bash', 'Hyper']  # list of tasks to kill
width, height = pyautogui.size()


def task_killer(tasks):
    pyautogui.click(100, 100)  # x and y coordinates of your terminal
    pyautogui.typewrite('tasklist')
    pyautogui.press('enter')

    for task in tasks:
        pyautogui.typewrite(f'taskkill /F /IM {task}.exe /T')
        pyautogui.press('enter')
        time.sleep(1)
    pyautogui.typewrite('exit')
    pyautogui.press('enter')


timer = [5, 4, 3, 2, 1, 0]
for x in range(1):
    print(f'Open your terminal in...')
    for t in timer:
        print(t)
        time.sleep(1)
task_killer(task_list)
