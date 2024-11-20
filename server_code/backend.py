import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

data_path = data_files['database.db']

@anvil.server.callable
def get_gefaengnisse():
    conn = sqlite3.connect(data_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT Name, GID FROM Gefaengnis")
    gefaengnisse = cursor.fetchall() 
    
    conn.close()
    return [(name, gid) for name, gid in gefaengnisse]

@anvil.server.callable
def get_gefaengnis_details(gefaengnis_id):
    conn = sqlite3.connect(data_path)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT Verwaltung.Direktor, Verwaltung.belegte_Zellen, Verwaltung.freie_Zellen
        FROM Verwaltung
        INNER JOIN Gefaengnis ON Verwaltung.VID = Gefaengnis.VID
        WHERE Gefaengnis.GID = ?
    """, (gefaengnis_id,))
    gefaengnis_details = cursor.fetchone()
    
    cursor.execute("""
        SELECT Zelle.Zellennummer, COUNT(bewohnt.HID) AS anzahl_häftlinge
        FROM Zelle
        LEFT JOIN bewohnt ON Zelle.ZID = bewohnt.ZID
        WHERE Zelle.GID = ?
        GROUP BY Zelle.ZID
    """, (gefaengnis_id,))

    zellen = cursor.fetchall()

    conn.close()
    if gefaengnis_details:
        direktor, belegte_zellen, freie_zellen = gefaengnis_details
        return {
            "direktor": direktor,
            "belegte_zellen": belegte_zellen,
            "freie_zellen": freie_zellen,
            "zellen": [{"zellennummer": z[0], "anzahl_häftlinge": z[1]} for z in zellen],
        }
    else:
        return None


@anvil.server.callable
def get_inmate_details(zellennummer):
    conn = sqlite3.connect(data_path)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT bewohnt.HID, bewohnt.Einzug, bewohnt.Auszug, bewohnt.Haftdauer
        FROM Zelle
        LEFT JOIN bewohnt ON Zelle.ZID = bewohnt.ZID
        WHERE Zelle.Zellennummer = ?
    """, (zellennummer,))

    inmate_details = cursor.fetchall()

    conn.close()

    return [{'haeftlingsnummer': inmate[0], 'einzug': inmate[1], 'auszug': inmate[2], 'haftdauer': inmate[3]} for inmate in inmate_details]
