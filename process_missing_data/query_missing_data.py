"""
En suivant les métadonnées de l'OMS

Données personnelles:           Identifiant (généré)
                                Nom (Obligatoire)
                                Prénom (Obligatoire)
                                Age (Obligatoire)
                                Sexe (Obligatoire)
                                Provenance (Obligatoire)
                                Tel (Obligatoire)
                                Location
                                Date de début des symptômes

Date de collecte de l'échantillon
Historique de voyage
Cluster or isolate name TODO: Champ à créer

Symptoms: 	                    fièvre (≥ 38 ºC) 
                                Toux 
                                mal de gorge
                                difficultés respiratoires
                                incapacité de boire ou de téter ;
                                tirage costal ou stridor chez l'enfant calme ;
                                léthargie ou inconscience ;
                                vomit tout ;
                                convulsions ou ATCD de convulsions liées à la présente symptomatologie ;  =====> maladie_neurologique_ou_neuromusculaire_chronique
                                polypnée.
                                enfant décédé d'une affection respiratoire aiguë inexpliquée

                                essoufflement 
                                difficultés respiratoires
                                Appropriate degree of symptoms; may include 
                                "severe”, “mild” and “out of norm”

Clinical outcome if known 	    No standard format 
                                Appropriate formats may include “recovered”, 
                                “death” and “unknown” 

                                Combien de temps après

Specimen source, sample type    No standard format  
                                Examples: “sputum”, “blood”, “serum”, 
                                “saliva”, “stool”, “nasopharyngeal swab”

Sequencing technology 	        No standard format  
                                Ideally, this should include the laboratory approach and sequencing platform (e.g. 
                                “Metagenomics on Illumina HiSeq 2500” or 
                                “ARTIC PCR primer scheme on ONT 
                                MinION”) 

Minimum  sequencing depth required 
to call sites during consensus sequence generation 	e.g. 20x 	Sequencing artefacts
"""

import pandas as pd
import numpy as np
from datetime import datetime


def query_missing_data(path: str, section: str):
    investigateurs = ['DAO PASCALI E', 'DAO pascaline', 'DAO Pascaline', 'DAO Pascaline', 'DAO PASCALINE', 'DAO PASCALINE',
                    'DAO,PASCALINE', 'KONDOMBO GREGOIRE ', 'KONDOMBO GREGOIRE', 'kondombo gregoire', 'ouedraogo carine', 'ouedraogo carine',
                    'Ouedraogo carine', 'OUEDRAOGO carine', 'OUEDRAOGO CARINE', 'SOMBIE FATIMA', 'sombié fatima', 'SOMBIE', 'SOMBIE Fatima',
                    'SOMBIE FATIMA', 'SOMBIE Fatima Madiamsé']

    iter_csv = pd.read_csv(path, iterator=True, chunksize=1000)
    iter_csv[["Event date", "Enrollment date"]] = iter_csv[["Event date", "Enrollment date"]].apply(pd.to_datetime)
    df = pd.concat([chunk[chunk['Event data'] > datetime(2022, 9, 9) & (chunk['Nom de l\'investigateur'].isin(investigateurs))] for chunk in iter_csv])

    df_queries = pd.DataFrame(columns=['Code Echantillon', 'Nom de l\'investigateur', 'District sanitaire', 'Valeur actuelle', 'Erreurs/Confirmations', 'Actions', 'Section', 'Valeur souhaitée', 'Observations'])
    # iterate through each row and select
    for i in df.index:
        if section == 'Section 1':  
    #         # =========================== Check des TYPE DE RESIDENCE =============================
    #         if df['Residence type'][i] is np.nan:
    #             residence_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['Residence type'][i],
    #                 'Erreurs/Confirmations' : 'Type de résidence non spécifié',
    #                 'Actions' : 'Sélectionner le type de résidence du patient',
    #                 'Section' : section,
    #                 'Valeur souhaitée': 'Urbain ou rural',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, residence_query], ignore_index=True)

    #         # =========================== Check des DU NOM DU TUTEUR =============================
    #         if (df['Nom du père /de la mère/du tuteur'][i] is np.nan and df['Age en années\xa0'][i] < 5) and (df['Age en jours (si<1 mois)'][i] is not np.nan or df['Age en jours (si<1 mois)'][i] is not np.nan):
    #             tuteur_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['Nom du père /de la mère/du tuteur'][i],
    #                 'Erreurs/Confirmations' : f"Age en années , Age en mois {df['Age en mois (si<12 mois)'][i]}, Age en jours {df['Age en jours (si<1 mois)'][i]}",
    #                 'Actions' : 'Il n\'y a pas de tuteur alors que le patient a moins de 5 ans',
    #                 'Section' : section,
    #                 'Valeur souhaitée': 'Nom du tuteur',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries,tuteur_query], ignore_index=True)
            
    #         # =========================== Check des NUMERO DE TELEPHONE DU PATIENT OU DES PARENTS =============================
    #         if df['N° téléphone du patient ou des parents'][i] is np.nan:
    #             tel_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['N° téléphone du patient ou des parents'][i],
    #                 'Erreurs/Confirmations' : 'Pas de numéro de téléphone du patient ou des parents',
    #                 'Actions' : 'Renseigner le numéro de téléphone',
    #                 'Section' : section,
    #                 'Valeur souhaitée': 'ex: 70010203',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, tel_query], ignore_index=True)

    #         # =========================== Check des DISTRICTS DE RESIDENCE =============================
    #         if df['District de residence'][i] is np.nan:
    #             district_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['District de residence'][i],
    #                 'Erreurs/Confirmations' : 'Pas de district de résidence, confirmer?',
    #                 'Actions' : 'Renseigner Disctrict de résidence',
    #                 'Section' : section,
    #                 'Valeur souhaitée': 'ex: DS Dafra',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, district_query], ignore_index=True) 
        
        elif section == 'Section 2':
    #         # =========================== Check des COORDONNEES GPS =============================
    #         if np.isnan(df["Geometry"][i]):
    #             geometry_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['Geometry'][i],
    #                 'Erreurs/Confirmations' : 'Coordonnées GPS manquantes',
    #                 'Actions' : 'Mettre à jour les coordonnées GPS',
    #                 'Section' : section,
    #                 'Valeur souhaitée': 'GPS',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, geometry_query], ignore_index=True)

    #         # =========================== Check de la temperature =============================
    #         if np.isnan(df["COVID Temperature"][i]):
    #             temp_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['COVID Temperature'][i],
    #                 'Erreurs/Confirmations' : 'Température non renseignée',
    #                 'Actions' : 'Renseigner la température du patient',
    #                 'Section' : section,
    #                 'Valeur souhaitée': 'Température',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, temp_query], ignore_index=True)

    #         # =========================== Check des SYMPTOMES =============================
    #         if df['COVID Date d’apparition des symptomes'][i] is np.nan:
    #             date_sympt_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['COVID Date d’apparition des symptomes'][i],
    #                 'Erreurs/Confirmations' : 'Pas de date d\'apparition des symptômes',
    #                 'Actions' : 'Renseigner la date d\'apparition des symptômes',
    #                 'Section' : section,
    #                 'Valeur souhaitée': 'ex: DS Dafra',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, date_sympt_query], ignore_index=True)

    #         # =========================== Check de la fievre =============================
    #         if df['COVID Fievre / Antecedent de fievre / frissons'][i] is np.nan:
    #             fievre_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['COVID Fievre / Antecedent de fievre / frissons'][i],
    #                 'Erreurs/Confirmations' : 'Pas de réponse',
    #                 'Actions' : 'Renseigner si Fievre/Antecedent de fievre Oui ou Non ',
    #                 'Section' : section,
    #                 'Valeur souhaitée': 'Oui ou Non',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, fievre_query], ignore_index=True)

            # =========================== Check de la toux =============================
            if df['COVID Toux'][i] is np.nan:
                toux_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'Disctrict sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Toux'][i],
                    'Erreurs/Confirmations' : 'Pas de réponse',
                    'Actions' : 'Renseigner si Toux Oui ou Non ',
                    'Section' : section,
                    'Valeur souhaitée': 'Oui ou Non',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, toux_query], ignore_index=True)

    #         # =========================== Check des vomissements =============================
    #         if df['COVID Nausee/vomissement'][i] is np.nan:
    #             vomiss_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['COVID Nausee/vomissement'][i],
    #                 'Erreurs/Confirmations' : 'Pas de réponse',
    #                 'Actions' : 'Renseigner si Nausée/vomissement Oui ou Non ',
    #                 'Section' : section,
    #                 'Valeur souhaitée': 'Oui ou Non',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, vomiss_query], ignore_index=True)
                
    #         # =========================== Check du manque d'air =============================
    #         if df['COVID Essoufflement, manque d’air'][i] is np.nan:
    #             essouf_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['COVID Essoufflement, manque d’air'][i],
    #                 'Erreurs/Confirmations' : 'Pas de réponse',
    #                 'Actions' : 'Renseigner si Essoufflement/manque d\'air Oui ou Non ',
    #                 'Section' : section,
    #                 'Valeur souhaitée': 'Oui ou Non',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, essouf_query], ignore_index=True)
                
    #     elif section == 'Section 3':
    #         # =========================== Check du STATU MATRIMONIAL =============================
    #         if df['Statut matrimonial'][i] is np.nan:
    #             statut_mat_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['Statut matrimonial'][i],
    #                 'Erreurs/Confirmations' : 'Pas de statut matrimonial du patient',
    #                 'Actions' : 'Renseigner le statut matrimonial du patient',
    #                 'Section' : 'Section 3',
    #                 'Valeur souhaitée': 'ex: Celibataire',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, statut_mat_query], ignore_index=True)
            
    #         # =========================== Check des antécédants de voyages =============================
    #         if df['COVID Le patient a-t-il voyagé au cours des 14 jours précédant l\'apparition des symptômes'][i] is np.nan:
    #             antec_voyage_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['COVID Le patient a-t-il voyagé au cours des 14 jours précédant l\'apparition des symptômes'][i],
    #                 'Erreurs/Confirmations' : 'Pas d\'information de voyage',
    #                 'Actions' : 'Le patient à t-il voyagé Oui ou Non',
    #                 'Section' : 'Section 3',
    #                 'Valeur souhaitée': 'Oui ou Non',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, antec_voyage_query], ignore_index=True)

    #         # =========================== Check de pays de voyage =============================
    #         if df['COVID Le patient a-t-il voyagé au cours des 14 jours précédant l\'apparition des symptômes'][i] == 'Oui' and df['COVID Pays de voyage 1'][i] is np.nan:
    #             pays_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['COVID Pays de voyage 1'][i],
    #                 'Erreurs/Confirmations' : 'Patient ayant voyagé mais pas d\'information de pays',
    #                 'Actions' : 'Renseigner le(s) pays de voyage',
    #                 'Section' : 'Section 3',
    #                 'Valeur souhaitée': 'Exemple: Burkina Faso',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, pays_query], ignore_index=True)
                    
    #         # =========================== Check de ville de voyage =============================
    #         if df['COVID Le patient a-t-il voyagé au cours des 14 jours précédant l\'apparition des symptômes'][i] == 'Oui' and df['COVID Ville du Pays de voyage 1'][i] is np.nan:
    #             ville_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['COVID Ville du Pays de voyage 1'][i],
    #                 'Erreurs/Confirmations' : 'Patient ayant voyagé mais pas d\'information de la ville',
    #                 'Actions' : 'Renseigner la ville de voyage',
    #                 'Section' : 'Section 3',
    #                 'Valeur souhaitée': 'Exemple: Kaya',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, ville_query], ignore_index=True)

    #     elif section == 'Section 4':
    #         # =========================== Check de la date de prélèvement de l'échantillon =============================
    #         if df['COVID Date du prelevement'][i] is np.nan:
    #             date_prel_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'Disctrict sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['COVID Date du prelevement'][i],
    #                 'Erreurs/Confirmations' : 'Pas de date du prelevement',
    #                 'Actions' : 'Renseigner la date du prelevement',
    #                 'Section' : 'Section 4',
    #                 'Valeur souhaitée': 'Date',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries, date_prel_query], ignore_index=True)
                
    #         # =========================== Check de la nature du prélèvement =============================
    #         if df['COVID Nature du prelevement'][i] is np.nan:
    #            nature_prel_query = pd.DataFrame(data={
    #                'Code Echantillon' : [df['Code Echantillon'][i]],
    #                'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                'Disctrict sanitaire': df['Organisation unit name'][i],
    #                'Valeur actuelle' : df['COVID Nature du prelevement'][i],
    #                'Erreurs/Confirmations' : 'Pas de nature du prelevement',
    #                'Actions' : 'Renseigner la nature du prelevement',
    #                'Section' : 'Section 4',
    #                'Valeur souhaitée': 'Naso ou Oro',
    #                'Observations': ''
    #            })
    #            df_queries = pd.concat([df_queries, nature_prel_query], ignore_index=True)

    return df_queries