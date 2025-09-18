# Vitrine

Desenvolvedores do Sistema:
- Cecília Elen Dourado Teixeira (20221GBI23I0021);
- Natan Felipe dos Santos Silva (20221GBI23I0068),
- Italo de Oliveira Ribeiro (20221GBI23I0077)

Turma: 3BII 
(TA’s 2024)

# O que é? Qual é seu objetivo?

Um sistema de catálogo virtual projetado para otimizar as vendas online de pequenos e médios comércios, facilitando a exposição de produtos para clientes na internet.
Muitos comércios, especialmente os de menor porte, ainda não possuem um catálogo virtual. Isso cria um desafio para os vendedores, que acabam tendo dificuldades para mostrar todas as mercadorias disponíveis para a clientela online. Esse processo manual pode gerar desentendimentos, atrasos na comunicação e, consequentemente, a perda de vendas.

# Como Executar Localmente
1. Pré-requisitos
Antes de começar, você precisa ter dois programas instalados.
Python 3.8 (ou superior): A linguagem em que o projeto foi construído.
Download em: python.org
(Importante para Windows): Durante a instalação, marque a caixa "Add Python to PATH".
Git: A ferramenta que vamos usar para baixar o projeto do GitHub.
Download em: git-scm.com
Durante a instalação, pode apenas clicar em "Next" em todas as telas.

2. Instruções
   
1- Abra o terminal do seu computador para digitar os comandos abaixo.
(No Windows, procure por "Prompt de Comando" ou "PowerShell". No macOS ou Linux, procure por "Terminal").
Clone o Repositório
Este comando baixa uma cópia do projeto para o seu computador.
 git clone https://github.com/cecilia-elen/TrabalhoPsw.git

2. Entre na Pasta do Projeto (Passo Essencial!)
Você precisa entrar na pasta que acabou de ser criada antes de continuar.
cd TrabalhoPsw


3. Crie e Ative o Ambiente Virtual
Isso cria uma "caixa" segura para as dependências do projeto.


- Cria o ambiente

 python -m venv venv
 
- Ativa o ambiente (use o comando para o seu sistema)

No Windows:

.\venv\Scripts\activate

No macOS ou Linux:

source venv/bin/activate

4. Instale as Dependências
Este comando instala o Django e tudo mais que o projeto precisa.
  pip install -r requirements.txt
  
5. Prepare o Banco de Dados
Este comando cria as tabelas do sistema.
 python manage.py migrate
 
6. Inicie o Servidor
Agora, vamos colocar o sistema para funcionar!
python manage.py runserver

7. Acesse o Projeto
Após o último comando, copie o link que aparece no terminal 


# Perfis pré-feitos no sistema (usernames):

administrador (com permissões especiais de gerenciar o sistema);

Ceci (dona de Atelier)

Natan (dono de uma concessionária)

Ítalo (dono de uma loja de eletrônicos)


#IMPORTANTE A senha é igual para todos os usuários povoados: projetopsw

