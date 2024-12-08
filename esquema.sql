-- TABELA RESPONSÁVEL
create table Responsavel (
	CPF char(14),
	Nome varchar(30) not null,
	DataNascimento date not null,
	constraint PK_RESPONSAVEL primary key (CPF),
	constraint CK_CPF Check(regexp_like(CPF,'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}'))
);
-- TABELA CLUBE
create table Clube(
	CNPJ char(18),
	Nome varchar(50) not null,
	constraint PK_CLUBE primary key(CNPJ),
	constraint CK_CNPJ check(regexp_like(CNPJ, '[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}\-[0-9]{2}'))
);

-- TABELA ATLETA
create table Atleta (
	CPF char(14),
	Nome varchar(50) not null,
	Altura numeric(3,2),
	Peso numeric (5,2), 
	DataNascimento date not null,
	Posicao char(7) not null,
	NumeroDeJogos int,
	NumeroDeJogosTitular int,
	Clube char(18), 
	Responsavel char(14),
	constraint PK_ATLETA primary key(CPF),
	constraint FK_ATLETA_CLUBE foreign key(Clube) references 
	Clube(CNPJ) on delete set null,
	constraint FK_ATLETA_RESPONSAVEL foreign key (Responsavel) references
	Responsavel(CPF) on delete set null,
	constraint CK_CPF_ATLETA check(regexp_like(CPF,'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}')),
	constraint CK_POSICAO_ATLETA check(upper(posicao) in ('GOLEIRO', 'LINHA'))
);

-- TABELA GOLEIRO - DOS ATLETAS QUE SÃO GOLEIROS
create table Goleiro(
	CPF char(14),
	GolsSofridos int,
	GolsSofridosPorPartida numeric (4,2),
	PenaltisDefendidos int,
	DefesasPorJogo numeric (4,2),
	GolsSofridosForaDaArea int,
	DefesasRealizadas int,
	DefesasRealizadasForaDaArea int,
	constraint PK_GOLEIRO primary key (CPF),
	constraint FK_GOLEIRO foreign key (CPF) references
	Atleta(CPF) on delete cascade,
	constraint CK_CPF_GOLEIRO check(regexp_like(CPF,'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}'))
);

-- TABELA LINHA - DOS JOGADORES DE LINHA
create table Linha (
	CPF char(14),
	Gols int,
	assistencias int,
	mapaDeCalor varchar(100),
	errosCapitais int,
	chutesPorJogo numeric (3,1),
	grandesChancescriadas int,
	passesCertosPorPartida numeric (3,1),
	DesarmesPorJogo numeric (4,2),
	constraint PK_LINHA primary key (CPF),
	constraint FK_LINHA foreign key (CPF) references 
	Atleta(CPF) on delete cascade,
	constraint CK_CPF_LINHA check(regexp_like(CPF,'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}'))
);

-- TABELA TREINADOR
create table Treinador (
	CPF char(14), 
	Nome varchar(50) not null,
	DataNascimento date not null,
	constraint PK_TREINADOR primary key (CPF),
	constraint CK_CPF_TREINADOR check(regexp_like(CPF,'[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}'))
)

-- TABELA TREINO
create table Treino (
	idTreino serial,
	atleta char(14) NOT NULL,
	horaTreino time NOT NULL,
	dataTreino date NOT NULL,
	Treinador char(14) NOT NULL,
	LocalTreino varchar(100),
	Enfoque varchar(30),
	Duracao time,
	constraint PK_TREINO primary key(idTreino),
	constraint FK_TREINO_ATLETA foreign key(atleta) 
	references Atleta(CPF) on delete cascade,
	constraint FK_TREINO_TREINADOR foreign key (Treinador)
	references Treinador(CPF) on delete CASCADE,
	constraint UN_TREINO unique(atleta, horaTreino,dataTreino, Treinador)
);

-- TABELA EXERCICIO-TREINO
create table ExercicioTreino (
	IDtreino serial,
	NomeExercicio varchar(30),
	Series int,
	repeticoes int,
	constraint PK_EX_TREINO primary key(IDtreino, NomeExercicio),
	constraint FK_EX_TREINO foreign key(IDtreino) references Treino (idTreino)
	on delete cascade
)

-- TABELA TREINADOR-CLUBE
create table TreinadorClube(
	Treinador char(14),
	Clube char(18),
	constraint PK_TR_CL primary key (Treinador, Clube),
	constraint FK_TR_CL_TR foreign key (Treinador) references
	Treinador(CPF) on delete cascade,
	constraint FK_TR_CL_CL foreign key (Clube) references 
	Clube(CNPJ) on delete cascade
);

-- TABELA MEDICO
create table Medico (
	CRM char(10),
	Nome varchar(50) not null,
	Rua varchar(30),
	Bairro varchar(20),
	Numero int,
	Cidade varchar(20),
	Estado char(2),
	Telefone char(13),
	constraint PK_MEDICO primary key(CRM),
	constraint CK_CRM_MEDICO check(regexp_like(CRM,'^[0-9]{6,7}\/?[A-Z]{2}$'))
)

-- TABELA TIPO DE LESAO
create table TipoLesao (
	tipo varchar(20),
	constraint PK_TIPO_LESAO primary key(tipo)
);

-- TABELA LESAO
create table Lesao(
	idLesao serial,
	tipo varchar(20) NOT NULL,
	atleta char(14) NOT NULL,
	dataLesao date NOT NULL,
	horaLesao time NOT NULL,
	gravidade int,
	localFerimento varchar(20),
	descricao varchar(150),
	constraint PK_LESAO primary key (idLesao),
	constraint UN_LESAO unique(tipo, atleta, dataLesao, horaLesao),
	constraint FK_LESAO_TIPO foreign key(tipo) references
	TipoLesao(tipo) on delete cascade,
	constraint FK_LESAO_ATLETA foreign key(atleta) references
	Atleta(cpf) ON DELETE CASCADE,
	CONSTRAINT CK_GRAV CHECK(GRAVIDADE BETWEEN 1 AND 5)
);

-- TABELA TRATAMENTO
create table Tratamento (
	idLesao serial,
	Medico char(10),
	DataInicio date not null,
	DataTermino date,
	constraint PK_TRATAMENTO primary key(idLesao, Medico),
	constraint FK_TRATAMENTO_IDLESAO foreign key(idLesao)
	references Lesao(IdLesao) ON DELETE CASCADE,
	constraint FK_TRATAMENTO_MEDICO foreign key(Medico)
	references Medico(CRM) ON DELETE SET NULL
);

-- TABELA COMPETICAO
create table Competicao (
	idCompeticao serial,
	Nome varchar(50) not null,
	Edicao int not null,
	Estado char(2) not null,
	Cidade varchar(30) not null,
	Vencedor varchar(30),
	constraint PK_COMPETICAO primary key(idCompeticao),
	constraint UN_COMPETICAO unique(Nome,Edicao,Estado,Cidade)
);

-- TABELA PARTIDA
create table Partida (
	idPartida serial,
	dataPartida date not null,
	horaPartida time not null,
	localPartida varchar(50) not null,
	tempoMaximo time not null,
	idCompeticao serial,
	constraint PK_PARTIDA primary key(idPartida),
	constraint UN_PARTIDA unique(dataPartida, horaPartida, localPartida),
	constraint FK_PARTIDA_COMP foreign key (idCompeticao) 
	references Competicao (idCompeticao) on delete set null
);

-- TABELA ATLETA-PARTIDA
create table AtletaPartida(
	idPartida serial,
	Atleta char(14),
	gols int,
	assistencias int,
	defesas int,
	golsSalvos int,
	desempenho int,
	constraint PK_ATL_PART primary key(idPartida,Atleta),
	constraint FK_ATL_PART_PART foreign key (idPartida) 
	references Partida(idPartida) on delete cascade,
	constraint FK_ATL_PART_ATL foreign key (Atleta) 
	references Atleta(CPF) on delete cascade
);

