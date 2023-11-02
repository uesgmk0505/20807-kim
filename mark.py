from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

window.fullscreen = True
window.borderless = True

# Define a Voxel class.
class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture='grass',
            color=color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )

for z in range(30):
    for x in range(30):
        voxel = Voxel(position=(x, 0, z))

def input(key):
    if key == 'right mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)
    if key == 'left mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)
    
    if key == 'escape':
        app.quit()

hand = Entity(
    parent=camera.ui,
    model='cube',  # 기본 큐브 모델 사용
    texture='grass',  # 텍스처를 'block'으로 설정하거나 원하는 텍스처로 변경할 수 있습니다.
    scale=0.4,
    rotation=Vec3(-10, -10, 10),
    position=Vec2(0.5, -0.5)
)

# Light and Sky 설정
DirectionalLight()
AmbientLight(color=(0.5, 0.5, 0.5))
Sky()

player = FirstPersonController(position=(random.randint(0, 29), 1, random.randint(0, 29)))


def update():  # 매 프레임마다 실행
    if player.y < -50:  # 플레이어의 y 좌표가 -50 이하인 경우
        player.position = (random.randint(0, 29), 1, random.randint(0, 29))  # 플레이어 위치를 리셋

    # 왼쪽 또는 오른쪽 마우스 버튼을 누를 때 hand 엔티티의 위치 변경
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.position = Vec2(0.4, -0.5)
    else:
        hand.position = Vec2(0.6, -0.6)

app.run()
