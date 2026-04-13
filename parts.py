from .models import Piece

class PartsRegistry:
    # --- BACK PANELS ---
    P1 = Piece(1, "BACK PANEL 400x500", "Fond 400 x 500", "—", 3.21)
    P2 = Piece(2, "BACK PANEL 500x500", "Fond 500 x 500", "—", 4.11)
    P3 = Piece(3, "BACK PANEL 400x700", "Fond 400 x 700", "—", 3.47)
    P4 = Piece(4, "BACK PANEL 500x700", "Fond 500 x 700", "—", 4.27)
    P5 = Piece(5, "SLIDING BACK PANEL 400x700", "Fond extensible 400", "—", 6.23)
    P6 = Piece(6, "SLIDING BACK PANEL 500x700", "Fond extensible 500", "—", 7.66)

    # --- SHELVES MONOBLOCK ---
    P7 = Piece(7, "SHELF MONOBLOCK 200x500", "Tablette 200 x 500", "sans trou", 2.45)
    P8 = Piece(8, "SHELF MONOBLOCK 200x700", "Tablette 200 x 700", "sans trou", 3.39)
    P9 = Piece(9, "SHELF MONOBLOCK 200x700", "Tablette 200 x 700 bacs soldeurs", "perforation verre", 3.39)
    P10 = Piece(10, "SHELF MONOBLOCK 300x700", "Tablette 300 x 700 bacs soldeurs", "perforation verre", 4.06)
    P11 = Piece(11, "SHELF MONOBLOCK 400x700", "Tablette 400 x 700 bacs soldeurs", "perforation verre", 4.06)
    P12 = Piece(12, "SHELF MONOBLOCK 200x500", "Tablette 200 x 500 bacs soldeurs", "perforation verre", 4.06)
    P13 = Piece(13, "SHELF MONOBLOCK 300x500", "Tablette 300 x 500 bacs soldeurs", "perforation verre", 4.06)
    P14 = Piece(14, "SHELF MONOBLOCK 400x500", "Tablette 400 x 500 bacs soldeurs", "perforation verre", 4.06)
    P15 = Piece(15, "SHELF MONOBLOCK 300x500", "Tablette 300 x 500", "sans trou", 4.06)
    P16 = Piece(16, "SHELF MONOBLOCK 400x500", "Tablette 400 x 500", "sans trou", 4.06)
    P17 = Piece(17, "SHELF MONOBLOCK 300x700", "Tablette 300 x 700", "sans trou", 4.06)
    P18 = Piece(18, "SHELF MONOBLOCK 400x700", "Tablette 400 x 700", "sans trou", 5.30)
    P19 = Piece(19, "PERFORATED SHELF 300x700", "Tablette 300 x 700 perforée", "standard", 5.31)
    P20 = Piece(20, "PERFORATED SHELF 400x700", "Tablette 400 x 700 perforée", "standard", 5.31)

    # --- GLASS ACCESSORIES ---
    P21 = Piece(21, "GLASS SEPARATOR CORNER", "Séparateur verre angle", "—", 0.24)
    P22 = Piece(22, "GLASS SEPARATOR FLAT", "Séparateur verre plat", "—", 0.17)
    P23 = Piece(23, "SIDE GLASS SEPARATOR 200x180", "Verre latéral 200", "trempé 6mm", 7.20)
    P24 = Piece(24, "SIDE GLASS SEPARATOR 300x180", "Verre latéral 300", "trempé 6mm", 7.20)
    P25 = Piece(25, "SIDE GLASS SEPARATOR 400x180", "Verre latéral 400", "trempé 6mm", 7.20)

    # --- FRONT GLASS ---
    P26 = Piece(26, "FRONT WINDOW 700x100", "Verre frontal 700", "trempé 6mm", 7.20)
    P27 = Piece(27, "FRONT WINDOW 500x100", "Verre frontal 500", "trempé 6mm", 7.20)

    # --- GLASS SHELVES ---
    P28 = Piece(28, "GLASS SHELF 200x500", "Tablette verre 200x500", "inter comptoir", 8.79)
    P29 = Piece(29, "GLASS SHELF 200x500", "Tablette verre 200x500", "mural", 8.79)
    P30 = Piece(30, "GLASS SHELF 200x700", "Tablette verre 200x700", "mural", 9.62)
    P31 = Piece(31, "GLASS SHELF 300x500", "Tablette verre 300x500", "mural", 9.62)
    P32 = Piece(32, "GLASS SHELF 300x700", "Tablette verre 300x700", "mural", 9.62)

    # --- SLIDING SHELVES ---
    P33 = Piece(33, "SLIDING SHELF 200x700", "Tablette extensible 200", "RAL9003", 6.62)
    P34 = Piece(34, "SLIDING SHELF 300x700", "Tablette extensible 300", "RAL9003", 6.62)
    P35 = Piece(35, "SLIDING SHELF 400x700", "Tablette extensible 400", "RAL9003", 8.65)

    # --- CONSOLES VERRE ---
    P36 = Piece(36, "GLASS SHELF CONSOLE 200x700", "Console verre 200x700", "—", 7.22)
    P37 = Piece(37, "GLASS SHELF CONSOLE 200x500", "Console verre 200x500", "—", 5.16)
    P38 = Piece(38, "GLASS SHELF CONSOLE 300x500", "Console verre 300x500", "—", 7.22)
    P39 = Piece(39, "GLASS SHELF CONSOLE 300x700", "Console verre 300x700", "—", 7.22)

    # --- SUPPORTS ---
    P40 = Piece(40, "METAL BRACKET 200", "Console 200", "—", 0.66)
    P41 = Piece(41, "METAL BRACKET 300", "Console 300", "—", 0.73)
    P42 = Piece(42, "METAL BRACKET 400", "Console 400", "—", 0.73)

    # --- STRUCTURE ---
    P43 = Piece(43, "SLIDING PLINTH", "Plinthe extensible", "—", 1.86)
    P44 = Piece(44, "METAL PLINTH 500", "Plinthe 500", "—", 0.97)
    P45 = Piece(45, "METAL PLINTH 700", "Plinthe 700", "—", 0.83)
    P46 = Piece(46, "PROFILE 2200", "Montant 2200", "—", 10.50)
    P47 = Piece(47, "PROFILE 1800", "Montant 1800", "—", 8.63)
    P48 = Piece(48, "PROFILE 1600", "Montant 1600", "—", 6.78)
    P49 = Piece(49, "PROFILE 1400", "Montant 1400", "—", 6.78)

    # --- PIEDS ---
    P50 = Piece(50, "FOOT 200", "Pied 200", "—", 2.67)
    P51 = Piece(51, "FOOT 300", "Pied 300", "—", 3.44)
    P52 = Piece(52, "FOOT 400", "Pied 400", "—", 3.44)

    # --- FIXATIONS ---
    P53 = Piece(53, "ADJUSTER CLIP", "Clip réglage", "—", 0.16)
    P54 = Piece(54, "SET SCREW M10", "Vis réglage", "—", 0.28)
    P55 = Piece(55, "BOLT M10", "Boulon", "—", 0.12)
    P56 = Piece(56, "NUT M10", "Écrou", "—", 0.03)

    # --- ACCESSOIRES ---
    P57 = Piece(57, "CARRIER BAR 700", "Barre charge 700", "—", 3.49)
    P58 = Piece(58, "CANOPY 500", "Capot pub 500", "vis incluses", 4.85)
    P59 = Piece(59, "CANOPY 700", "Capot pub 700", "vis incluses", 6.80)
    P60 = Piece(60, "FLOOR FIXING", "Fixation sol", "—", 1.14)
    P61 = Piece(61, "FRONT WIRE 700", "Butée frontale", "—", 1.22)
    P62 = Piece(62, "INTERCONNECTION BAR", "Barre maintien", "—", 2.15)

    # --- HABILLAGE ---
    P63 = Piece(63, "SIDE RIGHT 2200", "Cache droit 2200", "—", 5.56)
    P64 = Piece(64, "SIDE LEFT 2200", "Cache gauche 2200", "—", 5.56)
    P65 = Piece(65, "SIDE RIGHT 1800", "Cache droit 1800", "—", 5.56)
    P66 = Piece(66, "SIDE LEFT 1800", "Cache gauche 1800", "—", 5.56)
    P67 = Piece(67, "SIDE RIGHT 1600", "Cache droit 1600", "—", 5.56)
    P68 = Piece(68, "SIDE LEFT 1600", "Cache gauche 1600", "—", 5.56)
    P69 = Piece(69, "SIDE RIGHT 1400", "Cache droit 1400", "—", 3.39)
    P70 = Piece(70, "SIDE LEFT 1400", "Cache gauche 1400", "—", 3.39)

    # --- CAPOTS ---
    P71 = Piece(71, "TOP CAP", "Capot 700", "—", 2.13)
    P72 = Piece(72, "SLIDING CAP", "Capot extensible", "—", 2.70)
    P73 = Piece(73, "FOOT CAP RIGHT 200", "Cache pied droit 200", "—", 0.69)
    P74 = Piece(74, "FOOT CAP LEFT 200", "Cache pied gauche 200", "—", 0.69)
    P75 = Piece(75, "FOOT CAP RIGHT 300", "Cache pied droit 300", "—", 0.98)
    P76 = Piece(76, "FOOT CAP LEFT 300", "Cache pied gauche 300", "—", 0.98)
    P77 = Piece(77, "FOOT CAP RIGHT 400", "Cache pied droit 400", "—", 0.98)
    P78 = Piece(78, "FOOT CAP LEFT 400", "Cache pied gauche 400", "—", 0.69)

    # --- COMPTOIRS ---
    P79 = Piece(79, "COUNTER PANEL", "Panneau perforé", "—", 19.14)
    P80 = Piece(80, "MIDDLE COUNTER", "Intercomptoir", "kit vis inclus", 160.23)
    P81 = Piece(81, "RIGHT COUNTER", "Comptoir droit", "kit vis inclus", 207.94)
    P82 = Piece(82, "LEFT COUNTER", "Comptoir gauche", "kit vis inclus", 207.94)

    # --- CROCHETS ---
    P83 = Piece(83, "HOOK 200", "Broche 200", "—", 0.75)
    P84 = Piece(84, "HOOK 300", "Broche 300", "—", 0.75)
    P85 = Piece(85, "HOOK 400", "Broche 400", "—", 0.75)
    P86 = Piece(86, "HOOK PANEL", "Broche panneau perforé", "—", 0.75)

    @classmethod
    def get_all(cls):
        """Retourne la liste de toutes les pièces pour l'interface web"""
        return [getattr(cls, attr) for attr in dir(cls) if attr.startswith('P') and not callable(getattr(cls, attr))]