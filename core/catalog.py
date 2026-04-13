from .parts import PartsRegistry
from .models import ProduitCompose

class Catalog:
    # --- 1. EXTENSIBLE (Métal Standard) ---
    def composition_L2200_400(k):
        return [
            (PartsRegistry.P5, 4), (PartsRegistry.P6, 1), (PartsRegistry.P35, 1+k),
            (PartsRegistry.P46, 2), (PartsRegistry.P52, 2), (PartsRegistry.P53, 2),
            (PartsRegistry.P54, 2), (PartsRegistry.P55, 2), (PartsRegistry.P56, 2),
            (PartsRegistry.P43, 1), (PartsRegistry.P45, 1), (PartsRegistry.P77, 1),
            (PartsRegistry.P78, 1), (PartsRegistry.P60, 2), (PartsRegistry.P63, 2)
        ]

    def composition_L2200_300(k):
        return [
            (PartsRegistry.P5, 4), (PartsRegistry.P6, 1), (PartsRegistry.P34, 1+k),
            (PartsRegistry.P41, 2*k), (PartsRegistry.P46, 2), (PartsRegistry.P51, 2),
            (PartsRegistry.P53, 2), (PartsRegistry.P54, 2), (PartsRegistry.P55, 2),
            (PartsRegistry.P56, 2), (PartsRegistry.P43, 1), (PartsRegistry.P45, 1),
            (PartsRegistry.P75, 1), (PartsRegistry.P76, 1), (PartsRegistry.P60, 2), (PartsRegistry.P63, 2)
        ]

    def composition_L2200_200(k):
        return [
            (PartsRegistry.P5, 4), (PartsRegistry.P6, 1), (PartsRegistry.P33, 1+k),
            (PartsRegistry.P40, 2*k), (PartsRegistry.P46, 2), (PartsRegistry.P50, 2),
            (PartsRegistry.P53, 2), (PartsRegistry.P54, 2), (PartsRegistry.P55, 2),
            (PartsRegistry.P56, 2), (PartsRegistry.P43, 1), (PartsRegistry.P45, 1),
            (PartsRegistry.P73, 1), (PartsRegistry.P74, 1), (PartsRegistry.P60, 2), (PartsRegistry.P63, 2)
        ]

    # --- 2. EXTENSIBLE MÉTAL (Base + 7) ---
    def compo_M_700_300(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 1), (PartsRegistry.P17, 1+k),
            (PartsRegistry.P41, 2*k), (PartsRegistry.P45, 1), (PartsRegistry.P46, 2),
            (PartsRegistry.P51, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2),
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P60, 2),
            (PartsRegistry.P63, 1), (PartsRegistry.P64, 1), (PartsRegistry.P75, 1), (PartsRegistry.P76, 1)
        ]

    def compo_M_700_300_SUITE(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 1), (PartsRegistry.P17, 1+k),
            (PartsRegistry.P41, 2*k), (PartsRegistry.P45, 1), (PartsRegistry.P46, 1),
            (PartsRegistry.P51, 1), (PartsRegistry.P53, 1), (PartsRegistry.P54, 1),
            (PartsRegistry.P55, 1), (PartsRegistry.P56, 1), (PartsRegistry.P60, 1)
        ]

    def compo_M_700_200(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 1), (PartsRegistry.P8, 1+k),
            (PartsRegistry.P40, 2*k), (PartsRegistry.P45, 1), (PartsRegistry.P46, 2),
            (PartsRegistry.P50, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2),
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P60, 2),
            (PartsRegistry.P63, 1), (PartsRegistry.P64, 1), (PartsRegistry.P73, 1), (PartsRegistry.P74, 1)
        ]

    def compo_M_700_200_SUITE(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 1), (PartsRegistry.P8, 1+k),
            (PartsRegistry.P40, 2*k), (PartsRegistry.P45, 1), (PartsRegistry.P46, 1),
            (PartsRegistry.P50, 1), (PartsRegistry.P53, 1), (PartsRegistry.P54, 1),
            (PartsRegistry.P55, 1), (PartsRegistry.P56, 1), (PartsRegistry.P60, 1)
        ]

    def compo_M_500_200(k):
        return [
            (PartsRegistry.P1, 4), (PartsRegistry.P2, 1), (PartsRegistry.P7, 1+k),
            (PartsRegistry.P40, 2*k), (PartsRegistry.P44, 1), (PartsRegistry.P46, 2),
            (PartsRegistry.P50, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2),
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P60, 2),
            (PartsRegistry.P63, 1), (PartsRegistry.P64, 1), (PartsRegistry.P73, 1), (PartsRegistry.P74, 1)
        ]

    def compo_M_500_300(k):
        return [
            (PartsRegistry.P1, 4), (PartsRegistry.P2, 1), (PartsRegistry.P15, 1+k),
            (PartsRegistry.P41, 2*k), (PartsRegistry.P44, 1), (PartsRegistry.P46, 2),
            (PartsRegistry.P51, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2),
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P60, 2),
            (PartsRegistry.P63, 1), (PartsRegistry.P64, 1), (PartsRegistry.P75, 1), (PartsRegistry.P76, 1)
        ]

    # --- 3. GONDOLE SIMPLE 1400 (Base + 6) ---
    def compo_G_1400_700_300(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 2), (PartsRegistry.P17, 1+k),
            (PartsRegistry.P41, 2*k), (PartsRegistry.P45, 1), (PartsRegistry.P49, 2),
            (PartsRegistry.P51, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2),
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P59, 1),
            (PartsRegistry.P60, 2), (PartsRegistry.P69, 1), (PartsRegistry.P70, 1),
            (PartsRegistry.P75, 1), (PartsRegistry.P76, 1)
        ]

    def compo_G_1400_700_300_SUITE(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 2), (PartsRegistry.P17, 1+k),
            (PartsRegistry.P41, 2*k), (PartsRegistry.P45, 1), (PartsRegistry.P49, 1),
            (PartsRegistry.P51, 1), (PartsRegistry.P53, 1), (PartsRegistry.P54, 1),
            (PartsRegistry.P55, 1), (PartsRegistry.P56, 1), (PartsRegistry.P59, 1),
            (PartsRegistry.P60, 1)
        ]

    def compo_G_1400_500_300(k):
        return [
            (PartsRegistry.P1, 4), (PartsRegistry.P2, 2), (PartsRegistry.P15, 1+k),
            (PartsRegistry.P41, 2*k), (PartsRegistry.P44, 1), (PartsRegistry.P49, 2),
            (PartsRegistry.P51, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2),
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P58, 1),
            (PartsRegistry.P60, 2), (PartsRegistry.P69, 1), (PartsRegistry.P70, 1),
            (PartsRegistry.P75, 1), (PartsRegistry.P76, 1)
        ]

    def compo_G_1400_700_200(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 2), (PartsRegistry.P8, 1+k),
            (PartsRegistry.P40, 2*k), (PartsRegistry.P45, 1), (PartsRegistry.P49, 2),
            (PartsRegistry.P50, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2),
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P59, 1),
            (PartsRegistry.P60, 2), (PartsRegistry.P69, 1), (PartsRegistry.P70, 1),
            (PartsRegistry.P73, 1), (PartsRegistry.P74, 1)
        ]

    def compo_G_1400_700_200_SUITE(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 2), (PartsRegistry.P8, 1+k),
            (PartsRegistry.P40, 2*k), (PartsRegistry.P45, 1), (PartsRegistry.P49, 1),
            (PartsRegistry.P50, 1), (PartsRegistry.P53, 1), (PartsRegistry.P54, 1),
            (PartsRegistry.P55, 1), (PartsRegistry.P56, 1), (PartsRegistry.P59, 1),
            (PartsRegistry.P60, 1)
        ]

    def compo_G_1400_500_200(k):
        return [
            (PartsRegistry.P1, 4), (PartsRegistry.P2, 2), (PartsRegistry.P7, 1+k),
            (PartsRegistry.P40, 2*k), (PartsRegistry.P44, 1), (PartsRegistry.P49, 2),
            (PartsRegistry.P50, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2),
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P58, 1),
            (PartsRegistry.P60, 2), (PartsRegistry.P69, 1), (PartsRegistry.P70, 1),
            (PartsRegistry.P73, 1), (PartsRegistry.P74, 1)
        ]
    
    # --- 4. GONDOLE SIMPLE 1600 (Base + 7) ---
    def compo_G_1600_700_300(k):
        return [
            (PartsRegistry.P17, 1+k), (PartsRegistry.P41, 2*k), (PartsRegistry.P45, 1),
            (PartsRegistry.P48, 2), (PartsRegistry.P51, 2), (PartsRegistry.P53, 2),
            (PartsRegistry.P54, 2), (PartsRegistry.P55, 2), (PartsRegistry.P56, 2),
            (PartsRegistry.P59, 1), (PartsRegistry.P60, 2), (PartsRegistry.P67, 1),
            (PartsRegistry.P68, 1), (PartsRegistry.P75, 1), (PartsRegistry.P76, 1)
        ]

    def compo_G_1600_700_300_SUITE(k):
        return [
            (PartsRegistry.P4, 6), (PartsRegistry.P17, 1+k), (PartsRegistry.P41, 2*k),
            (PartsRegistry.P45, 1), (PartsRegistry.P48, 1), (PartsRegistry.P51, 1),
            (PartsRegistry.P53, 1), (PartsRegistry.P54, 1), (PartsRegistry.P55, 1),
            (PartsRegistry.P56, 1), (PartsRegistry.P59, 1), (PartsRegistry.P60, 1)
        ]

    def compo_G_1600_500_300(k):
        return [
            (PartsRegistry.P2, 6), (PartsRegistry.P15, 1+k), (PartsRegistry.P41, 2*k),
            (PartsRegistry.P44, 1), (PartsRegistry.P48, 2), (PartsRegistry.P51, 2),
            (PartsRegistry.P53, 2), (PartsRegistry.P54, 2), (PartsRegistry.P55, 2),
            (PartsRegistry.P56, 2), (PartsRegistry.P58, 1), (PartsRegistry.P60, 2),
            (PartsRegistry.P67, 1), (PartsRegistry.P68, 1), (PartsRegistry.P75, 1), (PartsRegistry.P76, 1)
        ]

    def compo_G_1600_700_200(k):
        return [
            (PartsRegistry.P4, 6), (PartsRegistry.P8, 1+k), (PartsRegistry.P40, 2*k),
            (PartsRegistry.P45, 1), (PartsRegistry.P48, 2), (PartsRegistry.P50, 2),
            (PartsRegistry.P53, 2), (PartsRegistry.P54, 2), (PartsRegistry.P55, 2),
            (PartsRegistry.P56, 2), (PartsRegistry.P59, 1), (PartsRegistry.P60, 2),
            (PartsRegistry.P67, 1), (PartsRegistry.P68, 1), (PartsRegistry.P73, 1), (PartsRegistry.P74, 1)
        ]

    def compo_G_1600_700_200_SUITE(k):
        return [
            (PartsRegistry.P4, 6), (PartsRegistry.P8, 1+k), (PartsRegistry.P40, 2*k),
            (PartsRegistry.P45, 1), (PartsRegistry.P48, 1), (PartsRegistry.P50, 1),
            (PartsRegistry.P53, 1), (PartsRegistry.P54, 1), (PartsRegistry.P55, 1),
            (PartsRegistry.P56, 1), (PartsRegistry.P59, 1), (PartsRegistry.P60, 1)
        ]

    def compo_G_1600_500_200(k):
        return [
            (PartsRegistry.P2, 6), (PartsRegistry.P7, 1+k), (PartsRegistry.P40, 2*k),
            (PartsRegistry.P44, 1), (PartsRegistry.P48, 2), (PartsRegistry.P50, 2),
            (PartsRegistry.P53, 2), (PartsRegistry.P54, 2), (PartsRegistry.P55, 2),
            (PartsRegistry.P56, 2), (PartsRegistry.P58, 1), (PartsRegistry.P60, 2),
            (PartsRegistry.P67, 1), (PartsRegistry.P68, 1), (PartsRegistry.P73, 1), (PartsRegistry.P74, 1)
        ]
    
    # --- 5. GONDOLE SIMPLE 1800 (Nouveau - Base + 8) ---
    def compo_G_1800_700_300(k):
        return [
            (PartsRegistry.P3, 6), (PartsRegistry.P4, 2), (PartsRegistry.P17, 1+k), 
            (PartsRegistry.P41, 2*k), (PartsRegistry.P45, 1), (PartsRegistry.P47, 2), 
            (PartsRegistry.P51, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2), 
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P59, 1), 
            (PartsRegistry.P60, 2), (PartsRegistry.P65, 1), (PartsRegistry.P66, 1), 
            (PartsRegistry.P75, 1), (PartsRegistry.P76, 1)
        ]

    def compo_G_1800_700_300_SUITE(k):
        return [
            (PartsRegistry.P3, 6), (PartsRegistry.P4, 2), (PartsRegistry.P17, 1+k), 
            (PartsRegistry.P41, 2*k), (PartsRegistry.P45, 1), (PartsRegistry.P47, 1), 
            (PartsRegistry.P51, 1), (PartsRegistry.P53, 1), (PartsRegistry.P54, 1), 
            (PartsRegistry.P55, 1), (PartsRegistry.P56, 1), (PartsRegistry.P59, 1), 
            (PartsRegistry.P60, 1)
        ]

    def compo_G_1800_500_300(k):
        return [
            (PartsRegistry.P1, 6), (PartsRegistry.P2, 2), (PartsRegistry.P15, 1+k), 
            (PartsRegistry.P41, 2*k), (PartsRegistry.P44, 1), (PartsRegistry.P47, 2), 
            (PartsRegistry.P51, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2), 
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P58, 1), 
            (PartsRegistry.P60, 2), (PartsRegistry.P65, 1), (PartsRegistry.P66, 1), 
            (PartsRegistry.P75, 1), (PartsRegistry.P76, 1)
            ]

    def compo_G_1800_700_200(k):
        return [
            (PartsRegistry.P3, 6), (PartsRegistry.P4, 2), (PartsRegistry.P8, 1+k), 
            (PartsRegistry.P40, 2*k), (PartsRegistry.P45, 1), (PartsRegistry.P47, 2), 
            (PartsRegistry.P50, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2), 
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P59, 1), 
            (PartsRegistry.P60, 2), (PartsRegistry.P65, 1), (PartsRegistry.P66, 1), 
            (PartsRegistry.P73, 1), (PartsRegistry.P74, 1)
            ]

    def compo_G_1800_700_200_SUITE(k):
        return [
            (PartsRegistry.P3, 6), (PartsRegistry.P4, 2), (PartsRegistry.P8, 1+k), 
            (PartsRegistry.P40, 2*k), (PartsRegistry.P45, 1), (PartsRegistry.P47, 1), 
            (PartsRegistry.P50, 1), (PartsRegistry.P53, 1), (PartsRegistry.P54, 1), 
            (PartsRegistry.P55, 1), (PartsRegistry.P56, 1), (PartsRegistry.P59, 1), 
            (PartsRegistry.P60, 1)]

    def compo_G_1800_500_200(k):
        return [
            (PartsRegistry.P1, 6), (PartsRegistry.P2, 2), (PartsRegistry.P7, 1+k), 
            (PartsRegistry.P40, 2*k), (PartsRegistry.P44, 1), (PartsRegistry.P47, 2), 
            (PartsRegistry.P50, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2), 
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P58, 1), 
            (PartsRegistry.P60, 2), (PartsRegistry.P65, 1), (PartsRegistry.P66, 1), 
            (PartsRegistry.P73, 1), (PartsRegistry.P74, 1)
        ]

    # --- 4. EXTENSIBLE VERRE ---
    def compo_V_700_300(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 1), (PartsRegistry.P17, 1),
            (PartsRegistry.P32, k), (PartsRegistry.P39, k), (PartsRegistry.P45, 1),
            (PartsRegistry.P46, 2), (PartsRegistry.P51, 2), (PartsRegistry.P53, 2),
            (PartsRegistry.P54, 2), (PartsRegistry.P55, 2), (PartsRegistry.P56, 2),
            (PartsRegistry.P60, 2), (PartsRegistry.P63, 1), (PartsRegistry.P64, 1),
            (PartsRegistry.P75, 1), (PartsRegistry.P76, 1)
        ]

    def compo_V_700_300_SUITE(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 1), (PartsRegistry.P17, 1),
            (PartsRegistry.P32, k), (PartsRegistry.P39, k), (PartsRegistry.P45, 1),
            (PartsRegistry.P46, 1), (PartsRegistry.P51, 1), (PartsRegistry.P53, 1),
            (PartsRegistry.P54, 1), (PartsRegistry.P55, 1), (PartsRegistry.P56, 1),
            (PartsRegistry.P60, 1)
        ]

    def compo_V_700_200(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 1), (PartsRegistry.P8, 1),
            (PartsRegistry.P30, k), (PartsRegistry.P36, k), (PartsRegistry.P45, 1),
            (PartsRegistry.P46, 2), (PartsRegistry.P50, 2), (PartsRegistry.P53, 2),
            (PartsRegistry.P54, 2), (PartsRegistry.P55, 2), (PartsRegistry.P56, 2),
            (PartsRegistry.P60, 2), (PartsRegistry.P63, 1), (PartsRegistry.P64, 1),
            (PartsRegistry.P73, 1), (PartsRegistry.P74, 1)
        ]

    def compo_V_700_200_SUITE(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 1), (PartsRegistry.P8, 1),
            (PartsRegistry.P30, k), (PartsRegistry.P36, k), (PartsRegistry.P45, 1),
            (PartsRegistry.P46, 1), (PartsRegistry.P50, 1), (PartsRegistry.P53, 1),
            (PartsRegistry.P54, 1), (PartsRegistry.P55, 1), (PartsRegistry.P56, 1),
            (PartsRegistry.P60, 1)
        ]

    def compo_V_500_200(k):
        return [
            (PartsRegistry.P1, 4), (PartsRegistry.P2, 1), (PartsRegistry.P7, 1),
            (PartsRegistry.P29, k), (PartsRegistry.P37, k), (PartsRegistry.P44, 1),
            (PartsRegistry.P46, 2), (PartsRegistry.P50, 2), (PartsRegistry.P53, 2),
            (PartsRegistry.P54, 2), (PartsRegistry.P55, 2), (PartsRegistry.P56, 2),
            (PartsRegistry.P60, 2), (PartsRegistry.P63, 1), (PartsRegistry.P64, 1),
            (PartsRegistry.P73, 1), (PartsRegistry.P74, 1)
        ]

    def compo_V_500_300(k):
        return [
            (PartsRegistry.P1, 4), (PartsRegistry.P2, 1), (PartsRegistry.P15, 1),
            (PartsRegistry.P31, k), (PartsRegistry.P38, k), (PartsRegistry.P44, 1),
            (PartsRegistry.P46, 2), (PartsRegistry.P51, 2), (PartsRegistry.P52, 8),
            (PartsRegistry.P53, 2), (PartsRegistry.P54, 2), (PartsRegistry.P55, 2),
            (PartsRegistry.P56, 2), (PartsRegistry.P60, 2), (PartsRegistry.P63, 1),
            (PartsRegistry.P64, 1), (PartsRegistry.P75, 1), (PartsRegistry.P76, 1),
            (PartsRegistry.P77, 1), (PartsRegistry.P78, 1)
        ]
    

    # --- 6. GONDOLE DOUBLE FACE 1400 (Base + 6) ---
    def compo_G_DB_1400_700_300(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 2), (PartsRegistry.P17, (1+k)*2),
            (PartsRegistry.P41, (2*k)*2), (PartsRegistry.P45, 1), (PartsRegistry.P49, 2),
            (PartsRegistry.P51, 4), (PartsRegistry.P53, 4), (PartsRegistry.P54, 4),
            (PartsRegistry.P55, 4), (PartsRegistry.P56, 4), (PartsRegistry.P59, 1),
            (PartsRegistry.P60, 4), (PartsRegistry.P69, 1), (PartsRegistry.P70, 1),
            (PartsRegistry.P75, 2), (PartsRegistry.P76, 2)
        ]

    def compo_G_DB_1400_700_300_SUITE(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 2), (PartsRegistry.P17, (1+k)*2),
            (PartsRegistry.P41, (2*k)*2), (PartsRegistry.P45, 1), (PartsRegistry.P49, 1),
            (PartsRegistry.P51, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2),
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P59, 1),
            (PartsRegistry.P60, 2)
        ]

    def compo_G_DB_1400_500_300(k):
        return [
            (PartsRegistry.P1, 4), (PartsRegistry.P2, 2), (PartsRegistry.P15, (1+k)*2),
            (PartsRegistry.P41, (2*k)*2), (PartsRegistry.P44, 1), (PartsRegistry.P49, 2),
            (PartsRegistry.P51, 4), (PartsRegistry.P53, 4), (PartsRegistry.P54, 4),
            (PartsRegistry.P55, 4), (PartsRegistry.P56, 4), (PartsRegistry.P58, 1),
            (PartsRegistry.P60, 4), (PartsRegistry.P69, 1), (PartsRegistry.P70, 1),
            (PartsRegistry.P75, 2), (PartsRegistry.P76, 2)
        ]

    def compo_G_DB_1400_700_200(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 2), (PartsRegistry.P8, (1+k)*2),
            (PartsRegistry.P40, (2*k)*2), (PartsRegistry.P45, 1), (PartsRegistry.P49, 2),
            (PartsRegistry.P50, 4), (PartsRegistry.P53, 4), (PartsRegistry.P54, 4),
            (PartsRegistry.P55, 4), (PartsRegistry.P56, 4), (PartsRegistry.P59, 1),
            (PartsRegistry.P60, 4), (PartsRegistry.P69, 1), (PartsRegistry.P70, 1),
            (PartsRegistry.P73, 2), (PartsRegistry.P74, 2)
        ]

    def compo_G_DB_1400_700_200_SUITE(k):
        return [
            (PartsRegistry.P3, 4), (PartsRegistry.P4, 2), (PartsRegistry.P8, (1+k)*2),
            (PartsRegistry.P40, (2*k)*2), (PartsRegistry.P45, 1), (PartsRegistry.P49, 1),
            (PartsRegistry.P50, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2),
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P59, 1),
            (PartsRegistry.P60, 2)
        ]

    def compo_G_DB_1400_500_200(k):
        return [
            (PartsRegistry.P1, 4), (PartsRegistry.P2, 2), (PartsRegistry.P7, (1+k)*2),
            (PartsRegistry.P40, (2*k)*2), (PartsRegistry.P44, 1), (PartsRegistry.P49, 2),
            (PartsRegistry.P50, 4), (PartsRegistry.P53, 4), (PartsRegistry.P54, 4),
            (PartsRegistry.P55, 4), (PartsRegistry.P56, 4), (PartsRegistry.P58, 1),
            (PartsRegistry.P60, 4), (PartsRegistry.P69, 1), (PartsRegistry.P70, 1),
            (PartsRegistry.P73, 2), (PartsRegistry.P74, 2)
        ]
    
    # --- 7. GONDOLE DOUBLE FACE 1600 (Base + 7) ---
    def compo_G_DB_1600_700_300(k):
        return [
            (PartsRegistry.P4, 6), (PartsRegistry.P17, (1+k)*2), (PartsRegistry.P41, (2*k)*2),
            (PartsRegistry.P45, 1), (PartsRegistry.P48, 2), (PartsRegistry.P51, 4),
            (PartsRegistry.P53, 4), (PartsRegistry.P54, 4), (PartsRegistry.P55, 4),
            (PartsRegistry.P56, 4), (PartsRegistry.P59, 1), (PartsRegistry.P60, 4),
            (PartsRegistry.P67, 1), (PartsRegistry.P68, 1), (PartsRegistry.P75, 2), (PartsRegistry.P76, 2)
        ]

    def compo_G_DB_1600_700_300_SUITE(k):
        return [
            (PartsRegistry.P4, 6), (PartsRegistry.P17, (1+k)*2), (PartsRegistry.P41, (2*k)*2),
            (PartsRegistry.P45, 1), (PartsRegistry.P48, 1), (PartsRegistry.P51, 2),
            (PartsRegistry.P53, 2), (PartsRegistry.P54, 2), (PartsRegistry.P55, 2),
            (PartsRegistry.P56, 2), (PartsRegistry.P59, 1), (PartsRegistry.P60, 2)
        ]

    def compo_G_DB_1600_500_300(k):
        return [
            (PartsRegistry.P2, 6), (PartsRegistry.P15, (1+k)*2), (PartsRegistry.P41, (2*k)*2),
            (PartsRegistry.P44, 1), (PartsRegistry.P48, 2), (PartsRegistry.P51, 4),
            (PartsRegistry.P53, 4), (PartsRegistry.P54, 4), (PartsRegistry.P55, 4),
            (PartsRegistry.P56, 4), (PartsRegistry.P58, 1), (PartsRegistry.P60, 4),
            (PartsRegistry.P67, 1), (PartsRegistry.P68, 1), (PartsRegistry.P75, 2), (PartsRegistry.P76, 2)
        ]

    def compo_G_DB_1600_700_200(k):
        return [
            (PartsRegistry.P4, 6), (PartsRegistry.P8, (1+k)*2), (PartsRegistry.P40, (2*k)*2),
            (PartsRegistry.P45, 1), (PartsRegistry.P48, 2), (PartsRegistry.P50, 4),
            (PartsRegistry.P53, 4), (PartsRegistry.P54, 4), (PartsRegistry.P55, 4),
            (PartsRegistry.P56, 4), (PartsRegistry.P59, 1), (PartsRegistry.P60, 4),
            (PartsRegistry.P67, 1), (PartsRegistry.P68, 1), (PartsRegistry.P73, 2), (PartsRegistry.P74, 2)
        ]

    def compo_G_DB_1600_700_200_SUITE(k):
        return [
            (PartsRegistry.P4, 6), (PartsRegistry.P8, (1+k)*2), (PartsRegistry.P40, (2*k)*2),
            (PartsRegistry.P45, 1), (PartsRegistry.P48, 1), (PartsRegistry.P50, 2),
            (PartsRegistry.P53, 2), (PartsRegistry.P54, 2), (PartsRegistry.P55, 2),
            (PartsRegistry.P56, 2), (PartsRegistry.P59, 1), (PartsRegistry.P60, 2)
        ]

    def compo_G_DB_1600_500_200(k):
        return [
            (PartsRegistry.P2, 6), (PartsRegistry.P7, (1+k)*2), (PartsRegistry.P40, (2*k)*2),
            (PartsRegistry.P44, 1), (PartsRegistry.P48, 2), (PartsRegistry.P50, 4),
            (PartsRegistry.P53, 4), (PartsRegistry.P54, 4), (PartsRegistry.P55, 4),
            (PartsRegistry.P56, 4), (PartsRegistry.P58, 1), (PartsRegistry.P60, 4),
            (PartsRegistry.P67, 1), (PartsRegistry.P68, 1), (PartsRegistry.P73, 2), (PartsRegistry.P74, 2)
        ]
    
    # --- 8. GONDOLE DOUBLE FACE 1800 (Base + 8) ---
    def compo_G_DB_1800_700_300(k):
        return [
            (PartsRegistry.P3, 6), (PartsRegistry.P4, 2), (PartsRegistry.P17, (1+k)*2),
            (PartsRegistry.P41, (2*k)*2), (PartsRegistry.P45, 1), (PartsRegistry.P47, 2),
            (PartsRegistry.P51, 4), (PartsRegistry.P53, 4), (PartsRegistry.P54, 4),
            (PartsRegistry.P55, 4), (PartsRegistry.P56, 4), (PartsRegistry.P59, 1),
            (PartsRegistry.P60, 4), (PartsRegistry.P65, 1), (PartsRegistry.P66, 1),
            (PartsRegistry.P75, 2), (PartsRegistry.P76, 2)
        ]

    def compo_G_DB_1800_700_300_SUITE(k):
        return [
            (PartsRegistry.P3, 6), (PartsRegistry.P4, 2), (PartsRegistry.P17, (1+k)*2),
            (PartsRegistry.P41, (2*k)*2), (PartsRegistry.P45, 1), (PartsRegistry.P47, 1),
            (PartsRegistry.P51, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2),
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P59, 1),
            (PartsRegistry.P60, 2)
        ]

    def compo_G_DB_1800_500_300(k):
        return [
            (PartsRegistry.P1, 6), (PartsRegistry.P2, 2), (PartsRegistry.P15, (1+k)*2),
            (PartsRegistry.P41, (2*k)*2), (PartsRegistry.P44, 1), (PartsRegistry.P47, 2),
            (PartsRegistry.P51, 4), (PartsRegistry.P53, 4), (PartsRegistry.P54, 4),
            (PartsRegistry.P55, 4), (PartsRegistry.P56, 4), (PartsRegistry.P58, 1),
            (PartsRegistry.P60, 4), (PartsRegistry.P65, 1), (PartsRegistry.P66, 1),
            (PartsRegistry.P75, 2), (PartsRegistry.P76, 2)
        ]

    def compo_G_DB_1800_700_200(k):
        return [
            (PartsRegistry.P3, 6), (PartsRegistry.P4, 2), (PartsRegistry.P8, (1+k)*2),
            (PartsRegistry.P40, (2*k)*2), (PartsRegistry.P45, 1), (PartsRegistry.P47, 2),
            (PartsRegistry.P50, 4), (PartsRegistry.P53, 4), (PartsRegistry.P54, 4),
            (PartsRegistry.P55, 4), (PartsRegistry.P56, 4), (PartsRegistry.P59, 1),
            (PartsRegistry.P60, 4), (PartsRegistry.P65, 1), (PartsRegistry.P66, 1),
            (PartsRegistry.P73, 2), (PartsRegistry.P74, 2)
        ]

    def compo_G_DB_1800_700_200_SUITE(k):
        return [
            (PartsRegistry.P3, 6), (PartsRegistry.P4, 2), (PartsRegistry.P8, (1+k)*2),
            (PartsRegistry.P40, (2*k)*2), (PartsRegistry.P45, 1), (PartsRegistry.P47, 1),
            (PartsRegistry.P50, 2), (PartsRegistry.P53, 2), (PartsRegistry.P54, 2),
            (PartsRegistry.P55, 2), (PartsRegistry.P56, 2), (PartsRegistry.P59, 1),
            (PartsRegistry.P60, 2)
        ]

    def compo_G_DB_1800_500_200(k):
        return [
            (PartsRegistry.P1, 6), (PartsRegistry.P2, 2), (PartsRegistry.P7, (1+k)*2),
            (PartsRegistry.P40, (2*k)*2), (PartsRegistry.P44, 1), (PartsRegistry.P47, 2),
            (PartsRegistry.P50, 4), (PartsRegistry.P53, 4), (PartsRegistry.P54, 4),
            (PartsRegistry.P55, 4), (PartsRegistry.P56, 4), (PartsRegistry.P58, 1),
            (PartsRegistry.P60, 4), (PartsRegistry.P65, 1), (PartsRegistry.P66, 1),
            (PartsRegistry.P73, 2), (PartsRegistry.P74, 2)
        ]

    # --- CONFIGURATION DES PRODUITS PAR CATÉGORIE ---
    CATEGORIES = {
        "Extensible": {
            "L2200_400": ProduitCompose("Linéaire 2200 x 400", composition_L2200_400),
            "L2200_300": ProduitCompose("Linéaire 2200 x 300", composition_L2200_300),
            "L2200_200": ProduitCompose("Linéaire 2200 x 200", composition_L2200_200),
        },
        "Extensible Métal": {
            "M_700_300": ProduitCompose("LINEAIRE 2200x700x300 (Métal)", compo_M_700_300),
            "M_700_300_S": ProduitCompose("SUITE LINEAIRE 2200x700x300 (Métal)", compo_M_700_300_SUITE),
            "M_700_200": ProduitCompose("LINEAIRE 2200x700x200 (Métal)", compo_M_700_200),
            "M_700_200_S": ProduitCompose("SUITE LINEAIRE 2200x700x200 (Métal)", compo_M_700_200_SUITE),
            "M_500_200": ProduitCompose("LINEAIRE 2200x500x200 (Métal)", compo_M_500_200),
            "M_500_300": ProduitCompose("LINEAIRE 2200x500x300 (Métal)", compo_M_500_300),
        },
        "Gondole simple": {
            "1400": {
            "G_1400_700_300": ProduitCompose("GONDOLE SIMPLE 1400x700x300", compo_G_1400_700_300),
            "G_1400_700_300_S": ProduitCompose("SUITE GONDOLE SIMPLE 1400x700x300", compo_G_1400_700_300_SUITE),
            "G_1400_500_300": ProduitCompose("GONDOLE SIMPLE 1400x500x300", compo_G_1400_500_300),
            "G_1400_700_200": ProduitCompose("GONDOLE SIMPLE 1400x700x200", compo_G_1400_700_200),
            "G_1400_700_200_S": ProduitCompose("SUITE GONDOLE SIMPLE 1400x700x200", compo_G_1400_700_200_SUITE),
            "G_1400_500_200": ProduitCompose("GONDOLE SIMPLE 1400x500x200", compo_G_1400_500_200),
            },    
            "1600": {
                "G_1600_700_300": ProduitCompose("GONDOLE SIMPLE 1600x700x300", compo_G_1600_700_300),
                "G_1600_700_300_S": ProduitCompose("SUITE GONDOLE SIMPLE 1600x700x300", compo_G_1600_700_300_SUITE),
                "G_1600_500_300": ProduitCompose("GONDOLE SIMPLE 1600x500x300", compo_G_1600_500_300),
                "G_1600_700_200": ProduitCompose("GONDOLE SIMPLE 1600x700x200", compo_G_1600_700_200),
                "G_1600_700_200_S": ProduitCompose("SUITE GONDOLE SIMPLE 1600x700x200", compo_G_1600_700_200_SUITE),
                "G_1600_500_200": ProduitCompose("GONDOLE SIMPLE 1600x500x200", compo_G_1600_500_200),
            },
            "1800": {
                "G_1800_700_300": ProduitCompose("GONDOLE SIMPLE 1800x700x300", compo_G_1800_700_300),
                "G_1800_700_300_S": ProduitCompose("SUITE GONDOLE SIMPLE 1800x700x300", compo_G_1800_700_300_SUITE),
                "G_1800_500_300": ProduitCompose("GONDOLE SIMPLE 1800x500x300", compo_G_1800_500_300),
                "G_1800_700_200": ProduitCompose("GONDOLE SIMPLE 1800x700x200", compo_G_1800_700_200),
                "G_1800_700_200_S": ProduitCompose("SUITE GONDOLE SIMPLE 1800x700x200", compo_G_1800_700_200_SUITE),
                "G_1800_500_200": ProduitCompose("GONDOLE SIMPLE 1800x500x200", compo_G_1800_500_200),
            }
        },

        "Gondole Double": {
            "1400": {
                "G_DB_1400_700_300": ProduitCompose("GONDOLE DOUBLE FACE 1400x700x300", compo_G_DB_1400_700_300),
                "G_DB_1400_700_300_S": ProduitCompose("SUITE GONDOLE DB FACE 1400x700x300", compo_G_DB_1400_700_300_SUITE),
                "G_DB_1400_500_300": ProduitCompose("GONDOLE DOUBLE FACE 1400x500x300", compo_G_DB_1400_500_300),
                "G_DB_1400_700_200": ProduitCompose("GONDOLE DOUBLE FACE 1400x700x200", compo_G_DB_1400_700_200),
                "G_DB_1400_700_200_S": ProduitCompose("SUITE GONDOLE DB FACE 1400x700x200", compo_G_DB_1400_700_200_SUITE),
                "G_DB_1400_500_200": ProduitCompose("GONDOLE DOUBLE FACE 1400x500x200", compo_G_DB_1400_500_200),
            },
            "1600": {
                "G_DB_1600_700_300": ProduitCompose("GONDOLE DOUBLE FACE 1600x700x300", compo_G_DB_1600_700_300),
                "G_DB_1600_700_300_S": ProduitCompose("SUITE GONDOLE DB FACE 1600x700x300", compo_G_DB_1600_700_300_SUITE),
                "G_DB_1600_500_300": ProduitCompose("GONDOLE DOUBLE FACE 1600x500x300", compo_G_DB_1600_500_300),
                "G_DB_1600_700_200": ProduitCompose("GONDOLE DOUBLE FACE 1600x700x200", compo_G_DB_1600_700_200),
                "G_DB_1600_700_200_S": ProduitCompose("SUITE GONDOLE DB FACE 1600x700x200", compo_G_DB_1600_700_200_SUITE),
                "G_DB_1600_500_200": ProduitCompose("GONDOLE DOUBLE FACE 1600x500x200", compo_G_DB_1600_500_200),
            },
            "1800": {
                "G_DB_1800_700_300": ProduitCompose("GONDOLE DOUBLE FACE 1800x700x300", compo_G_DB_1800_700_300),
                "G_DB_1800_700_300_S": ProduitCompose("SUITE GONDOLE DB FACE 1800x700x300", compo_G_DB_1800_700_300_SUITE),
                "G_DB_1800_500_300": ProduitCompose("GONDOLE DOUBLE FACE 1800x500x300", compo_G_DB_1800_500_300),
                "G_DB_1800_700_200": ProduitCompose("GONDOLE DOUBLE FACE 1800x700x200", compo_G_DB_1800_700_200),
                "G_DB_1800_700_200_S": ProduitCompose("SUITE GONDOLE DB FACE 1800x700x200", compo_G_DB_1800_700_200_SUITE),
                "G_DB_1800_500_200": ProduitCompose("GONDOLE DOUBLE FACE 1800x500x200", compo_G_DB_1800_500_200),
            }
        },
        
        "Extensible Verre": {
            "V_700_300": ProduitCompose("LINEAIRE 2200x700x300 (Verre)", compo_V_700_300),
            "V_700_300_S": ProduitCompose("SUITE LINEAIRE 2200x700x300 (Verre)", compo_V_700_300_SUITE),
            "V_700_200": ProduitCompose("LINEAIRE 2200x700x200 (Verre)", compo_V_700_200),
            "V_700_200_S": ProduitCompose("SUITE LINEAIRE 2200x700x200 (Verre)", compo_V_700_200_SUITE),
            "V_500_200": ProduitCompose("LINEAIRE 2200x500x200 (Verre)", compo_V_500_200),
            "V_500_300": ProduitCompose("LINEAIRE 2200x500x300 (Verre)", compo_V_500_300),
        }
    }

    # Liste plate pour la recherche par ID dans app.py
    # --- LOGIQUE DE FLATTENING CORRIGÉE ---
    PRODUCTS = {}
    for cat_name, content in CATEGORIES.items():
        # On vérifie si le premier élément est un dictionnaire (cas des Gondoles)
        first_item = next(iter(content.values()))
        if isinstance(first_item, dict):
            # C'est une catégorie imbriquée (ex: Gondole -> 1400 -> Produits)
            for sub_content in content.values():
                PRODUCTS.update(sub_content)
        else:
            # C'est une catégorie plate (ex: Extensible -> Produits)
            PRODUCTS.update(content)