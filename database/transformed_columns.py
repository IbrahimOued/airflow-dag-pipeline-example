def transformed_columns():
    new_columns = {
        "Event date": "event_date",
        "Enrollment date": "enrollment_date",
        "Organisation unit name": "nom_district_sanitaire",
        "Incident date": "incident_date",
        "Numero de la  semaine": "numero_semaine",
        "Numero de Cas": "numero_cas",
        "Nom de l\'investigateur": "nom_investigateur",
        "Code EIR / EPID": "numero_epid",
        "Code Echantillon": "code_echantillon",
        "COVID CNIB": "numero_cnib",
        "COVID Numero Passeport": "numero_passport",
        "Nom du patient": "nom",
        "Prénom(s) du patient": "prenom",
        "Date de naissance": "date_naissance",
        "Age en années\xa0": "age_annee",
        "Age en mois (si<12 mois)": "age_mois",
        "Age en jours (si<1 mois)": "age_jour",
        "Sexe du patient": "sexe",
        "Ville/Village": "ville_village",
        "Quartier/Secteur": "quartier_secteur",
        "Residence type": "residence",
        "Coordonnées GPS": "coords_gps",
        "Geometry": "geometrie",
        "Nom du père /de la mère/du tuteur": "nom_tuteur",
        "N° téléphone du patient ou des parents": "numero_patient_ou_tuteur",
        "COVID Mail": "email",
        "Classification initiale": "classification_initiale",
        "District de residence": "ds_residence",
        "Personne Contact": "personne_contact",
        "Population a risque": "population_a_risque",
        "Agents de premiere ligne": "agent_premiere_ligne",
        "Hemodialyse": "hemodialyse",
        "Voyageur": "voyageur",
        "Covis type depistage": "autre_depistage",
        "Date de l’investigation": "date_investigation",
        "COVID Date d’apparition des symptomes": "date_apparition_symptomes",
        "COVID Date de consultation\xa0": "date_consultation",
        "COVID Fievre / Antecedent de fievre / frissons": "fievre_antecedant_fievre_frissons",
        "COVID Faiblesse generale": "faiblesse_generale",
        "COVID Toux": "toux",
        "COVID Maux de gorge": "maux_de_gorge",
        "COVID Ecoulement nasal": "ecoulement_nasal",
        "COVID Essoufflement, manque d’air": "essouflement",
        "COVID Diarrhee": "diarrhee",
        "COVID Nausee/vomissement": "nausee_vomissement",
        "COVID Cephalees": "cephalees",
        "COVID Irritabilite / confusion mentale": "irritabilite_confusion_mentale",
        "COVID Autre Symptomes": "autres_symptomes",
        "COVID Preciser Symptomes": "precision_autres_symptomes",
        "COVID Temperature": "temperature",
        "COVID Douleur Musculaire": "douleur_musculaire",
        "COVID Douleur Abdominale": "douleur_abdominale",
        "COVID Douleur Poitrine": "douleur_poitrine",
        "COVID Douleur Articulation": "douleur_articulation",
        "COVID Douleur (Cochez les cases)": "douleurs",
        "COVID Statut du patient": "statut_patient",
        "COVID Evolution": "evolution",
        "COVID Grossesse": "grossesse",
        "COVID Age grossesse (trimestre)": "age_grossesse",
        "COVID Post-partum": "post_partum",
        "COVID Diabete": "diabete",
        "COVID Maladie du foie": "maladie_foie",
        "COVID Maladie renale": "maladie_renale",
        "COVID Maladie cardiovasculaire incluant HTA": "maladie_cardiovasculaire_incluant_hta",
        "COVID Maladie neurologique ou neuromusculaire chronique": "maladie_neurologique_ou_neuromusculaire_chronique",
        "COVID Immunodepression incluant le VIH": "immunodepression_incluant_vih",
        "COVID Maladie chronique des poumons": "maladie_chronique_poumons",
        "COVID Cancer": "cancer",
        "COVID Autre Conditions sous-jacentes et comorbidite": "autres_conditions_et_commorbidite",
        "COVID Preciser Autre Conditions sous-jacentes et comorbidite": "precision_autres_conditions_et_commorbidite",
        "Vacciné contre la COVID-19": "deja_vaccine_covid19",
        "Nombre de doses": "nombre_dose",
        "Connaissez vous le vaccin?": "connaissance_vaccin",
        "Préciser les vaccins": "precision_vaccin",
        "Date de la dernière dose": "souvenir_date_derniere_dose_vaccin",
        "Date de la dernière dose du vaccin reçue": "derniere_dose_si_sup_a_4",
        "Avez-vous déjà eu la COVID-19 ?": "deja_eu_covid19",
        "Avec un diagnostic confirmé par le laboratoire": "diagnostic_confirme_laboratoire",
        "Date du diagnostic de la COVID-19": "date_diagnostic",
        "Suivez vous un traitement en ce moment": "traitement_en_cours",
        "Quels traitements": "precision_traitements",
        "Doses journalières": "doses_journalieres",
        "Date de début du traitement": "date_debut_traitement",
        "Vous rappelez vous de la date de la dernière dose": "date_derniere_dose_traitement",
        "Provenance (secteur/pays, ville)": "provenance",
        "Statut matrimonial": "statut_matrimonial",
        "Nom de la personne à prévenir en cas de besoin": "personne_a_prevenir",
        "Numéro de Téléphone de la personne à prévenir": "numero_personne_a_prevenir",
        "Lieu de vie": "lieu_de_vie",
        "Autre lieu de vie": "autre_lieu_de_vie",
        "Taile du ménage": "taille_du_menage",
        "Nombre de pièces du domicile": "nombre_pieces_domicile",
        "Nombre de chambres à coucher": "nombre_chambres_a_coucher",
        "COVID Etudiant": "etudiant",
        "COVID Professionnel de sante": "professionel_sante",
        "lieu où l'établissement de l'agent de santé": "lieu_etablissement_agent_de_sante",
        "COVID Travailleur en contact avec les animaux": "travailleur_en_contact_avec_animaux",
        "COVID Professionnel de laboratoire": "professionel_laboratoire",
        "COVID Autre Profession": "autre_profession",
        "COVID Preciser Autre Profession": "precision_autre_profession",
        "COVID Le patient a-t-il voyagé au cours des 14 jours précédant l'apparition des symptômes": "voyage_14_jours_avant_symptomes",
        "COVID Pays de voyage 1": "pays_voyage_1",
        "COVID Ville du Pays de voyage 1": "ville_voyage_1",
        "COVID Pays de voyage 2": "pays_voyage_2",
        "COVID Ville du Pays de voyage 2": "ville_voyage_2",
        "COVID Pays de voyage 3": "pays_voyage_3",
        "COVID Ville du Pays de voyage 3": "ville_voyage_3",
        "COVID Le patient a-t-il visité des établissements de soins de santé au cours des 14 jours précédant l'apparition des symptômes": "visite_etablissement_sante_14_jours_avant_symptomes",
        "COVID Structure de sante": "precision_etablissement_sante_visite",
        "COVID Le patient a-t-il eu un contact etroit avec une personne atteinte d'une infection respiratoire aigue au cours des 14 jours précédant l'apparition des symptomes ?": "contact_etroit_personne_atteinte_iras_14_jours_avant_symptomes",
        "Structure de sante": "struct_sante_iras",
        "COVID Cadre familial": "cadre_familial_iras",
        "COVID Lieu de travail": "lieu_travail_iras",
        "COVID Inconnu": "inconnu_iras",
        "COVID Autres lieu": "autres_lieu_iras",
        "COVID Preciser Autres lieu": "precision_autres_lieux_iras",
        "COVID Le patient a-t-il ete en contact avec un cas probable ou confirme au cours des 14 jours precedant l'apparition des symptomes": "contact_etroit_cas_prob_ou_conf_14_jours_avant_symptomes",
        "COVID Structure de sante conf": "struct_sante_conf",
        "COVID Cadre familial conf": "cadre_familial_conf",
        "COVID Lieu de travail conf":  "lieu_travail_conf",
        "COVID Inconnu conf": "inconnu_conf",
        "COVID Autres lieu conf": "autres_lieu_conf",
        "COVID Preciser Autres lieu conf": "precision_autres_lieux_conf",
        "COVID Irritabilite / confusion mentale": "irritabilite_confusion_mentale",
        "COVID Avez-vous visite des marches d'animaux vivants au cours des 14 jours precedant l'apparition des symptomes": "visite_marche_animaux_vivants_14_jours_avant_symptomes",
        "COVID Avez-vous régulièrement porté un masque dans les lieux publics au cours des 14 jours précédant l'apparition des symptômes": "port_du_masque_14_jours_avant_symptomes",
        "COVID Avez-vous régulièrement observé l’hygiène des mains au cours des 14 jours précédant l'apparition des symptômes": "hygiene_mains_14_jours_avant_symptomes",
        "COVID Echantillon Preleve": "echantillon_preleve",
        "COVID Date du prelevement": "date_prelevement_echantillon",
        "COVID Heure du prelevement": "heure_prelevement_echantillon",
        # MAPPING SUPPLEMENTAIRE
        "COVID Date du voyage": "date_du_voyage",
        "COVID Heure du voyage": "heure_du_voyage",
        "COVID Manque de competence": "manque_de_competence",
        "COVID Manque de kit": "manque_de_kit",
        "COVID Observations prelevement": "observations_prelevement",
        "COVID Autres causes": "autres_causes",
        "COVID Preciser Autres causes": "precision_autres_causes",
        "COVID Refus du patient": "refus_du_patient",
        "COVID Etat du malade": "etat_du_malade",
        "COVID Quittance prelevement": "quittance_prelevement",
        "COVID Type de quittance prelevement": "type_de_quittance_prelevement",
        # FIN MAPPING
        "COVID Nature du prelevement": "nature_prelevement",
        "COVID Autre Prelevement": "autre_prelevement",
        "COVID Nom et prénom de l'agent ayant effectue le prelevement": "nom_prenom_agent_preleveur",
        "COVID Numero de l'agent ayant effectue le prelevement": "numero_agent_preleveur",
        "COVID Conservation de l’échantillon": "conservation_echantillon_avant_transport",
        "COVID Autres Conservation de l’échantillon avant le transport": "autre_conservation_echantillon_avant_transport",
        "COVID Preciser Autres Conservation de l’échantillon avant le transport": "precision_autre_conservation_echantillon_avant_transport",
        "COVID Date et heure d’envoi au laboratoire national de référence": "date_heure_envoi_lnrg",
        "N° Colis SONAPOST": "numero_colis_sonapost",
        "Consentement éclairé": "consentement_eclaire",
        "COVID Laboratoire D’analyse": "laboratoire_analyse",
        "COVID Examen Demande": "examen_demande",
        "COVID Date de reception": "date_reception",
        "COVID Heure de reception": "heure_reception",
        "COVID Condition de l’échantillon à la réception": "condition_echantillon_reception",
        "COVID N° dans le registre du labo": "numero_registre_laboratoire",
        "COVID N° sticker": "numero_sticker",
        "COVID Température à la réception": "temperature_reception",
        "COVID PCR realisee": "pcr_realise",
        "COVID Kit (trousse) de reactifs labo": "kit_reactifs_laboratoire",
        "COVID Platefome Utilisee": "plateforme_utilisee",
        "COVID Date de la PCR": "date_pcr",
        "COVID Resultat labo": "resultat_labo",
        "COVID Date de transmission des resultats a la DPSP": "date_transmission_resultats_dpsp",
        "COVID Resultat sequencage": "resultat_sequencage",
        "COVID Observations": "observations",
        "COVID Type de variant": "type_de_variant",
        "COVID Autre type de variant": "autre_type_de_variant",
        # Grippe
        "Adenovirus": "adenovirus",
        "Autre sous-type influenza": "autre_sous_type_influenza",
        "Autre test (preciser type et resultats) ": "autre_test_precision_et_resultat",
        "Bocavirus": "bocavirus",
        "COVID Bordetella spp. (except Bordetella parapertusis)": "bordetella_except_bordetella_parapertusis",
        "COVID Mycoplasma pneumoniae": "mycoplasma_pneumoniae",
        "COVID Date de la PCR LNRG": "date_pcr_lnrg",
        "COVID PCR pour influenza": "pcr_influenza", 
        "COVID PCR realisee LNRG": "pcr_realisee_lnrg",
        "Chlamydia pneumoniae No 6": "chlamydia_pneumoniae_no_6",
        "Condition de l'échantillon a la réception ": "condition_echantillon_reception_lnrg",
        "Coronavirus HKU1": "coronavirus_hku1",
        "Coronavirus 229E": "coronavirus_229e",
        "Coronavirus NL63": "coronavirus_nl63",
        "Coronavirus OC43": "coronavirus_oc43",
        "Date de sous-typage": "date_sous_typage",
        "Date de transmission des resultats a la DPSP ": "date_transmission_dpsp_lnrg",
        "Date et heure de réception de l’échantillon": "date_heure_reception_echantillon",
        "Enterovirus": "enterovirus",
        "Haemophilus influenzae": "haemophilus_influenzae",
        "Haemophilus influenzae type B": "haemophilus_influenzae_type_b",
        "Human metapneumovirus A/B": "human_metapneumovirus_a_b",
        "Influenza A (FluA)": "influenza_a",
        "Influenza B (FluB)": "influenza_b",
        "Influenza C (FluC)": "influenza_c",
        "Influenza A (H1N1) swl": "influenza_a_h1n1_swl",
        "Klebsiella pneumoniae": "klebsiella_pneumoniae",
        "Legionella pneumophila/Legionella longbeachae": "legionella_pneumophila_ou_legionella_longbeachae",
        "Moraxella catarrhalis": "moraxella_catarrhalis",
        "N° Colis SONAPOST LNRG": "numero_colis_sonapost_lnrg",
        "N° dans le registre du labo ": "numero_registre_laboratoire_lnrg",
        "N° sticker ": "numero_sticker_lnrg",
        "Parainfluenza 1": "parainfluenza_1",
        "Parainfluenza 2": "parainfluenza_2",
        "Parainfluenza 3": "parainfluenza_3",
        "Parainfluenza 4": "parainfluenza_4",
        "Parechovirus": "parechovirus",
        "Respiratory syncytial viruses A/B" : "respiratory_syncytial_viruses_a_b",
        "Rhinovirus": "rhinovirus",
        "Pneumocystis jirovecii": "pneumocystis_jirovecii",
        "Résultat de sous-typage": "resultat_sous_typage",
        "Résultats de la PCR pour influenza": "resultat_pcr_influenza",
        "Salmonella spp": "salmonella_spp",
        "Staphylococcus aureus": "staphylococcus_aureus",
        "Streptococcus pneumoniae": "staphylococcus_pneumoniae",
        "Température à la réception": "temperature_reception_lnrg",
        "Type de sous typage": "type_sous_typage",
        "Observations": "observations_lnrg",
        # Fin grippe
        "COVID Date d'admission": "date_admission",
        "COVID Heure d'admission": "heure_admission",
        "COVID Structure de reference": "structure_de_reference",
        "COVID Structure de soins": "structure_de_soin",
        "COVID Cardiopathie": "cardiopathie",
        "COVID Asthme": "asthme",
        "COVID Transfusion": "transfusion",
        "COVID Autres Antecedents": "autres_antecedants_medico_sociaux",
        "COVID Preciser Autres Antecedents": "precision_autres_antecedants_medico_sociaux",
        "COVID Type de diabete": "type_diabete",
        "COVID maladie rhumatologique": "maladie_rhumatologique",
        "COVID maladie_hematologique_chronique": "maladie_hematologique_chronique",
        "COVID Type de hepathopathie": "type_hematophathie",
        "COVID Demence": "demence",
        "COVID VIH-SIDA": "vih_sida",
        "COVID obesite": "obesite",
        "COVID Fumeur": "fumeur",
        "COVID Tumeur maligne": "tumeur_maligne",
        "COVID Denutrition": "denutrition",
        "COVID Fatigue": "fatigue", 
        "COVID Asthenie": "asthenie",
        "COVID Anorexie": "anorexie",
        "COVID Agueusie": "agueusie",
        "COVID_Type de Toux": "type_toux",
        "COVID_PRURIT A LA GORGE": "prurit_gorge",
        "COVID Rhinorrhee": "rhinorrhee",
        "COVID Anosmie": "anosmie",
        "COVID Amoxicilline + Ac. Clav.": "amoxicilline_plus_ac_clav",
        "COVID details Amoxicilline + Ac. Clav." : "details_amoxicilline_plus_ac_clav",
        "COVID Anxiolytique": "anxiolytique",
        "COVID Autre Antibiotique": "autre_antibiotique",
        "COVID Preciser Autre Antibiotique": "precision_autre_antibiotique",
        "COVID Autres traitements": "autres_traitements",
        "COVID Azithromycine": "azithromycine",
        "COVID Bromure d’ipratopium": "bromure_ipratopium",
        "COVID Ceftriaxone": "ceftriaxone",
        "COVID details Ceftriaxone": "details_ceftriaxone",
        "COVID Consentement Signe": "consentement_signe",
        "COVID Corticoides inhales": "corticoides_inhales",
        "COVID Details Corticoïde inhalé" : "details_cortocoide_inhale",
        "COVID Corticoides injectables": "corticoides_injectables",

        "COVID chloroquine" : "chloroquine",
        "COVID Date de mise sous chloroquine" : "date_mise_sous_chloroquine",
        "COVID Details Anxiolytique" : "details_anxiolytique",
        "COVID Details Azithromycine" : "details_azithromycine",
        "COVID Details Bromure d’ipratopium" : "details_bromure_ispratopium",
        "COVID Details Enoxaparine" : "details_enoxaparine",
        "COVID Métoclopramide (Primpéran*)" : "metoclopramide",
        "COVID Details Métoclopramide (Primpéran*)" : "details_metoclopramide",
        "COVID Métopimazine (Vogalène*)" : "metopimazine",
        "COVID Details Métopimazine (Vogalène*)" : "details_metopimazine",
        "COVID Omeprazole" : "omeprazole",
        "COVID Details Omeprazole" : "details_omeprazole",
        "COVID_Paracétamol" : "paracetamol",
        "COVID Details PARACETAMOL" : "details_paracetamol",
        "COVID Salbutamol" : "salbutamol",
        "COVID Details Salbutamol" : "details_salbutamol",
        "COVID_Vitamine C": "vitamine_c",
        "COVID Details Vitamine C" : "details_vitamine_c",
        "COVID Details Voie veineuse" : "details_voie_veineuse",
        "COVID Details chloroquine" : "details_chloroquine",
        "COVID Levofloxacine" : "levofloxacine",
        "COVID Vomissements" : "vomissements",
        "COVID Enoxaparine" : "enoxaparine",
        "COVID Hospitalisation Centre Ref." : "hospitalisation_centre_ref",
        "COVID Hospitalisation REA" : "hospitalisation_rea",
        "COVID Hospitalisation USI" : "hospitalisation_usi",
        "COVID Incubation orotracheale" : "incubation_orotracheale",
        "COVID Oxygenotherapie" : "oxygenotherapie",
        "COVID Resultat Examen de Contrôle" : "resultat_examen_controle",
        "COVID Date Resultat Examen de Contrôle" : "date_resultat_examen_controle",
        "COVID Patient inclus dans l' etude": "patient_inclus_dans_etude",
        "COVID Prelevement nasopharynge" : "prelevement_nasopharynge",
        "COVID Prelevement oropharynge" : "prelevement_oropharynge",
        "COVID Classification OMS" : "classification_oms",
        "COVID Date de sortie" : "date_de_sortie",

        "DOULEURS A L'OREILLE": "douleur_oreille",
        "COVID_SIFFLEMENT": "sifflement",
        "COVID Douleur thoracique": "douleur_thoracique",
        "COVID TIRAILLEMENT DE LA PAROI THORACIQUE INFERIEURE": "tiraillement_paroi_thoracique_inferieure",
        "COVID Myalgie": "myalgie",
        "COVID Arthralgie": "arthralgie",
        "COVID Dyspnee": "dyspnee",
        "COVID_DYSPHONIE": "dysphonie",
        "COVID_DYSPHAGIE": "dysphagie",
        "COVID Éruption cutanée": "eruption_cutanee",
        "COVID ULCERATIONS CUTANEES": "ulcerations_cutanees",
        "COVID Voie veineuse": "voie_veineuse",
        "COVID Conjonctivite": "conjonctivite",
        "COVID Lymphadenopathie": "lymphadenopathie",
        "COVID_ALTERATION DE CONSCIENCE/CONFUSION": "alteration_conscience_confusion",
        "COVID Hemoragie": "hemoragie",
        "COVID Preciser le site d'hemoragie": "precision_site_hemoragie",
        "COVID Obstructuction nasale": "obstruction_nasale",
        "COVID Autres signes cliniques": "autres_signes_clinique",
        "COVID Preciser autres signes cliniques": "precision_autres_signes_clinique",
        "COVID ETAT GENERAL": "etat_general",
        "COVID_CONSCIENCE": "conscience",
        "COVID_CONJONCTIVES": "conjonctives",
        "COVID_ANOREXIE": "anorexie_investigation",
        "COVID_OMI": "omi",
        "COVID_ETAT D'HYDRATATION": "etat_hydratation",
        "COVID Temperature Investigation": "temperature_investigation", # Unique à la section 8
        "COVID Score de glasgow": "score_glasgow",
        "COVID Suivi a domicile": "suivi_a_domicile",
        "COVID Frequence cardiaque": "freq_cardiaque",
        "COVID Frequence respiratoire": "freq_respiratoire",
        "COVID Saturation en oxygene": "saturation_en_oxygene",
        "COVID Tension arterielle systolique": "tension_arterielle_systolique",
        "COVID Tension arterielle diastolique": "tension_arterielle_diastolique",
        "COVID TEMPS DE RECOLORATION UNGUEALE": "temps_recoloration_ungueale",
        "COVID_APPAREIL RESPIRATOIRE": "appareil_respiratoires_signes",
        "COVID SYSTEME CARDIO-VASCULAIRE": "systeme_cardio_vasculaire",
        "COVID AUTRES APPAREILS ET SYSTEMES": "autres_appareils_et_systemes",
        "COVID Taux d'hemoglobine": "taux_hemoglobine",
        "COVID Volume globulaire moyen": "volume_globulaire_moyen",
        "COVID Globules blancs": "globules_blancs",
        "COVID Lymphocytes": "lymphocytes",
        "COVID Neutrophiles": "neutrophiles",
        "COVID Monocytes": "monocytes",
        "COVID Plaquettes": "plaquettes",
        "COVID C-reactive protein": "c_reactive_protein",
        "COVID Aspartate aminotransferases": "aspartate_aminotransferases",
        "COVID Alanine aminotransferases": "alanine_aminotransferases",
        "COVID Creatinemie": "creatinemie",
        "COVID Goute epaisse": "goutte_epaisse",
        "COVID Natremie": "natremie",
        "COVID Kaliemie": "kaliemie",
        "COVID Calcemie": "calcemie",
        "COVID Resultat radio thoracique": "resultat_radio_thoracique",
        "COVID Resultat scanner": "resultat_scanner",
    }
    return new_columns