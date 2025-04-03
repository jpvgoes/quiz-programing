# Quiz de Programação

Este é um projeto de um quiz interativo desenvolvido com Flask, HTML, CSS e JavaScript. O objetivo do quiz é ensinar conceitos básicos de programação de forma divertida e interativa.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **`templates/`**: Contém os arquivos HTML que definem as páginas do quiz.
  - `index.html`: Página inicial do projeto.
  - `fases.html`: Página de seleção de fases.
  - `fase1.html`, `fase2.html`, `fase3.html`: Páginas das fases do quiz.
  - `result.html`: Página de resultado final.

- **`static/`**: Contém os arquivos estáticos, como imagens e estilos CSS.
  - Arquivos CSS para cada fase (`styles-fase1.css`, `styles-fase2.css`, `styles-fase3.css`) e estilos gerais (`styles.css`, `styles-fases.css`).
  - Imagens representando os níveis (`level1.png`, `level2.png`, `level3.png`).

- **`teste.py`**: Arquivo principal do projeto, que contém a lógica do servidor Flask e as rotas para as páginas.

## Funcionalidades

1. **Página Inicial**: Introduz o usuário ao quiz e permite iniciar o jogo.
2. **Seleção de Fases**: Permite escolher entre as fases disponíveis.
3. **Fase 1**: Quiz de múltipla escolha com perguntas sobre lógica de programação.
4. **Fase 2**: Quiz interativo com arrastar e soltar para preencher lacunas.
5. **Fase 3**: Quiz de múltipla escolha com perguntas sobre conceitos básicos de programação.
6. **Resultado Final**: Exibe uma mensagem de conclusão ao passar por todas as fases.

## Tecnologias Utilizadas

- **Flask**: Framework web para Python.
- **HTML/CSS**: Para estrutura e estilização das páginas.
- **JavaScript/jQuery**: Para interatividade, como o recurso de arrastar e soltar na Fase 2.

## Como Executar o Projeto

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as dependências necessárias:
   ```bash
   pip install flask
