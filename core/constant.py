class AppConfig:
    APP_NAME = "PyProcessor Pro"
    VERSION = "2.1.0"
    AUTHOR = "Gemini Developer"

class ProcessingRules:
    """Regroupe les paramètres fixes du fichier d'origine"""
    TAX_RATE = 0.20
    DISCOUNT_THRESHOLD = 500
    ALLOWED_CATEGORIES = ["Électronique", "Services", "Matériel"]
    
    UNIT_MAPPING = {
        "Électronique": "Unité",
        "Services": "Heure",
        "Matériel": "Kg"
    }

class UITheme:
    PRIMARY_COLOR = "#2563eb"
    SUCCESS_COLOR = "#16a34a"