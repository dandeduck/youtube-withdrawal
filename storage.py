import sqlite3
import json
import datetime


class LastCheckedDatetime:
    connection = None
    cursor = None

    def __init__(self, databasePath):
        self.connection = sqlite3.connect(databasePath)
        self.cursor = self.connection.cursor()

    def initialize(self):
        try:
            self.cursor.execute('''CREATE TABLE LAST_CHECKED_DATETIME 
            ([generated_id] INTEGER PRIMARY KEY, [Year] integer, [Month] integer, [Day] integer, [Hour] integer, [Minute] integer, [Second] integer)''')
            self.cursor.execute('''INSERT INTO LAST_CHECKED_DATETIME(Year, Month, Day, Hour, Minute, Second)
            VALUES(0,0,0,0,0,0)''')
        except sqlite3.OperationalError:
            return
        self.connection.commit()

    def update(self):
        currDatetime = datetime.datetime.now()

        self.cursor.execute('''UPDATE LAST_CHECKED_DATETIME
        SET Year = ?, Month = ?, Day = ?, Hour = ?, Minute = ?, Second = ?
        WHERE generated_id = 1;''', [currDatetime.year, currDatetime.month, currDatetime.day, currDatetime.hour, currDatetime.minute, currDatetime.second])
        self.connection.commit()

    def get(self):
        self.cursor.execute('''SELECT * FROM LAST_CHECKED_DATETIME''')
        return self.cursor.fetchall()
