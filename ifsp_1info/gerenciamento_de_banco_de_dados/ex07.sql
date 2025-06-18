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