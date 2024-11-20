from ._anvil_designer import RowDetailsClickTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowDetailsClick(RowDetailsClickTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    def Details_click(self, **event_args):
        """This method is called when the button is clicked"""
        parent = self.parent.parent.parent.parent 

        zellennummer = self.item['zellennummer']

        inmate_details = anvil.server.call('get_inmate_details', zellennummer)

        if inmate_details:
            parent.repeating_panel_zellendetails.items = inmate_details
        else:
            parent.repeating_panel_zellendetails.items = [{'haeftlingsnummer': 'Keine Daten gefunden', 'einzug': '', 'auszug': '', 'haftdauer': ''}]