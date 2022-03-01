"""
오토 클릭 매크로.
==============
마우스의 뷰 포트 위치를 추출하여 해당 위치에서 지정 횟수만큼 클릭을 반복한다.
클릭 외 마우스 이동, 우클릭, 인터벌 클릭, 더블 클릭, 드래그, 키보드 입력이 가능하다.

Document: https://pyautogui.readthedocs.io/
"""

import pyautogui
import keyboard
import time

click_count = int(input("몇 번 클릭?(숫자 입력 후 엔터): "))
print("클릭할 위치에 마우스를 올리고 엔터키를 누르세요. (나가려면 Ctrl + c)")


def mouse_position() -> pyautogui.Point:
    position: pyautogui.Point = pyautogui.position()

    if keyboard.is_pressed('enter'):
        print(position.x, position.y)

    return position


def limited_click(position: pyautogui.Point, count: int = 10) -> None:
    for i in range(1, count+1):
        pyautogui.click(x=position.x, y=position.y)
        time.sleep(3.0)

        print(f"남은 클릭 수 {(count + 1) - i}회 (마치려면 esc 키를 3초 이상 누르세요.)")
        if keyboard.is_pressed('esc'):
            break

    return None


mouse_position = mouse_position()
limited_click(mouse_position, click_count)
