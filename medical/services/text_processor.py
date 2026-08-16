import re
from bidi.algorithm import get_display
from .claim_service import ExtractClaim
class TextProcessor:
    @staticmethod
    def clean(text):
        """
        processing text before search in db.
        """
        text= text[::1]
        text=text.lower()
        text=text.strip()
        text = " ".join(text.split())
        text = re.sub(r"[^a-z0-9\s.]", "", text)
        obj_extract=ExtractClaim()
        claim=obj_extract.extract_claim(text)
        return claim
       