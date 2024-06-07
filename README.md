# GSPYTHON
# RMS
Vinicius Issa Gois Rm 553814
Vinicius Caetano Rm552904
Gustavo Manganelli Felex rm554242
# Projeto do AquaClean

## Introdução
Este projeto visa desenvolver um protótipo funcional de um sistema de monitoramento da saúde dos oceanos e redução da poluição marinha, utilizando Python. O sistema captura dados simulados sobre poluição marinha, processa esses dados para gerar estatísticas básicas e apresenta as informações de forma clara. Além disso, o sistema salva os dados processados em um arquivo para análise futura.

## Motivação
A poluição da água é um problema crescente que ameaça a saúde dos oceanos e dos ecossistemas marinhos. Plásticos, produtos químicos tóxicos e o aumento da temperatura da água estão contribuindo negativamente para a qualidade da água e, consequentemente, afetando a vida marinha e os seres humanos que dependem desses recursos. Monitorar a saúde dos oceanos é crucial para entender a extensão da poluição e tomar medidas eficazes para mitigá-la.

## Problema
Atualmente, a falta de sistemas eficientes e acessíveis para monitorar a poluição marinha dificulta a obtenção de dados precisos e em tempo real. Isso resulta em uma resposta tardia e ineficaz às ameaças ambientais. Portanto, há uma necessidade urgente de desenvolver um sistema que possa capturar, processar e apresentar dados de poluição marinha de maneira eficiente.

## Descrição da Solução
O projeto propõe o desenvolvimento de um sistema que:
- Simula a coleta de dados de poluição marinha.
- Processa esses dados para calcular estatísticas importantes.
- Apresenta as estatísticas de maneira legível.
- Salva os dados processados em um arquivo JSON.
- Lida com erros de maneira robusta.

## Funcionalidades Implementadas
1. **Captura de Dados:** Utilização de listas e dicionários para armazenar dados simulados e funções para encapsular a lógica de captura de dados.
2. **Processamento de Dados:** Cálculo de médias, máximos e mínimos utilizando estruturas de controle (loops e condicionais). Manipulação de listas e dicionários para extrair e processar dados.
3. **Apresentação de Dados:** Formatação e exibição de resultados no console. Função dedicada para imprimir as estatísticas de maneira organizada.
4. **Salvamento de Dados:** Escrita de dados processados em um arquivo JSON. Manipulação de arquivos (abertura, escrita e fechamento de arquivos).
5. **Tratamento de Exceções:** Implementação de blocos try-except para captura e tratamento de erros.

## Instruções de Uso

### Requisitos
- Python 3.x

### Dependências
- Nenhuma dependência externa é necessária além do Python padrão.

### Como Executar
1. Clone este repositório para sua máquina local.
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <NOME_DO_REPOSITORIO>
    ```
2. Execute o script principal `main.py`.
    ```bash
    python main.py
    ```
3. O script irá capturar dados simulados, processá-los e exibir as estatísticas no console.
4. Verifique o arquivo `estatisticas.json` para os dados processados salvos.

### main.py
Contém o código principal do sistema, incluindo:
- Captura de dados simulados.
- Processamento de dados para calcular estatísticas.
- Apresentação de dados no console.
- Salvamento de dados processados em um arquivo JSON.
- Tratamento de exceções.

### estatisticas.json
Arquivo gerado pelo script contendo os dados processados.

## Estrutura do Projeto
/projeto-monitoramento-oceanos
│-- main.py
│-- estatisticas.json (gerado após a execução do script)
│-- README.md
## Melhorias e Próximos Passos
- Integração com APIs reais de monitoramento marinho para coleta de dados em tempo real.
- Desenvolvimento de uma interface gráfica para visualização dos dados.
- Implementação de métodos avançados de análise de dados para prever tendências de poluição.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.
