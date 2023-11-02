from ursina import *
import subprocess
import os

app = Ursina()

# 배경 이미지 로드 (원하는 이미지 파일의 경로로 수정하세요)
background_texture = load_texture("mark0.jpg")

# 배경 스프라이트 생성
background = Sprite(texture=background_texture, scale=(1.3, 1.3), z=1)  # 16:9 화면 비율로 수정

# 플레이 버튼 생성
play_button = Button(
    text="Play",  # 버튼 텍스트
    scale=(0.2, 0.1),  # 버튼 크기
    color=color.gray,  # 버튼 배경색
    text_color=color.white,  # 버튼 텍스트 색상
    position=(0, -0.4)  # 버튼 위치 (가운데 아래쪽)
)

# 'Play' 버튼을 누를 때 실행되는 함수
def start_game():
    subprocess.Popen(["python", "mark.py"])  # mark.py를 새로운 프로세스로 실행
    os._exit(0)  # 현재 스크립트 종료

play_button.on_click = start_game  # 'Play' 버튼을 누르면 start_game 함수 실행

# 전체 화면 모드로 전환
window.fullscreen = True

# Escape 키를 사용하여 애플리케이션 종료
def input(key):
    if key == 'escape':
        application.quit()

app.run()

