# 💧 Sistema de Classificação do Consumo de Água

 ## 📌 Sobre o Projeto

 O **Sistema de Classificação do Consumo de Água** é um programa desenvolvido em Python que permite informar o tipo de imóvel e o consumo mensal de água em metros cúbicos (m³).

 A partir dessas informações, o sistema analisa os dados e apresenta uma classificação de acordo com as regras estabelecidas para o consumo de água.

 ## 🎯 Objetivo

 O objetivo do projeto é desenvolver um sistema simples para **classificar o consumo mensal de água de um imóvel**, auxiliando na identificação de consumos econômicos, moderados ou excessivos.

 O projeto também tem como finalidade praticar conceitos básicos de programação, como:

- Entrada de dados;
- Saída de informações;
- Variáveis;
- Estruturas condicionais (`if` e `else`);
- Operadores lógicos;
- Comparações de valores;
- Conversão de tipos de dados.

 ## 🛠️ Tecnologias Utilizadas

<div style="display: inline_block"><br>
    <img align="center" alt="Python" height="40" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
<div style="dispaly: inline_block"><br>
    <img align="center" alt="GitHub" height="40" width="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg>

 ## ⚙️ Como funciona?

 O sistema funciona seguindo algumas etapas:

1. O usuário informa o **tipo de imóvel**.
2. O usuário informa o **consumo mensal de água em m³**.
3. O programa verifica as informações utilizando estruturas condicionais.
4. O sistema identifica a classificação correspondente.
5. Por fim, são exibidos o tipo de imóvel, o consumo informado e a classificação.

 ### Exemplo de entrada

```
Olá, qual é o tipo de imóvel? apartamento
E qual é o consumo mensal de água em m³? 8
```

 ### Exemplo de saída

```
SISTEMA DE CONSUMO DE ÁGUA
Aqui está o valor do consumo de água do imóvel apartamento:
Consumo água: 8.0 m³
Classificação: Consumo econômico - excenlente controle de água.

Obrigado por utilizar nosso Sistema!
```

 ## 📋 Regras do Sistema

 O sistema utiliza o tipo de imóvel e o consumo mensal para definir a classificação.

 | **Tipo de imóvel** | **Consumo** | **Classificação** |
| --- | --- | --- |
| *Comercial* | Qualquer consumo | Tarifa comercial aplicada - consulte o plano corporativo. |
| *Apartamento* | Menor que 10 m³ | Consumo econômico - excelente controle de água. |
| *Apartamento* ou *casa* | Até 25 m³ | Consumo moderado - dentro do padrão residencial. |
| *Outros casos* | Acima dos limites definidos | Consumo excessivo - adote medidas de economia e verifique vazamentos. |

### Regras do Sistema

- **Imóveis comerciais:** a classificação comercial é aplicada independentemente do valor do consumo.
- **Apartamentos com consumo menor que 10 m³:** o sistema classifica como **consumo econômico**.
- **Apartamentos ou casas com consumo de até 25 m³:** o sistema classifica como **consumo moderado**, desde que a condição anterior não tenha sido atendida.
- **Demais casos:** o sistema classifica como **consumo excessivo**.

 ## 📚 Conteúdos Utilizados

 Durante o desenvolvimento do projeto foram utilizados os seguintes conteúdos de programação:

- Variáveis;
- Função `input()`;
- Função `print()`;
- Conversão de dados com `float()`;
- Métodos `.lower()` e `.strip()`;
- Estruturas condicionais `if` e `else`;
- Operadores de comparação (`<`, `<=`);
- Operadores lógicos (`or`);
- F-strings para formatação de textos;
- Estrutura básica de um programa em Python.

 ## 👩‍💻 Autora

 **Emanuelly Nicolly**

 Projeto desenvolvido para fins de aprendizado e prática de programação em Python.