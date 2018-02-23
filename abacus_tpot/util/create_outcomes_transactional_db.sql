DROP TABLE IF EXISTS Participant CASCADE;
CREATE TABLE Participant (
    ParticipantID		INTEGER UNIQUE,
    WioaParticipant		BOOLEAN,
    WioaItaParticipant		BOOLEAN
);

DROP TABLE IF EXISTS Wage;
CREATE TABLE Wage (
    WageStartDate		DATE,
    WageEndDate			DATE,
    ParticipantID		INTEGER REFERENCES Participant(ParticipantID),
    WageAmt			FLOAT
);

DROP TABLE IF EXISTS ParticipantProgram;
CREATE TABLE ParticipantProgram (
    ParticipantID		INTEGER REFERENCES Participant(ParticipantID),
    ProgramID			INTEGER,
    EntryDate			DATE,
    Enrolled			BOOLEAN,
    ExitDate			DATE,
    ExitTypeID			INTEGER,
    ObtainedCredential		BOOLEAN
);
