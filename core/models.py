class Piece:
    """Représente un composant individuel avec son prix."""
    def __init__(self, num, nom_en, nom_fr, remarque, prix):
        self.numPiece = num
        self.nomPieceEN = nom_en
        self.nomPieceFR = nom_fr
        self.remarquePiece = remarque if remarque not in ["—", ""] else ""
        self.prixPiece = float(prix)

class ProduitCompose:
    """Un Produit est composé d'un nom et d'une liste de tuples (Piece, Quantité)."""
    def __init__(self, nom, composition_func):
        """
        :param nom: Nom du produit (ex: 'Linéaire 2200 x 400')
        :param composition_func: La fonction qui définit la liste de pièces.
        """
        self.nom = nom
        self.composition_func = composition_func

    def generer_liste_materiel(self, k):
        """
        Calcule les quantités et le prix final pour une commande spécifique.
        """
        # On appelle la fonction du catalogue pour récupérer la liste de (Piece, Qte)
        liste_de_pieces_brute = self.composition_func(k)
        
        detail_commande = []
        total_global = 0.0

        for piece, quantite in liste_de_pieces_brute:
            if quantite > 0:
                prix_ligne = piece.prixPiece * quantite
                total_global += prix_ligne
                
                detail_commande.append({
                    "id": piece.numPiece,
                    "nom": piece.nomPieceFR,
                    "qte": quantite,
                    "prix_u": piece.prixPiece,
                    "total_ligne": round(prix_ligne, 2),
                    "remarque": piece.remarquePiece
                })

        return {
            "nom_produit": self.nom,
            "k_utilise": k,
            "composants": detail_commande,
            "prix_total_ht": round(total_global, 2)
        }