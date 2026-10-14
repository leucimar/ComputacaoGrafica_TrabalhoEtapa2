# Arquivo inicial da atividade. Leia ATIVIDADE.md e altere os trechos marcados com TODO.
from pathlib import Path
import argparse
from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from core.texture import Texture
from material.textureMaterial import TextureMaterial

from geometry.boxGeometry import BoxGeometry
IMAGENS=Path(__file__).resolve().parent/'images'
TEXTURA='mosaico.png'  # 1: textura do cubo principal
VELOCIDADE=0.8  # radianos por segundo
class Cubo(Base):
    def initialize(self):
        self.renderer=Renderer();self.scene=Scene()
        self.camera=Camera(aspectRatio=960/640)
        self.camera.setPosition([0,0,3.2])
        self.velocidade=VELOCIDADE
        # cubo principal
        textura=Texture(IMAGENS/TEXTURA)
        self.mesh=Mesh(BoxGeometry(),TextureMaterial(textura))
        self.mesh.rotateX(0.35);self.mesh.rotateY(0.5)
        self.scene.add(self.mesh)
        # 2: grade UV repetida duas vezes em cada direção de cada face.
        texturaSatelite=Texture(IMAGENS/'grade_uv.png')
        self.satelite=Mesh(BoxGeometry(),TextureMaterial(texturaSatelite,{'repeatUV':[2,2]}))
        # 3: T @ S preserva a distância 1.3; o pai fornece a órbita.
        self.satelite.setPosition([1.3,0,0])
        self.satelite.scale(0.4)
        self.mesh.add(self.satelite)
    def update(self):
        # 4: aceleração por segundo; velocidade mínima igual a zero.
        if self.isKeyPressed('up'):
            self.velocidade+=1.0*self.deltaTime
        if self.isKeyPressed('down'):
            self.velocidade=max(0.0,self.velocidade-1.0*self.deltaTime)
        self.mesh.rotateY(self.velocidade*self.deltaTime)
        # 5: rotação local à direita de T @ S, sem deslocar o centro.
        self.satelite.rotateX(2.0*self.deltaTime)
        self.renderer.render(self.scene,self.camera)
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--frames',type=int);parser.add_argument('--screenshot')
    args=parser.parse_args();Cubo().run(args.frames,args.screenshot)
