from .catalog import ProductCatalog

class OrderEngine:
    """Gère la logique de calcul des commandes"""
    
    @staticmethod
    def calculate_lineaire(type_lin, nb_modules, config_base):
        """
        Calcule les besoins selon la règle Base + X détectée dans tes fichiers
        """
        results = []
        # Simulation de la logique complexe du fichier Excel
        multiplier = int(config_base.replace("Base + ", "")) # ex: 7, 8 ou 9
        
        # On récupère les items de base
        base_items = ProductCatalog.COMPONENTS.get("LINEAIRE_VERRE" if "Verre" in type_lin else "GONDOLE_SIMPLE")
        
        for item in base_items:
            qty = nb_modules if "BASE" in item['ref'] else nb_modules * multiplier
            results.append({
                "ref": item['ref'],
                "nom": item['designation'],
                "qty": qty,
                "total_prix": qty * item['prix']
            })
            
        return results