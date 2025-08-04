import pyautogui as py
import pyperclip as pc
import keyboard as kb
import time

dados = [
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
    ["S4TAX_STATUS", "/S4TAX/STATUS", "Status de documentos fiscais"],
    # ["S4TAX_NFSE_001", "/S4TAX/NFSE_001", "Cadastro de categorias de nota NFS-e"],
    # ["S4TAX_NFSE_002", "/S4TAX/NFSE_002", "Valores customizados do item NFS-e"],
    # ["S4TAX_NFSE_003", "/S4TAX/NFSE_003", "Valores customizados da filial NFS-e"],
    # ["S4TAX_NFSE_004", "/S4TAX/NFSE_004", "Impostos NFS-e definidos na pricing"],
    # ["S4TAX_NFSE_005", "/S4TAX/NFSE_005", "Intervalo de numeração para RPS NFSe"],
    # ["S4TAX_NFSE_006", "/S4TAX/NFSE_006", "Configuração Filial -> Município"],
    # ["S4TAX_NFSE_007", "/S4TAX/NFSE_007", "Motivos de cancelamento NFS-e"],
    # ["S4TAX_NFSE_008", "/S4TAX/NFSE_008", "Tipos de impostos NFS-e"],
    # ["S4TAX_NFSE_009", "/S4TAX/NFSE_009", "Municípios com emissão por arquivo"],
    # ["S4TAX_NFSE_010", "/S4TAX/NFSE_010", "Configurações default NFse"],
    # ["S4TAX_NFSE_011", "/S4TAX/NFSE_011", "Monitor de NFS-e"],
    # ["S4TAX_NFSE_012", "/S4TAX/NFSE_012", "Dashboard para documentos NFS-e"],
    # ["S4TAX_NFSE_013", "/S4TAX/NFSE_013", "Editor de dados para documentos NFSe"],
    # ["S4TAX_NFSE_MONITOR", "/S4TAX/NFSE_MONITOR", "Monitor de NFS-e"],
    ["S4TAX_SUPP_001", "/S4TAX/SUPP_001", "Configurações gerais 4unity"],
    ["S4TAX_SUPP_002", "/S4TAX/SUPP_002", "Etapas documentos 4Unity"],
    ["S4TAX_SUPP_003", "/S4TAX/SUPP_003", "Editor de dados de documentos 4Unity"],
    ["S4TAX_SUPP_004", "/S4TAX/SUPP_004", "Monitor 4Unity"],
    ["S4TAX_SUPP_005", "/S4TAX/SUPP_005", "Reintegração de fornecedores"],
    ["S4TAX_SUPP_006", "/S4TAX/SUPP_006", "Cadastro tag 4Unity em massa"],
    ["S4TAX_SUPP_007", "/S4TAX/SUPP_007", "Monitor pedido de compras"],
    # ["S4TAX_SUPP_008", "/S4TAX/SUPP_008", "Carga de parceiros para integração"],
    ["S4TAX_PART_001", "/S4TAX/PART_001", "Integrar Parceiro de Negócio"],
    # ["S4TAX_4SER_001", "/S4TAX/4SER_001", "Monitor apontamentos 4Service"],
    # ["S4TAX_4SER_002", "/S4TAX/4SER_002", "Relatório de horas apontadas (CSV)"],
    # ["S4TAX_4SER_003", "/S4TAX/4SER_003", "Configurações básicas 4service"],
    # ["S4TAX_4SER_004", "/S4TAX/4SER_004", "Configurações de integração 4Service"],
    # ["S4TAX_BANK_001", "/S4TAX/BANK_001", "Configurações de contas"],
    # ["S4TAX_BANK_002", "/S4TAX/BANK_002", "Configuração geral"],
    # ["S4TAX_BANK_003", "/S4TAX/BANK_003", "Monitor de boletos bancários"],
    # ["S4TAX_BANK_004", "/S4TAX/BANK_004", "Impostos para considerar descontos"],
    # ["S4TAX_BANK_005", "/S4TAX/BANK_005", "Configurações de Emissão Automática"],
    # ["S4TAX_BANK_006", "/S4TAX/BANK_006", "Configurações de Data de Compensação"]
]

qtdeDados = len(dados)

print(qtdeDados)

def type(string):
    pc.copy(string)
    py.hotkey("ctrl", "v")

def preencherIniciandoEm(indexInicio = 0, tempoEspera = 0.7 ):

    for i in range(qtdeDados):

        if indexInicio > 0:
            indexInicio -= 1
            continue

        objeto = dados[i][0]
        transacao = dados[i][1]
        descricao = dados[i][2]

        #Fica parado até o usuário apertar e soltar a tecla CTRL
        kb.wait('ctrl')
        time.sleep(tempoEspera*2)

        py.press('tab', 1)  #Título
        py.press('del')
        type(descricao)
        time.sleep(tempoEspera)

        py.press('tab', 3)  #Símbolo
        type('sap-icon://settings')
        time.sleep(tempoEspera)

        py.press('tab', 3)  #Objeto Semântico
        type(objeto)
        py.press('enter')
        time.sleep(tempoEspera)

        py.press('tab', 1)  #Ação
        type('display')
        py.press('enter')
        time.sleep(tempoEspera)

        py.press('tab', 6)  #Gravar
        time.sleep(tempoEspera / 2)
        py.press('enter')
        time.sleep(tempoEspera * 7)

        print(f"{i} | {objeto} - {descricao} bloco foi adicionado.")


def main():
    #OBS: É neessário estar em "Atribuições de Destino"
    # E deixar o mouse em cima do "Criar atribuição de destino"
    time.sleep(2)

    # indexInicio: colocar quantos itens já foram cadastrados
    # Isso mostra ali em cima nas bolinhas Blocos 0 Blocos 0 Atribuições... n
    # Tome cuidado que parece que esse n é 1 a menos da quantidade de itens que tem
    # Ou seja, por exemplo, se tiver aparecendo "28", quer dizer que já tem 29 itens cadastrados
    # Assim o indexInicio deve ser 29, pois já foram cadastrados 29 itens.
    preencherIniciandoEm(0)


main()