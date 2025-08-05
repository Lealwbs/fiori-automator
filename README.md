![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Tkinter](https://img.shields.io/badge/tkinter-GUI-blue?style=for-the-badge&logo=python)
# Fiori Automator GUI

Automatização com interface gráfica moderna do processo de Fiorização do produto S4TAX no SAP. Este projeto contém uma aplicação GUI desenvolvida em Python que automatiza a criação de atribuições de destino e adição de blocos no ambiente Fiori.

## 📋 Descrição

O Fiori Automator GUI é uma solução completa de automação desenvolvida em Python com interface gráfica intuitiva que utiliza PyAutoGUI para automatizar tarefas repetitivas no processo de configuração do SAP Fiori. A aplicação oferece:

- **Interface Gráfica Moderna**: Interface Tkinter profissional com controles intuitivos
- **Criar Atribuições de Destino**: Automatiza o cadastro de objetos semânticos, transações e configurações
- **Adicionar Blocos**: Automatiza a adição de blocos com títulos, símbolos e objetos semânticos
- **Configuração de Dados**: Sistema flexível para selecionar categorias de transações
- **Log em Tempo Real**: Acompanhamento detalhado do progresso da execução
- **Controle de Execução**: Botões para iniciar, parar e monitorar o processo

## 🚀 Funcionalidades

### 🖥️ Interface Gráfica Principal
- **Painel de Configurações**: Ajuste fácil de parâmetros como índice inicial e tempo de espera
- **Seleção de Dados**: Interface para escolher categorias de transações (GLOBAL, OUTBOUND, NFS-e, 4UNITY, etc.)
- **Controle de Execução**: Botões intuitivos para iniciar e parar processos
- **Monitor de Progresso**: Barra de progresso e log detalhado em tempo real
- **Status do Sistema**: Indicadores visuais do estado atual da execução

### 📊 Categorias de Dados Disponíveis
- **GLOBAL**: Configurações gerais e de ambiente (20 itens)
- **OUTBOUND**: Documentos fiscais e DFE (15 itens)  
- **NFS-e**: Funcionalidades específicas de Nota Fiscal de Serviço (14 itens)
- **4UNITY**: Integrações com fornecedores (8 itens)
- **PARCEIRO**: Integração de parceiros de negócio (1 item)
- **4SERVICE**: Apontamentos e relatórios (4 itens)
- **BANK**: Configurações bancárias e boletos (6 itens)

### 🔧 Funcionalidades de Automação

#### Script 1: Criar Atribuições de Destino
- Automatiza o preenchimento completo de formulários para criar atribuições de destino
- Processa objetos semânticos, transações e descrições automaticamente
- Suporte para retomada a partir de qualquer índice específico
- Configuração de tempo de espera personalizável por item
- Log detalhado de cada item processado

#### Script 2: Adicionar Bloco
- Automatiza a adição de blocos no sistema Fiori com controle manual
- Utiliza tecla CTRL para sincronização perfeita com o usuário
- Adiciona ícones padronizados (sap-icon://settings) automaticamente
- Processa títulos, símbolos e objetos semânticos
- Controle de progresso item por item

## 🛠️ Pré-requisitos

### Dependências Python
```bash
pip install pyautogui
pip install pyperclip
pip install keyboard
pip install tkinter  # Geralmente já incluído no Python
```

### Versões Recomendadas
- Python 3.7+
- pyautogui 0.9.54+
- pyperclip 1.8.2+
- keyboard 0.13.5+
- tkinter (biblioteca padrão Python)

### Requisitos do Sistema
- Sistema Operacional: Windows 10/11 (testado)
- RAM: Mínimo 4GB recomendado
- SAP GUI instalado e configurado
- Acesso ao ambiente SAP Fiori

## 📦 Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/italolealwbs/fiori-automator.git
cd fiori-automator
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

Ou instale manualmente:
```bash
pip install pyautogui pyperclip keyboard
```

3. **Configure o ambiente:**
- Certifique-se de que o SAP GUI está instalado e configurado
- Verifique se você tem acesso ao ambiente SAP Fiori
- Execute a aplicação com privilégios adequados (se necessário)

4. **Execute a aplicação:**
```bash
python FioriAutomatorGUI.py
```

## 🎯 Como Usar

### 🚀 Iniciando a Aplicação

1. **Execute o FioriAutomatorGUI:**
```bash
python FioriAutomatorGUI.py
```

2. **A interface gráfica será aberta com:**
   - Painel de configurações no topo
   - Seleção de script (Atribuições de Destino ou Adicionar Bloco)
   - Botões de controle (Executar/Parar)
   - Log de execução em tempo real
   - Barra de progresso

### ⚙️ Configurações Iniciais

#### 1. Configurar Parâmetros Básicos
- **Índice Inicial**: Número de itens já processados (Só usar caso queira retomar de um ponto específico)
  - **Exemplo**: Se já processou 10 itens, coloque 10 para continuar do 11º
- **Tempo de Espera**: Intervalo em segundos entre ações (ajuste conforme quiser, recomendado 1 a 1.5 segundos)

#### 2. Configurar Dados para Processamento
- Clique em "📋 Configurar Dados"
- Selecione as categorias desejadas:
  - ✅ **GLOBAL**: Sempre recomendado (configurações básicas)
  - ✅ **OUTBOUND**: Para documentos fiscais
  - ✅ **NFS-e**: Se usar Nota Fiscal de Serviço
  - ✅ **4UNITY**: Para integrações com fornecedores
  - ✅ **PARCEIRO**: Para parceiros de negócio
  - ✅ **4SERVICE**: Para apontamentos de serviço
  - ✅ **BANK**: Para configurações bancárias

#### 3. Selecionar Script
- **📝 Criar Atribuições de Destino**: Para cadastro inicial de transações
- **🧩 Adicionar Bloco**: Para adicionar blocos no Fiori Launchpad

### 🎮 Executando a Automação

#### Para Criar Atribuições de Destino:

1. **Prepare o SAP:**
   - Acesse a página do Fiori
   - Navegue até "Atribuições de Destino"
   - Posicione o cursor no botão "Criar atribuição de destino"

2. **Configure e Execute:**
   - Ajuste o índice inicial se necessário
   - Clique em "▶️ Executar"
   - Confirme na janela de diálogo
   - **NÃO MOVA O MOUSE** durante a execução

3. **Monitoramento:**
   - Acompanhe o progresso na barra e log
   - Use "⏹️ Parar" se necessário interromper

#### Para Adicionar Bloco:

1. **Prepare o SAP:**
   - Acesse o Fiori Launchpad em modo de edição
   - Navegue para a parte de adicionar blocos

2. **Configure e Execute:**
   - Selecione "🧩 Criar Bloco"
   - Selecione App Launcher - estático
   - Clique no novo Bloco e depois em Configurar
   - Clique em "▶️ Executar"
   - Confirme na janela de diálogo

3. **Controle Manual:**
   - O sistema aguardará você pressionar **CTRL** para cada item
   - Como esse processo ainda é semi-automático, você precisa de repetir o passo 2.
   - Pressione CTRL quando estiver pronto para processar o próximo
   - Acompanhe o log para ver qual item será processado

## ⚙️ Configuração Avançada

### 🎛️ Parâmetros da Interface

**Configurações Principais:**
- **Índice Inicial**: Permite retomar execução de onde parou (0 = começar do início)
- **Tempo de Espera**: Intervalo entre ações em segundos (1.5s recomendado)

**Configuração de Dados:**
- **Seleção por Categorias**: Escolha apenas as categorias necessárias
- **Botões de Seleção Rápida**:
  - "✅ Selecionar Tudo": Ativa todas as categorias
  - "❌ Deselecionar Tudo": Desativa todas as categorias  
  - "🔄 Apenas GLOBAL + OUTBOUND": Configuração básica recomendada

### 📊 Estrutura de Dados

Cada categoria contém transações organizadas por funcionalidade:

```python
# Exemplo de estrutura de dados
"GLOBAL": [
    ["S4TAX_0001", "/S4TAX/0001", "Configurações de ambiente"],
    ["S4TAX_0002", "/S4TAX/0002", "Configurações de comunicação"],
    # ... mais itens
]
```

**Campos por item:**
1. **Código do Objeto**: Identificador único da transação
2. **Caminho da Transação**: Path completo no SAP
3. **Descrição**: Funcionalidade da transação

## ⚠️ Precauções e Limitações

### ⚡ Antes de Executar
- ✅ **Teste em ambiente de desenvolvimento primeiro**
- ✅ **Não mova o mouse** durante a execução automática
- ✅ **Certifique-se que o SAP está na posição correta**
- ✅ **Configure backups dos dados antes de executar**
- ✅ **Execute com privilégios adequados se necessário**

### 🔧 Durante a Execução
- 👀 **Monitore o log** para acompanhar o progresso
- ⏸️ **Use o botão Parar** se precisar interromper
- 🎯 **Para "Adicionar Bloco"**: Use CTRL para controlar o ritmo
- 📊 **Acompanhe a barra de progresso** para estimar tempo restante

### ⚠️ Limitações Conhecidas
- **Dependência de Resolução**: Scripts dependem do layout e resolução da tela
- **Interface SAP**: Podem ser afetados por mudanças na interface do SAP Fiori
- **Supervisão Necessária**: Requerem monitoramento durante a execução
- **Configuração de Tela**: Funcionam melhor em monitor único com resolução padrão
- **Velocidade do Sistema**: Performance varia conforme velocidade do SAP e rede

### 🔍 Troubleshooting

**🐛 Problema: Interface não abre**
```bash
# Verificar instalação do tkinter
python -c "import tkinter; print('Tkinter OK')"
```
- **Solução**: Reinstale Python com tkinter ou instale tkinter separadamente

**🐛 Problema: Script não encontra elementos na tela**
- **Verificações**: 
  - Resolução da tela (recomendado: 1920x1080)
  - Posição e tamanho das janelas SAP
  - Zoom do navegador (100%)
- **Solução**: Ajuste o posicionamento das janelas SAP

**🐛 Problema: Execução muito rápida/lenta**
- **Solução**: Ajuste o "Tempo de Espera" na interface:
  - Sistema rápido: 1.0 - 1.5 segundos
  - Sistema lento: 2.0 - 3.0 segundos
  - Rede lenta: 3.0+ segundos

**🐛 Problema: Script para no meio da execução**
- **Diagnóstico**: Verifique o último item no log
- **Solução**: Anote o número e configure o "Índice Inicial" para retomar

**🐛 Problema: Erro de permissões**
- **Solução**: Execute como administrador ou ajuste permissões de teclado/mouse

**🐛 Problema: CTRL não funciona no "Adicionar Bloco"**
- **Verificações**:
  - Aplicação tem foco do sistema
  - Tecla CTRL não está travada
  - Não há conflitos com outros atalhos
- **Solução**: Reinicie a aplicação ou teste em ambiente limpo

## 📊 Dados Processados

O projeto processa **68+ transações S4TAX organizadas por categorias**:

### 📋 Detalhamento por Categoria

| Categoria | Qtd Itens | Descrição |
|-----------|-----------|-----------|
| **GLOBAL** | 20 itens | Configurações gerais, ambiente, comunicação, monitoramento |
| **OUTBOUND** | 15 itens | Documentos fiscais, DFE, status, conciliação |
| **NFS-e** | 14 itens | Nota Fiscal de Serviço, configurações municipais |
| **4UNITY** | 8 itens | Integrações com fornecedores, monitor, pedidos |
| **PARCEIRO** | 1 item | Integração de parceiros de negócio |
| **4SERVICE** | 4 itens | Apontamentos de serviço, relatórios de horas |
| **BANK** | 6 itens | Configurações bancárias, boletos, compensação |

### 🏷️ Exemplos de Transações Incluídas

**GLOBAL:**
- S4TAX_0001 - Configurações de ambiente
- S4TAX_0004 - Monitor de requisições ao Orbit
- S4TAX_0013 - Status do Conector
- S4TAX_CUTE - Editor de tabelas customizado

**OUTBOUND:**
- S4TAX_DFE_004 - Status de documentos fiscais
- S4TAX_DFE_007 - Envia e-mail com danfe/xml
- S4TAX_DFE_012 - Conciliação de documentos

**NFS-e:**
- S4TAX_NFSE_011 - Monitor de NFS-e
- S4TAX_NFSE_006 - Configuração Filial → Município
- S4TAX_NFSE_013 - Editor de dados para documentos NFSe

### 📈 Estimativas de Tempo

A serem calculadas.

*_Baseado em tempo de espera de 1.5s por item_

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. **Fork o projeto**
2. **Crie uma branch para sua feature**
   ```bash
   git checkout -b feature/MinhaNovaFuncionalidade
   ```
3. **Commit suas mudanças**
   ```bash
   git commit -m 'feat: Adiciona nova funcionalidade incrível'
   ```
4. **Push para a branch**
   ```bash
   git push origin feature/MinhaNovaFuncionalidade
   ```
5. **Abra um Pull Request**

### 🔄 Tipos de Contribuições Aceitas
- 🐛 **Bug fixes**: Correções de problemas identificados
- ✨ **Features**: Novas funcionalidades para a interface
- 📚 **Documentação**: Melhorias no README e comentários
- 🎨 **UI/UX**: Melhorias na interface gráfica
- ⚡ **Performance**: Otimizações de velocidade e recursos
- 🧪 **Testes**: Adição de testes automatizados

### 📝 Padrões de Commit
Use conventional commits para padronizar:
- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Mudanças na documentação
- `style:` - Formatação, não afeta funcionalidade
- `refactor:` - Refatoração de código
- `test:` - Adição ou correção de testes

## 📝 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Autores e Colaboradores

- **Lealwbs** - *Desenvolvedor * - [Lealwbs](https://github.com/Lealwbs)
  - Criação dos scripts originais de automação
  - Definição da estrutura de dados base
  - Conceitos iniciais de automação SAP

- **RenatoMAP77** - *Desenvolvedor* - [RenatoMAP77](https://github.com/RenatoMAP77)
  - Desenvolvimento da interface gráfica moderna
  - Implementação do sistema de categorias de dados
  - Refatoração e melhorias na arquitetura

### 🙏 Agradecimentos
- Equipe Seidor pelo suporte e feedback
- Comunidade Python pela documentação das bibliotecas
- Usuários que reportaram bugs e sugeriram melhorias

## 📞 Suporte e Contato

### 🆘 Para Dúvidas e Suporte
- **Email**: Entre em contato com a equipe de desenvolvimento

### 🐛 Reportar Bugs
Ao reportar bugs, inclua:
- Versão do Python e bibliotecas
- Sistema operacional
- Passos para reproduzir o problema
- Screenshots da interface (se aplicável)
- Log de erro completo

---

## 📋 Checklist de Pré-execução

Antes de executar o Fiori Automator GUI, verifique:

- [ ] Python 3.7+ instalado
- [ ] Todas as dependências instaladas (`pip install -r requirements.txt`)
- [ ] Acesso ao ambiente SAP Fiori configurado
- [ ] Nenhum outro processo interferindo com mouse/teclado

---

**⚠️ Aviso Importante**: Este projeto foi desenvolvido especificamente para automatizar processos internos do produto S4TAX da Seidor. Use com responsabilidade e **sempre teste em ambiente de desenvolvimento primeiro** antes de executar em produção.
