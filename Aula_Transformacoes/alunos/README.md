# Mini Sistema Solar

**Disciplina:** Computação Gráfica  
**Atividade:** Mini Sistema Solar  
**Integrante:** Leucimar Tiago da Silva Carvalho  
**Modalidade:** entrega individual, conforme informado pelo aluno.

## Descrição

O Sol gira no centro; o planeta orbita a 0,6 e possui giro próprio de 3 rad/s, diferente da órbita inicial de 0,8 rad/s. A Lua acompanha o planeta em uma órbita de raio 0,2. Todas as matrizes da solução usam somente make_translation, make_rotation_z e make_scale, combinadas por @.

A estrutura do professor foi preservada. Apenas os trechos indicados para preenchimento no arquivo `atividade_sistema_solar.py` foram alterados. Os módulos auxiliares, demonstrações, shaders e imagens são os originais da disciplina.

## Execução

Abra esta pasta `alunos` como projeto no PyCharm ou como diretório do terminal. Python 3.11 a 3.13; placa/driver com OpenGL 3.3 core.

### Windows (PowerShell)

```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe demo1_matrizes.py
.venv\Scripts\python.exe demo2_transformacoes.py
.venv\Scripts\python.exe demo3_global_local.py
.venv\Scripts\python.exe atividade_sistema_solar.py
```

Feche cada demonstração com ESC para executar a próxima.

### macOS/Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python demo1_matrizes.py
.venv/bin/python demo2_transformacoes.py
.venv/bin/python demo3_global_local.py
.venv/bin/python atividade_sistema_solar.py
```

## Controles e captura

↑ aumenta e ↓ diminui a velocidade orbital em 1 rad/s por segundo; mínimo 0. ESC fecha.

Pressione **P** durante a execução para salvar `capturas/resultado.png`. A imagem abaixo foi produzida pela execução da solução. 

![Resultado da atividade](capturas/resultado.png)

## Resposta da questão

Em uma composição de matrizes, a transformação mais à direita atua primeiro. Em `R @ T`, a translação posiciona o centro do planeta a 0,6 da origem e a rotação gira esse deslocamento em torno do Sol, produzindo a órbita. A rotação própria deve ficar à direita de `T`, em `R_orbita @ T @ R_propria @ S`, para girar os vértices em torno da origem local do planeta antes de posicioná-lo na órbita. Assim ela não altera o centro nem o raio da órbita. A escala fica à direita para alterar apenas o tamanho. A Lua reutiliza `R_orbita @ T` do planeta, acrescentando sua rotação orbital, translação de 0,2 e escala, sem herdar a escala ou a rotação própria do planeta.

## Material de referência

- [Enunciado original](ATIVIDADE.md)
- [Orientações originais da aula](README_AULA_ORIGINAL.md)
- [Guia principal de avaliação — 6 pontos](../../GUIA_PRINCIPAL.txt)
