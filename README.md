# teste-dev-jr-serasa

O código deste repositório foi desenvolvido para o processo seletivo de uma vaga de Desenvolvedora Python Jr. na Serasa Experian. O objetivo foi desenvolver, usando orientação a objetos e as bibliotecas BeautifulSoup e Selenium, uma automação que:
- abra o site https://finance.yahoo.com/screener/new, 
- adicione o filtro para a região recebida como parâmetro, 
- clique para gerar o resultado da busca pelas ações,
- extraia as informações "Symbol", "Name", e "Price (Intraday)" para cada ação 
- e armazene-as em um arquivo csv, que contenha uma linha para cada ação.

Para executar o código, siga os seguintes passos: 

1. Certifique-se que possui Python e pip instalados na sua máquina.

2. Clone o repositório usando o comando 
```bash
    git clone https://github.com/thaislauriano31/teste-dev-jr-serasa.git
```

3. Entre na pasta em que clonou o repositório e depois na pasta code.
```bash
    cd teste-dev-jr-serasa/code
```

4. Execute o comando a seguir para instalar as bibliotecas necessárias
```bash
    pip install -r requirements.txt no terminal
```

5. Execute o código com o comando 
```bash
py main.py 
```
(no lugar do comando acima, pode ser que precise digitar ***python main.py*** ou ***python3 main.py***, a depender das configurações do Python na sua máquina). Se estiver com o código aberto no VScode, apertar o botão de play no canto superior direito da janela também deve funcionar.

6. Uma mensagem aparecerá no terminal perguntando qual região deseja usar como filtro, digite o nome da região desejada como aparece nas opções do site.

7. Assim que a execução for finaliada, verifique se o arquivo csv com as informações das ações da região escolhida foi criado na pasta ***stock_files***.
