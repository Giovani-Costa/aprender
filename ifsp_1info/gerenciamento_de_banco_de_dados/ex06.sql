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