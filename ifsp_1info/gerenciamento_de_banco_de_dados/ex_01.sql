CREATE TABLE carro (
placa varchar (15),
modelo varchar (50),
marca varchar (50),
ano integer,
CONSTRAINT PK_CARRO PRIMARY KEY (placa)
);

----------------------------------------

CREATE TABLE alunos (
prontuario varchar (10),
nome varchar (50),
idade integer,
CONSTRAINT PK_ALUNO PRIMARY KEY (prontuario)
);

INSERT INTO alunos VALUES('VP3030431', 'Giovani da Costa Silva', 15),
                         ('VP3030831', 'David of the Silva Ribers ', 15),
                         ('VP30332728', 'Iago de Brito Lopes Laurêncio Plumboso', 15),
						 ('VP3030628', 'Felipe Gobato Fúnil', 15);

----------------------------------------

CREATE TABLE filmes (
codigo_filme integer,
titulo varchar (75) NOT NULL, 
genero varchar (20),
data_lancamento date,
CONSTRAINT PK_FILMES PRIMARY KEY (codigo_filme)
);
INSERT INTO filmes VALUES(1, 'Laurêncio Adventures: Em busca do minério plumboso', 'Drama familiar', '10/10/1969'),
                         (2, 'Laurêncio Adventures 2: A volta dos que não foram', 'Comédia romântica', '29/02/1960'),
						 (3, 'Laurêncio Adventures 3: O reecontro', 'Suspense', '29/02/1964'),
						 (4, 'Laurêncio Adventures 4: A Escuridão Radiante', 'Terror', '29/02/1968'),
						 (5, 'Laurêncio Adventures 5: A Pedro Filosofal', 'Ficção Científica', '29/02/1972'),
                         (6, 'Laurêncio Adventures 6: A Batalha contra os Parabólicos', 'Ação', '29/02/1976');
SELECT * FROM filmes;