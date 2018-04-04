DELETE FROM wage;
DELETE FROM program_participant;
DELETE FROM provider;

INSERT INTO wage VALUES
    (123456789, 2015, 1001, 2001, 3001, 4001),
    (123456789, 2016, 5001, 6001, 7001, 8001),
    (223456789, 2015, 1002, 2002, 3002, 4002),
    (223456789, 2016, 5002, 6002, 7002, 8002),
    (323456789, 2015, 0,    0,    0,    0   ),
    (323456789, 2016, 5000, 6000, 7000, 8000),
    (423456789, 2015, 1003, 2003, 3003, 4003),
    (423456789, 2016, 5003, 6003, 7003, 8003),
    (523456789, 2015, 1004, 2004, 3004, 4004),
    (523456789, 2016, 5004, 6004, 7004, 8004),
    (623456789, 2015, 1005, 2005, 3005, 4005),
    (623456789, 2016, 5005, 6005, 7005, 8005),
    (723456789, 2015, 1006, 2006, 3006, 4006),
    (723456789, 2016, 5006, 6006, 7006, 8006),
    (823456789, 2015, 1007, 2007, 3007, 4007),
    (823456789, 2016, 5007, 6007, 7007, 8007),
    (923456789, 2015, 1008, 2008, 3008, 4008),
    (923456789, 2016, 5008, 6008, 7008, 8008),
    (023456789, 2015, 1009, 2009, 3009, 4009),
    (023456789, 2016, 5009, 6009, 7009, 8009),
    (013456789, 2015, 1010, 2010, 3010, 4010),
    (013456789, 2016, 5010, 6010, 7010, 8010);

INSERT INTO provider VALUES
    (1, 'Fake Denver City College', 'Fake community college in Denver', 'info@fakecc.com', 'http://fakecc.com', 1950),
    (2, 'Fake Coding Bootcamp', 'Fake coding bootcamp', 'info@fakebc.com', 'http://fakebc.com', 2010);

INSERT INTO program_participant VALUES
    (1, 123456789, 1, 1, '1/1/2014', '12/31/2014', 'Graduated', TRUE, 'Associate Degree', 'WIOA', 'Nursing', 'Denver'),
    (2, 223456789, 1, 1, '1/1/2014', '12/31/2014', 'Withdrew', FALSE, 'Associate Degree', 'WIOA', 'Nursing', 'Denver'),
    (3, 323456789, 1, 2, '1/1/2014', '12/31/2014', 'Graduated', TRUE, 'Badge', NULL, 'Java', NULL),
    (4, 423456789, 1, 1, '1/1/2014', '12/31/2014', 'Graduated', TRUE, 'Associate Degree', 'WIOA', 'Nursing', 'Denver'),
    (5, 523456789, 1, 1, '1/1/2014', '12/31/2014', 'Graduated', TRUE, 'Associate Degree', 'WIOA', 'Nursing', 'Denver'),
    (6, 623456789, 1, 1, '1/1/2014', '12/31/2014', 'Graduated', TRUE, 'Associate Degree', 'WIOA', 'Nursing', 'Denver'),
    (7, 723456789, 1, 1, '1/1/2014', '12/31/2014', 'Graduated', TRUE, 'Associate Degree', 'WIOA', 'Nursing', 'Denver'),
    (8, 823456789, 1, 1, '1/1/2014', '12/31/2014', 'Graduated', TRUE, 'Associate Degree', 'WIOA', 'Nursing', 'Denver'),
    (9, 923456789, 1, 1, '1/1/2014', '12/31/2014', 'Graduated', TRUE, 'Associate Degree', 'WIOA', 'Nursing', 'Denver'),
    (10, 023456789, 1, 1, '1/1/2014', '12/31/2014', 'Graduated', TRUE, 'Associate Degree', 'WIOA', 'Nursing', 'Denver'),
    (11, 013456789, 1, 1, '1/1/2014', '12/31/2014', 'Graduated', TRUE, 'Associate Degree', 'WIOA', 'Nursing', 'Denver');

