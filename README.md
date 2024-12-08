
# Instruções para Utilização do Sistema

## 1. Clonar o Repositório do GitHub
Abra o terminal e execute o comando:  
```bash
git clone https://github.com/viniciusmpaiva/FutSteps.git
```  

## 2. Certifique-se de ter o Python Instalado
Garanta que o **Python** está instalado em sua máquina e que a versão corresponde à indicada no projeto.  

- **Se estiver em um ambiente Linux**, execute os comandos abaixo para instalar o Python:  
  ```bash
  sudo apt update
  sudo apt install python3 python3-venv python3-pip -y
  ```
  
- **Se estiver em um ambiente Windows**:  
  - Acesse o site oficial: [python.org/downloads](https://www.python.org/downloads).  
  - Baixe e instale o Python.  
  - **Lembre-se de marcar a opção "Add Python to PATH" durante a instalação.**

## 3. Instale o Gerenciador de Pacotes (pip)
- Em **Linux**, o pip geralmente já está incluído. Caso precise instalá-lo:  
  ```bash
  sudo apt install python3-pip -y
  ```  
- Em **Windows**, caso não esteja instalado, rode:  
  ```cmd
  python -m ensurepip --upgrade
  ```

## 4. Configurar o Ambiente Virtual
Após clonar o repositório e confirmar a instalação do Python, crie e ative o ambiente virtual:  

- **No Linux**:  
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

- **No Windows**:  
  ```cmd
  python -m venv .venv
  .venv\Scripts\activate
  ```

## 5. Instalar Dependências
No ambiente virtual ativo, instale a biblioteca **Psycopg2**:  
```bash
pip install psycopg2
```  
Verifique a instalação com:  
```bash
pip freeze
```

## 6. Conectar ao Banco de Dados PostgreSQL
Certifique-se de ter o software **pgAdmin** ou outra ferramenta de gerenciamento PostgreSQL instalada. Use os dados abaixo para configurar a conexão:  

- **Host**: `dbfutsteps.c1usiq2ee7fg.sa-east-1.rds.amazonaws.com`  
- **Porta**: `5432`  
- **Nome do Banco de Dados**: `futStepsDB`  
- **Usuário**: `futsteps`  
- **Senha**: `futsteps`  

## 7. Iniciar o Programa
Após configurar o banco de dados, execute o comando para iniciar o programa:  

- **No Linux**:  
  ```bash
  python3 Main.py
  ```  

- **No Windows**:  
  ```cmd
  python Main.py
  ```

Pronto! O sistema estará em funcionamento.
