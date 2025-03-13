# O projeto Token-Email 
foi desenvolvido como um simulador de smtp, para criação de um template para envio de emails sem utilizar css avançado

## Funcionalidades

- Geração de códigos de verificação únicos.
- Envio de e-mails com o código de verificação.
- Validação de códigos inseridos pelos usuários.
- Interface de usuário aprimorada para a inserção do código de verificação.

## Estrutura do Projeto

- **code_validator.py**: Contém a lógica para geração e validação dos códigos de verificação.
- **message.html**: Template HTML do e-mail de verificação.
- **style.css**: Estilos CSS para a interface de verificação.
- **assets/img/**: Imagens utilizadas na interface.

## Pré-requisitos

- Python 3.x
- Bibliotecas listadas no arquivo `pyproject.toml`

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/rdgr1/Token-Email.git
   cd Token-Email
   ```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## Configuração

1. Configure as credenciais de e-mail no arquivo `config.py` para permitir o envio dos códigos de verificação.

2. Personalize o template `message.html` conforme necessário para atender às necessidades do seu projeto.

## Uso

1. Execute o script principal:

   ```bash
   python code_validator.py
   ```

2. Siga as instruções na interface para inserir o e-mail, receber o código de verificação e validá-lo.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias ou correções.

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---
