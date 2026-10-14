# Lista de conferência — guia de 6 pontos

**Disciplina:** Computação Gráfica  
**Integrante:** Leucimar Tiago da Silva Carvalho  
**Atividades:** Mini Sistema Solar; Braço Robótico; Cubo com Satélite Texturizado.

## Atividade 1 — Transformações geométricas

Implementação: [atividade_sistema_solar.py](Aula_Transformacoes/alunos/atividade_sistema_solar.py).

| Requisito | Implementação / evidência |
|---|---|
| Usar somente make_translation, make_rotation_z e make_scale na solução | Os blocos de transformações utilizam somente esses três construtores; infraestrutura original preservada |
| Compor transformações por @ | Todas as composições dos três corpos usam @ |
| Sol girando no próprio centro | Rz(anguloSol) @ S(0.25); centro permanece na origem |
| Planeta orbitando com raio 0.6 | matrizOrbitaPlaneta = Rz(anguloOrbita) @ T(0.6,0,0) |
| Rotação própria com velocidade diferente | 3.0 rad/s para giro próprio; 0.8 rad/s iniciais para órbita |
| Lua orbitando o planeta com raio 0.2 | matrizOrbitaPlaneta @ Rz(anguloOrbitaLua) @ T(0.2,0,0) @ S(0.05) |
| ↑ aumenta e ↓ diminui a velocidade orbital | self.input.isKeyPressed; aceleração multiplicada por deltaTime |
| Velocidade orbital não negativa | max(0.0, ...) ao diminuir |
| Velocidades por segundo | Todos os incrementos angulares multiplicados por self.deltaTime |
| Captura pela tecla P | [capturas/resultado.png](Aula_Transformacoes/alunos/capturas/resultado.png), produzida pelo loop original com evento P |
| Resposta sobre R @ T e rotação própria | [README da atividade](Aula_Transformacoes/alunos/README.md#resposta-da-questão) |

## Atividade 2 — Grafo de cena

Implementação: [atividade_braco.py](Aula_GrafoCena/alunos/atividade_braco.py).

| Requisito | Implementação / evidência |
|---|---|
| Object3D no topo da base | Ombro é filho da base; posição local y=0.2, mundial y=0.4 |
| Braço laranja preso pela extremidade inferior | Caixa 0.3 × 1.2 × 0.3; filho do ombro; centro local y=0.6 |
| Cotovelo na extremidade do braço | Object3D filho do ombro; posição local y=1.2 |
| Antebraço azul conectado ao cotovelo | Caixa 0.25 × 1.0 × 0.25; filho do cotovelo; centro local y=0.5 |
| Garra cinza na extremidade | Caixa 0.5 × 0.15 × 0.5; filho do cotovelo; centro local y=1.0 |
| A/D: rotação da base e do conjunto em Y | self.base.rotateY(±angulo) |
| W/S: rotação do ombro em Z | self.ombro.rotateZ(±angulo) |
| I/K: rotação do cotovelo em Z | self.cotovelo.rotateZ(±angulo) |
| Movimentação por segundo | angulo = 1.5 × self.deltaTime |
| Captura pela tecla P, com braço dobrado | [capturas/resultado.png](Aula_GrafoCena/alunos/capturas/resultado.png), produzida pelo loop original com evento P |
| Resposta sobre a necessidade de pivôs | [README da atividade](Aula_GrafoCena/alunos/README.md#resposta-da-questão) |

## Atividade 3 — Texturas

Implementação: [atividade_cubo.py](Aula_Texturas/alunos/atividade_cubo.py).

| Requisito | Implementação / evidência |
|---|---|
| Cubo principal usa mosaico.png | TEXTURA='mosaico.png'; imagem original incluída em images/ |
| Satélite usa grade_uv.png | Texture(IMAGENS/'grade_uv.png'); imagem original incluída |
| repeatUV = [2,2] | Propriedade de TextureMaterial do satélite |
| Satélite é filho do cubo principal | self.mesh.add(self.satelite) |
| Distância de 1.3 do centro | setPosition([1.3,0,0]) antes de scale(0.4) |
| Escala 0.4 | self.satelite.scale(0.4) |
| Acompanha a órbita do pai | Matriz mundial herda a matriz do cubo principal |
| ↑/↓ alteram a velocidade de rotação | self.isKeyPressed; aceleração × deltaTime; mínimo 0 |
| Rotação própria em X a 2 rad/s | self.satelite.rotateX(2.0*self.deltaTime) |
| Texturas sem inversão vertical | Carregamento original preservado, com inversão das linhas para UV |
| Captura pela tecla S | [capturas/resultado.png](Aula_Texturas/alunos/capturas/resultado.png), produzida pelo loop original com evento S |
| Resposta sobre UV e repetição | [README da atividade](Aula_Texturas/alunos/README.md#resposta-da-questão) |

## Organização, execução e entrega

- [x] Os três arquivos de atividade foram preenchidos.
- [x] Somente os trechos indicados nos arquivos de atividade foram modificados.
- [x] Módulos auxiliares, demonstrações, shaders e texturas originais preservados.
- [x] Dependências e instruções de ambiente incluídas.
- [x] Demonstrações executadas e verificadas.
- [x] Cada atividade possui README, captura e resposta conceitual.
- [x] Nome completo do integrante real incluído nos quatro READMEs da entrega.
- [x] Entrega identificada como individual, conforme solicitado pelo aluno; não há segundo integrante fictício.
- [x] Testes com OpenGL real, controles e propriedades geométricas: [VALIDACAO.md](VALIDACAO.md).
- [x] Publicação dos arquivos na main e confirmação da entrega completa. Repositório público: https://github.com/leucimar/ComputacaoGrafica_TrabalhoEtapa2.
- [ ] Envio do link ao Blackboard pelo aluno.

O guia exige dupla. A realização individual é a modalidade informada pelo aluno e deve ser aceita pelo professor; este pacote não afirma que essa exceção já foi autorizada.
