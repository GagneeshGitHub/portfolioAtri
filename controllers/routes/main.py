from .atri import Atri
from fastapi import Request, Response
from atri_utils import *

def init_state(at: Atri):
    "Atri framework"
    pass

def handle_page_request(at: Atri, req: Request, res: Response, query: str):
    """
    This function is called whenever a user loads this route in the browser.
    """
    pass

def handle_event(at: Atri, req: Request, res: Response):
    
    pass