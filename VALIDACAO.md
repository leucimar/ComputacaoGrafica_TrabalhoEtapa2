# Validação da entrega

**Data:** 14/10/2026.  
**Ambiente testado:** Linux, Python 3.12.14, Pygame 2.6.1, PyOpenGL 3.1.10, NumPy 2.3.5.  
**Renderização:** OpenGL 4.5 Core, Mesa 25.2.8, llvmpipe (LLVM 20.1.2). Foi utilizado um contexto EGL sem monitor, com renderização real do código OpenGL. As imagens não foram desenhadas ou geradas artificialmente.

## Resultados

| Teste | Resultado |
|---|---|
| Sistema solar: centro do Sol, raios 0.6/0.2, composição de matrizes, giro próprio, setas, limite zero e dependência do tempo | 15 verificações aprovadas, incluindo captura |
| Braço: parentesco dos nós, posição dos pivôs, seis controles, sentidos inversos e coincidência das quatro extremidades após dobrar | 21 verificações aprovadas, incluindo captura |
| Cubos: nome da textura principal, hierarquia, repeatUV, distância 1.3, escala 0.4, giro do pai, giro local X de 2 rad/s e setas | 16 verificações aprovadas, incluindo captura |
| Erros OpenGL | GL_NO_ERROR nas três atividades |
| Entradas originais dos três programas | Execução de 6 quadros de cada uma, sem erro |
| Demonstrações de Transformações | demo1_matrizes, demo2_transformacoes e demo3_global_local executadas, sem erro |
| Demonstrações de Grafo de Cena | demo1_cena, demo2_hierarquia e demo3_camera executadas, sem erro |
| Demonstrações de Texturas | exemplo_retangulo e exemplo_cubo executadas, sem erro |
| Preservação da infraestrutura | 74 arquivos originais auxiliares comparados byte a byte, sem diferenças |

Total: **52 verificações de integração aprovadas** e **11 programas executados** (8 demonstrações + 3 atividades).

## Como reproduzir os testes

Com o ambiente preparado, a partir da raiz do repositório:

```powershell
.venv\Scripts\python.exe tests/validar.py
```

Os testes abrem um contexto gráfico real para cada atividade e utilizam estados de teclas controlados para verificar numericamente os movimentos. Não alteram os arquivos da implementação ou da infraestrutura. O modo padrão não sobrescreve as capturas.

Em Linux sem monitor, com driver Mesa e suporte EGL:

```bash
SDL_VIDEODRIVER=offscreen PYOPENGL_PLATFORM=egl LIBGL_ALWAYS_SOFTWARE=1 SDL_AUDIODRIVER=dummy .venv/bin/python tests/validar.py
```

## Origem das capturas

`tests/validar.py --capturar` utiliza a cena real das atividades e o método original `Base.run`. Ao final dos testes, prepara uma pose visível e posta um evento de tecla P (solar/braço) ou S (cubos), acionando a captura que já existe no código do professor. O framebuffer OpenGL é salvo como PNG. O braço é dobrado pelos mesmos métodos de rotação usados pelos controles. Na imagem de texturas, o pai está em uma orientação que permite visualizar o satélite por inteiro; a rotação própria do satélite permanece local.

As capturas ficam em `Aula_*/alunos/capturas/resultado.png`: 640 × 640 para o sistema solar e 960 × 640 para as outras atividades. Foram inspecionadas visualmente. A repetição 2 × 2 pode ser verificada nas faces do satélite; os arquivos `mosaico.png` e `grade_uv.png` são exatamente os do professor, mesmo que ambos apresentem padrões de grade com letras.

Para atualizar as capturas automaticamente, acrescente `--capturar` ao comando de testes. Para capturar manualmente, execute o programa da atividade dentro de sua pasta `alunos` e pressione a tecla correspondente; no braço, dobre as articulações antes de pressionar P.

## Limites da verificação

A execução foi validada em Linux com renderização por software. Os comandos para Windows estão documentados, mas não foram executados em uma máquina Windows nesta sessão. O computador do aluno precisa oferecer OpenGL 3.3 core. A publicação no GitHub e o envio ao Blackboard são etapas separadas da validação técnica.
