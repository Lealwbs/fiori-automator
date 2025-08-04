# Fiori Automator

Automatização via scripts Python do processo de Fiorização do produto S4TAX no SAP. Este projeto contém scripts que automatizam a criação de atribuições de destino e adição de blocos no ambiente Fiori.

## 📋 Descrição

O Fiori Automator é uma solução de automação desenvolvida em Python que utiliza PyAutoGUI para automatizar tarefas repetitivas no processo de configuração do SAP Fiori. O projeto inclui scripts para:

- **Criar Atribuições de Destino**: Automatiza o cadastro de objetos semânticos, transações e configurações
- **Adicionar Blocos**: Automatiza a adição de blocos com títulos, símbolos e objetos semânticos

## 🚀 Funcionalidades

### Script 1: Criar Atribuições de Destino (`4_criar_atribuicoes_de_destino.py`)
- Automatiza o preenchimento de formulários para criar atribuições de destino
- Processa uma lista de dados contendo objetos semânticos, transações e descrições
- Suporte para retomada a partir de um índice específico
- Configuração de tempo de espera personalizável

### Script 2: Adicionar Bloco (`5_adicionar_bloco.py`)
- Automatiza a adição de blocos no sistema Fiori
- Utiliza controle manual via tecla CTRL para sincronização
- Adiciona ícones padronizados (sap-icon://settings)
- Processa a mesma base de dados do script anterior

## 🛠️ Pré-requisitos

### Dependências Python
```bash
pip install pyautogui
pip install pyperclip
pip install keyboard
```

### Versões Recomendadas
- Python 3.7+
- pyautogui 0.9.54+
- pyperclip 1.8.2+
- keyboard 0.13.5+

## 📦 Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/Lealwbs/fiori-automator.git
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

## 🎯 Como Usar

### Preparação do Ambiente SAP

1. **Acesse o SAP GUI**
2. **Navegue até a tela de "Atribuições de Destino"**
3. **Posicione o cursor no local apropriado**

### Executando o Script de Atribuições de Destino

1. **Configure o índice inicial:**
   ```python
   # No final do arquivo 4_criar_atribuicoes_de_destino.py
   preencherIniciandoEm(42)  # Substitua 42 pelo número de itens já cadastrados
   ```

2. **Execute o script:**
   ```bash
   python 4_criar_atribuicoes_de_destino.py
   ```

3. **Posicione o mouse:**
   - Coloque o mouse sobre o botão "Criar atribuição de destino"
   - O script iniciará automaticamente após 2 segundos

### Executando o Script de Adicionar Bloco

1. **Configure o índice inicial:**
   ```python
   # No final do arquivo 5_adicionar_bloco.py
   preencherIniciandoEm(0)  # Substitua pelo número de itens já processados
   ```

2. **Execute o script:**
   ```bash
   python 5_adicionar_bloco.py
   ```

3. **Controle manual:**
   - O script aguardará você pressionar a tecla CTRL para cada item
   - Pressione e solte CTRL quando estiver pronto para o próximo item

## ⚙️ Configuração

### Parâmetros Ajustáveis

**Tempo de Espera:**
```python
tempoEspera = 1  # Ajuste conforme a velocidade do seu sistema
```

**Índice Inicial:**
```python
indexInicio = 0  # Número de itens já processados para retomar execução
```

### Dados de Entrada

Os dados são definidos na lista `dados` em ambos os scripts:
```python
dados = [
    ["CODIGO_OBJETO", "/CAMINHO/TRANSACAO", "Descrição da funcionalidade"],
    # ...
]
```

## ⚠️ Precauções e Limitações

### Antes de Executar
- ✅ **Não mova o mouse** durante a execução dos scripts

### Limitações Conhecidas
- Scripts dependem da resolução e layout da tela
- Podem ser afetados por mudanças na interface do SAP
- Requerem supervisão durante a execução
- Não funcionam com múltiplos monitores sem ajustes

### Troubleshooting

**Problema: Script não encontra os elementos na tela**
- Solução: Verifique a resolução da tela e posição das janelas

**Problema: Execução muito rápida/lenta**
- Solução: Ajuste o parâmetro `tempoEspera`

**Problema: Script para no meio da execução**
- Solução: Anote o último item processado e ajuste o `indexInicio`

## 📊 Dados Processados

O projeto processa aproximadamente **50+ transações S4TAX**, incluindo:

- Configurações de ambiente e comunicação
- Monitor de requisições e documentos fiscais
- Configurações de empresas, filiais e grupos
- Funcionalidades de DFE, 4Unity e parceiros de negócio
- Ferramentas de monitoramento e relatórios

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Autores

- **Lealwbs** - *Desenvolvimento inicial* - [Lealwbs](https://github.com/Lealwbs)
- **RenatoMAP77** - *Contribuições adicionais* - [RenatoMAP77](https://github.com/RenatoMAP77)

## 📞 Suporte

Para dúvidas e suporte:
- Crie uma [Issue](https://github.com/Lealwbs/fiori-automator/issues)
- Entre em contato com a equipe de desenvolvimento

---

**Nota**: Este projeto foi desenvolvido especificamente para automatizar processos internos do produto S4TAX da Seidor. Use com responsabilidade e sempre em ambientes de teste primeiro.
