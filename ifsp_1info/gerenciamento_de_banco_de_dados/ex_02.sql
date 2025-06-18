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
preco real,
data_de_validade date,
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