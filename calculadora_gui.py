import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        self.root.configure(bg="#f0f0f0")
        
        # Variáveis de estado
        self.operacao = None
        self.numero1 = None
        self.historico_operacoes = []
        
        self._configurar_estilos()
        self._criar_interface()
        
        # Configurar eventos do teclado
        self.root.bind('<Key>', self.teclado)
    
    def _configurar_estilos(self):
        """Configura os estilos visuais da interface."""
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10), padding=2)
        self.style.configure('Small.TButton', font=('Arial', 8), padding=1)
    
    def _criar_interface(self):
        """Cria todos os componentes da interface do usuário."""
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding=5)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self._criar_calculadora()
        self._criar_historico()
    
    def _criar_calculadora(self):
        """Cria o painel da calculadora."""
        # Frame da calculadora (lado esquerdo)
        self.calc_frame = ttk.Frame(self.main_frame)
        self.calc_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Display
        self.display = ttk.Entry(
            self.calc_frame, 
            justify="right", 
            font=("Arial", 20)
        )
        self.display.pack(fill=tk.X, pady=(0, 5), ipady=10)
        self.display.insert(0, "0")
        
        # Frame para os botões
        self.botoes_frame = ttk.Frame(self.calc_frame)
        self.botoes_frame.pack(fill=tk.BOTH, expand=True)
        
        # Configurar grade de botões
        self._configurar_botoes_numericos()
        self._configurar_botoes_operacao()
        
        # Configurar pesos da grade
        for i in range(5):
            self.botoes_frame.grid_rowconfigure(i, weight=1, uniform='row')
            self.botoes_frame.grid_columnconfigure(i, weight=1, uniform='col')
    
    def _criar_historico(self):
        """Cria o painel de histórico."""
        # Frame do histórico (lado direito)
        self.hist_frame = ttk.Frame(self.main_frame, width=250)
        self.hist_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))
        
        # Cabeçalho do histórico
        hist_header = ttk.Frame(self.hist_frame)
        hist_header.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(
            hist_header, 
            text="Histórico", 
            font=("Arial", 12, "bold")
        ).pack(side=tk.LEFT)
        
        # Botão para limpar histórico
        ttk.Button(
            hist_header,
            text="Limpar",
            command=self.limpar_historico,
            width=6,
            style='Small.TButton'
        ).pack(side=tk.RIGHT, padx=(10, 0))
        
        # Área de histórico com barra de rolagem
        self.historico = tk.Text(
            self.hist_frame, 
            height=20, 
            width=30,
            font=("Arial", 9),
            spacing1=2,
            spacing2=2,
            spacing3=2,
            wrap=tk.NONE
        )
        scrollbar = ttk.Scrollbar(
            self.hist_frame, 
            orient="vertical", 
            command=self.historico.yview
        )
        self.historico.configure(yscrollcommand=scrollbar.set)
        
        self.historico.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.historico.configure(state='disabled')
    
    def _configurar_botoes_numericos(self):
        """Configura os botões numéricos da calculadora."""
        botoes = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', ',', '←',
            'C'
        ]
        
        row = 0
        col = 0
        
        for btn in botoes:
            if btn == 'C':
                btn_widget = ttk.Button(
                    self.botoes_frame,
                    text='C',
                    command=lambda: self.clique_botao('C'),
                    width=5
                )
                btn_widget.grid(row=row, column=col, columnspan=3, padx=1, pady=1, sticky='nsew')
                row += 1
            elif btn == '←':
                btn_widget = ttk.Button(
                    self.botoes_frame,
                    text='←',
                    command=lambda: self.clique_botao('←'),
                    width=5
                )
                btn_widget.grid(row=row, column=col, padx=1, pady=1, sticky='nsew')
                col += 1
                if col > 2:
                    col = 0
                    row += 1
            else:
                btn_widget = ttk.Button(
                    self.botoes_frame,
                    text=btn,
                    command=lambda x=btn: self.clique_botao(x),
                    width=5
                )
                btn_widget.grid(row=row, column=col, padx=1, pady=1, sticky='nsew')
                col += 1
                if col > 2:
                    col = 0
                    row += 1
    
    def _configurar_botoes_operacao(self):
        """Configura os botões de operação da calculadora."""
        operacoes = ['+', '-', '*', '/']
        for i, op in enumerate(operacoes):
            btn = ttk.Button(
                self.botoes_frame,
                text=op,
                command=lambda x=op: self.operacao_selecionada(x),
                width=5
            )
            btn.grid(row=i, column=4, padx=1, pady=1, sticky='nsew')
        
        # Botão de igual
        ttk.Button(
            self.botoes_frame,
            text='=',
            command=self.calcular_resultado,
            width=5
        ).grid(row=4, column=4, rowspan=2, padx=1, pady=1, sticky='nsew')
    
    def adicionar_historico(self, operacao, resultado):
        try:
            # Formata o resultado
            if resultado == int(resultado):
                resultado_str = str(int(resultado))
            else:
                resultado_str = f"{float(resultado):.10f}".rstrip('0').rstrip('.')
                if '.' in resultado_str:
                    resultado_str = resultado_str.replace('.', ',')
            
            # Formata a operação
            partes = operacao.split()
            
            # Formata o primeiro número
            num1 = float(partes[0].replace(',', '.'))
            if num1 == int(num1):
                num1 = str(int(num1))
            else:
                num1 = str(num1).replace('.', ',').rstrip('0').rstrip(',')
            
            operador = partes[1]
            
            # Formata o segundo número
            num2 = float(partes[2].replace(',', '.'))
            if num2 == int(num2):
                num2 = str(int(num2))
            else:
                num2 = str(num2).replace('.', ',').rstrip('0').rstrip(',')
            
            operacao_formatada = f"{num1} {operador} {num2} = {resultado_str}"
            self.historico_operacoes.append(operacao_formatada)
            self.atualizar_historico()
        except Exception as e:
            print(f"Erro ao adicionar ao histórico: {e}")
    
    def atualizar_historico(self):
        """Atualiza a exibição do histórico com as operações salvas."""
        self.historico.configure(state='normal')
        self.historico.delete(1.0, tk.END)
        for operacao in self.historico_operacoes:
            self.historico.insert(tk.END, operacao + "\n")
        self.historico.configure(state='disabled')
        self.historico.see(tk.END)
    
    def limpar_historico(self):
        """Limpa todo o histórico de operações."""
        self.historico_operacoes = []
        self.atualizar_historico()
    
    def clique_botao(self, valor):
        #Trata o clique em um botão da calculadora.
        if valor == 'C':
            self.display.delete(0, tk.END)
            self.display.insert(0, "0")
            self.operacao = None
            self.numero1 = None
        elif valor == '←':
            atual = self.display.get()
            if len(atual) > 1:
                self.display.delete(0, tk.END)
                self.display.insert(0, atual[:-1])
            else:
                self.display.delete(0, tk.END)
                self.display.insert(0, "0")
        elif valor == ',':
            atual = self.display.get()
            if ',' not in atual.split()[-1]:
                if atual == "0":
                    self.display.delete(0, tk.END)
                self.display.insert(tk.END, valor)
        else:
            atual = self.display.get()
            if atual == "0":
                self.display.delete(0, tk.END)
            elif atual[-1] in ['+', '-', '*', '/']:
                self.display.insert(tk.END, "0")
            self.display.insert(tk.END, valor)
    
    def operacao_selecionada(self, operacao):
        try:
            display_atual = self.display.get()
            numero = float(display_atual.replace(',', '.'))
            # Formata o número para remover .0 de inteiros
            if numero.is_integer():
                numero_formatado = str(int(numero))
            else:
                numero_formatado = str(numero).replace('.', ',')
                
            self.numero1 = numero
            self.operacao = operacao
            self.display.delete(0, tk.END)
            self.display.insert(0, f"{numero_formatado} {operacao} ")
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Erro")
    
    def calcular_resultado(self):
        """Calcula o resultado da operação atual."""
        try:
            if not self.operacao or self.numero1 is None:
                return
                
            # Obtém o segundo número do display
            display_atual = self.display.get()
            partes = display_atual.split()
            
            # Se não houver segundo número, usa o primeiro número
            if len(partes) < 3:
                return
                
            numero2 = float(partes[2].replace(',', '.'))
            
            # Realiza o cálculo
            if self.operacao == '+':
                resultado = self.numero1 + numero2
            elif self.operacao == '-':
                resultado = self.numero1 - numero2
            elif self.operacao == '*':
                resultado = self.numero1 * numero2
            elif self.operacao == '/':
                if numero2 == 0:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Erro: Divisão por zero")
                    return
                resultado = self.numero1 / numero2
            
            # Adiciona ao histórico
            operacao_texto = f"{self.numero1} {self.operacao} {numero2}"
            self.adicionar_historico(operacao_texto, resultado)
            
            # Formata e exibe o resultado
            resultado_str = f"{float(resultado):.10f}".rstrip('0').rstrip('.')
            if '.' in resultado_str:
                resultado_str = resultado_str.replace('.', ',')
            
            self.display.delete(0, tk.END)
            self.display.insert(0, resultado_str)
            self.operacao = None
            self.numero1 = None
            
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Erro")
    
    def teclado(self, event):
        #trata eventos de teclado
        tecla = event.char
        
        # Números 0-9
        if tecla.isdigit():
            self.clique_botao(tecla)
        # Ponto ou vírgula decimal
        elif tecla in [',', '.']:
            self.clique_botao(',')
        # Operações básicas
        elif tecla in ['+', '-', '*', '/']:
            self.operacao_selecionada(tecla)
        # Enter para calcular
        elif event.keysym == 'Return':
            self.calcular_resultado()
        # Backspace para apagar
        elif event.keysym == 'BackSpace':
            self.clique_botao('←')
        # Esc para sair
        elif event.keysym == 'Escape':
            self.root.quit()
        # C para limpar
        elif event.keysym.lower() == 'c':
            self.clique_botao('C')


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
