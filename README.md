Automação de Processos com Python e PyAutoGUI
Este script Python demonstra uma automação de processos simples usando a biblioteca PyAutoGUI. A automação envolve abrir um software específico, escrever uma mensagem predefinida e salvar um arquivo com um carimbo de data e hora.

Requisitos
Python 3.x
PyAutoGUI
Módulo de configuração (importado como SLEEP_TIMES de config)

Certifique-se de ter o Python instalado em sua máquina. Instale as bibliotecas necessárias listadas em requirements.txt

*Configuração
Ajuste o dicionário SLEEP_TIMES no arquivo config.py para personalizar as durações de espera entre as ações.

*Explicação do Script
O script é estruturado como uma classe Python chamada ProcessAutomation. Aqui está uma explicação de suas funcionalidades:

*Inicialização
PyAutoGUI é configurado para habilitar a funcionalidade failsafe.
Uma mensagem para sucesso na automação é definida.
O diretório do projeto e as configurações de logging são inicializados.
*Abrir Software
O método open_soft abre o software especificado usando o atalho 'Win + R' e digita o nome do software.
*Escrever Mensagem
O método write_message escreve uma mensagem predefinida na janela do software.
*Verificar e Modificar Nome do Arquivo
O método check_and_modify_file_name verifica se um nome de arquivo já existe no diretório do projeto. Se existir, um número é anexado ao nome do arquivo.
*Salvar Arquivo
O método save_arquive salva um arquivo com um carimbo de data e hora. Ele verifica a existência de arquivos, modifica o nome do arquivo se necessário e salva o arquivo no diretório especificado ou padrão.
*Automação de Processo
O método process_automation orquestra todo o processo de automação.
*Uso no Bloco Principal
Uma instância de ProcessAutomation é criada, e o processo de automação é iniciado para a aplicação Notepad.
*Personalização
Sinta-se à vontade para personalizar as durações de espera e outras configurações no arquivo config.py e adaptar o script para diferentes softwares ou tarefas de automação.




