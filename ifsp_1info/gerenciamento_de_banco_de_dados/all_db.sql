CREATE TABLE carro (
placa varchar (15),
modelo varchar (50),
marca varchar (50),
ano integer,
CONSTRAINT PK_CARRO PRIMARY KEY (placa)
);

----------------------------------------

CREATE TABLE alunos_1 (
prontuario varchar (10),
nome varchar (50),
idade integer,
CONSTRAINT PK_ALUNOS_1 PRIMARY KEY (prontuario)
);

INSERT INTO alunos_1 VALUES('VP3030431', 'Giovani da Costa Silva', 15),
                         ('VP3030831', 'David of the Silva Ribers ', 15),
                         ('VP30332728', 'Iago de Brito Lopes Laurêncio Plumboso', 15),
						 ('VP3030628', 'Felipe Fúnil Gobato', 15),
						 ('VP3030857', 'Henrique Scarparo', 15);
						 
						 						 

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

----------------------------------------

CREATE TABLE pais (
nome varchar (50),
capital varchar (50),
continente varchar (50),
populacao integer,
idh real,
CONSTRAINT PK_PAIS PRIMARY KEY (nome)
);

INSERT INTO pais VALUES('Brasil', 'Brasília', 'América do Sul', 213000000, 0.765),
                       ('Estados Unidos', 'Washington', 'América do Norte', 331000000, 0.926),
                       ('Japão', 'Tóquio', 'Ásia', 125000000, 0.919),
					   ('França', 'Paris', 'Europa', 67000000, 0.901),
					   ('Canadá', 'Ottawa', 'América do Norte', 38000000, 0.929),
					   ('Índia', 'Nova Déli', 'Ásia', 1420000000, 0.645),
					   ('Alemanha', 'Berlim', 'Europa', 83000000, 0.950),
					   ('Austrália', 'Canberra', 'Oceania', 26000000, 0.948),
					   ('África do Sul', 'Pretória', 'África', 60000000, 0.705),
					   ('Suécia', 'Estocolmo', 'Europa', 10000000, 0.953);
						
SELECT * FROM pais;

----------------------------------------

CREATE TABLE animais (
animal_id integer,
nome varchar (50),
especie varchar (50),
pais_de_origem varchar (50),
CONSTRAINT PK_ANIMAIS PRIMARY KEY (animal_id)
);

INSERT INTO animais VALUES(1 , 'Onça', 'Panthera onca', 'Brasil'),
                          (2 , 'Panda Gigante', 'Ailuropoda melanoleuca', 'China'),
                       (3 , 'Canguru', 'Macropus', 'Austrália'),
					   (4 , 'Leão', 'Panthera leo', 'África'),
					   (5 , 'Tigre', 'Panthera tigris', 'Índia'),
					   (6 , 'Coala', 'Phascolarctos cinereus', 'Austrália'),
					   (7 , 'Lobo-Guará', 'Chrysocyon brachyurus', 'Brasil'),
					   (8 , 'Pinguim Imperador', 'Aptenodytes forsteri', 'Antártida'),
					   (9 , 'Elefante Africano', 'Loxodonta africana', 'Quênia'),
					   (10 , 'Búfalo Africano', 'Syncerus caffer', 'Tanzânia');
						
SELECT * FROM animais;

----------------------------------------

CREATE TABLE produtos (
produto_id integer,
nome varchar (50),
marca varchar (50),
preco real,
data_de_validade date,
CONSTRAINT PK_PRODUTOS PRIMARY KEY (produto_id)
);

INSERT INTO produtos VALUES(1 , 'Maionese', 'Hellmanns', 7.99, '22/09/2024'),
                       (2 , 'Macarrão Instantâneo', 'Nissin Lámen', 9.90, '15/06/2025'),
                       (3 , 'Suco de Laranja', 'Do Bem', 1.89, '10/11/2024'),
					   (4 , 'Iogurte Grego', 'Vigor', 6.49, '12/12/2024'),
					   (5 , 'Óleo de Soja', 'Soya', 4.89, '23/08/2025'),
					   (6 , 'Creme Dental', 'Colgate', 5.69, '05/03/2025'),
					   (7 , 'Bolacha', 'Oreo', 3.29, '30/09/2024'),
					   (8 , 'Pão de Forma', 'Pullman', 7.50, '18/05/2024'),
					   (9 , 'Achocolatado em Pó', 'Nescau', 4.29, '03/01/2025'),
					   (10 , 'Manteiga', 'Président', 11.90, '10/02/2025');
						
SELECT * FROM produtos;

----------------------------------------

CREATE TABLE alunos_2 (
prontuario varchar (10),
nome varchar (50),
idade integer,
CONSTRAINT PK_ALUNOS_2 PRIMARY KEY (prontuario)
);

INSERT INTO alunos_2 VALUES('VP3030431', 'Giovani da Costa Silva', 15),
                         ('VP3030831', 'David of the Silva Ribers', 15),
                         ('VP30332728', 'Iago de Brito Lopes Laurêncio Plumboso', 15),
						 ('VP3030628', 'Felipe Gobato Fúnil', 15),
						 ('VP3030857', 'Henrique Scarparo', 15);
DELETE FROM alunos_2 WHERE nome = 'David of the Silva Ribers';
UPDATE alunos_2 SET nome='Felipe Fúnil Gobato' WHERE nome = 'Felipe Gobato Fúnil';
SELECT * FROM alunos_2;

----------------------------------------

CREATE TABLE filme (codFilme integer NOT NULL, 
		    nome VARCHAR (50) NOT NULL, 
		    genero VARCHAR (20) NOT NULL, 
		    dtaLanc date, 
		    CONSTRAINT pk_filme PRIMARY KEY(codFilme));

INSERT INTO filme VALUES (1,'Um Sonho de Liberdade','Drama','14/10/1994');
INSERT INTO filme VALUES (2,'O Poderoso Chefão','Crime','24/03/1972');
INSERT INTO filme VALUES (3,'O Poderoso Chefão II','Crime','20/12/1974');
INSERT INTO filme VALUES (4,'Pulp Fiction - Tempo de Violência','Crime','18/02/1995');
INSERT INTO filme VALUES (5,'Três Homens em Conflito','Aventura','29/12/1967');
INSERT INTO filme VALUES (6,'12 Homens e uma Sentença','Drama','04/04/1957');
INSERT INTO filme VALUES (7,'A Lista de Schindler','Drama','17/12/1993');
INSERT INTO filme VALUES (8,'Batman - O Cavaleiro das Trevas','Ação','20/07/2008');
INSERT INTO filme VALUES (9,'O Senhor dos Anéis - O Retorno do Rei','Aventura','17/12/2003');
INSERT INTO filme VALUES (10,'Star Wars - Episódio 5 - O Império Contra Ataca','Aventura','21/05/1980');
INSERT INTO filme VALUES (11,'Clube da Luta','Drama','29/10/1999');
INSERT INTO filme VALUES (12,'Os Setes Samurais','Ação','19/11/1956');
INSERT INTO filme VALUES (13,'A Origem','Aventura','06/08/2010');
INSERT INTO filme VALUES (14,'O Senhor dos Anéis - As Duas Torres','Aventura','27/12/2002'); --ok
INSERT INTO filme VALUES (15,'Gladiador','Ação','19/05/2000');
INSERT INTO filme VALUES (16,'Uma Mente Brilhante','Drama','15/02/2002'); --ok
INSERT INTO filme VALUES (17,'Cidade de Deus','Crime','30/07/2002'); --ok
INSERT INTO filme VALUES (18,'O Auto da Compadecida','Comédia','10/09/2000');
INSERT INTO filme VALUES (19,'Titanic','Drama','16/01/1998');
INSERT INTO filme VALUES (20,'Os Infiltrados','Crime','10/11/2006'); --ok
INSERT INTO filme VALUES (21,'Onze Homens e um Segredo','Aventura','22/02/2002');
INSERT INTO filme VALUES (22,'Como Se Fosse a Primeira Vez','Comédia','30/04/2004');
INSERT INTO filme VALUES (23,'Entrando Numa Fria','Comédia','12/01/2001');
INSERT INTO filme VALUES (24,'Um Sonho Possível','Drama','19/03/2010');
INSERT INTO filme VALUES (25,'Pânico 4','Suspense','15/04/2011');
INSERT INTO filme VALUES (26,'Um Estranho no Ninho','Drama','21/11/1975');
INSERT INTO filme VALUES (27,'American Pie I','Comédia','29/10/1999');
INSERT INTO filme VALUES (28,'Entrevista com o Vampiro','Drama','11/11/1994');

INSERT INTO filme VALUES (29, 'Flow', 'Animação');
UPDATE filme SET dtaLanc='20/02/2025' WHERE codFilme = 29;
UPDATE filme SET genero='Desenho Animado' WHERE genero='Animação';
UPDATE filme SET dtaLanc='11/09/2018' WHERE codFilme = 1;
DELETE FROM filme WHERE genero='Drama';
DELETE FROM filme WHERE dtaLanc >'30/08/2017';

SELECT * FROM filme;

----------------------------------------

CREATE TABLE empregados(
	empregado_id integer PRIMARY KEY, 
	nome varchar (20) NOT NULL, 
	sobrenome varchar(20) NOT NULL, 
	idade integer, 
	salario real NOT NULL, 
	cargo varchar(30) NOT NULL);

INSERT INTO empregados VALUES (1, 'Carlos', 'Alberto', 24, 2500,' Técnico em Segurança');
INSERT INTO empregados VALUES (2, 'Pedro', 'Augusto', 32, 3500,' Analista de Sistemas');
INSERT INTO empregados VALUES (3, 'Mara', 'Antonia', 27, 1200,' Secretária');
INSERT INTO empregados VALUES (4, 'Derci', 'Gonçalves', 56, 6500,' Gerente');
INSERT INTO empregados VALUES (5, 'Pedro', 'Bueno', 28, 1500,' Estagiário');
INSERT INTO empregados VALUES (6, 'Edson', 'Arantes', 60, 7500,' Gerente');
INSERT INTO empregados VALUES (7, 'Odete', 'Roitman', 54, 2000,' Técnico em Segurança');
INSERT INTO empregados VALUES (8, 'Antonio', 'Da Lua ', 38,2500 ,'Analista de Sistemas');
INSERT INTO empregados VALUES (9, 'Sassa', 'Mutema', 55, 3000,' Vendedor');
INSERT INTO empregados VALUES (10, 'José', 'Silvério', 42, 2800,' Vendedor');
INSERT INTO empregados VALUES (11, 'Gabriel', 'Oliveira', 24, 2500,' Técnico em Segurança');
INSERT INTO empregados VALUES (12, 'Flávia', 'Camargo', 29, 4200,' Analista de Sistemas');
INSERT INTO empregados VALUES (13, 'Marina', 'Delbonis', 20, 1000,' Secretária');
INSERT INTO empregados VALUES (14, 'Paulo', 'Roberto', 33, 1500,' Vendedor');
INSERT INTO empregados VALUES (15, 'José', 'Carlos da  Silva ',27 ,2900,'Analista de Sistemas');
INSERT INTO empregados VALUES (16, 'Rúbia', 'Miranda', 29, 3500,' Administrador');
INSERT INTO empregados VALUES (17, 'Roberto', 'Andrade Silva ', 35,3300 ,'Vendedor');
INSERT INTO empregados VALUES (18, 'Ana', 'Julia', 31, 2900,' Secretária');
INSERT INTO empregados VALUES (19, 'Pedro', 'Antonio', 41, 3500,' Administrador');
INSERT INTO empregados VALUES (20, 'Ana', 'Mara', 22, 2200,' Psicóloga');
INSERT INTO empregados VALUES (21, 'João', 'Augusto', 44, 5500,' Gerente');

SELECT nome, sobrenome, salario FROM empregados;
SELECT idade, cargo FROM empregados;
SELECT sobrenome, salario FROM empregados WHERE sobrenome >= 3000

----------------------------------------

CREATE TABLE paises_02(
	nome VARCHAR (50), 
    capital VARCHAR (50) NOT NULL,
	populacao real,
	idh real, 
	continente varchar (30),
	CONSTRAINT PK_PAISES_02 PRIMARY KEY (nome));

INSERT INTO paises_02 VALUES ('Afeganistão', 'Cabul', 29.1, 0.349, 'Ásia'), ('Angola', 'Luanda', 18.4, 0.403, 'África'), ('Áustria', 'Viena', 8.2, 0.895, 'Europa');
INSERT INTO paises_02 VALUES ('Bolívia', 'La Paz', 10.9, 0.675, 'América do Sul'), ('Camarões', 'Iaundê', 19.1, 0.482, 'África'), ('Alemanha', 'Berlim', 81.76, 0.920, 'Europa');
INSERT INTO paises_02 VALUES ('Argentina', 'Buenos Aires', 40.0, 0.811, 'América do Sul'), ('Austrália', 'Camberra', 22.6, 0.938, 'Oceania'), ('Brasil', 'Brasília', 190.732, 0.730, 'América do Sul');
INSERT INTO paises_02 VALUES ('Canadá', 'Ottawa', 34.48, 0.911, 'América do Norte'), ('Chile', 'Santiago do Chile', 17.09, 0.819, 'América do Sul'), ('Coréia do Sul', 'Seul', 48.3, 0.909, 'Ásia');
INSERT INTO paises_02 VALUES ('Costa do Marfim', 'Abidjan', 20.1, 0.397, 'África'), ('Cuba', 'Havana', 11.07, 0.780, 'América Central'), ('Equador', 'Quito', 14.3, 0.724, 'América do Sul');
INSERT INTO paises_02 VALUES ('Espanha', 'Madri', 47.19, 0.885, 'Europa'), ('Estados Unidos da América', 'Washington DC', 308.745, 0.937, 'América do Norte'), ('França', 'Paris', 65.3, 0.893, 'Europa');
INSERT INTO paises_02 VALUES ('Guatemala', 'Cidade da Guatemala', 14, 0.560, 'América Central'), ('Islândia', 'Reykjavik', 0.318, 0.906, 'Europa'), ('Rússia', 'Moscou', 142.9, 0.788, 'Europa e Ásia');
INSERT INTO paises_02 VALUES ('Argélia', 'Argel', 40.400, 0.748, 'África'), ('África do Sul', 'Pretória', 57.39, 0.709, 'África'), ('Arábia Saudita', 'Riade', 33.55, 0.854, 'Ásia');
INSERT INTO paises_02 VALUES ('Bélgica', 'Bruxelas', 11.500, 0.931, 'Europa'), ('Bulgária', 'Sófia', 7.03, 0.816, 'Europa'), ('Burquina Faso', 'Uagadugu', 19.7, 0.305, 'África');
INSERT INTO paises_02 VALUES ('Cabo Verde', 'Praia', 0.553, 0.665, 'África'), ('Colômbia', 'Bogotá', 49.464, 0.767, 'América do Sul'), ('Croácia', 'Zagreb', 4.16, 0.767, 'Europa');
INSERT INTO paises_02 VALUES ('Dinamarca', 'Copenhaga', 5.75, 0.866, 'Europa'), ('Egito', 'Cairo', 99.375, 0.707, 'África'), ('Filipinas', 'Manila', 106.512, 0.718, 'Ásia');
INSERT INTO paises_02 VALUES ('China', 'Pequim', 1412, 0.788, 'Ásia'), ('Dominica', 'Roseau', 0.071, 0.717, 'América Central'), ('Escócia', 'Edimburgo ', 5.424, 0.901, 'Europa');
INSERT INTO paises_02 VALUES ('Irlanda do Norte', 'Belfast', 1.885, 0.899, 'Europa'), ('Finlândia', 'Helsinque', 5.556, 0.871, 'Europa'), ('Gana', 'Acra', 33.48, 0.467, 'Ásia');
INSERT INTO paises_02 VALUES ('Holanda', 'Amsterdã', 17.7, 0.944, 'Europa'), ('Honduras', 'Tegucigalpa', 10.43, 0.632, 'América Central'), ('Marrocos', 'Rabat', 37.46, 0.683, 'África');

SELECT nome, continente FROM paises_02;
SELECT nome, capital, idh FROM paises_02;
SELECT nome, capital, populacao FROM paises_02 WHERE populacao > 20;
SELECT nome, continente FROM paises_02 WHERE continente = 'Ásia'
SELECT nome, continente, idh FROM paises_02 WHERE idh < 0.8

----------------------------------------

CREATE TABLE carros_2(chassi varchar(20), 
		modelo VARCHAR (40) NOT NULL,
		ano integer,
		preco real,
		constraint pk_carros_2 PRIMARY KEY (chassi));

INSERT INTO carros_2 (chassi, modelo, ano, preco) VALUES ('1A1A', 'CORSA', 2011, 19900);
INSERT INTO carros_2 VALUES ('1B1B', 'FIESTA', 2012, 28000),
			 	 ('1C1C', 'FOX', 2013, 30000),
			 	 ('1D1D', 'PÁLIO', 2014, 25000),
			 	 ('1E1E', 'STRADA', 2016, 38500);
DELETE carro FROM ano = 2011;
UPDATE carro SET preco = 31000 WHERE chassi = '1C1C';			 
SELECT modelo, preco FROM carros_2 WHERE preco < 25000;