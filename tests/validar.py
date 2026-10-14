"""Testes de integração com contexto OpenGL real, sem alterar os módulos da aula.

Da raiz: python tests/validar.py
Linux sem monitor: SDL_VIDEODRIVER=offscreen PYOPENGL_PLATFORM=egl
LIBGL_ALWAYS_SOFTWARE=1 SDL_AUDIODRIVER=dummy python tests/validar.py

--capturar também aciona as teclas P/S no loop original e atualiza as imagens.
"""
from pathlib import Path
import argparse
import importlib
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ATIVIDADES = {
    'solar': ('Aula_Transformacoes', 'atividade_sistema_solar', 'SistemaSolar', 'p'),
    'braco': ('Aula_GrafoCena', 'atividade_braco', 'Braco', 'p'),
    'cubo': ('Aula_Texturas', 'atividade_cubo', 'Cubo', 's'),
}


def testar(nome, capturar):
    import numpy as np
    import pygame
    from OpenGL.GL import glGetError, GL_NO_ERROR, glGetString, GL_RENDERER, GL_VERSION

    aula, modulo, classe, tecla = ATIVIDADES[nome]
    pasta = ROOT / aula / 'alunos'
    os.chdir(pasta)
    sys.path.insert(0, str(pasta))
    atividade = importlib.import_module(modulo)
    app = getattr(atividade, classe)()
    app.initialize()
    print('OpenGL:', glGetString(GL_VERSION).decode(), '/', glGetString(GL_RENDERER).decode())
    passos = 0

    def igual(real, esperado):
        nonlocal passos
        np.testing.assert_allclose(real, esperado, atol=1e-6)
        passos += 1

    teclas = set()
    if nome == 'solar':
        app.input.isKeyPressed = lambda tecla: tecla in teclas
        matrizes = []
        upload = app.modelMatrix.uploadData

        def registrar():
            matrizes.append(np.array(app.modelMatrix.data, copy=True))
            upload()

        app.modelMatrix.uploadData = registrar
        app.deltaTime = 0.25
        app.update()
        sol, planeta, lua = matrizes[-3:]
        origem = np.array([0, 0, 0, 1])
        pos_planeta, pos_lua = planeta @ origem, lua @ origem
        igual(sol @ origem, origem)
        igual(np.linalg.norm(pos_planeta[:3]), 0.6)
        igual(np.linalg.norm(pos_lua[:3] - pos_planeta[:3]), 0.2)
        igual([app.anguloSol, app.anguloOrbita, app.anguloRotacaoPlaneta,
               app.anguloOrbitaLua], [0.075, 0.2, 0.75, 0.625])
        M = atividade.Matrix
        orbita = M.make_rotation_z(0.2) @ M.make_translation(0.6, 0, 0)
        igual(sol, M.make_rotation_z(0.075) @ M.make_scale(0.25))
        igual(planeta, orbita @ M.make_rotation_z(0.75) @ M.make_scale(0.1))
        igual(lua, orbita @ M.make_rotation_z(0.625)
              @ M.make_translation(0.2, 0, 0) @ M.make_scale(0.05))
        teclas.add('down')
        app.deltaTime = 2.0
        app.update()
        igual(app.velocidadeOrbita, 0)
        app.update()
        igual(app.velocidadeOrbita, 0)
        teclas.clear()
        teclas.add('up')
        app.deltaTime = 0.4
        app.update()
        igual(app.velocidadeOrbita, 0.4)
        # Mesma duração, diferentes tamanhos de passo: os ângulos coincidem.
        teclas.clear()
        for dt, quantidade in [(1.0, 1), (0.1, 10)]:
            app.anguloSol = app.anguloOrbita = app.anguloRotacaoPlaneta = app.anguloOrbitaLua = 0
            app.deltaTime = dt
            for _ in range(quantidade):
                app.update()
            igual([app.anguloSol, app.anguloOrbita, app.anguloRotacaoPlaneta,
                   app.anguloOrbitaLua], [0.3, 0.4, 3.0, 2.5])
        # Pose de captura; continua a mesma animação e o mesmo renderizador.
        app.velocidadeOrbita = 0.8
        app.anguloSol, app.anguloOrbita = 0.45, 1.2
        app.anguloRotacaoPlaneta, app.anguloOrbitaLua = 4.5, 3.75
    elif nome == 'braco':
        app.isKeyPressed = lambda tecla: tecla in teclas
        assert app.ombro.parent is app.base
        assert app.braco.parent is app.ombro
        assert app.cotovelo.parent is app.ombro
        assert app.antebraco.parent is app.cotovelo
        assert app.garra.parent is app.cotovelo
        passos += 5
        igual(app.ombro.getWorldPosition(), [0, 0.4, 0])
        igual(app.cotovelo.getWorldPosition(), [0, 1.6, 0])
        igual(app.garra.getWorldPosition(), [0, 2.6, 0])
        M = importlib.import_module('core.matrix').Matrix
        for positiva, negativa, no, rotacao in [
            ('a', 'd', app.base, M.makeRotationY),
            ('w', 's', app.ombro, M.makeRotationZ),
            ('i', 'k', app.cotovelo, M.makeRotationZ),
        ]:
            original = no.transform.copy()
            teclas.add(positiva)
            app.deltaTime = 0.1
            app.update()
            igual(no.transform, original @ rotacao(0.15))
            teclas.clear()
            teclas.add(negativa)
            app.update()
            igual(no.transform, original)
            teclas.clear()
        # Braço dobrado: usa os mesmos controles que o aluno utiliza.
        for tecla_pose, dt in [('a', 0.2), ('s', 0.43), ('i', 0.75)]:
            teclas.add(tecla_pose)
            app.deltaTime = dt
            app.update()
            teclas.clear()
        # Pontas coincidem com os pivôs mesmo após as rotações.
        igual((app.braco.getWorldMatrix() @ [0, -0.6, 0, 1])[:3], app.ombro.getWorldPosition())
        igual((app.braco.getWorldMatrix() @ [0, 0.6, 0, 1])[:3], app.cotovelo.getWorldPosition())
        igual((app.antebraco.getWorldMatrix() @ [0, -0.5, 0, 1])[:3], app.cotovelo.getWorldPosition())
        igual((app.antebraco.getWorldMatrix() @ [0, 0.5, 0, 1])[:3], app.garra.getWorldPosition())
    else:
        app.isKeyPressed = lambda tecla: tecla in teclas
        assert atividade.TEXTURA == 'mosaico.png'
        assert app.satelite.parent is app.mesh
        passos += 2
        igual(app.satelite.getPosition(), [1.3, 0, 0])
        igual(np.linalg.norm(app.satelite.transform[:3, :3], axis=0), [0.4, 0.4, 0.4])
        igual(app.satelite.material.uniforms['repeatUV'].data, [2, 2])
        igual(app.mesh.material.uniforms['repeatUV'].data, [1, 1])
        from core.matrix import Matrix as M
        original = app.satelite.transform.copy()
        pai = app.mesh.transform.copy()
        app.deltaTime = 0.25
        app.update()
        igual(app.satelite.transform, original @ M.makeRotationX(0.5))
        igual(app.mesh.transform, pai @ M.makeRotationY(0.2))
        igual(np.linalg.norm(np.array(app.satelite.getWorldPosition())
                             - np.array(app.mesh.getWorldPosition())), 1.3)
        igual(app.satelite.getPosition(), [1.3, 0, 0])
        teclas.add('down')
        app.deltaTime = 2.0
        app.update()
        igual(app.velocidade, 0)
        app.update()
        igual(app.velocidade, 0)
        teclas.clear()
        teclas.add('up')
        app.deltaTime = 0.4
        app.update()
        igual(app.velocidade, 0.4)
        teclas.clear()
        # Pai na orientação inicial e satélite ligeiramente girado para mostrar UV.
        app.mesh.transform = pai
        app.mesh.rotateY(5.4)
        app.satelite.transform = original @ M.makeRotationX(0.35)
        app.velocidade = 0.8

    igual(glGetError(), GL_NO_ERROR)
    if capturar:
        # O loop original inicializaria novamente: reutiliza a cena já testada.
        # O programa da entrega e Base permanecem sem alterações.
        app.initialize = lambda: None
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.key.key_code(tecla)))
        app.run(frames=1)
        imagem = pasta / 'capturas/resultado.png'
        assert imagem.is_file()
        surface = pygame.image.load(str(imagem))
        igual(surface.get_size(), app.screenSize)
        # A captura deve conter geometria e cores, não apenas um fundo vazio.
        rgb = pygame.surfarray.array3d(surface)
        assert np.unique(rgb.reshape(-1, 3), axis=0).shape[0] >= 7
        passos += 1
    else:
        pygame.quit()
    print(f'PASS {nome}: {passos} verificações; captura={capturar}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--atividade', choices=ATIVIDADES)
    parser.add_argument('--capturar', action='store_true')
    args = parser.parse_args()
    if args.atividade:
        testar(args.atividade, args.capturar)
    else:
        for nome in ATIVIDADES:
            comando = [sys.executable, str(Path(__file__).resolve()), '--atividade', nome]
            if args.capturar:
                comando.append('--capturar')
            subprocess.run(comando, check=True)
        print('PASS: todas as atividades validadas.')


if __name__ == '__main__':
    main()
