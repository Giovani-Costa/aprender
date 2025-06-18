DROP TABLE alunos_2;
CREATE TABLE alunos (
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