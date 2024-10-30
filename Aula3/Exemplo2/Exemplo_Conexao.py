from sqlalchemy import create_engine, text

# VARIÁVEIS DE CONEXÃO COM O BANCO
host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_produtos'

#FUNÇÃO PARA CONECTAR AO BANCO
def conecta_banco():
    try:
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
        with engine.connect() as conexao:
            query = "SELECT * FROM vendas"
            resultados = conexao.execute(text(query))
            for item in resultados:
                print(f'Produto: {item[0]}, Categoria: {item[1]}, Loja: {item[2]}, Valor: {item[3]}, Quantidade: {item[4]}')

    except ImportError as e:
        print(f'Erro: {e}')

#CHAMA FUNÇÃO QUE CONECTA AO BANCO DE DADOS
conecta_banco()