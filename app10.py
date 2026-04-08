import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURATION ET STYLE BLANC & BLEU ---
st.set_page_config(page_title="MobiConfig", layout="wide", initial_sidebar_state="expanded")

LOGO_FILE = "Logo_MobiConfig.png"
EXCEL_FILE = "OUTILS DE COMMANDE FINAL.xlsx"

# Injection CSS pour le design et le footer fixe
st.markdown("""
    <style>
    /* Style Global */
    .main { background-color: #f8f9fa; color: #1e293b; }
    
    /* Sidebar */
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #dee2e6; }
    
    /* Bouton Bleu (Actif) */
    div.stButton > button[kind="primary"] {
        background-color: #007bff !important;
        color: white !important;
        border: none !important;
    }
    
    /* Footer Fixe en bas de page */
    .fixed-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: white;
        padding: 10px 40px;
        border-top: 2px solid #007bff;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 999;
    }
    
    /* Espace pour éviter que le footer cache le contenu */
    .content-area { margin-bottom: 120px; }
    
    /* Style des tableaux */
    .stTable { background-color: white; border-radius: 10px; }
    
    /* Métriques */
    [data-testid="stMetricValue"] { color: #007bff !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CHARGEMENT DES DONNÉES ---
@st.cache_data
def load_excel_all(file):
    if os.path.exists(file):
        # On charge tout sans header pour contrôler les lignes fusionnées
        return pd.read_excel(file, sheet_name=None, header=None)
    return None

all_data = load_excel_all(EXCEL_FILE)

# --- 3. MÉMOIRE ET NAVIGATION ---
if 'panier' not in st.session_state:
    st.session_state.panier = {}
if 'page_index' not in st.session_state:
    st.session_state.page_index = 0

if all_data:
    exclure = ["DEBUT", "FIN", "TOTAL COM", "BLANCDEBUT", "BLANCFIN"]
    onglets = sorted([s for s in all_data.keys() if s not in exclure])
    liste_pages = ["📋 RÉCAPITULATIF TOTAL"] + onglets
else:
    liste_pages = ["Fichier introuvable"]

def changer_page(idx):
    st.session_state.page_index = idx
    st.rerun()

# --- 4. BARRE LATÉRALE ---
with st.sidebar:
    if os.path.exists(LOGO_FILE):
        st.image(LOGO_FILE, use_container_width=True)
    st.markdown("<h2 style='text-align: center; color: #007bff;'>MobiConfig</h2>", unsafe_allow_html=True)
    
    for i, nom in enumerate(liste_pages):
        active = (st.session_state.page_index == i)
        if st.button(nom, key=f"side_{i}", use_container_width=True, type="primary" if active else "secondary"):
            changer_page(i)

# --- 5. LOGIQUE DE CALCUL DU TOTAL (PRO) ---
def extraire_donnees_panier():
    recap = {} # { "NomFR": {"qty": 0, "prix": 0, "en": "...", "rem": "..."} }
    total_ht = 0.0
    
    for onglet, data in st.session_state.panier.items():
        df = all_data[onglet]
        k_val = data.get('K', 8)
        
        for meuble_nom, qte_voulue in data.get('items', {}).items():
            if qte_voulue <= 0: continue
            
            # Trouver la colonne du meuble (cherche dans ligne 0 ou 1)
            col_idx = -1
            for c in range(4, df.shape[1]):
                if str(df.iloc[0, c]) == meuble_nom or str(df.iloc[1, c]) == meuble_nom:
                    col_idx = c
                    break
            
            if col_idx != -1:
                # On scanne les pièces (dès la ligne 3 pour éviter les en-têtes)
                for r in range(3, len(df)):
                    try:
                        nom_fr = str(df.iloc[r, 1]).strip()
                        if nom_fr in ["nan", "None", ""] or "Désignation" in nom_fr: continue
                        
                        nom_en = str(df.iloc[r, 0]).strip()
                        remarques = str(df.iloc[r, 2]).strip()
                        prix_u = float(str(df.iloc[r, 3]).replace(',', '.'))
                        
                        ratio_cell = df.iloc[r, col_idx]
                        ratio = float(k_val) if str(ratio_cell).upper() == 'K' else float(ratio_cell)
                        
                        if ratio > 0:
                            total_besoin = qte_voulue * ratio
                            if nom_fr in recap:
                                recap[nom_fr]['qty'] += total_besoin
                            else:
                                recap[nom_fr] = {
                                    'qty': total_besoin, 
                                    'prix': prix_u, 
                                    'en': nom_en if nom_en != "nan" else "",
                                    'rem': remarques if remarques != "nan" else ""
                                }
                    except: continue
    return recap

# --- 6. AFFICHAGE DU CONTENU ---
st.markdown('<div class="content-area">', unsafe_allow_html=True)

if st.session_state.page_index == 0:
    st.title("📋 Récapitulatif de votre Commande")
    resultats = extraire_donnees_panier()
    
    if resultats:
        items_table = []
        total_final = 0.0
        for nom, info in resultats.items():
            stot = info['qty'] * info['prix']
            total_final += stot
            items_table.append({
                "Désignation (FR)": nom,
                "Désignation (EN)": info['en'],
                "Remarques": info['rem'],
                "Quantité": int(info['qty']),
                "Prix Unitaire": f"{info['prix']:.2f} €",
                "Total HT": f"{stot:.2f} €"
            })
        
        st.table(pd.DataFrame(items_table))
        st.metric("MONTANT TOTAL HT", f"{total_final:.2f} €")
        
        # Export CSV
        csv = pd.DataFrame(items_table).to_csv(index=False).encode('utf-8')
        st.download_button("📥 Télécharger le Bon de Commande", csv, "MobiConfig_Commande.csv")
    else:
        st.info("🛍️ Votre panier est vide. Sélectionnez des meubles dans le catalogue.")

else:
    page_nom = liste_pages[st.session_state.page_index]
    st.title(f"🛠️ Configuration : {page_nom}")
    df_sheet = all_data[page_nom]
    
    if page_nom not in st.session_state.panier:
        st.session_state.panier[page_nom] = {'K': 8, 'items': {}}
    
    # Facteur K (si présent)
    if "K" in str(df_sheet.iloc[0:5, 0:5]):
        st.session_state.panier[page_nom]['K'] = st.number_input(
            "Réglage du facteur K (Hauteur)", 
            min_value=1, 
            value=int(st.session_state.panier[page_nom]['K']),
            key=f"k_{page_nom}"
        )
        st.divider()

    # Recherche des noms de meubles (Colonnes 4+)
    meubles_noms = []
    for c in range(4, df_sheet.shape[1]):
        n = str(df_sheet.iloc[0, c])
        if n == "nan": n = str(df_sheet.iloc[1, c])
        if n != "nan" and "TOTAL" not in n.upper():
            meubles_noms.append(n)

    st.subheader("Nombre de meubles à commander :")
    cols = st.columns(3)
    for idx, m in enumerate(meubles_noms):
        val_ex = st.session_state.panier[page_nom]['items'].get(m, 0)
        with cols[idx % 3]:
            st.session_state.panier[page_nom]['items'][m] = st.number_input(
                f"{m}", 
                min_value=0, 
                value=int(val_ex), 
                key=f"in_{page_nom}_{m}"
            )

st.markdown('</div>', unsafe_allow_html=True)

# --- 7. FOOTER FIXE (NAVIGATION) ---
# On utilise un conteneur HTML fixe pour les boutons
st.markdown("""
    <div class="fixed-footer">
        <div id="footer-buttons"></div>
    </div>
    """, unsafe_allow_html=True)

# Création des vrais boutons Streamlit alignés en bas
cols_nav = st.columns([1, 4, 1])
with cols_nav[0]:
    if st.session_state.page_index > 0:
        if st.button("⬅️ PRÉCÉDENT", use_container_width=True):
            changer_page(st.session_state.page_index - 1)
with cols_nav[2]:
    if st.session_state.page_index < len(liste_pages) - 1:
        if st.button("SUIVANT ➡️", use_container_width=True):
            changer_page(st.session_state.page_index + 1)