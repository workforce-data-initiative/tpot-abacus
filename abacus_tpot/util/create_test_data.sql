DELETE FROM wage;
DELETE FROM program_participant;
DELETE FROM provider;

INSERT INTO wage VALUES
    (123456789, 2015, 1000, 1000, 1000, 1000),
    (123456789, 2016, 1000, 1000, 1000, 1000),
    (223456789, 2015, 1000, 1000, 1000, 1000),
    (223456789, 2016, 1000, 1000, 1000, 1000),
    (323456789, 2015, 0,    0,    0,    0   ),
    (323456789, 2016, 1000, 1000, 1000, 1000),
    (423456789, 2015, 2000, 2000, 2000, 2000),
    (423456789, 2016, 2000, 2000, 2000, 2000),
    (523456789, 2015, 1000, 1000, 1000, 1000),
    (523456789, 2016, 1000, 1000, 1000, 1000),
    (623456789, 2015, 1000, 1000, 1000, 1000),
    (623456789, 2016, 1000, 1000, 1000, 1000),
    (723456789, 2015, 1000, 1000, 1000, 1000),
    (723456789, 2016, 1000, 1000, 1000, 1000),
    (823456789, 2015, 1000, 1000, 1000, 1000),
    (823456789, 2016, 1000, 1000, 1000, 1000),
    (923456789, 2015, 1000, 1000, 1000, 1000),
    (923456789, 2016, 1000, 1000, 1000, 1000),
    (023456789, 2015, 1000, 1000, 1000, 1000),
    (023456789, 2016, 1000, 1000, 1000, 1000),
    (013456789, 2015, 1000, 1000, 1000, 1000),
    (013456789, 2016, 1000, 1000, 1000, 1000);

INSERT INTO provider VALUES
    (1, 'Fake Denver City College', 'Fake community college in Denver', 'info@fakecc.com', 'http://fakecc.com', 1950),
    (2, 'Fake Coding Bootcamp', 'Fake coding bootcamp', 'info@fakebc.com', 'http://fakebc.com', 2010);

INSERT INTO program_participant VALUES
    (1, 123456789, 1, 1, '1/1/2014', '12/31/2014', 'graduated', TRUE, 'associate degree', 'WIOA', 'Nursing', 'Denver'),
    (2, 223456789, 1, 1, '1/1/2014', '12/31/2014', 'graduated', TRUE, 'badge', NULL, 'Java', NULL),
    (3, 323456789, 1, 1, '1/1/2014', '12/31/2014', 'dropped out', FALSE, 'associate degree', 'WIOA', 'Nursing', 'Denver'),
    (4, 423456789, 1, 1, '1/1/2014', '12/31/2014', 'graduated', TRUE, 'associate degree', 'WIOA', 'Nursing', 'Denver'),
    (5, 523456789, 1, 1, '1/1/2014', '12/31/2014', 'graduated', TRUE, 'associate degree', 'WIOA', 'Nursing', 'Denver'),
    (6, 623456789, 1, 1, '1/1/2014', '12/31/2014', 'graduated', TRUE, 'associate degree', 'WIOA', 'Nursing', 'Denver'),
    (7, 723456789, 1, 1, '1/1/2014', '12/31/2014', 'graduated', TRUE, 'associate degree', 'WIOA', 'Nursing', 'Denver'),
    (8, 823456789, 1, 1, '1/1/2014', '12/31/2014', 'graduated', TRUE, 'associate degree', 'WIOA', 'Nursing', 'Denver'),
    (9, 923456789, 1, 1, '1/1/2014', '12/31/2014', 'graduated', TRUE, 'associate degree', 'WIOA', 'Nursing', 'Denver'),
    (10, 023456789, 1, 1, '1/1/2014', '12/31/2014', 'graduated', TRUE, 'associate degree', 'WIOA', 'Nursing', 'Denver'),
    (11, 013456789, 1, 1, '1/1/2014', '12/31/2014', 'graduated', TRUE, 'associate degree', 'WIOA', 'Nursing', 'Denver');

