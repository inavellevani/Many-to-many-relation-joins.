import sqlite3

conn = sqlite3.connect('sqlite3.db')

cursor = conn.cursor()

cursor.executescript('''
CREATE TABLE Advisor(
AdvisorID INTEGER NOT NULL,
AdvisorName TEXT NOT NULL,
PRIMARY KEY(AdvisorID)
);

CREATE TABLE Student(
StudentID NUMERIC NOT NULL,
StudentName NUMERIC NOT NULL,
AdvisorID INTEGER,
FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
PRIMARY KEY(StudentID)
);

INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES
(1,"John Paul"),
(2,"Anthony Roy"),
(3,"Raj Shetty"),
(4,"Sam Reeds"),
(5,"Arthur Clintwood");

INSERT INTO Student(StudentID, StudentName, AdvisorID) VALUES
(501,"Geek1",1),
(502,"Geek2",1),
(503,"Geek3",3),
(504,"Geek4",2),
(505,"Geek5",4),
(506,"Geek6",2),
(507,"Geek7",2),
(508,"Geek8",3),
(509,"Geek9",NULL),
(510,"Geek10",1);

CREATE TABLE StudentAdvisor(
StudentID INTEGER,
AdvisorID INTEGER,
FOREIGN KEY(StudentID) REFERENCES Student(StudentID),
FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
PRIMARY KEY(StudentID, AdvisorID)
);

INSERT INTO StudentAdvisor(StudentID, AdvisorID) VALUES
(501, 1),
(502, 1),
(503, 3),
(504, 2),
(505, 4),
(506, 2),
(507, 2),
(508, 3),
(509, 5),
(510, 1);
''')

cursor.execute('''
SELECT Advisor.AdvisorName, COUNT(StudentAdvisor.StudentID) AS num_students
FROM Advisor
LEFT JOIN StudentAdvisor ON Advisor.AdvisorID = StudentAdvisor.AdvisorID
GROUP BY Advisor.AdvisorID
''')

for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
