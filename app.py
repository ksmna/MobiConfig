import sys
import os
from flask import Flask, render_template, request, session, redirect, url_for

# On s'assure que le dossier courant est dans le path pour importer 'core'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from core.catalog import Catalog

app = Flask(__name__)
app.secret_key = "mobiconfig_secret_key_98765" 

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'panier' not in session:
        session['panier'] = []

    categories = Catalog.CATEGORIES
    liste_produits_plate = Catalog.PRODUCTS
    resultat_preview = None 

    if request.method == 'POST':
        id_p = request.form.get('id_produit')
        action = request.form.get('action')
        
        try:
            k = int(request.form.get('k_value', 7))
            qte_voulue = int(request.form.get('qte_produit', 1))
        except (ValueError, TypeError):
            k, qte_voulue = 7, 1
            
        if id_p in liste_produits_plate:
            infos = liste_produits_plate[id_p].generer_liste_materiel(k)
            
            if action == 'calculer':
                resultat_preview = infos
                # Multiplication par la quantité pour la prévisualisation
                for comp in resultat_preview['composants']:
                    comp['qte'] *= qte_voulue
                    comp['total_ligne'] = round(comp['prix_u'] * comp['qte'], 2)
                resultat_preview['prix_total_ht'] = round(infos['prix_total_ht'] * qte_voulue, 2)
                resultat_preview['qte_voulue'] = qte_voulue

            elif action == 'ajouter':
                temp_panier = session['panier']
                id_unique = f"{id_p}_k{k}"
                
                # Regroupement si le même produit (même k) est déjà là
                deja_present = False
                for item in temp_panier:
                    if item['id_selection'] == id_unique:
                        item['qte'] += qte_voulue
                        item['total_ht'] = round(item['prix_unit_ht'] * item['qte'], 2)
                        deja_present = True
                        break
                
                if not deja_present:
                    temp_panier.append({
                        'id_selection': id_unique,
                        'nom': infos['nom_produit'],
                        'k': k,
                        'qte': qte_voulue,
                        'prix_unit_ht': infos['prix_total_ht'],
                        'total_ht': round(infos['prix_total_ht'] * qte_voulue, 2),
                        'composants': infos['composants']
                    })
                
                session['panier'] = temp_panier
                session.modified = True 
                return redirect(url_for('index'))

    # Calcul du récapitulatif global
    recap_global = {}
    total_panier_ht = 0
    for item in session['panier']:
        total_panier_ht += item['total_ht']
        for comp in item['composants']:
            ref = f"P{comp['id']}"
            if ref not in recap_global:
                recap_global[ref] = {
                    'nom': comp['nom'],
                    'qte': 0,
                    'prix_u': comp['prix_u'],
                    'remarque': comp['remarque']
                }
            recap_global[ref]['qte'] += comp['qte'] * item['qte']

    return render_template('index.html', 
                           categories=categories, 
                           panier=session['panier'], 
                           recap_global=recap_global,
                           total_panier_ht=round(total_panier_ht, 2),
                           resultat=resultat_preview)

@app.route('/vider')
def vider_panier():
    session['panier'] = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)