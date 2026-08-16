from paddleocr import PaddleOCR
from .text_processor import TextProcessor

class OCRService:
    def __init__(self):
        self.ocr = PaddleOCR(lang="en")

    def extract_text(self,image_path):
        """
        arg: it must be as path to send this function.
        """
        result=self.ocr.ocr(image_path)
        texts=[]
        for page in result:
            for line in page:
                row_text=line[1][0]
                cleaned=TextProcessor.clean(row_text)
                texts.append(cleaned)
        return texts
   



