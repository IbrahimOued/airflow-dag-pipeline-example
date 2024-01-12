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
                    'SOMBIE FATIMA', 'SOMBIE Fatima Madiamsé', 'BANHORO HONORÉ ACHILLE']

    
    converter = {'Code Echantillon': str}
    iter_csv = pd.read_csv(path, converters=converter)
    iter_csv[["Event date", "Enrollment date"]] = iter_csv[["Event date", "Enrollment date"]].apply(pd.to_datetime)
    df = iter_csv[(iter_csv['Event date'] > datetime(2022, 9, 9)) & (iter_csv['Nom de l\'investigateur'].isin(investigateurs))]

    # will be used to check the missing data of the sections 6, 7, 8, 9 and 10
    df_labo_path = '/home/ibra/documents/afroscreen/clean_data/bobo/section_5.csv'
    df_labo = pd.read_csv(df_labo_path, converters=converter)

    df_queries = pd.DataFrame(columns=['Code Echantillon', 'Nom de l\'investigateur', 'District sanitaire', 'Valeur actuelle', 'Erreurs/Confirmations', 'Actions', 'Section', 'Valeur souhaitée', 'Observations'])
    # iterate through each row and select
    for i in df.index:
        if section == 'Section 1':
            
            # =========================== Check des COORDONNEES GPS =============================
            if df["Coordonnées GPS"][i] is np.isnan:
                geometry_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df["Coordonnées GPS"][i],
                    'Erreurs/Confirmations' : 'Coordonnées GPS manquantes',
                    'Actions' : 'Mettre à jour les coordonnées GPS',
                    'Section' : section,
                    'Valeur souhaitée': 'GPS',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, geometry_query], ignore_index=True) 
            
            # =========================== Check des TYPE DE RESIDENCE =============================
            if df['Residence type'][i] is np.nan:
                residence_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['Residence type'][i],
                    'Erreurs/Confirmations' : 'Type de résidence non spécifié',
                    'Actions' : 'Sélectionner le type de résidence du patient',
                    'Section' : section,
                    'Valeur souhaitée': 'Urbain ou rural',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, residence_query], ignore_index=True)

            # =========================== Check des DU NOM DU TUTEUR =============================
    #         if (df['Nom du père /de la mère/du tuteur'][i] is np.nan and df['Age en années\xa0'][i] < 5) and (df['Age en jours (si<1 mois)'][i] is not np.nan or df['Age en jours (si<1 mois)'][i] is not np.nan):
    #             tuteur_query = pd.DataFrame(data={
    #                 'Code Echantillon' : [df['Code Echantillon'][i]],
    #                 'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
    #                 'District sanitaire': df['Organisation unit name'][i],
    #                 'Valeur actuelle' : df['Nom du père /de la mère/du tuteur'][i],
    #                 'Erreurs/Confirmations' : f"Age en années , Age en mois {df['Age en mois (si<12 mois)'][i]}, Age en jours {df['Age en jours (si<1 mois)'][i]}",
    #                 'Actions' : 'Il n\'y a pas de tuteur alors que le patient a moins de 5 ans',
    #                 'Section' : section,
    #                 'Valeur souhaitée': 'Nom du tuteur',
    #                 'Observations': ''
    #             })
    #             df_queries = pd.concat([df_queries,tuteur_query], ignore_index=True)
            
            # =========================== Check des NUMERO DE TELEPHONE DU PATIENT OU DES PARENTS =============================
            if df['N° téléphone du patient ou des parents'][i] is np.nan:
                tel_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['N° téléphone du patient ou des parents'][i],
                    'Erreurs/Confirmations' : 'Pas de numéro de téléphone du patient ou des parents',
                    'Actions' : 'Renseigner le numéro de téléphone',
                    'Section' : section,
                    'Valeur souhaitée': 'ex: 70010203',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, tel_query], ignore_index=True)

            # =========================== Check des DISTRICTS DE RESIDENCE =============================
            if df['District de residence'][i] is np.nan:
                district_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire' : df['Organisation unit name'][i],
                    'Valeur actuelle' : df['District de residence'][i],
                    'Erreurs/Confirmations' : 'Pas de district de résidence, confirmer?',
                    'Actions' : 'Renseigner District de résidence',
                    'Section' : section,
                    'Valeur souhaitée' : 'ex: DS Dafra',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, district_query], ignore_index=True) 
        
        elif section == 'Section 2':
            
            # =========================== Check de la grossesse =============================
            if df["COVID Grossesse"][i] is np.nan and df['Sexe du patient'][i] == 'Feminin' and df['Age en années\xa0'][i] >= 12:
                temp_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Grossesse'][i],
                    'Erreurs/Confirmations' : 'Etat de grossesse non renseigné',
                    'Actions' : 'Etat de grossesse de la patiente de plus de 12 ans oui ou non',
                    'Section' : section,
                    'Valeur souhaitée': 'Oui ou Non',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, temp_query], ignore_index=True) 

            # =========================== Check de la temperature =============================
            if np.isnan(df["COVID Temperature"][i]):
                temp_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Temperature'][i],
                    'Erreurs/Confirmations' : 'Température non renseignée',
                    'Actions' : 'Renseigner la température du patient',
                    'Section' : section,
                    'Valeur souhaitée': 'Température',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, temp_query], ignore_index=True)

            # =========================== Check des SYMPTOMES =============================
            if df['COVID Date d’apparition des symptomes'][i] is np.nan:
                date_sympt_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Date d’apparition des symptomes'][i],
                    'Erreurs/Confirmations' : 'Pas de date d\'apparition des symptômes',
                    'Actions' : 'Renseigner la date d\'apparition des symptômes',
                    'Section' : section,
                    'Valeur souhaitée': 'ex: DS Dafra',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, date_sympt_query], ignore_index=True)

            # =========================== Check de la fievre =============================
            if df['COVID Fievre / Antecedent de fievre / frissons'][i] is np.nan:
                fievre_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Fievre / Antecedent de fievre / frissons'][i],
                    'Erreurs/Confirmations' : 'Pas de réponse',
                    'Actions' : 'Renseigner si Fievre/Antecedent de fievre Oui ou Non ',
                    'Section' : section,
                    'Valeur souhaitée': 'Oui ou Non',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, fievre_query], ignore_index=True)

            # =========================== Check des maladies neurologiques =============================
            if df['COVID Maladie neurologique ou neuromusculaire chronique'][i] is np.nan:
                maladie_neuro_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Maladie neurologique ou neuromusculaire chronique'][i],
                    'Erreurs/Confirmations' : 'Pas de réponse',
                    'Actions' : 'Renseigner si Maladie neurologique ou neuromusculaire chronique Oui ou Non ',
                    'Section' : section,
                    'Valeur souhaitée': 'Oui ou Non',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, maladie_neuro_query], ignore_index=True)

            # =========================== Check de la toux =============================
            if df['COVID Toux'][i] is np.nan:
                toux_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Toux'][i],
                    'Erreurs/Confirmations' : 'Pas de réponse',
                    'Actions' : 'Renseigner si Toux Oui ou Non ',
                    'Section' : section,
                    'Valeur souhaitée': 'Oui ou Non',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, toux_query], ignore_index=True)

            # =========================== Check des vomissements =============================
            if df['COVID Nausee/vomissement'][i] is np.nan:
                vomiss_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Nausee/vomissement'][i],
                    'Erreurs/Confirmations' : 'Pas de réponse',
                    'Actions' : 'Renseigner si Nausée/vomissement Oui ou Non ',
                    'Section' : section,
                    'Valeur souhaitée': 'Oui ou Non',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, vomiss_query], ignore_index=True)
                
            # =========================== Check du manque d'air =============================
            if df['COVID Essoufflement, manque d’air'][i] is np.nan:
                essouf_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Essoufflement, manque d’air'][i],
                    'Erreurs/Confirmations' : 'Pas de réponse',
                    'Actions' : 'Renseigner si Essoufflement/manque d\'air Oui ou Non ',
                    'Section' : section,
                    'Valeur souhaitée': 'Oui ou Non',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, essouf_query], ignore_index=True)
                
        elif section == 'Section 3':            
            # =========================== Check des antécédants de voyages =============================
            if df['COVID Le patient a-t-il voyagé au cours des 14 jours précédant l\'apparition des symptômes'][i] is np.nan:
                antec_voyage_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Le patient a-t-il voyagé au cours des 14 jours précédant l\'apparition des symptômes'][i],
                    'Erreurs/Confirmations' : 'Pas d\'information de voyage',
                    'Actions' : 'Le patient à t-il voyagé Oui ou Non',
                    'Section' : section,
                    'Valeur souhaitée': 'Oui ou Non',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, antec_voyage_query], ignore_index=True)

            # =========================== Check du STATU MATRIMONIAL =============================
            if df['Statut matrimonial'][i] is np.nan and df['Age en années\xa0'][i] >= 18:
                statut_mat_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['Statut matrimonial'][i],
                    'Erreurs/Confirmations' : 'Pas de statut matrimonial du patient',
                    'Actions' : 'Renseigner le statut matrimonial du patient',
                    'Section' : section,
                    'Valeur souhaitée': 'ex: Celibataire',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, statut_mat_query], ignore_index=True)

            # =========================== Check de pays de voyage =============================
            if df['COVID Le patient a-t-il voyagé au cours des 14 jours précédant l\'apparition des symptômes'][i] == 'Oui' and df['COVID Pays de voyage 1'][i] is np.nan:
                pays_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Pays de voyage 1'][i],
                    'Erreurs/Confirmations' : 'Patient ayant voyagé mais pas d\'information de pays',
                    'Actions' : 'Renseigner le(s) pays de voyage',
                    'Section' : section,
                    'Valeur souhaitée': 'Exemple: Cote d\'Ivoire',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, pays_query], ignore_index=True)
                    
            # =========================== Check de ville de voyage =============================
            if df['COVID Le patient a-t-il voyagé au cours des 14 jours précédant l\'apparition des symptômes'][i] == 'Oui' and df['COVID Ville du Pays de voyage 1'][i] is np.nan:
                ville_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Ville du Pays de voyage 1'][i],
                    'Erreurs/Confirmations' : 'Patient ayant voyagé mais pas d\'information de la ville',
                    'Actions' : 'Renseigner la ville de voyage',
                    'Section' : section,
                    'Valeur souhaitée': 'Exemple: Abobo',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, ville_query], ignore_index=True)

        elif section == 'Section 4':
            # =========================== Check de la date de prélèvement de l'échantillon =============================
            if df['COVID Date du prelevement'][i] is np.nan:
                date_prel_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Valeur actuelle' : df['COVID Date du prelevement'][i],
                    'Erreurs/Confirmations' : 'Pas de date du prelevement',
                    'Actions' : 'Renseigner la date du prelevement',
                    'Section' : section,
                    'Valeur souhaitée': 'Date',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, date_prel_query], ignore_index=True)
                
            # =========================== Check de la nature du prélèvement =============================
            if df['COVID Nature du prelevement'][i] is np.nan:
               nature_prel_query = pd.DataFrame(data={
                   'Code Echantillon' : [df['Code Echantillon'][i]],
                   'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                   'District sanitaire': df['Organisation unit name'][i],
                   'Valeur actuelle' : df['COVID Nature du prelevement'][i],
                   'Erreurs/Confirmations' : 'Pas de nature du prelevement',
                   'Actions' : 'Renseigner la nature du prélèvement',
                   'Section' : section,
                   'Valeur souhaitée': 'Naso ou Oro',
                   'Observations': ''
               })
               df_queries = pd.concat([df_queries, nature_prel_query], ignore_index=True)

        elif section == 'Section 5':
            # =========================== Check du resultat de labo =============================
            if df['COVID Resultat labo'][i] is np.nan:
                res_labo_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Date de reception' : df['COVID Date de reception'][i],
                    'Valeur actuelle' : df['COVID Resultat labo'][i],
                    'Erreurs/Confirmations' : 'Pas de resultat labo',
                    'Actions' : 'Renseigner le resultat du patient',
                    'Section' : section,
                    'Valeur souhaitée': 'Positif, Négatif ou Indeterminé',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, res_labo_query], ignore_index=True)

        elif section == 'Section 6':
            # =========================== Check du resultat de labo grippe =============================
            # if df['Résultats de la PCR pour influenza'][i] is np.nan:
            #     res_labo_query = pd.DataFrame(data={
            #         'Code Echantillon' : [df['Code Echantillon'][i]],
            #         'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
            #         'District sanitaire': df['Organisation unit name'][i],
            #         'Valeur actuelle' : df['COVID Resultat labo LNRG'][i],
            #         'Erreurs/Confirmations' : 'Pas de resultat Grippe',
            #         'Actions' : 'Renseigner le resultat du patient',
            #         'Section' : section,
            #         'Valeur souhaitée': 'Positif, Négatif',
            #         'Observations': ''
            #     })
            #     df_queries = pd.concat([df_queries, res_labo_query], ignore_index=True)

            # =========================== Check du resultat de labo grippe sous typage =============================
            if df['Résultat de sous-typage'][i] is np.nan:
                res_labo_lnrg_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Date de reception' : df['Date et heure de réception de l’échantillon'][i],
                    'Valeur actuelle' : df['Résultat de sous-typage'][i],
                    'Erreurs/Confirmations' : 'Pas de resultat Grippe sous typage',
                    'Actions' : 'Renseigner le resultat du patient',
                    'Section' : section,
                    'Valeur souhaitée': 'Positif, Négatif',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, res_labo_lnrg_query], ignore_index=True)

            # =========================== Check du resultat de labo grippe sous typage =============================
            if df['Résultat de sous-typage'][i] is 'Positif' and df['Type de sous typage'][i] is np.nan:
                sous_typage_query = pd.DataFrame(data={
                    'Code Echantillon' : [df['Code Echantillon'][i]],
                    'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                    'District sanitaire': df['Organisation unit name'][i],
                    'Date de reception' : df['Date et heure de réception de l’échantillon'][i],
                    'Valeur actuelle' : df['Type de sous typage'][i],
                    'Erreurs/Confirmations' : 'Préciser le type de sous typage',
                    'Actions' : 'Renseigner le type de sous type',
                    'Section' : section,
                    'Valeur souhaitée': 'Sous typage',
                    'Observations': ''
                })
                df_queries = pd.concat([df_queries, sous_typage_query], ignore_index=True)            


        # TODO: Utiliser l'issue du patient pour voir les cas positifs non investigués
        elif section == 'Section 7':
            # if df_labo[(df_labo['Code Echantillon'] == df['Code Echantillon'][i])]['COVID Resultat labo'][i] != 'Positif':
            # sec7_df = df_labo[(df_labo['Code Echantillon'] == df['Code Echantillon'][i])]['COVID Resultat labo'][i]
            resultats_labo_df = df_labo[df_labo['Code Echantillon'] == df['Code Echantillon'][i]]
            print(resultats_labo_df)
            # Return the first element of the underlying data as a Python scalar.

            # if len(resultats_labo_df) == 1 and resultats_labo_df['COVID Resultat labo'].item():
            #     break
            # else:
            # if len(resultats_labo_df) > 0:
            controls = resultats_labo_df[resultats_labo_df['COVID Resultat labo'] == 'Positif']['COVID Resultat labo'].to_list() 
            for resultat in controls:
                if resultat == 'Positif' and df['COVID Asthme'][i] is np.nan:
                    # =========================== Check du des sections des investigués =============================
                    asthme_query = pd.DataFrame(data={
                        'Code Echantillon' : [df['Code Echantillon'][i]],
                        'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                        'District sanitaire': df['Organisation unit name'][i],
                        'Valeur actuelle' : df['COVID Asthme'][i],
                        'Erreurs/Confirmations' : 'Pas d\'information sur l\'asthme',
                        'Actions' : 'Renseigner si présence d\'asthme ou pas',
                        'Section' : section,
                        'Valeur souhaitée': 'Oui ou Non',
                        'Observations': ''
                    })
                    df_queries = pd.concat([df_queries, asthme_query], ignore_index=True)
                    
                if resultat == 'Positif' and df['COVID Cardiopathie'][i] is np.nan:
                    # =========================== Check du cardiopathie =============================
                    cardiopathie_query = pd.DataFrame(data={
                        'Code Echantillon' : [df['Code Echantillon'][i]],
                        'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                        'District sanitaire': df['Organisation unit name'][i],
                        'Valeur actuelle' : df['COVID Cardiopathie'][i],
                        'Erreurs/Confirmations' : 'Pas d\'information cardiopathie',
                        'Actions' : 'Renseigner si présence d\'une cardiopathie',
                        'Section' : section,
                        'Valeur souhaitée': 'Oui ou Non',
                        'Observations': ''
                    })
                    df_queries = pd.concat([df_queries, cardiopathie_query], ignore_index=True)

                if resultat == 'Positif' and df['COVID Diabete'][i] is np.nan:
                    # =========================== Check du diabete =============================
                    diabete_query = pd.DataFrame(data={
                        'Code Echantillon' : [df['Code Echantillon'][i]],
                        'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                        'District sanitaire': df['Organisation unit name'][i],
                        'Valeur actuelle' : df['COVID Diabete'][i],
                        'Erreurs/Confirmations' : 'Pas d\'information de diabète',
                        'Actions' : 'Renseigner si présence d\'un diabète',
                        'Section' : section,
                        'Valeur souhaitée': 'Oui ou Non',
                        'Observations': ''
                    })
                    df_queries = pd.concat([df_queries, diabete_query], ignore_index=True)

                if resultat == 'Positif' and df['COVID Diabete'][i] == 'Oui' and df['COVID Type de diabete'] is np.nan:
                    # =========================== Check du type de diabète =============================
                    type_diab_query = pd.DataFrame(data={
                        'Code Echantillon' : [df['Code Echantillon'][i]],
                        'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                        'District sanitaire': df['Organisation unit name'][i],
                        'Valeur actuelle' : df['COVID Type de diabete'][i],
                        'Erreurs/Confirmations' : 'Pas d\'information sur le type de diabète',
                        'Actions' : 'Renseigner le type de diabète',
                        'Section' : section,
                        'Valeur souhaitée': 'exemple : SUCRE NON COMPLIQUE',
                        'Observations': ''
                    })
                    df_queries = pd.concat([df_queries, type_diab_query], ignore_index=True)


                if resultat == 'Positif' and df['COVID Diabete'][i] == 'Non' and df['COVID Type de diabete'] is np.nan:
                    # =========================== Check du type de diabète inversé =============================
                    diabete_to_yes_query = pd.DataFrame(data={
                        'Code Echantillon' : [df['Code Echantillon'][i]],
                        'Nom de l\'investigateur' : df['Nom de l\'investigateur'][i],
                        'District sanitaire': df['Organisation unit name'][i],
                        'Valeur actuelle' : df['COVID Diabete'][i],
                        'Erreurs/Confirmations' : 'Type de diabète donné mais diabète à Non',
                        'Actions' : 'Changer le diabète en Oui',
                        'Section' : section,
                        'Valeur souhaitée': 'Oui dans le champ diabète',
                        'Observations': ''
                    })
                    df_queries = pd.concat([df_queries, diabete_to_yes_query], ignore_index=True)

        # COVID Asthme,COVID Autres Antecedents,COVID Cardiopathie,COVID Date d'admission,COVID Demence,COVID Denutrition,COVID Diabete,COVID Fumeur,COVID Heure d'admission,COVID Maladie cardiovasculaire incluant HTA,COVID Preciser Autres Antecedents,COVID Structure de reference,COVID Structure de soins,COVID Transfusion,COVID Tumeur maligne,COVID Type de diabete,COVID Type de hepathopathie,COVID VIH-SIDA,COVID maladie rhumatologique,COVID maladie_hematologique_chronique,COVID obesite


        # TODO: Utiliser l'issue du patient pour voir les cas positifs non investigués
        # elif section == 'Section 6':
        #     if df['COVID Resultat labo'][i] != 'Positif':
        #         # =========================== Check du des sections des investigués =============================
        #         break

        # elif section == 'Section 7':
        #     if df['COVID Resultat labo'][i] != 'Positif':
        #         # =========================== Check du des sections des investigués =============================
        #         break

        # elif section == 'Section 8':
        #     if df['COVID Resultat labo'][i] != 'Positif':
        #         # =========================== Check du des sections des investigués =============================
        #         break

        # elif section == 'Section 9':
        #     if df['COVID Resultat labo'][i] != 'Positif':
        #         # =========================== Check du des sections des investigués =============================
        #         break

        # elif section == 'Section 10':
        #     if df['COVID Resultat labo'][i] != 'Positif':
        #         # =========================== Check du des sections des investigués =============================
        #         break

    return df_queries