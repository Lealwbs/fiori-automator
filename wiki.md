## 1. Introdução
**Objetivo:** Permitir que nossos programas ABAP personalizados (programas Z) sejam acessados diretamente pelo Fiori Launchpad, proporcionando uma experiência de usuário moderna e intuitiva.


A seguir, um passo a passo detalhado para integrar nossos programas ao Fiori.
<br>


## 2. Criar Objeto Semântico

**2.a)** Insira a transação `SPRO`, execute a opção *Definir objetos semânticos para navegação*, que pode ser acessado diretamente pela transação `/n/UI2/SEMOBJ`, ou encontrado pelo caminho de navegação abaixo:
```
SAP NetWeaver / Plataforma ABAP
└─Tecnologias UI 
  └─SAP Fiori 
    └─Instalação do conteúdo Launchpad  
      └─Instalação dos catálogos técnicos
```

![objeto_semantico.png](/seidorimagens/seidor4taxcloud/conector/objeto_semantico.png)
<br>

**2.b)** Clique no botão <kbd>Entradas Novas</kbd> para criar os objetos semânticos `S4TAX_*`. Siga o exemplo abaixo:

![entradas_novas.png](/seidorimagens/seidor4taxcloud/conector/entradas_novas.png)
<br>

**Observação:**  
Se você possuir planilhas contendo todos os dados (como as exibidas abaixo, separadas por grupo), é possível copiá-las e colá-las de uma só vez, sem a necessidade de inserir item por item manualmente. Essa prática torna o processo mais ágil e eficiente, especialmente quando há muitos objetos semânticos envolvidos.

Antes de copiar, verifique se os objetos listados em cada grupo atendem às suas necessidades. Caso precise realizar ajustes, copie a tabela correspondente para uma planilha local, edite conforme necessário (adicionando, removendo ou modificando objetos), e só então cole os dados finais no "Objetos Semânticos - visão do cliente" do ambiente do cliente.

<br>

<h3> 🌐 Global – Menu de transações modulares </h3>

| Objeto semântico | Nome objeto semântico                | Descrição objeto semântico           |
| ---------------- | ------------------------------------ | ------------------------------------ |
| S4TAX_0001       | Configurações de ambiente            | Configurações de ambiente            |
| S4TAX_0002       | Configurações de comunicação         | Configurações de comunicação         |
| S4TAX_0003       | Habilitar tipo de documento fiscal   | Habilitar tipo de documento fiscal   |
| S4TAX_0004       | Monitor de requisições ao Orbit      | Monitor de requisições ao Orbit      |
| S4TAX_0005       | Cadastro de Grupos SAP <-> Orbit     | Cadastro de Grupos SAP <-> Orbit     |
| S4TAX_0006       | Cadastro de Empresas SAP <-> Orbit   | Cadastro de Empresas SAP <-> Orbit   |
| S4TAX_0007       | Cadastro de Filiais SAP <-> Orbit    | Cadastro de Filiais SAP <-> Orbit    |
| S4TAX_0008       | Versionamento de Produtos            | Versionamento de Produtos            |
| S4TAX_0009       | Lista de transações por módulos 4Tax | Lista de transações por módulos 4Tax |
| S4TAX_0010       | Tarefas de Instalação                | Tarefas de Instalação                |
| S4TAX_0011       | Exibição de várias tabelas           | Exibição de várias tabelas           |
| S4TAX_0012       | Lista de jobs do produto             | Lista de jobs do produto             |
| S4TAX_0013       | Status do Conector                   | Status do Conector                   |
| S4TAX_0014       | Editor tabelas via CSV               | Editor tabelas via CSV               |
| S4TAX_0015       | Configurações de envio de erros      | Configurações de envio de erros      |
| S4TAX_0016       | Configurações tabelas CUTE           | Configurações tabelas CUTE           |
| S4TAX_0017       | Configurações campos CUTE            | Configurações campos CUTE            |
| S4TAX_CUTE       | Editor de tabelas customizado        | Editor de tabelas customizado        |
| S4TAX_MB_001     | Relatório de documentos              | Relatório de documentos              |
| S4TAX_MENU       | Lista de transações por módulos 4Tax | Lista de transações por módulos 4Tax |
| S4TAX_TASKS      | Tarefas de instalação                | Tarefas de instalação                |

<br>
<h3> 📤 Outbound – Menu outbound </h3>

| Objeto semântico  | Nome objeto semântico                | Descrição objeto semântico           |
| ----------------- | ------------------------------------ | ------------------------------------ |
| S4TAX_CCE\_PRINT  | Impressão de carta de correção dfe's | Impressão de carta de correção dfe's |
| S4TAX_DFE\_001    | Configuração de e-mail para DFE's    | Configuração de e-mail para DFE's    |
| S4TAX_DFE\_002    | Configurações gerais DF-e            | Configurações gerais DF-e            |
| S4TAX_DFE\_003    | Gerador de cópias de dfe's           | Gerador de cópias de dfe's           |
| S4TAX_DFE\_004    | Status de documentos fiscais         | Status de documentos fiscais         |
| S4TAX_DFE\_005    | Download de dfe's em massa Remoto    | Download de dfe's em massa Remoto    |
| S4TAX_DFE\_006    | Gerador de dfe's mockadas            | Gerador de dfe's mockadas            |
| S4TAX_DFE\_007    | Envia e-mail com danfe/xml           | Envia e-mail com danfe/xml           |
| S4TAX_DFE\_008    | Programa para simular emissões       | Programa para simular emissões       |
| S4TAX_DFE\_009    | Configuração modelos e-mail DFE      | Configuração modelos e-mail DFE      |
| S4TAX_DFE\_010    | Carga dos XMLs do SAP GRC NFe        | Carga dos XMLs do SAP GRC NFe        |
| S4TAX_DFE\_011    | Download de dfe's em massa local     | Download de dfe's em massa local     |
| S4TAX_DFE\_012    | Conciliação de documentos            | Conciliação de documentos            |
| S4TAX_DFE\_013    | URL base do serviço de consulta      | URL base do serviço de consulta      |
| S4TAX_DFE\_014    | Configurações Reforma Tributária     | Configurações Reforma Tributária     |
| S4TAX_STATUS      | Status de documentos fiscais         | Status de documentos fiscais         |

<br>
<h3> 🧾 NFS-e – Menu NFSe </h3>

| Objeto semântico     | Nome objeto semântico                | Descrição objeto semântico           |
| -------------------- | ------------------------------------ | ------------------------------------ |
| S4TAX_NFSE\_001      | Cadastro de categorias de nota NFS-e | Cadastro de categorias de nota NFS-e |
| S4TAX_NFSE\_002      | Valores customizados do item NFS-e   | Valores customizados do item NFS-e   |
| S4TAX_NFSE\_003      | Valores customizados da filial NFS-e | Valores customizados da filial NFS-e |
| S4TAX_NFSE\_004      | Impostos NFS-e definidos na pricing  | Impostos NFS-e definidos na pricing  |
| S4TAX_NFSE\_005      | Intervalo de numeração para RPS NFSe | Intervalo de numeração para RPS NFSe |
| S4TAX_NFSE\_006      | Configuração Filial -> Município     | Configuração Filial -> Município     |
| S4TAX_NFSE\_007      | Motivos de cancelamento NFS-e        | Motivos de cancelamento NFS-e        |
| S4TAX_NFSE\_008      | Tipos de impostos NFS-e              | Tipos de impostos NFS-e              |
| S4TAX_NFSE\_009      | Municípios com emissão por arquivo   | Municípios com emissão por arquivo   |
| S4TAX_NFSE\_010      | Configurações default NFse           | Configurações default NFse           |
| S4TAX_NFSE\_011      | Monitor de NFS-e                     | Monitor de NFS-e                     |
| S4TAX_NFSE\_012      | Dashboard para documentos NFS-e      | Dashboard para documentos NFS-e      |
| S4TAX_NFSE\_013      | Editor de dados para documentos NFSe | Editor de dados para documentos NFSe |
| S4TAX_NFSE\_MONITOR  | Monitor de NFS-e                     | Monitor de NFS-e                     |

<br>
<h3> 🧑‍💼 Portal de Fornecedores – Menu Partner Portal </h3>

| Objeto semântico | Nome objeto semântico                | Descrição objeto semântico           |
| ---------------- | ------------------------------------ | ------------------------------------ |
| S4TAX_SUPP\_001  | Configurações gerais 4unity          | Configurações gerais 4unity          |
| S4TAX_SUPP\_002  | Etapas documentos 4Unity             | Etapas documentos 4Unity             |
| S4TAX_SUPP\_003  | Editor de dados de documentos 4Unity | Editor de dados de documentos 4Unity |
| S4TAX_SUPP\_004  | Monitor 4Unity                       | Monitor 4Unity                       |
| S4TAX_SUPP\_005  | Reintegração de fornecedores         | Reintegração de fornecedores         |
| S4TAX_SUPP\_006  | Cadastro tag 4Unity em massa         | Cadastro tag 4Unity em massa         |
| S4TAX_SUPP\_007  | Monitor pedido de compras            | Monitor pedido de compras            |
| S4TAX_SUPP\_008  | Carga de parceiros para integração   | Carga de parceiros para integração   |
| S4TAX_SUPP\_009  | Configuração tipos pedido de compra  | Configuração tipos pedido de compra  |

<br>
<h3> 🧍 Parceiro de Negócios – Menu Parceiro de Negócios </h3>

| Objeto semântico | Nome objeto semântico        | Descrição objeto semântico   |
| ---------------- | ---------------------------- | ---------------------------- |
| S4TAX_PART\_001  | Integrar Parceiro de Negócio | Integrar Parceiro de Negócio |
| S4TAX_PART\_002  | Monitor de parceiros         | Monitor de parceiros         |
| S4TAX_PART\_003  | Configurações de parceiro    | Configurações de parceiro    |


<br>
<h3> 🛠️ Serviços – Menu de Serviços </h3>

| Objeto semântico | Nome objeto semântico                | Descrição objeto semântico           |
| ---------------- | ------------------------------------ | ------------------------------------ |
| S4TAX_4SER\_001  | Monitor apontamentos 4Service        | Monitor apontamentos 4Service        |
| S4TAX_4SER\_002  | Relatório de horas apontadas (CSV)   | Relatório de horas apontadas (CSV)   |
| S4TAX_4SER\_003  | Configurações básicas 4service       | Configurações básicas 4service       |
| S4TAX_4SER\_004  | Configurações de integração 4Service | Configurações de integração 4Service |

<br>
<h3> 🏦 Bank – Menu integração bancária </h3>

| Objeto semântico | Nome objeto semântico                | Descrição objeto semântico           |
| ---------------- | ------------------------------------ | ------------------------------------ |
| S4TAX_BANK\_001  | Configurações de contas              | Configurações de contas              |
| S4TAX_BANK\_002  | Configuração geral                   | Configuração geral                   |
| S4TAX_BANK\_003  | Monitor de boletos bancários         | Monitor de boletos bancários         |
| S4TAX_BANK\_004  | Impostos para considerar descontos   | Impostos para considerar descontos   |
| S4TAX_BANK\_005  | Configurações de Emissão Automática  | Configurações de Emissão Automática  |
| S4TAX_BANK\_006  | Configurações de Data de Compensação | Configurações de Data de Compensação |



<br>

**2.c)** Ao final da atualização, será necessário salvar as alterações em uma **Request de Workbench**.

<br><br>


## 3. Criar Catálogo
> Não será possível acessar o *SAP Fiori Launchpad Designer* se você estiver acessando o servidor SAP **via router**. Neste caso, peça  **o acesso via VPN** ao colaborador responsável.
{.is-warning}

**3.a)** Escolha *SAP Fiori Launchpad Designer (específico/dependente de mandante)*, que pode ser acessado diretamente pela transação `/n/UI2/FLPD_CUST` ou ser encontrado pelo caminho de navegação abaixo: 
```
SAP NetWeaver / Plataforma ABAP
└─Tecnologias IU
  └─SAP Fiori
    └─Instalação do conteúdo Launchpad
      └─Instalação dos catálogos técnicos
        └─Atualização dos catálogos técnicos, 
          criados com SAP Fiori Launchpad Designer
```

![catalogo1.png](/seidorimagens/seidor4taxcloud/conector/catalogo1.png)
<br>

**3.b)** Clique no ícone <kbd>+</kbd> na parte inferior-esquerda da tela para criar um novo catálogo.

![catalogo2.png](/seidorimagens/seidor4taxcloud/conector/catalogo2.png)
<br>

**3.c)** Insira os `Título` e `ID` do catálogo conforme mostrado abaixo e clique em <kbd>Gravar</kbd>.

![catalogo3.png](/seidorimagens/seidor4taxcloud/conector/catalogo3.png)
<br>

**3.d)** Nesse momento, será necessária a criação de uma **Request de Customizing**. Crie a request pela transação `SE09` / `SE10` no SAP.

Em seguida, clique no botão <kbd>⚙</kbd> do canto superior-direito, desmarque a opção `Sem (objeto local)`. Selecione a Request de Customizing e pressione <kbd>Ok</kbd>:

![catalogo4.png](/seidorimagens/seidor4taxcloud/conector/catalogo4.png)
<br><br>


## 4. Criar Atribuições de Destino

**4.a)** Clique no ícone <kbd>Atribuições de Destino</kbd> da parte superior da tela e, em seguida, clique no botão <kbd>Criar atribuição de destino</kbd> da parte inferior da tela.

![atribuicao1.png](/seidorimagens/seidor4taxcloud/conector/atribuicao1.png)
<br>

**4.b)** Na tela de configuração da atribuição, preencha os seguintes campos:

| Campo              | Valor                           |
|--------------------|---------------------------------|
| **Objeto Semântico**  | Nome do objeto criado anteriormente no SAP |
| **Ação**              | `display`                    |
| **Tipo de Aplicação** | `Transação`                  |
| **Título**            | Título descritivo do objeto  |
| **Transação**         | Código de transação `/S4TAX/*` correspondente|

Após preencher todos os campos, clique no botão <kbd>Gravar</kbd> localizado na parte inferior da tela para salvar as configurações.

![atribuicao2.png](/seidorimagens/seidor4taxcloud/conector/atribuicao2.png)
<br><br>


## 5. Adicionar Bloco

**5.a)** Escolha o ícone <kbd>Blocos</kbd> e clique no ícone <kbd>+</kbd> para adicionar um bloco.

![bloco1.png](/seidorimagens/seidor4taxcloud/conector/bloco1.png)
<br>

**5.b)** Na próxima tela, dentre as opções disponíveis de modelos de bloco, escolha a *App Launcher – Static*.

![bloco2.png](/seidorimagens/seidor4taxcloud/conector/bloco2.png)
<br>

**5.c)** Insira os seguintes detalhes: `Título`, `Símbolo`, `Objeto Semântico` e `Ação`, e clique em <kbd>Gravar</kbd>.

![bloco3.png](/seidorimagens/seidor4taxcloud/conector/bloco3.png)
<br><br>


## 6. Criar grupo e atribuir bloco ao grupo

**6.a)** Para criar um novo grupo, vá na barra de ferramentas superior e clique em <kbd>Grupos</kbd>. Em seguida, clique no ícone <kbd>+</kbd> da parte inferior-esquerda da tela.

![bloco1.png](/seidorimagens/seidor4taxcloud/conector/grupo1.png)
<br>

**6.b)** Na janela *pop-up*, digite os `Título` e `ID` do grupo, e clique no botão <kbd>Gravar</kbd>.

![bloco1.png](/seidorimagens/seidor4taxcloud/conector/grupo2.png)
<br>

**6.c)** Na próxima tela, clique no ícone <kbd>Add Bloco</kbd> para atribuir o bloco ao Grupo, conforme imagem abaixo:

![bloco1.png](/seidorimagens/seidor4taxcloud/conector/grupo3.png)
<br>

**6.d)** Clique no ícone <kbd>+</kbd> para adicionar o bloco recém-criado ao grupo.
<br>

**OBS:** A princípio, todos os blocos devem ser atribuidos aos seus respectivos grupos que serão criados (NFE, NFSE, PORTAL, etc...). Alguns blocos abaixos são mais utilizados, favor validar se eles estão presentes e **funcionando**:

![imagem_2025-07-28_093035462.png](/seidorimagens/imagem_2025-07-28_093035462.png)

<br><br>

## 7. Criar função e adicionar autorizações

**7.a)** No código de transação `PFCG`, digite o nome da função customizada a ser criada, exemplo `ZR_TESTE` e clique no botão <kbd>Criar Função</kbd>:

![funcao1.png](/seidorimagens/seidor4taxcloud/conector/funcao1.png)
<br>

**7.b)** Digite a `Descrição` para a função, clique na aba <kbd>Menu</kbd>.

![funcao1.png](/seidorimagens/seidor4taxcloud/conector/funcao2.png)
<br>

**7.c)** Selecione <kbd>Sim</kbd> na janela pop-up que aparece a seguir.

**7.d)** Em `Transação`, escolha *SAP Fiori Lauchpad ➞ Catalago de Lauchpad*.

![funcao1.png](/seidorimagens/seidor4taxcloud/conector/funcao3.png)
<br>

**7.e)** Na janela pop-up, escolha o ID do catálogo `/S4TAX/`.

![funcao_corre.png](/seidorimagens/seidor4taxcloud/conector/funcao_corre.png)
<br>

**7.f)** Em `Transação`, escolha *SAP Fiori Lauchpad ➞ Grupo de Lauchpads*.

![funcao1.png](/seidorimagens/seidor4taxcloud/conector/funcao5.png)
<br>

**7.g)** Na janela pop-up, escolha o ID do grupo `/S4TAX/*`.

![funcao1.png](/seidorimagens/seidor4taxcloud/conector/funcao6.png)
<br>

**7.h)** Por último, clique na aba <kbd>Usuário</kbd> na barra de menu, insira o `ID` do usuário e salve suas alterações.

![funcao7.png](/seidorimagens/seidor4taxcloud/conector/funcao7.png)
<br><br>


## 8. Apêndices

### Apêndice A: Arquivo Host (VTD, VTQ e VTP)

Será necessário configurar o arquivo de hosts para acessar o FIORI no VTD, VTQ e VTP. Adicionar as seguintes linhas no arquivo:

![host1.png](/seidorimagens/seidor4taxcloud/conector/host1.png)

E adicionar a seguintes linhas ao arquivo:

```
#SEIDOR
192.168.225.52 srvseidor11 srvseidor11.veritasti.local
192.168.225.26 srvseidor13 srvseidor13.veritasti.local
192.168.225.55 srvseidor10 srvseidor10.veritasti.local
```
<br><br>


### Apêndice B: Acesse o Programa Personalizado no Fiori

1. Através do navegador acessando diretamento o Fiori Launchpad.

VTD: https://srvseidor11.veritasti.local:44300/sap/bc/ui2/flp#Shell-home
VTQ: https://srvseidor13.veritasti.local:44300/sap/bc/ui2/flp#Shell-home
VTP: https://srvseidor13.veritasti.local:44300/sap/bc/ui2/flp#Shell-home
<br>

2. Através do SAP GUI acessando pela transação "/UI2/FLP".

![monitor1.png](/seidorimagens/seidor4taxcloud/conector/monitor1.png)
