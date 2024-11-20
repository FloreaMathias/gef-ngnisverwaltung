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
    # get Form1
    parent = self.parent.parent.parent.parent
    zellennummer = self.item['zellennummer']
    parent.repeating_panel_zellendetails.items = [{'haeftlingsnummer': 'TODO', 'einzug': 'TODO', 'auszug': 'TODO', 'haftdauer': 'TODO'},
                                                  {'haeftlingsnummer': 'TODO1', 'einzug': 'TODO1', 'auszug': 'TODO1', 'haftdauer': 'TODO1'}]
