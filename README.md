# Calculadora-Python
Calculadora simples, com interface gráfica em Python para operações básicas (soma, subtração, multiplicação e divisão).

Uma calculadora completa desenvolvida em Python com interface gráfica utilizando Tkinter. Este projeto oferece uma experiência de usuário intuitiva com suporte a operações matemáticas básicas e histórico de cálculos.

# Funcionalidades Principais
🖩 Operações básicas: adição (+), subtração (-), multiplicação (*) e divisão (/)
📋 Histórico de operações
⌨️ Suporte a teclado
🔄 Botão para limpar histórico

# Conceitos de Python Utilizados
# 1. Programação Orientada a Objetos (POO)
- **Classes e Objetos**: A aplicação é estruturada em uma classe principal `Calculadora`
- **Métodos**: Diferentes métodos para organizar a lógica da calculadora
- **Atributos de Instância**: Como `self.operacao`, `self.numero1` e `self.historico_operacoes`
- **Encapsulamento**: Uso de métodos privados (com `_` no início) para organização interna

# 2. Interface Gráfica com Tkinter
- **Widgets**: Uso de diversos widgets como `Frame`, `Button`, `Entry`, `Text`, `Label`, `Scrollbar`
- **Gerenciadores de Layout**: `pack()` e `grid()` para organização dos elementos na interface
- **Estilização**: Personalização da aparência com `ttk.Style()`
- **Eventos**: Tratamento de eventos de teclado e mouse

# 3. Manipulação de Strings
- Formatação de números decimais
- Substituição de caracteres (`replace()`)
- Verificação de conteúdo em strings (`in`, `split()`)
- Remoção de caracteres desnecessários (`rstrip()`, `lstrip()`)

# 4. Estruturas de Dados
- **Listas**: Para armazenar o histórico de operações
- **Dicionários**: Para mapeamento de teclas e operações

# 5. Controle de Fluxo
- Estruturas condicionais (`if/elif/else`)
- Tratamento de exceções com `try/except`
- Laços de repetição (`for`)

# 6. Funções
- Definição de funções com parâmetros e valores de retorno
- Funções anônimas (`lambda`)
- Documentação com docstrings

# 7. Conversão de Tipos
- Conversão entre strings, inteiros e números de ponto flutuante
- Tratamento de erros em conversões

# 8. Módulos e Pacotes
- Importação de módulos (`import tkinter as tk`, `from tkinter import ttk`)
- Uso de `if __name__ == "__main__"`

# Tecnologias Utilizadas
Python
Tkinter (biblioteca padrão do Python para interfaces gráficas)

# Como Executar
Certifique-se de ter o Python 3.x instalado
Execute o arquivo calculadora_gui.py:
