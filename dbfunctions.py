import sqlite3
import customtkinter

con = sqlite3.connect("database/farematrix.db")

cursor = con.cursor()

def CreateSingleJourneyTables(con, cursor):
    cursor.execute(''' 
            CREATE TABLE Origin (
                origin_id INTEGER PRIMARY KEY,
                origin_name TEXT NOT NULL      
            )         
        ''')
        
    cursor.execute(''' 
            CREATE TABLE Destination (
                destination_id INTEGER PRIMARY KEY,
                destination_name TEXT NOT NULL      
            )         
        ''')

    cursor.execute(''' 
            CREATE TABLE SingleJourneyFare (
                fare_id INTEGER PRIMARY KEY,
                origin_id INTEGER NOT NULL,
                destination_id INTEGER NOT NULL,
                fare_price REAL NOT NULL,
                FOREIGN KEY (origin_id) REFERENCES Origin(origin_id),
                FOREIGN KEY (destination_id) REFERENCES Destination(destination_id)      
            )         
        ''')
        
    con.commit()

def CreateSingleSummary(con, cursor):
    cursor.execute(''' 
            CREATE TABLE SingleJourneyFare (
                fare_id INTEGER NOT NULL,
                origin_id INTEGER NOT NULL,
                destination_id INTEGER NOT NULL,
                fare_price REAL NOT NULL,
                FOREIGN KEY (origin_id) REFERENCES Origin(origin_id),
                FOREIGN KEY (destination_id) REFERENCES Destination(destination_id)    
                FOREIGN KEY (fare_price) REFERENCES SingleJourneyFare(fare_price)        
            )         
        ''')

def InsertValues(con, cursor):
    
    originValues = [
        (1, "Recto"),
        (2, "Legarda"),        
        (3, "Pureza"),        
        (4, "V. Mapa"),        
        (5, "J. Ruiz"),        
        (6, "Gilmore"),        
        (7, "Betty Go"),        
        (8, "Cubao"),        
        (9, "Anonas"),        
        (10, "Katipunan"),        
        (11, "Santolan"),        
        (12, "Marikina"),        
        (13, "Antipolo"),           
    ]
    
    destinationValues = [
        (1, "Recto"),
        (2, "Legarda"),        
        (3, "Pureza"),        
        (4, "V. Mapa"),        
        (5, "J. Ruiz"),        
        (6, "Gilmore"),        
        (7, "Betty Go"),        
        (8, "Cubao"),        
        (9, "Anonas"),        
        (10, "Katipunan"),        
        (11, "Santolan"),        
        (12, "Marikina"),        
        (13, "Antipolo"),           
    ]
    
    cursor.executemany('''
        INSERT INTO Origin (origin_id, origin_name)
        VALUES (?, ?)       
    ''', originValues)
    
    cursor.executemany('''
        INSERT INTO Destination (destination_id, destination_name)
        VALUES (?, ?)       
    ''', destinationValues)
    
    con.commit()

def InsertSingleJourneyFare(con, cursor):
    
    fareTableValues = [
        (1, 1, 1, 0),
        (2, 1, 2, 15),
        (3, 1, 3, 20),
        (4, 1, 4, 20),
        (5, 1, 5, 20),
        (6, 1, 6, 25),
        (7, 1, 7, 25),
        (8, 1, 8, 25),
        (9, 1, 9, 25),
        (10, 1, 10, 30),
        (11, 1, 11, 30),
        (12, 1, 12, 35),
        (13, 1, 13, 35),
        (14, 2, 1, 15),
        (15, 2, 2, 0),
        (16, 2, 3, 15),
        (17, 2, 4, 20),
        (18, 2, 5, 20),
        (19, 2, 6, 20),
        (20, 2, 7, 25),
        (21, 2, 8, 25),
        (22, 2, 9, 25),
        (23, 2, 10, 25),
        (24, 2, 11, 30),
        (25, 2, 12, 30),
        (26, 2, 13, 35),
        (27, 3, 1, 20),
        (28, 3, 2, 15),
        (29, 3, 3, 0),
        (30, 3, 4, 15),
        (31, 3, 5, 20),
        (32, 3, 6, 20),
        (33, 3, 7, 20),
        (34, 3, 8, 20),
        (35, 3, 9, 25),
        (36, 3, 10, 25),
        (37, 3, 11, 30),
        (38, 3, 12, 30),
        (39, 3, 13, 30),
        (40, 4, 1, 20),
        (41, 4, 2, 20),
        (42, 4, 3, 15),
        (43, 4, 4, 0),
        (44, 4, 5, 15),
        (45, 4, 6, 20),
        (46, 4, 7, 20),
        (47, 4, 8, 20),
        (48, 4, 9, 20),
        (49, 4, 10, 25),
        (50, 4, 11, 25),
        (51, 4, 12, 30),
        (52, 4, 13, 30),
        (53, 5, 1, 20),
        (54, 5, 2, 20),
        (55, 5, 3, 20),
        (56, 5, 4, 15),
        (57, 5, 5, 0),
        (58, 5, 6, 15),
        (59, 5, 7, 20),
        (60, 5, 8, 20),
        (61, 5, 9, 20),
        (62, 5, 10, 20),
        (63, 5, 11, 25),
        (64, 5, 12, 25),
        (65, 5, 13, 30),
        (66, 6, 1, 25),
        (67, 6, 2, 20),
        (68, 6, 3, 20),
        (69, 6, 4, 20),
        (70, 6, 5, 15),
        (71, 6, 6, 0),
        (72, 6, 7, 15),
        (73, 6, 8, 20),
        (74, 6, 9, 20),
        (75, 6, 10, 20),
        (76, 6, 11, 25),
        (77, 6, 12, 25),
        (78, 6, 13, 30),
        (79, 7, 1, 25),
        (80, 7, 2, 25),
        (81, 7, 3, 20),
        (82, 7, 4, 20),
        (83, 7, 5, 20),
        (84, 7, 6, 15),
        (85, 7, 7, 0),
        (86, 7, 8, 15),
        (87, 7, 9, 20),
        (88, 7, 10, 20),
        (89, 7, 11, 20),
        (90, 7, 12, 25),
        (91, 7, 13, 25),
        (92, 8, 1, 25),
        (93, 8, 2, 25),
        (94, 8, 3, 20),
        (95, 8, 4, 20),
        (96, 8, 5, 20),
        (97, 8, 6, 20),
        (98, 8, 7, 15),
        (99, 8, 8, 0),
        (100, 8, 9, 15),
        (101, 8, 10, 20),
        (102, 8, 11, 20),
        (103, 8, 12, 25),
        (104, 8, 13, 25),
        (105, 9, 1, 25),
        (106, 9, 2, 25),
        (107, 9, 3, 25),
        (108, 9, 4, 20),
        (109, 9, 5, 20),
        (110, 9, 6, 20),
        (111, 9, 7, 20),
        (112, 9, 8, 15),
        (113, 9, 9, 0),
        (114, 9, 10, 15),
        (115, 9, 11, 20),
        (116, 9, 12, 20),
        (117, 9, 13, 25),
        (118, 10, 1, 30),
        (119, 10, 2, 25),
        (120, 10, 3, 25),
        (121, 10, 4, 25),
        (122, 10, 5, 20),
        (123, 10, 6, 20),
        (124, 10, 7, 20),
        (125, 10, 8, 20),
        (126, 10, 9, 15),
        (127, 10, 10, 0),
        (128, 10, 11, 20),
        (129, 10, 12, 20),
        (130, 10, 13, 25),
        (131, 11, 1, 30),
        (132, 11, 2, 30),
        (133, 11, 3, 30),
        (134, 11, 4, 25),
        (135, 11, 5, 25),
        (136, 11, 6, 25),
        (137, 11, 7, 20),
        (138, 11, 8, 20),
        (139, 11, 9, 20),
        (140, 11, 10, 20),
        (141, 11, 11, 0),
        (142, 11, 12, 15),
        (143, 11, 13, 20),
        (144, 12, 1, 35),
        (145, 12, 2, 30),
        (146, 12, 3, 30),
        (147, 12, 4, 30),
        (148, 12, 5, 25),
        (149, 12, 6, 25),
        (150, 12, 7, 25),
        (151, 12, 8, 25),
        (152, 12, 9, 20),
        (153, 12, 10, 20),
        (154, 12, 11, 15),
        (155, 12, 12, 0),
        (156, 12, 13, 20),
        (157, 13, 1, 35),
        (158, 13, 2, 35),
        (159, 13, 3, 30),
        (160, 13, 4, 30),
        (161, 13, 5, 30),
        (162, 13, 6, 30),
        (163, 13, 7, 25),
        (164, 13, 8, 25),
        (165, 13, 9, 25),
        (166, 13, 10, 25),
        (167, 13, 11, 20),
        (168, 13, 12, 20),
        (169, 13, 13, 0),
    ]
    
    cursor.executemany('''
        INSERT INTO SingleJourneyFare (fare_id, origin_id, destination_id, fare_price)
        VALUES (?, ?, ?, ?)        
    ''', fareTableValues)
    
    con.commit()

def OriginDropdown(parent):
    con = sqlite3.connect("database/farematrix.db")
    cursor = con.cursor()
    query = "SELECT origin_name FROM origin"
    cursor.execute(query)

    stationNames = [row[0] for row in cursor.fetchall()]
    
    cursor.close()
    con.close()

    dropdownFont = customtkinter.CTkFont(family="Century Gothic", size=20, weight="bold")
    locationDropdown = customtkinter.CTkComboBox(parent, values=stationNames, width=240, height=30, font=dropdownFont, justify="center")
    locationDropdown.place(relx=0.5, rely=0.32, anchor="center")

    return locationDropdown


def DestinationNames(parent):
    con = sqlite3.connect("database/farematrix.db")
    cursor = con.cursor()
    query = "SELECT destination_name FROM destination"
    cursor.execute(query)
    
    destNames = [row[0] for row in cursor.fetchall()]
    
    cursor.close()
    con.close
    parent.destNames = destNames

def GetFarePrice(originID, destinationID):
    con = sqlite3.connect("database/farematrix.db")
    cursor = con.cursor()
    query = "SELECT fare_price FROM SingleJourneyFare WHERE origin_id = ? AND destination_id = ?"
    cursor.execute(query, (originID, destinationID))

    result = cursor.fetchone()
    naResult = 'No Fare Available'
    con.close()

    if result:
        return result[0]
    else:
        return None

def GetOriginID(originName):
    con = sqlite3.connect("database/farematrix.db")
    cursor = con.cursor()
    query = "SELECT origin_id FROM Origin WHERE origin_name = ?"
    cursor.execute(query,(originName,))

    result = cursor.fetchone()
    con.close()

    if result:
        originID = result[0]
        return originID
    else:
        return None




con.close()