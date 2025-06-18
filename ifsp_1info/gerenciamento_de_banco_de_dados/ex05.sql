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