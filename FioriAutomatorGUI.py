import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import pyautogui as py
import pyperclip as pc
import keyboard as kb
import time
import threading
import webbrowser
from datetime import datetime

class FioriAutomatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fiori Automator - Interface Gráfica")
        self.root.geometry("800x700")
        self.root.configure(bg='#f0f0f0')
        
        # Variáveis de controle
        self.is_running = False
        self.stop_execution = False
        
        # Dados organizados por categorias
        self.dados_categorias = {
            "GLOBAL": [
                ["S4TAX_0001", "/S4TAX/0001", "Configurações de ambiente"],
                ["S4TAX_0002", "/S4TAX/0002", "Configurações de comunicação"],
                ["S4TAX_0003", "/S4TAX/0003", "Habilitar tipo de documento fiscal"],
                ["S4TAX_0004", "/S4TAX/0004", "Monitor de requisições ao Orbit"],
                ["S4TAX_0005", "/S4TAX/0005", "Cadastro de Grupos SAP <-> Orbit"],
                ["S4TAX_0006", "/S4TAX/0006", "Cadastro de Empresas SAP <-> Orbit"],
                ["S4TAX_0007", "/S4TAX/0007", "Cadastro de Filiais SAP <-> Orbit"],
                ["S4TAX_0008", "/S4TAX/0008", "Versionamento de Produtos"],
                ["S4TAX_0009", "/S4TAX/0009", "Lista de transações por módulos 4Tax"],
                ["S4TAX_0010", "/S4TAX/0010", "Tarefas de Instalação"],
                ["S4TAX_0011", "/S4TAX/0011", "Exibição de várias tabelas"],
                ["S4TAX_0012", "/S4TAX/0012", "Lista de jobs do produto"],
                ["S4TAX_0013", "/S4TAX/0013", "Status do Conector"],
                ["S4TAX_0014", "/S4TAX/0014", "Editor tabelas via CSV"],
                ["S4TAX_0015", "/S4TAX/0015", "Configurações de envio de erros"],
                ["S4TAX_0016", "/S4TAX/0016", "Configurações tabelas CUTE"],
                ["S4TAX_0017", "/S4TAX/0017", "Configurações campos CUTE"],
                ["S4TAX_CUTE", "/S4TAX/CUTE", "Editor de tabelas customizado"],
                ["S4TAX_MENU", "/S4TAX/MENU", "Lista de transações por módulos 4Tax"],
                ["S4TAX_TASKS", "/S4TAX/TASKS", "Tarefas de instalação"],
            ],
            "OUTBOUND": [
                ["S4TAX_CCE_PRINT", "/S4TAX/CCE_PRINT", "Impressão de carta de correção dfe's"],
                ["S4TAX_DFE_001", "/S4TAX/DFE_001", "Configuração de e-mail para DFE's"],
                ["S4TAX_DFE_002", "/S4TAX/DFE_002", "Configurações gerais DF-e"],
                ["S4TAX_DFE_003", "/S4TAX/DFE_003", "Gerador de cópias de dfe's"],
                ["S4TAX_DFE_004", "/S4TAX/DFE_004", "Status de documentos fiscais"],
                ["S4TAX_DFE_005", "/S4TAX/DFE_005", "Download de dfe's em massa Remoto"],
                ["S4TAX_DFE_006", "/S4TAX/DFE_006", "Gerador de dfe's mockadas"],
                ["S4TAX_DFE_007", "/S4TAX/DFE_007", "Envia e-mail com danfe/xml"],
                ["S4TAX_DFE_008", "/S4TAX/DFE_008", "Programa para simular emissões"],
                ["S4TAX_DFE_009", "/S4TAX/DFE_009", "Configuração modelos e-mail DFE"],
                ["S4TAX_DFE_010", "/S4TAX/DFE_010", "Carga dos XMLs do SAP GRC NFe"],
                ["S4TAX_DFE_011", "/S4TAX/DFE_011", "Download de dfe's em massa local"],
                ["S4TAX_DFE_012", "/S4TAX/DFE_012", "Conciliação de documentos"],
                ["S4TAX_DFE_013", "/S4TAX/DFE_013", "URL base do serviço de consulta"],
                ["S4TAX_DFE_014", "/S4TAX/DFE_014", "Configurações Reforma Tributária"],
                ["S4TAX_STATUS", "/S4TAX/STATUS", "Status de documentos fiscais"],
            ],
            "NFS-e": [
                ["S4TAX_NFSE_001", "/S4TAX/NFSE_001", "Cadastro de categorias de nota NFS-e"],
                ["S4TAX_NFSE_002", "/S4TAX/NFSE_002", "Valores customizados do item NFS-e"],
                ["S4TAX_NFSE_003", "/S4TAX/NFSE_003", "Valores customizados da filial NFS-e"],
                ["S4TAX_NFSE_004", "/S4TAX/NFSE_004", "Impostos NFS-e definidos na pricing"],
                ["S4TAX_NFSE_005", "/S4TAX/NFSE_005", "Intervalo de numeração para RPS NFSe"],
                ["S4TAX_NFSE_006", "/S4TAX/NFSE_006", "Configuração Filial -> Município"],
                ["S4TAX_NFSE_007", "/S4TAX/NFSE_007", "Motivos de cancelamento NFS-e"],
                ["S4TAX_NFSE_008", "/S4TAX/NFSE_008", "Tipos de impostos NFS-e"],
                ["S4TAX_NFSE_009", "/S4TAX/NFSE_009", "Municípios com emissão por arquivo"],
                ["S4TAX_NFSE_010", "/S4TAX/NFSE_010", "Configurações default NFse"],
                ["S4TAX_NFSE_011", "/S4TAX/NFSE_011", "Monitor de NFS-e"],
                ["S4TAX_NFSE_012", "/S4TAX/NFSE_012", "Dashboard para documentos NFS-e"],
                ["S4TAX_NFSE_013", "/S4TAX/NFSE_013", "Editor de dados para documentos NFSe"],
                ["S4TAX_NFSE_MONITOR", "/S4TAX/NFSE_MONITOR", "Monitor de NFS-e"],
            ],
            "4UNITY": [
                ["S4TAX_SUPP_001", "/S4TAX/SUPP_001", "Configurações gerais 4unity"],
                ["S4TAX_SUPP_002", "/S4TAX/SUPP_002", "Etapas documentos 4Unity"],
                ["S4TAX_SUPP_003", "/S4TAX/SUPP_003", "Editor de dados de documentos 4Unity"],
                ["S4TAX_SUPP_004", "/S4TAX/SUPP_004", "Monitor 4Unity"],
                ["S4TAX_SUPP_005", "/S4TAX/SUPP_005", "Reintegração de fornecedores"],
                ["S4TAX_SUPP_006", "/S4TAX/SUPP_006", "Cadastro tag 4Unity em massa"],
                ["S4TAX_SUPP_007", "/S4TAX/SUPP_007", "Monitor pedido de compras"],
                ["S4TAX_SUPP_008", "/S4TAX/SUPP_008", "Carga de parceiros para integração"],
                ["S4TAX_SUPP_009", "/S4TAX/SUPP_009", "Configuração tipos pedido de compra"],
            ],
            "PARCEIRO": [
                ["S4TAX_PART_001", "/S4TAX/PART_001", "Integrar Parceiro de Negócio"],
                ["S4TAX_PART_002", "/S4TAX/PART_002", "Monitor de parceiros"],
                ["S4TAX_PART_003", "/S4TAX/PART_003", "Configurações de parceiro"],
            ],
            "4SERVICE": [
                ["S4TAX_4SER_001", "/S4TAX/4SER_001", "Monitor apontamentos 4Service"],
                ["S4TAX_4SER_002", "/S4TAX/4SER_002", "Relatório de horas apontadas (CSV)"],
                ["S4TAX_4SER_003", "/S4TAX/4SER_003", "Configurações básicas 4service"],
                ["S4TAX_4SER_004", "/S4TAX/4SER_004", "Configurações de integração 4Service"],
            ],
            "BANK": [
                ["S4TAX_BANK_001", "/S4TAX/BANK_001", "Configurações de contas"],
                ["S4TAX_BANK_002", "/S4TAX/BANK_002", "Configuração geral"],
                ["S4TAX_BANK_003", "/S4TAX/BANK_003", "Monitor de boletos bancários"],
                ["S4TAX_BANK_004", "/S4TAX/BANK_004", "Impostos para considerar descontos"],
                ["S4TAX_BANK_005", "/S4TAX/BANK_005", "Configurações de Emissão Automática"],
                ["S4TAX_BANK_006", "/S4TAX/BANK_006", "Configurações de Data de Compensação"],
            ]
        }
        
        # Controle de categorias selecionadas (apenas GLOBAL e OUTBOUND ativas por padrão)
        self.categorias_ativas = {
            "GLOBAL": True,
            "OUTBOUND": True,
            "NFS-e": False,
            "4UNITY": False,
            "PARCEIRO": True,  # Era a única outra que estava ativa no original
            "4SERVICE": False,
            "BANK": False
        }
        
        # Dados filtrados baseados na seleção
        self.dados = self.get_dados_filtrados()
        
        self.setup_ui()
    
    def get_dados_filtrados(self):
        """Retorna dados filtrados baseados nas categorias selecionadas"""
        dados_filtrados = []
        for categoria, ativa in self.categorias_ativas.items():
            if ativa:
                dados_filtrados.extend(self.dados_categorias[categoria])
        return dados_filtrados
    
    def atualizar_dados(self):
        """Atualiza a lista de dados baseada na seleção de categorias"""
        self.dados = self.get_dados_filtrados()
        # Atualiza o contador no log
        total_itens = len(self.dados)
        categorias_ativas = [cat for cat, ativa in self.categorias_ativas.items() if ativa]
        self.log_message(f"📊 Dados atualizados: {total_itens} itens em {len(categorias_ativas)} categorias")
        self.log_message(f"🏷️ Categorias ativas: {', '.join(categorias_ativas)}")
        
    def abrir_selecao_dados(self):
        """Abre janela para seleção de categorias de dados"""
        self.janela_dados = tk.Toplevel(self.root)
        self.janela_dados.title("📋 Configurar Dados para Processamento")
        self.janela_dados.geometry("800x720")
        self.janela_dados.configure(bg='#f0f0f0')
        self.janela_dados.transient(self.root)
        self.janela_dados.grab_set()
        
        # Título
        titulo_frame = tk.Frame(self.janela_dados, bg='#34495e', height=60)
        titulo_frame.pack(fill='x', padx=10, pady=(10, 0))
        titulo_frame.pack_propagate(False)
        
        tk.Label(titulo_frame, text="🎯 Selecionar Categorias de Dados", 
                font=('Arial', 14, 'bold'), fg='white', bg='#34495e').pack(expand=True)
        
        # Frame principal
        main_frame = tk.Frame(self.janela_dados, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Instruções
        instrucoes = tk.Label(main_frame, 
                             text="Selecione as categorias que deseja processar:\n"
                                  "✅ = Incluir na execução  |  ❌ = Excluir da execução",
                             font=('Arial', 10), bg='#f0f0f0', fg='#2c3e50')
        instrucoes.pack(pady=(0, 10))
        
        # Frame para checkboxes com scroll
        canvas_frame = tk.Frame(main_frame, bg='#f0f0f0')
        canvas_frame.pack(fill='both', expand=True)
        
        canvas = tk.Canvas(canvas_frame, bg='#f0f0f0')
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#f0f0f0')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Variáveis de controle para checkboxes
        self.categoria_vars = {}
        
        # Criar checkboxes para cada categoria
        for categoria, dados_cat in self.dados_categorias.items():
            categoria_frame = tk.LabelFrame(scrollable_frame, 
                                          text=f"📁 {categoria} ({len(dados_cat)} itens)",
                                          font=('Arial', 11, 'bold'),
                                          bg='#ecf0f1', fg='#2c3e50')
            categoria_frame.pack(fill='x', padx=5, pady=5)
            
            # Checkbox para categoria
            var = tk.BooleanVar(value=self.categorias_ativas[categoria])
            self.categoria_vars[categoria] = var
            
            checkbox = tk.Checkbutton(categoria_frame, 
                                    text=f"Incluir categoria {categoria}",
                                    variable=var,
                                    font=('Arial', 10, 'bold'),
                                    bg='#ecf0f1',
                                    command=lambda cat=categoria: self.toggle_categoria(cat))
            checkbox.pack(anchor='w', padx=10, pady=5)
            
            # Lista de itens da categoria (primeiros 5 + total)
            items_frame = tk.Frame(categoria_frame, bg='#ecf0f1')
            items_frame.pack(fill='x', padx=20, pady=(0, 10))
            
            for i, item in enumerate(dados_cat[:5]):  # Mostrar apenas os primeiros 5
                item_text = f"• {item[0]} - {item[2]}"
                tk.Label(items_frame, text=item_text, 
                        font=('Arial', 8), bg='#ecf0f1', fg='#34495e',
                        anchor='w').pack(fill='x')
            
            if len(dados_cat) > 5:
                tk.Label(items_frame, 
                        text=f"... e mais {len(dados_cat) - 5} itens",
                        font=('Arial', 8, 'italic'), 
                        bg='#ecf0f1', fg='#7f8c8d',
                        anchor='w').pack(fill='x')
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botões de ação
        botoes_frame = tk.Frame(main_frame, bg='#f0f0f0')
        botoes_frame.pack(fill='x', pady=(10, 0))
        
        # Botões de seleção rápida
        tk.Button(botoes_frame, text="✅ Selecionar Tudo", 
                 command=self.selecionar_todas_categorias,
                 font=('Arial', 9), bg='#27ae60', fg='white').pack(side='left', padx=(0, 5))
        
        tk.Button(botoes_frame, text="❌ Deselecionar Tudo", 
                 command=self.deselecionar_todas_categorias,
                 font=('Arial', 9), bg='#e74c3c', fg='white').pack(side='left', padx=5)
        
        tk.Button(botoes_frame, text="🔄 Apenas GLOBAL + OUTBOUND", 
                 command=self.selecionar_basico,
                 font=('Arial', 9), bg='#3498db', fg='white').pack(side='left', padx=5)
        
        # Botões principais
        tk.Button(botoes_frame, text="💾 Aplicar", 
                 command=self.aplicar_selecao_dados,
                 font=('Arial', 10, 'bold'), bg='#27ae60', fg='white',
                 width=10).pack(side='right', padx=(5, 0))
        
        tk.Button(botoes_frame, text="❌ Cancelar", 
                 command=self.janela_dados.destroy,
                 font=('Arial', 10), bg='#95a5a6', fg='white',
                 width=10).pack(side='right')
    
    def toggle_categoria(self, categoria):
        """Alterna o estado de uma categoria"""
        pass  # A variável já é atualizada automaticamente
    
    def selecionar_todas_categorias(self):
        """Seleciona todas as categorias"""
        for var in self.categoria_vars.values():
            var.set(True)
    
    def deselecionar_todas_categorias(self):
        """Deseleciona todas as categorias"""
        for var in self.categoria_vars.values():
            var.set(False)
    
    def selecionar_basico(self):
        """Seleciona apenas GLOBAL e OUTBOUND"""
        for categoria, var in self.categoria_vars.items():
            var.set(categoria in ['GLOBAL', 'OUTBOUND'])
    
    def aplicar_selecao_dados(self):
        """Aplica a seleção de categorias"""
        # Atualiza as categorias ativas
        for categoria, var in self.categoria_vars.items():
            self.categorias_ativas[categoria] = var.get()
        
        # Verifica se pelo menos uma categoria foi selecionada
        if not any(self.categorias_ativas.values()):
            messagebox.showwarning("Aviso", "Pelo menos uma categoria deve ser selecionada!")
            return
        
        # Atualiza os dados
        self.atualizar_dados()
        
        # Fecha a janela
        self.janela_dados.destroy()
        
        messagebox.showinfo("Sucesso", f"Configuração atualizada!\n"
                                      f"Total de itens selecionados: {len(self.dados)}")
        
        # Atualiza a interface principal
        self.atualizar_interface_principal()
    
    def atualizar_interface_principal(self):
        """Atualiza elementos da interface principal baseado na seleção"""
        # Atualiza o label de total de itens no final das instruções
        total_itens = len(self.dados)
        categorias_ativas = [cat for cat, ativa in self.categorias_ativas.items() if ativa]
        
        # Atualiza o contador na interface
        self.contador_label.config(text=f"📊 {total_itens} itens selecionados")

        # Atualiza preview do índice
        self.atualizar_preview_indice()

        # Adiciona informação no status
        self.update_status(f"Pronto - {total_itens} itens selecionados", '#27ae60')
        
    def atualizar_preview_indice(self):
        """Atualiza o label que mostra o item correspondente ao índice digitado"""
        if not hasattr(self, 'indice_preview_label'):
            return
        try:
            idx = int(self.index_var.get())
            if 0 <= idx < len(self.dados):
                item = self.dados[idx]
                texto = f"→  [{idx}]  {item[0]}  —  {item[2]}"
                cor = '#2c3e50'
            elif len(self.dados) == 0:
                texto = "Lista vazia — configure as categorias primeiro"
                cor = '#e74c3c'
            else:
                texto = f"⚠️  Índice {idx} fora do intervalo (0 – {len(self.dados) - 1})"
                cor = '#e74c3c'
        except ValueError:
            texto = "Índice inválido"
            cor = '#e74c3c'
        self.indice_preview_label.config(text=texto, fg=cor)

    def abrir_selecao_indice(self):
        """Abre janela com tabela de itens para seleção visual do índice inicial"""
        if not self.dados:
            messagebox.showwarning("Aviso", "Nenhum dado disponível. Configure as categorias primeiro.")
            return

        janela = tk.Toplevel(self.root)
        janela.title("📋 Selecionar Índice Inicial")
        janela.geometry("760x500")
        janela.configure(bg='#f0f0f0')
        janela.transient(self.root)
        janela.grab_set()

        # Título
        titulo_frame = tk.Frame(janela, bg='#2c3e50', height=48)
        titulo_frame.pack(fill='x', padx=10, pady=(10, 0))
        titulo_frame.pack_propagate(False)
        tk.Label(titulo_frame, text="🎯 Selecionar Item de Início",
                font=('Arial', 13, 'bold'), fg='white', bg='#2c3e50').pack(expand=True)

        # Barra de pesquisa
        search_frame = tk.Frame(janela, bg='#f0f0f0')
        search_frame.pack(fill='x', padx=10, pady=8)
        tk.Label(search_frame, text="🔍 Filtrar:", font=('Arial', 10), bg='#f0f0f0').pack(side='left')
        search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=search_var, font=('Arial', 10), width=35)
        search_entry.pack(side='left', padx=(5, 0))
        search_entry.focus_set()

        # Treeview
        tree_frame = tk.Frame(janela, bg='#f0f0f0')
        tree_frame.pack(fill='both', expand=True, padx=10)

        cols = ('#', 'Código', 'Caminho', 'Descrição')
        tree = ttk.Treeview(tree_frame, columns=cols, show='headings', selectmode='browse')
        tree.heading('#', text='#')
        tree.heading('Código', text='Código')
        tree.heading('Caminho', text='Caminho')
        tree.heading('Descrição', text='Descrição')
        tree.column('#', width=45, stretch=False, anchor='center')
        tree.column('Código', width=130, stretch=False)
        tree.column('Caminho', width=140, stretch=False)
        tree.column('Descrição', width=390)

        vsb = ttk.Scrollbar(tree_frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        tree.pack(side='left', fill='both', expand=True)
        vsb.pack(side='right', fill='y')

        # Popula a árvore respeitando o filtro
        def popular_tree(filtro=''):
            tree.delete(*tree.get_children())
            filtro_lower = filtro.lower()
            for i, item in enumerate(self.dados):
                if (not filtro_lower
                        or filtro_lower in str(i)
                        or filtro_lower in item[0].lower()
                        or filtro_lower in item[2].lower()):
                    tree.insert('', 'end', iid=str(i), values=(i, item[0], item[1], item[2]))

        popular_tree()

        # Destaca o índice atual
        try:
            idx_atual = str(int(self.index_var.get()))
            if tree.exists(idx_atual):
                tree.selection_set(idx_atual)
                tree.see(idx_atual)
        except ValueError:
            pass

        search_var.trace_add('write', lambda *_: popular_tree(search_var.get()))

        # Rodapé: info + botões
        info_label = tk.Label(janela,
                             text=f"Total: {len(self.dados)} itens  |  Duplo-clique ou selecione e clique Confirmar",
                             font=('Arial', 9, 'italic'), bg='#f0f0f0', fg='#7f8c8d')
        info_label.pack(pady=(4, 0))

        btn_frame = tk.Frame(janela, bg='#f0f0f0')
        btn_frame.pack(fill='x', padx=10, pady=8)

        def confirmar():
            sel = tree.selection()
            if sel:
                self.index_var.set(sel[0])
            janela.destroy()

        tree.bind('<Double-1>', lambda _: confirmar())
        tk.Button(btn_frame, text="✅ Confirmar", command=confirmar,
                 font=('Arial', 10, 'bold'), bg='#27ae60', fg='white', width=12).pack(side='right', padx=(5, 0))
        tk.Button(btn_frame, text="❌ Cancelar", command=janela.destroy,
                 font=('Arial', 10), bg='#95a5a6', fg='white', width=12).pack(side='right')

    def setup_ui(self):
        # Título principal
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        title_frame.pack(fill='x', padx=10, pady=(10, 0))
        title_frame.pack_propagate(False)
        
        title_label = tk.Label(title_frame, text="🚀 Fiori Automator", 
                              font=('Arial', 18, 'bold'), 
                              fg='white', bg='#2c3e50')
        title_label.pack(expand=True)
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Frame de configurações
        config_frame = tk.LabelFrame(main_frame, text="⚙️ Configurações", 
                                   font=('Arial', 12, 'bold'),
                                   bg='#f0f0f0', fg='#2c3e50')
        config_frame.pack(fill='x', pady=(0, 10))
        
        # Linha 1: Índice Inicial e Tempo de Espera
        row1_frame = tk.Frame(config_frame, bg='#f0f0f0')
        row1_frame.pack(fill='x', padx=10, pady=10)
        
        # Índice Inicial
        tk.Label(row1_frame, text="Índice Inicial:",
                font=('Arial', 10), bg='#f0f0f0').pack(side='left')
        self.index_var = tk.StringVar(value="0")
        index_entry = tk.Entry(row1_frame, textvariable=self.index_var,
                              width=6, font=('Arial', 10))
        index_entry.pack(side='left', padx=(5, 3))

        tk.Button(row1_frame, text="📋", command=self.abrir_selecao_indice,
                 font=('Arial', 9), bg='#3498db', fg='white',
                 padx=4, pady=0).pack(side='left', padx=(0, 20))

        # Tempo de Espera
        tk.Label(row1_frame, text="Tempo de Espera (s):",
                font=('Arial', 10), bg='#f0f0f0').pack(side='left')
        self.tempo_var = tk.StringVar(value="1.5")
        tempo_entry = tk.Entry(row1_frame, textvariable=self.tempo_var,
                              width=8, font=('Arial', 10))
        tempo_entry.pack(side='left', padx=5)

        # Preview do item correspondente ao índice digitado
        row1b_frame = tk.Frame(config_frame, bg='#f0f0f0')
        row1b_frame.pack(fill='x', padx=10, pady=(0, 6))
        self.indice_preview_label = tk.Label(row1b_frame, text="",
                                            font=('Arial', 9, 'italic'),
                                            bg='#f0f0f0', fg='#7f8c8d')
        self.indice_preview_label.pack(side='left')
        self.index_var.trace_add('write', lambda *_: self.atualizar_preview_indice())
        self.atualizar_preview_indice()

        # Linha 2: Botão Configurar Dados
        row2_frame = tk.Frame(config_frame, bg='#f0f0f0')
        row2_frame.pack(fill='x', padx=10, pady=(5, 10))
        
        config_dados_btn = tk.Button(row2_frame, text="📋 Configurar Dados", 
                                   command=self.abrir_selecao_dados,
                                   font=('Arial', 10, 'bold'),
                                   bg='#3498db', fg='white',
                                   width=20, height=1)
        config_dados_btn.pack(side='left')
        
        # Label com contador de itens selecionados
        self.contador_label = tk.Label(row2_frame, 
                                     text=f"📊 {len(self.dados)} itens selecionados",
                                     font=('Arial', 10), bg='#f0f0f0', fg='#2c3e50')
        self.contador_label.pack(side='left', padx=(20, 0))
        
        # Frame de seleção de script
        script_frame = tk.LabelFrame(main_frame, text="📋 Selecionar Script", 
                                   font=('Arial', 12, 'bold'),
                                   bg='#f0f0f0', fg='#2c3e50')
        script_frame.pack(fill='x', pady=(0, 10))
        
        # Radio buttons para seleção de script
        self.script_var = tk.StringVar(value="atribuicoes")
        
        radio_frame = tk.Frame(script_frame, bg='#f0f0f0')
        radio_frame.pack(padx=10, pady=10)
        
        tk.Radiobutton(radio_frame, text="📝 Criar Atribuições de Destino", 
                      variable=self.script_var, value="atribuicoes",
                      font=('Arial', 10), bg='#f0f0f0').pack(anchor='w')
        
        tk.Radiobutton(radio_frame, text="🧩 Adicionar Bloco", 
                      variable=self.script_var, value="bloco",
                      font=('Arial', 10), bg='#f0f0f0').pack(anchor='w')
        
        # Frame de controle
        control_frame = tk.Frame(main_frame, bg='#f0f0f0')
        control_frame.pack(fill='x', pady=(0, 10))
        
        # Botões de controle
        self.start_btn = tk.Button(control_frame, text="▶️ Executar", 
                                  command=self.start_execution,
                                  font=('Arial', 12, 'bold'),
                                  bg='#27ae60', fg='white',
                                  width=15, height=2)
        self.start_btn.pack(side='left', padx=(0, 10))
        
        self.stop_btn = tk.Button(control_frame, text="⏹️ Parar", 
                                 command=self.stop_execution_func,
                                 font=('Arial', 12, 'bold'),
                                 bg='#e74c3c', fg='white',
                                 width=15, height=2,
                                 state='disabled')
        self.stop_btn.pack(side='left')
        
        # Status
        status_frame = tk.Frame(main_frame, bg='#f0f0f0')
        status_frame.pack(fill='x', pady=(0, 10))
        
        tk.Label(status_frame, text="Status:", 
                font=('Arial', 10, 'bold'), bg='#f0f0f0').pack(side='left')
        self.status_label = tk.Label(status_frame, text="Pronto para executar", 
                                   font=('Arial', 10), bg='#f0f0f0', fg='#27ae60')
        self.status_label.pack(side='left', padx=5)
        
        # Progresso
        self.progress = ttk.Progressbar(main_frame, length=400, mode='determinate')
        self.progress.pack(fill='x', pady=(0, 10))
        
        # Rodapé — criadores (empacotado antes do log para não ser espremido pelo expand)
        footer_frame = tk.Frame(main_frame, bg='#f0f0f0')
        footer_frame.pack(side='bottom', fill='x', pady=(4, 0))

        def link(parent, texto, url):
            lbl = tk.Label(parent, text=texto, font=('Arial', 8, 'underline'),
                          bg='#f0f0f0', fg='#3498db', cursor='hand2')
            lbl.pack(side='right', padx=2)
            lbl.bind('<Button-1>', lambda _: webbrowser.open(url))

        link(footer_frame, "Lealwbs", "https://www.linkedin.com/in/lealwbs/")
        tk.Label(footer_frame, text="&",
                font=('Arial', 8), bg='#f0f0f0', fg='#95a5a6').pack(side='right', padx=2)
        link(footer_frame, "RenatoMAP77", "https://www.linkedin.com/in/renato-matos-alves-penna-646108276/")
        tk.Label(footer_frame, text="Criado por",
                font=('Arial', 8), bg='#f0f0f0', fg='#95a5a6').pack(side='right', padx=(0, 4))

        # Log de execução
        log_frame = tk.LabelFrame(main_frame, text="📄 Log de Execução",
                                font=('Arial', 12, 'bold'),
                                bg='#f0f0f0', fg='#2c3e50')
        log_frame.pack(fill='both', expand=True)

        self.log_text = scrolledtext.ScrolledText(log_frame, height=15,
                                                 font=('Consolas', 9),
                                                 bg='#2c3e50', fg='#ecf0f1')
        self.log_text.pack(fill='both', expand=True, padx=10, pady=10)

        # Instruções iniciais
        self.log_message("=== FIORI AUTOMATOR INICIADO ===")
        self.log_message("📌 INSTRUÇÕES:")
        self.log_message("1. Configure o Índice Inicial (quantos itens já foram processados)")
        self.log_message("2. Ajuste o Tempo de Espera conforme a velocidade do sistema")
        self.log_message("3. Use 'Configurar Dados' para selecionar categorias desejadas")
        self.log_message("4. Selecione o script desejado")
        self.log_message("5. Posicione o SAP na tela correta antes de executar")
        self.log_message("6. Para 'Adicionar Bloco': use CTRL para controlar o avanço")
        self.log_message(f"📊 Total de itens disponíveis: {len(self.dados)} (todas as categorias)")
        categorias_ativas = [cat for cat, ativa in self.categorias_ativas.items() if ativa]
        self.log_message(f"🏷️ Categorias ativas: {', '.join(categorias_ativas)}")
        self.log_message("="*50)
        
    def log_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}\n"
        self.log_text.insert(tk.END, formatted_message)
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def update_status(self, status, color='#27ae60'):
        self.status_label.config(text=status, fg=color)
        self.root.update_idletasks()
        
    def type_text(self, string):
        pc.copy(string)
        py.hotkey("ctrl", "v")
        
    def criar_atribuicoes_destino(self, index_inicio, tempo_espera):
        qtde_dados = len(self.dados)
        self.progress.config(maximum=qtde_dados)
        
        self.log_message(f"🚀 Iniciando Criação de Atribuições de Destino")
        self.log_message(f"⚙️ Índice inicial: {index_inicio}, Tempo espera: {tempo_espera}s")
        
        # Aguarda posicionamento
        self.update_status("Aguardando posicionamento (2s)...", '#f39c12')
        time.sleep(2)
        
        for i in range(qtde_dados):
            if self.stop_execution:
                self.log_message("⏹️ Execução interrompida pelo usuário")
                break
                
            if index_inicio > 0:
                index_inicio -= 1
                self.progress['value'] = i + 1
                continue

            objeto = self.dados[i][0]
            transacao = self.dados[i][1]
            descricao = self.dados[i][2]
            
            self.update_status(f"Processando {i+1}/{qtde_dados}: {objeto}", '#3498db')
            self.log_message(f"📝 Processando: {objeto} - {descricao}")

            try:
                py.click()  # Criar atribuição de Destino
                time.sleep(tempo_espera * 5)

                py.press('tab', 1)  # Objeto Semântico
                self.type_text(objeto)
                time.sleep(tempo_espera)

                py.press('tab', 1)  # Ação
                self.type_text('display')
                py.press('enter')
                time.sleep(tempo_espera)

                py.press('tab', 1)  # Tipo de Aplicação
                self.type_text('Transação')
                time.sleep(tempo_espera/2)
                py.press('enter')
                time.sleep(tempo_espera)

                py.press('tab', 1)  # Título
                self.type_text(descricao)
                py.press('enter')
                time.sleep(tempo_espera)

                py.press('tab', 1)  # Transação
                self.type_text(transacao)
                py.press('enter')
                time.sleep(tempo_espera)

                py.press('tab', 11)  # Gravar
                time.sleep(tempo_espera / 2)
                py.press('enter')
                time.sleep(tempo_espera * 7)

                self.log_message(f"✅ {objeto} - {descricao} cadastrado com sucesso")
                
            except Exception as e:
                self.log_message(f"❌ Erro ao processar {objeto}: {str(e)}")
                
            self.progress['value'] = i + 1
            self.root.update_idletasks()
            
        if not self.stop_execution:
            self.log_message("🎉 Criação de Atribuições de Destino CONCLUÍDA!")
            
    def adicionar_bloco(self, index_inicio, tempo_espera):
        qtde_dados = len(self.dados)
        self.progress.config(maximum=qtde_dados)
        
        self.log_message(f"🧩 Iniciando Adição de Blocos")
        self.log_message(f"⚙️ Índice inicial: {index_inicio}, Tempo espera: {tempo_espera}s")
        self.log_message("⌨️ Use CTRL para avançar para o próximo item")
        
        # Aguarda posicionamento
        self.update_status("Aguardando posicionamento (2s)...", '#f39c12')
        time.sleep(2)
        
        for i in range(qtde_dados):
            if self.stop_execution:
                self.log_message("⏹️ Execução interrompida pelo usuário")
                break
                
            if index_inicio > 0:
                index_inicio -= 1
                self.progress['value'] = i + 1
                continue

            objeto = self.dados[i][0]
            transacao = self.dados[i][1]
            descricao = self.dados[i][2]
            
            self.update_status(f"Aguardando CTRL para {i+1}/{qtde_dados}: {objeto}", '#f39c12')
            self.log_message(f"⌨️ Pressione CTRL para processar: {objeto} - {descricao}")

            try:
                # Aguarda o usuário pressionar CTRL
                kb.wait('ctrl')
                time.sleep(tempo_espera * 2)
                
                self.update_status(f"Processando {i+1}/{qtde_dados}: {objeto}", '#3498db')

                py.press('tab', 1)  # Título
                py.press('del')
                self.type_text(descricao)
                # time.sleep(tempo_espera)

                py.press('tab', 3)  # Símbolo
                self.type_text('sap-icon://action-settings')
                # time.sleep(tempo_espera)

                py.press('tab', 3)  # Objeto Semântico
                self.type_text(objeto)
                py.press('enter')
                # time.sleep(tempo_espera)

                py.press('tab', 1)  # Ação
                self.type_text('display')
                py.press('enter')
                # time.sleep(tempo_espera)

                py.press('tab', 6)  # Gravar
                # time.sleep(tempo_espera / 2)
                py.press('enter')
                time.sleep(tempo_espera * 2)

                self.log_message(f"✅ {i} | {objeto} - {descricao} bloco adicionado")
                
            except Exception as e:
                self.log_message(f"❌ Erro ao processar {objeto}: {str(e)}")
                
            self.progress['value'] = i + 1
            self.root.update_idletasks()
            
        if not self.stop_execution:
            self.log_message("🎉 Adição de Blocos CONCLUÍDA!")
    
    def start_execution(self):
        try:
            index_inicio = int(self.index_var.get())
            tempo_espera = float(self.tempo_var.get())
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos!")
            return
            
        if index_inicio < 0 or tempo_espera <= 0:
            messagebox.showerror("Erro", "Valores devem ser positivos!")
            return
            
        # Confirmação
        script_nome = "Criar Atribuições de Destino" if self.script_var.get() == "atribuicoes" else "Adicionar Bloco"
        resultado = messagebox.askyesno("Confirmar Execução", 
                                       f"Executar: {script_nome}\n"
                                       f"Índice Inicial: {index_inicio}\n"
                                       f"Tempo de Espera: {tempo_espera}s\n\n"
                                       f"Certifique-se de que o SAP está posicionado corretamente!\n"
                                       f"Continuar?")
        
        if not resultado:
            return
            
        # Configurar interface para execução
        self.is_running = True
        self.stop_execution = False
        self.start_btn.config(state='disabled')
        self.stop_btn.config(state='normal')
        self.progress['value'] = 0
        
        # Executar em thread separada
        if self.script_var.get() == "atribuicoes":
            thread = threading.Thread(target=self.run_atribuicoes, 
                                     args=(index_inicio, tempo_espera))
        else:
            thread = threading.Thread(target=self.run_bloco, 
                                     args=(index_inicio, tempo_espera))
        
        thread.daemon = True
        thread.start()
        
    def run_atribuicoes(self, index_inicio, tempo_espera):
        try:
            self.criar_atribuicoes_destino(index_inicio, tempo_espera)
        except Exception as e:
            self.log_message(f"❌ Erro durante execução: {str(e)}")
        finally:
            self.finish_execution()
            
    def run_bloco(self, index_inicio, tempo_espera):
        try:
            self.adicionar_bloco(index_inicio, tempo_espera)
        except Exception as e:
            self.log_message(f"❌ Erro durante execução: {str(e)}")
        finally:
            self.finish_execution()
    
    def stop_execution_func(self):
        self.stop_execution = True
        self.log_message("⏹️ Solicitação de parada enviada...")
        self.update_status("Parando execução...", '#e74c3c')
        
    def finish_execution(self):
        self.is_running = False
        self.start_btn.config(state='normal')
        self.stop_btn.config(state='disabled')
        
        if self.stop_execution:
            self.update_status("Execução interrompida", '#e74c3c')
        else:
            self.update_status("Execução concluída", '#27ae60')
            
        self.log_message("="*50)

def main():
    root = tk.Tk()
    app = FioriAutomatorGUI(root)
    
    # Configurar fechamento da aplicação
    def on_closing():
        if app.is_running:
            if messagebox.askokcancel("Sair", "Execução em andamento. Deseja realmente sair?"):
                app.stop_execution = True
                root.destroy()
        else:
            root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()