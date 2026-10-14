# Computação Gráfica — Trabalho Etapa 2

**Disciplina:** Computação Gráfica  
**Atividade:** Mini Sistema Solar; Braço Robótico; Cubo com Satélite Texturizado  
**Integrante:** Leucimar Tiago da Silva Carvalho  
**Modalidade:** individual, conforme informado pelo aluno.  
**Guia principal:** [Atividade Prática — 6 pontos](GUIA_PRINCIPAL.txt).

## Descrição

Implementação das três atividades em Python, Pygame e OpenGL, preservando os projetos da disciplina e preenchendo apenas os trechos indicados nos arquivos de atividade. Cada pasta inclui o programa, dependências, demonstrações, captura real do resultado e resposta conceitual.

| Atividade | Implementação | Captura (tecla) | Instruções e resposta |
|---|---|---|---|
| Mini Sistema Solar | [atividade_sistema_solar.py](Aula_Transformacoes/alunos/atividade_sistema_solar.py) | [P](Aula_Transformacoes/alunos/capturas/resultado.png) | [README](Aula_Transformacoes/alunos/README.md) |
| Braço Robótico | [atividade_braco.py](Aula_GrafoCena/alunos/atividade_braco.py) | [P](Aula_GrafoCena/alunos/capturas/resultado.png) | [README](Aula_GrafoCena/alunos/README.md) |
| Cubo com Satélite Texturizado | [atividade_cubo.py](Aula_Texturas/alunos/atividade_cubo.py) | [S](Aula_Texturas/alunos/capturas/resultado.png) | [README](Aula_Texturas/alunos/README.md) |

## Preparar e executar no Windows

No terminal, a partir da raiz do repositório:

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
Set-Location Aula_Transformacoes/alunos
../../.venv/Scripts/python.exe demo1_matrizes.py
../../.venv/Scripts/python.exe demo2_transformacoes.py
../../.venv/Scripts/python.exe demo3_global_local.py
../../.venv/Scripts/python.exe atividade_sistema_solar.py
Set-Location ../../Aula_GrafoCena/alunos
../../.venv/Scripts/python.exe demo1_cena.py
../../.venv/Scripts/python.exe demo2_hierarquia.py
../../.venv/Scripts/python.exe demo3_camera.py
../../.venv/Scripts/python.exe atividade_braco.py
Set-Location ../../Aula_Texturas/alunos
../../.venv/Scripts/python.exe exemplo_retangulo.py
../../.venv/Scripts/python.exe exemplo_cubo.py
../../.venv/Scripts/python.exe atividade_cubo.py
Set-Location ../..
```

Feche cada janela com ESC para continuar. Execute os programas a partir da pasta `alunos` correspondente para resolver os imports e salvar as capturas no local correto. No PyCharm, abra cada pasta `alunos` como projeto. As instruções independentes de Windows e macOS/Linux estão nos READMEs das atividades.

**Ambiente:** Python 3.11–3.13, Pygame 2.6.1, PyOpenGL 3.1.10 e NumPy 1.26 ou 2.x. É necessário driver com suporte a OpenGL 3.3 core. Use as versões de [requirements.txt](requirements.txt).

## Respostas das questões

### 1. Mini Sistema Solar — por que R @ T e rotação própria à direita?

Em uma composição de matrizes, a transformação mais à direita atua primeiro. Em `R @ T`, a translação posiciona o centro do planeta a 0,6 da origem e a rotação gira esse deslocamento em torno do Sol, produzindo a órbita. A rotação própria deve ficar à direita de `T`, em `R_orbita @ T @ R_propria @ S`, para girar os vértices em torno da origem local do planeta antes de posicioná-lo na órbita. Assim ela não altera o centro nem o raio da órbita. A escala fica à direita para alterar apenas o tamanho. A Lua reutiliza `R_orbita @ T` do planeta, acrescentando sua rotação orbital, translação de 0,2 e escala, sem herdar a escala ou a rotação própria do planeta.

### 2. Braço Robótico — por que utilizar pivôs?

As caixas são centradas na origem local. Girá-las diretamente faria o braço e o antebraço girarem em torno dos próprios centros, deslocando as pontas e rompendo a conexão entre as peças. Os pivôs `Object3D` estabelecem a origem da rotação exatamente nas articulações: o ombro no topo da base e o cotovelo na extremidade superior do braço. Cada caixa é deslocada por metade da sua altura, deixando a ponta inferior no pivô. Pela hierarquia, a matriz mundial de um filho é a matriz mundial do pai multiplicada pela matriz local: girar a base leva todo o conjunto; girar o ombro leva cotovelo, antebraço e garra; girar o cotovelo leva antebraço e garra.

### 3. Cubo Texturizado — UV e repeatUV = [2,2]

As coordenadas UV associam cada ponto da superfície a uma posição bidimensional da imagem: U corresponde à direção horizontal e V à vertical. O rasterizador interpola essas coordenadas nos triângulos para consultar a textura. Com `repeatUV = [2,2]`, o shader multiplica as coordenadas por 2 nas duas direções. Como a textura usa `GL_REPEAT`, cada face passa a exibir duas repetições horizontais e duas verticais da imagem, totalizando quatro cópias, sem mudar a geometria. O carregamento original inverte as linhas da imagem para compatibilizar sua origem superior com a origem inferior das coordenadas UV.

**Repositório público:** https://github.com/leucimar/ComputacaoGrafica_TrabalhoEtapa2  
**Branch de entrega:** `main`.

## Verificação e entrega

Veja [CHECKLIST.md](CHECKLIST.md) para a correspondência de cada requisito com a implementação e [VALIDACAO.md](VALIDACAO.md) para os testes executados e a origem das capturas.

A entrega no Blackboard consiste em enviar o link deste repositório. Essa etapa deve ser realizada pelo aluno em sua conta. O guia descreve trabalho em dupla; esta entrega identifica somente o integrante real, por ter sido solicitada como individual. Confirme com o professor a aceitação dessa modalidade.

## Origem dos arquivos

Material-base: [rodrygofesantos/pygame](https://github.com/rodrygofesantos/pygame), professor Rodrigo Fernandes dos Santos, revisão `bcc4079703c5947556563c4f2a558064e12b7242`. As bibliotecas auxiliares e exemplos foram mantidos sem modificações. Os READMEs da entrega são novos; os READMEs originais das aulas foram preservados como `README_AULA_ORIGINAL.md`. O guia anexo de 6 pontos é a referência principal quando houver divergência de pontuação nos enunciados gerais.
