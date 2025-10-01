import pandas as pd
cliente= pd.read_csv('cliente.csv')
garanzie= pd.read_csv('garanzie.csv')
polizze= pd.read_csv('polizze.csv')
preventivi= pd.read_csv('preventivi.csv')

#inner join - polize per id_cliente
#se ripetizioni in lista 



print("TABELLE ORIGINALI")



# ============================================================================
# VISTA 1: INNER JOIN tra CLIENTE e POLIZZA con aggregazione
# ============================================================================

print("VISTA 1: INNER JOIN CLIENTE-POLIZZA (clienti con almeno una polizza)")


# Inner join tra cliente e polizza
df_inner = pd.merge(cliente, polizze, on='id_cliente', how='inner')

# Aggregazione per cliente
vista_cliente_polizza_inner = df_inner.groupby([
    'id_cliente', 
    'anno_nascita', 
    'cod_sesso', 
    'flg_persona_giuridica',
    'flg_figli_conviv',
    'cod_provincia_residenza',
    'comune_residenza',
    'cap_residenza'
]).agg({
    'id_polizza': list,
    'numero_preventivo_generante': list,
    'data_decorrenza': list
}).reset_index()

print(vista_cliente_polizza_inner)

# ============================================================================
# VISTA 2: FULL OUTER JOIN tra CLIENTE e POLIZZA con aggregazione
# ============================================================================

print("VISTA 2: FULL OUTER JOIN CLIENTE-POLIZZA (tutti i clienti e tutte le polizze)")


# Full outer join tra cliente e polizza
df_outer = pd.merge(cliente, polizze, on='id_cliente', how='outer')

# Aggregazione per cliente (gestendo i NaN)
vista_cliente_polizza_outer = df_outer.groupby([
    'id_cliente', 
    'anno_nascita', 
    'cod_sesso', 
    'flg_persona_giuridica',
    'flg_figli_conviv',
    'cod_provincia_residenza',
    'comune_residenza',
    'cap_residenza'
], dropna=False).agg({
    'id_polizza': lambda x: list(x.dropna()) if x.notna().any() else None,
    'numero_preventivo_generante': lambda x: list(x.dropna()) if x.notna().any() else None,
    'data_decorrenza': lambda x: list(x.dropna()) if x.notna().any() else None
}).reset_index()

print(vista_cliente_polizza_outer)

# ============================================================================
# VISTA 3 (BONUS): Join completo CLIENTE-POLIZZA-PREVENTIVO-GARANZIE
# ============================================================================
print("\n" + "=" * 100)
print("VISTA 3 (BONUS): Join completo con PREVENTIVO e GARANZIE")
print("=" * 100)

# Join tra polizza e preventivo
df_polizza_prev = pd.merge(
    polizze, 
    preventivi, 
    left_on='numero_preventivo_generante', 
    right_on='numero_preventivo', 
    how='inner'
)

# Join con garanzie
df_completo = pd.merge(
    df_polizza_prev,
    garanzie,
    on='id_preventivo',
    how='left'
)

# Join con cliente
df_completo = pd.merge(
    cliente,
    df_completo,
    on='id_cliente',
    how='inner'
)

# Aggregazione completa
vista_completa = df_completo.groupby([
    'id_cliente',
    'anno_nascita',
    'cod_sesso',
    'comune_residenza'
]).agg({
    'id_polizza': list,
    'numero_preventivo_generante': list,
    'data_decorrenza': list,
    'canale': list,
    'premio': list,
    'cod_marca': list,
    'desc_marca': list,
    'cod_garanzia': lambda x: [list(set(x))] if x.notna().any() else None  # garanzie uniche per cliente
}).reset_index()

print(vista_completa)

print("\n" + "=" * 100)
print("RIEPILOGO:")
print("=" * 100)
print("✓ VISTA 1 (INNER): Solo clienti con almeno una polizza")
print("✓ VISTA 2 (OUTER): Tutti i clienti, anche senza polizze (con liste None)")
print("✓ VISTA 3 (BONUS): Vista completa con preventivi e garanzie aggregate")

vista_cliente_polizza_outer = df_outer.groupby([
    'id_cliente', 
    'anno_nascita', 
    'cod_sesso', 
    'flg_persona_giuridica',
    'flg_figli_conviv',
    'cod_provincia_residenza',
    'comune_residenza',
    'cap_residenza'
], dropna=False).agg({
    'id_polizza': lambda x: list(x.dropna()) if x.notna().any() else None,
    'numero_preventivo_generante': lambda x: list(x.dropna()) if x.notna().any() else None,
    'data_decorrenza': lambda x: list(x.dropna()) if x.notna().any() else None
}).reset_index()

# Salvataggio VISTA 2
vista_cliente_polizza_outer.to_csv('vista_cliente_polizza_outer.csv', index=False, encoding='utf-8-sig')
print("✓ VISTA 2 salvata in: vista_cliente_polizza_outer.csv")
print(f"  Righe: {len(vista_cliente_polizza_outer)}")
print(vista_cliente_polizza_outer.head())

print("\n" + "=" * 100)
print("COMPLETATO!")
