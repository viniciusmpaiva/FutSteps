
-- TABELA CLUBE
INSERT INTO clube VALUES ('12.345.678/0001-01', 'Clube Esportivo Central');
INSERT INTO clube VALUES ('23.456.789/0002-02', 'Associação Atlética Sul');
INSERT INTO clube VALUES ('34.567.890/0003-03', 'Futebol Clube Norte');
INSERT INTO clube VALUES ('45.678.901/0004-04', 'Esporte Clube Oeste');
INSERT INTO clube VALUES ('12.345.678/0001-00', 'Palmeiras');


INSERT INTO responsavel VALUES ('123.456.789-01', 'Carlos Silva', '1975-04-10');
INSERT INTO responsavel VALUES ('234.567.890-12', 'Maria Oliveira', '1980-09-15');
INSERT INTO responsavel VALUES ('345.678.901-23', 'João Pereira', '1990-01-20');
INSERT INTO responsavel VALUES ('456.789.012-34', 'Ana Costa', '1985-06-25');
INSERT INTO responsavel VALUES ('525.018.648-32', 'Vanderlei', '2000-06-09');
INSERT INTO responsavel VALUES ('567.890.123-45', 'Roberto Andrade', '1970-12-05');
INSERT INTO responsavel VALUES ('678.901.234-56', 'Cláudia Nunes', '1978-08-30');
INSERT INTO responsavel VALUES ('789.012.345-67', 'Sérgio Almeida', '1982-03-18');
INSERT INTO responsavel VALUES ('890.123.456-78', 'Fernanda Lopes', '1975-11-22');
INSERT INTO responsavel VALUES ('901.234.567-79', 'Patrícia Santos', '1987-07-10');


-- TABELA ATLETA

INSERT INTO atleta VALUES ('123.456.789-02', 'Lucas Andrade', 1.75, 70.50, '2000-08-15', 'LINHA  ', 50, 40, '12.345.678/0001-01', '123.456.789-01');
INSERT INTO atleta VALUES ('234.567.890-13', 'Rafael Nunes', 1.80, 75.00, '1998-03-12', 'GOLEIRO', 45, 45, '23.456.789/0002-02', '234.567.890-12');
INSERT INTO atleta VALUES ('345.678.901-24', 'Gabriel Costa', 1.88, 82.30, '2001-07-20', 'LINHA  ', 30, 25, '34.567.890/0003-03', '345.678.901-23');
INSERT INTO atleta VALUES ('456.789.012-35', 'Felipe Lima', 1.72, 68.00, '1999-12-01', 'GOLEIRO', 55, 50, '45.678.901/0004-04', '456.789.012-34');
INSERT INTO atleta VALUES ('123.456.789-01', 'Atleta1', 1.88, NULL, '1989-10-10', 'LINHA  ', 30, 20, '34.567.890/0003-03', '456.789.012-34');
INSERT INTO atleta VALUES ('525.018.648-32', 'atleta2', 1.88, 90.00, '2005-07-22', 'linha  ', 44, 25, '34.567.890/0003-03', '456.789.012-34');
INSERT INTO atleta VALUES ('567.890.123-46', 'João Pedro', 1.85, 78.00, '1997-09-10', 'LINHA  ', 60, 55, '12.345.678/0001-01', '567.890.123-45');
INSERT INTO atleta VALUES ('678.901.234-57', 'Thiago Alves', 1.90, 80.50, '2000-05-14', 'GOLEIRO', 48, 48, '23.456.789/0002-02', '678.901.234-56');
INSERT INTO atleta VALUES ('789.012.345-68', 'Bruno Silva', 1.77, 72.00, '2002-01-20', 'LINHA  ', 25, 20, '34.567.890/0003-03', '789.012.345-67');
INSERT INTO atleta VALUES ('890.123.456-79', 'Rodrigo Pereira', 1.81, 76.00, '1996-11-11', 'GOLEIRO', 70, 65, '45.678.901/0004-04', '890.123.456-78');
INSERT INTO atleta VALUES ('901.234.567-80', 'André Santos', 1.78, 74.00, '1999-06-30', 'LINHA  ', 40, 35, '12.345.678/0001-01', '901.234.567-79');
INSERT INTO atleta VALUES ('999.999.999-99', 'Juice wrld', NULL, NULL, '2009-03-27', 'linha  ', 54, 21, '12.345.678/0001-00', '123.456.789-01');


-- TABELA COMPETICAO
INSERT INTO competicao VALUES (5, 'Copa Nacional', 2024, 'SP', 'São Paulo', 'Clube Esportivo Central');
INSERT INTO competicao VALUES (6, 'Torneio Regional', 2024, 'RJ', 'Rio de Janeiro', 'Clube Meninos da Vila');
INSERT INTO competicao VALUES (7, 'Campeonato Estadual', 2024, 'MG', 'Belo Horizonte', 'Sociedade Esportiva do Vale');
INSERT INTO competicao VALUES (8, 'Liga Juvenil', 2024, 'RS', 'Porto Alegre', 'Futebol Clube Norte');


-- TABELA PARTIDA

INSERT INTO partida VALUES (1, '2024-11-10', '14:00:00', 'Estádio Central', '01:30:00', 5);
INSERT INTO partida VALUES (2, '2024-11-12', '16:00:00', 'Arena Nacional', '02:00:00', 6);
INSERT INTO partida VALUES (3, '2024-11-14', '18:00:00', 'Campo Municipal', '01:45:00', 7);
INSERT INTO partida VALUES (4, '2024-11-16', '20:00:00', 'Estádio da Juventude', '02:15:00', 8);


-- TABELA ATLETAPARTIDA

INSERT INTO atletapartida VALUES (1, '123.456.789-02', 2, 1, 0, 0, 9);
INSERT INTO atletapartida VALUES (2, '234.567.890-13', 1, 2, 0, 0, 8);
INSERT INTO atletapartida VALUES (3, '345.678.901-24', 0, 1, 4, 2, 7);
INSERT INTO atletapartida VALUES (4, '456.789.012-35', 3, 0, 0, 0, 10);


-- TABELA TREINADOR

INSERT INTO treinador VALUES ('321.654.987-65', 'Paulo Henrique', '1975-07-15');
INSERT INTO treinador VALUES ('741.852.963-74', 'Juliana Alves', '1980-03-09');
INSERT INTO treinador VALUES ('852.963.741-85', 'Carla Souza', '1988-12-21');
INSERT INTO treinador VALUES ('963.258.147-96', 'Fernando Lima', '1990-10-10');


-- TABELA TREINO
INSERT INTO treino VALUES (17, '123.456.789-02', '07:30:00', '2024-11-01', '321.654.987-65', 'Estádio Central', 'Finalização', '01:30:00');
INSERT INTO treino VALUES (18, '234.567.890-13', '09:00:00', '2024-11-02', '741.852.963-74', 'Centro Esportivo', 'Defesa', '02:00:00');
INSERT INTO treino VALUES (19, '345.678.901-24', '15:00:00', '2024-11-03', '852.963.741-85', 'Campo do Oeste', 'Tática', '01:45:00');
INSERT INTO treino VALUES (20, '456.789.012-35', '17:00:00', '2024-11-04', '963.258.147-96', 'Estádio Leste', 'Condição Física', '02:15:00');


-- TABELA EXERCICIOTREINO
INSERT INTO exerciciotreino VALUES (17, 'Corrida de resistência', 5, 10);
INSERT INTO exerciciotreino VALUES (18, 'Defesa posicional', 3, 15);
INSERT INTO exerciciotreino VALUES (19, 'Chutes ao gol', 4, 20);
INSERT INTO exerciciotreino VALUES (20, 'Treinamento de passe longo', 6, 12);


-- TABELA GOLEIRO

INSERT INTO goleiro VALUES ('234.567.890-13', 30, 0.67, 8, 3.50, 10, 150, 50);
INSERT INTO goleiro VALUES ('456.789.012-35', 25, 0.45, 12, 4.00, 8, 160, 60);
INSERT INTO goleiro VALUES ('678.901.234-57', 40, 0.83, 5, 2.80, 12, 120, 40);
INSERT INTO goleiro VALUES ('890.123.456-79', 20, 0.29, 15, 4.50, 6, 180, 70);


-- TABELA TIPOLESAO

INSERT INTO tipolesao VALUES ('Entorse de tornozelo');
INSERT INTO tipolesao VALUES ('Ruptura de ligamento');
INSERT INTO tipolesao VALUES ('Fratura óssea');
INSERT INTO tipolesao VALUES ('Lesão muscular');


-- TABELA LESAO

INSERT INTO lesao VALUES (5, 'Entorse de tornozelo', '123.456.789-02', '2024-11-05', '10:00:00', 2, 'Tornozelo direito', 'Causada durante partida');
INSERT INTO lesao VALUES (6, 'Ruptura de ligamento', '234.567.890-13', '2024-10-15', '14:00:00', 4, 'Joelho esquerdo', 'Ocorrida em treino');
INSERT INTO lesao VALUES (7, 'Fratura óssea', '345.678.901-24', '2024-09-30', '16:00:00', 5, 'Braço direito', 'Impacto com adversário');
INSERT INTO lesao VALUES (8, 'Lesão muscular', '456.789.012-35', '2024-11-02', '18:00:00', 3, 'Coxa esquerda', 'Excesso de esforço');


-- TABELA LINHA

INSERT INTO linha VALUES ('123.456.789-02', 15, 10, 'Zona Central', 2, 2.5, 8, 85.5, 1.20);
INSERT INTO linha VALUES ('345.678.901-24', 20, 15, 'Lateral Esquerda', 1, 3.0, 10, 90.0, 1.50);
INSERT INTO linha VALUES ('567.890.123-46', 18, 12, 'Zona Direita', 3, 2.8, 9, 88.5, 1.40);
INSERT INTO linha VALUES ('789.012.345-68', 10, 8, 'Meio-Campo', 0, 1.8, 5, 82.0, 1.00);
INSERT INTO linha VALUES ('901.234.567-80', 12, 7, 'Zona Esquerda', 1, 2.2, 6, 85.0, 1.30);
INSERT INTO linha VALUES ('890.123.456-79', 10, 5, 'Ponta-Esquerdo', 0, 10.0, 20, 99.0, 1.00);


-- TABELA MEDICO

INSERT INTO medico VALUES ('123456/SP ', 'Dr. Ricardo Silva', 'Rua das Flores', 'Centro', 100, 'São Paulo', 'SP', '11 98765-4321');
INSERT INTO medico VALUES ('234567/RJ ', 'Dra. Maria Oliveira', 'Av. Brasil', 'Copacabana', 200, 'Rio de Janeiro', 'RJ', '21 99876-5432');
INSERT INTO medico VALUES ('345678/MG ', 'Dr. João Santos', 'Rua da Paz', 'Savassi', 300, 'Belo Horizonte', 'MG', '31 98765-4321');
INSERT INTO medico VALUES ('456789/RS ', 'Dra. Ana Costa', 'Av. Independência', 'Moinhos', 400, 'Porto Alegre', 'RS', '51 98765-4321');


-- TABELA TRATAMENTO

INSERT INTO tratamento VALUES (5, '123456/SP ', '2024-11-06', '2024-12-01');
INSERT INTO tratamento VALUES (6, '234567/RJ ', '2024-10-16', '2024-11-15');
INSERT INTO tratamento VALUES (7, '345678/MG ', '2024-10-01', NULL);
INSERT INTO tratamento VALUES (8, '456789/RS ', '2024-11-03', '2024-11-20');


-- TABELA TREINADORCLUBE

INSERT INTO treinadorclube VALUES ('321.654.987-65', '12.345.678/0001-01');
INSERT INTO treinadorclube VALUES ('741.852.963-74', '23.456.789/0002-02');
INSERT INTO treinadorclube VALUES ('852.963.741-85', '34.567.890/0003-03');
INSERT INTO treinadorclube VALUES ('963.258.147-96', '45.678.901/0004-04');


