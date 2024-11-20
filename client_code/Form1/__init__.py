from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
    self.gefaengnisse_drop_down.items = anvil.server.call('get_gefaengnisse')
    self.label_direktor.text = ''
    self.label_freie_zellen.text = ''
    self.repeating_zellen.items = []
    self.gefaengnisse_drop_down_change()
    
  
  def gefaengnisse_drop_down_change(self, **event_args):
    selected_gefaengnis = self.gefaengnisse_drop_down.selected_value
    if selected_gefaengnis:
        gefaengnis_id = selected_gefaengnis
        details = anvil.server.call('get_gefaengnis_details', gefaengnis_id)
        #zellendetails = anvil.server.call('get_inmate_details', gefaengnis_id)
        if details:
            self.label_direktor.text = details['direktor']
            self.label_freie_zellen.text = details['freie_zellen']
            self.repeating_zellen.items = details['zellen']
          
            #self.repeating_panel_zellendetails = zellendetails['zellendetails']
        else:
            self.label_direktor.text = "Keine Daten gefunden"
            self.label_freie_zellen.text = ""
            self.repeating_zellen.items = []



 


