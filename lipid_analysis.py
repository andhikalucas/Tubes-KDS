import numpy as np
import pandas as pd

# ==============================================================================
# PARAMETER GLOBAL & KONSTANTA (Sesuai Konteks Biokimia WHO/Harvard)
# ==============================================================================
# Base assumptions for scoring standard lengths and properties
THRESHOLD_CARBON = 18.0 
W_SATURATED = 2.5  # Moderate penalty for LDL accumulation
W_TRANS = 4.0      # Maximum penalty for dual impact (raises LDL, lowers HDL)
W_CIS = 1.5        # Risk reduction incentive for vascular flexibility
W_CARBON = 0.05    # Multiplier for hydrophobic pathology tendency

import numpy as np
import pandas as pd

def create_lipid_dataset(n_random=50) -> pd.DataFrame:
    """
    Menginisialisasi dataset gabungan: 
    1. Data faktual konstan (referensi riil)
    2. Data acak teoretis (in silico screening)
    """
    
    factual_data = {
        'Molecule_Name': [
            # Saturated Fats (Aterogenik)
            'Palmitic Acid', 'Stearic Acid', 'Myristic Acid', 'Arachidic Acid',
            # Cis-Unsaturated (Kardioprotektif)
            'Oleic Acid', 'Linoleic Acid', 'Arachidonic Acid', 'EPA',
            # Trans-Unsaturated (Sangat Aterogenik)
            'Elaidic Acid', 'Linoelaidic Acid', 'Vaccenic Acid'
        ],
        'Carbon_Length': [
            16, 18, 14, 20,  # Saturated
            18, 18, 20, 20,  # Cis
            18, 18, 18       # Trans
        ],
        'Double_Bonds': [
            0, 0, 0, 0,      # Saturated
            1, 2, 4, 5,      # Cis
            1, 2, 1          # Trans
        ],
        'Isomer_Type': [
            'none', 'none', 'none', 'none',
            'cis', 'cis', 'cis', 'cis',
            'trans', 'trans', 'trans'
        ]
    }
    df_factual = pd.DataFrame(factual_data)
    df_factual['Data_Source'] = 'Factual Reference'

    np.random.seed(42) 
    
    synthetic_carbons = np.random.choice([12, 14, 16, 18, 20, 22, 24], n_random)
    
    synthetic_bonds = [np.random.randint(0, (c // 3)) for c in synthetic_carbons] 
    
    synthetic_isomers = []
    for b in synthetic_bonds:
        if b == 0:
            synthetic_isomers.append('none')
        else:
            synthetic_isomers.append(np.random.choice(['cis', 'trans'], p=[0.7, 0.3]))

    synthetic_data = {
        'Molecule_Name': [f'Synthetic_Lipid_{i+1}' for i in range(n_random)],
        'Carbon_Length': synthetic_carbons,
        'Double_Bonds': synthetic_bonds,
        'Isomer_Type': synthetic_isomers
    }
    df_synthetic = pd.DataFrame(synthetic_data)
    df_synthetic['Data_Source'] = 'Synthetic Random'

    df_combined = pd.concat([df_factual, df_synthetic], ignore_index=True)
    return df_combined

def extract_structural_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Mengekstrak data kualitatif menjadi matriks biner (0/1) secara tervektor.
    """
    df = df.copy()
    
    # Vectorized boolean mapping to represent biochemical properties
    df['is_saturated'] = np.where(df['Double_Bonds'] == 0, 1, 0)
    df['is_trans'] = np.where(df['Isomer_Type'].str.lower() == 'trans', 1, 0)
    df['is_cis'] = np.where(df['Isomer_Type'].str.lower() == 'cis', 1, 0)
    
    return df

def calculate_srs_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Mengeksekusi formula matematika SRS secara tervektor untuk menghitung risiko struktural.
    """
    df = df.copy()
    
    # SRS Formula implementation: Evaluates structural danger based on global clinical evidence
    df['Risk_Score'] = (
        (W_SATURATED * df['is_saturated']) + 
        (W_TRANS * df['is_trans']) - 
        (W_CIS * df['is_cis']) + 
        (W_CARBON * (df['Carbon_Length'] / THRESHOLD_CARBON))
    )
    
    return df

def classify_risk_level(df: pd.DataFrame) -> pd.DataFrame:
    """
    Melakukan klasifikasi makro (binning) menjadi label diskret menggunakan pengondisian.
    """
    df = df.copy()
    
    # Define macro risk levels using numpy's select for vectorized conditional logic
    conditions = [
        (df['Risk_Score'] < 2.0),
        (df['Risk_Score'] >= 2.0) & (df['Risk_Score'] <= 4.5),
        (df['Risk_Score'] > 4.5)
    ]
    choices = ['Low Risk', 'Moderate Risk', 'High Risk']
    
    df['Risk_Level'] = np.select(conditions, choices, default='Unknown')
    
    return df

# ==============================================================================
# VALIDASI SISTEM & UNIT TESTING
# ==============================================================================
def test_biochemical_integrity():
    """
    Blok pengujian fungsionalitas logika otomatis.
    Memastikan hukum dasar biokimia lipid terpenuhi dalam scoring.
    """
    # Setup test case isolating isomer impact on 18-carbon chains
    test_data = pd.DataFrame({
        'Molecule_Name': ['Test Cis', 'Test Trans', 'Test Saturated'],
        'Carbon_Length': [18, 18, 18],
        'Double_Bonds': [1, 1, 0],
        'Isomer_Type': ['cis', 'trans', 'none']
    })
    
    df_features = extract_structural_features(test_data)
    df_scored = calculate_srs_score(df_features)
    
    score_cis = df_scored.loc[df_scored['Molecule_Name'] == 'Test Cis', 'Risk_Score'].values[0]
    score_trans = df_scored.loc[df_scored['Molecule_Name'] == 'Test Trans', 'Risk_Score'].values[0]
    score_sat = df_scored.loc[df_scored['Molecule_Name'] == 'Test Saturated', 'Risk_Score'].values[0]

    # Assertion 1: Trans isomers must be strictly more atherogenic than Cis isomers
    assert score_trans > score_cis, f"Biochemical logic error: Trans ({score_trans}) must score higher than Cis ({score_cis})"
    
    # Assertion 2: Trans fats must score highest overall due to double penalty logic
    assert score_trans > score_sat, f"Biochemical logic error: Trans ({score_trans}) must score higher than Saturated ({score_sat})"
    
    # Assertion 3: Cis fats should demonstrate negative/protective scoring compared to baseline
    assert score_cis < score_sat, "Biochemical logic error: Cis should act as a risk reducer compared to Saturated fats"
    
    print("Unit Testing: OK. All biochemical integrity constraints passed.")

# ==============================================================================
# RUNTIME EXECUTOR
# ==============================================================================
if __name__ == "__main__":
    # 1. Run unit tests to validate logic
    print("--- Running Tests ---")
    test_biochemical_integrity()
    
    # 2. Execute main pipeline
    print("\n--- Executing Lipid Analysis Pipeline ---")
    raw_data = create_lipid_dataset()
    features_data = extract_structural_features(raw_data)
    scored_data = calculate_srs_score(features_data)
    final_results = classify_risk_level(scored_data)
    
    # 3. Output results
    output_columns = ['Molecule_Name', 'Carbon_Length', 'Double_Bonds', 'Isomer_Type', 'Risk_Score', 'Risk_Level']
    print("\n[ Final Structural Risk Report ]")
    print(final_results[output_columns].to_string(index=False))