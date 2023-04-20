-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.patientsafroscreen
(
    patient_id SERIAL NOT NULL,
    event_date date NOT NULL,
    enrollment_date date NOT NULL,
    nom_district_sanitaire text NOT NULL,
    incident_date date NOT NULL,
    numero_semaine smallint NOT NULL,
    numero_cas character varying NOT NULL,
    nom_investigateur text NOT NULL,
    numero_epid character varying NOT NULL,
    code_echantillon text NOT NULL,
    numero_passport character varying,
    nom text NOT NULL,
    prenom text NOT NULL,
    date_naissance date,
    age_annee smallint NOT NULL,
    age_mois smallint,
    age_jour smallint,
    sexe text NOT NULL,
    ville_village text NOT NULL,
    quartier_secteur character varying NOT NULL,
    residence text,
    coords_gps text,
    nom_tuteur text,
    numero_patient_ou_tuteur text NOT NULL,
    email character varying,
    classification_initiale text NOT NULL,
    ds_residence text NOT NULL,
    personne_contact text NOT NULL,
    population_a_risque text,
    agent_premiere_ligne text,
    hemodialyse text,
    voyageur text,
    autre_depistage text,
    numero_enregistrement smallint,
    date_investigation date NOT NULL,
    unite_organisation text NOT NULL,
    date_apparition_symptomes date NOT NULL,
    date_consultation date NOT NULL,
    fievre_antecedant_fievre_frissons text,
    faiblesse_generale text,
    toux text,
    maux_de_gorge text,
    ecoulement_nasal text,
    essouflement text,
    diarrhee text,
    nausee_vomissement text,
    cephalees text,
    irritabilite_confusion_mentale text,
    autres_symptomes text,
    precision_autres_symptomes text,
    temperature smallint,
    douleur_musculaire text,
    douleur_abdominale text,
    douleur_poitrine text,
    douleur_articulation text,
    douleurs text,
    statut_patient text,
    evolution text,
    grossesse text,
    age_grossesse smallint,
    post_partum text,
    diabete text,
    maladie_foie text,
    maladie_renale text,
    maladie_cardiovasculaire_incluant_hta text,
    maladie_neurologique_ou_neuromusculaire_chronique text,
    immunodepression_incluant_vih text,
    maladie_chronique_poumons text,
    cancer text,
    autres_conditions_et_commorbidite text,
    precision_autres_conditions_et_commorbidite text,
    deja_vaccine_covid19 text,
    nombre_dose smallint,
    connaissance_vaccin text,
    precision_vaccin text,
    souvenir_date_derniere_dose_vaccin date,
    derniere_dose_si_sup_a_4 date,
    deja_eu_covid19 text,
    diagnostic_confirme_laboratoire text,
    date_diagnostic date,
    traitement_en_cours text,
    precision_traitements text,
    doses_journalieres smallint,
    date_debut_traitement date,
    date_derniere_dose_traitement date,
    provenance character varying,
    statut_matrimonial text,
    personne_a_prevenir text,
    numero_personne_a_prevenir text,
    lieu_de_vie text,
    autre_lieu_de_vie text,
    taille_du_menage smallint,
    nombre_pieces_domicile smallint,
    nombre_chambres_a_coucher smallint,
    etudiant text,
    professionel_sante text,
    lieu_etablissement_agent_de_sante text,
    travailleur_en_contact_avec_animaux text,
    professionel_laboratoire text,
    autre_profession text,
    precision_autre_profession text,
    voyage_14_jours_avant_symptomes text,
    pays_voyage_1 text,
    ville_voyage_1 text,
    pays_voyage_2 text,
    ville_voyage_2 text,
    pays_voyage_3 text,
    ville_voyage_3 text,
    visite_etablissement_sante_14_jours_avant_symptomes text,
    precision_etablissement_sante_visite text,
    contact_etroit_personne_atteinte_iras_14_jours_avant_symptomes text,
    struct_sante_iras text,
    cadre_familial_iras text,
    lieu_travail_iras text,
    inconnu_iras text,
    autres_lieu_iras text,
    precision_autres_lieux_iras text,
    contact_etroit_cas_prob_ou_conf_14_jours_avant_symptomes text,
    struct_sante_conf text,
    cadre_familial_conf text,
    lieu_travail_conf text,
    inconnu_conf text,
    autres_lieu_conf text,
    precision_autres_lieux_conf text,
    visite_marche_animaux_vivants_14_jours_avant_symptomes text,
    port_du_masque_14_jours_avant_symptomes text,
    hygiene_mains_14_jours_avant_symptomes text,
    echantillon_preleve text,
    date_prelevement_echantillon date,
    heure_prelevement_echantillon time without time zone,
    nature_prelevement text,
    autre_prelevement text,
    nom_prenom_agent_preleveur text,
    numero_agent_preleveur text,
    conservation_echantillon_avant_transport text,
    autre_conservation_echantillon_avant_transport text,
    precision_autre_conservation_echantillon_avant_transport text,
    date_heure_envoi_lnr date,
    numero_colis_sonapost character varying,
    consentement_eclaire text,
    investigation_realisee text, -- field not present in dhis2
    raison_non_realisation_investigation text, -- field not present in dhis2
    laboratoire_analyse text,
    examen_demande text,
    date_reception date,
    heureu_reception timestamp without time zone,
    numero_registre_laboratoire character varying,
    numer_sticker character varying,
    temperature_reception character varying,
    pcr_realise text,
    kit_reactifs_laboratoire text,
    plateforme_utilisee text,
    date_pcr date,
    date_transmission_resultats_dpsp date,
    resultat_sequencage text,
    observations text,
    date_admission date NOT NULL,
    heure_admission time without time zone NOT NULL,
    structure_de_reference text,
    structure_de_soin text,
    cardiopathie text,
    asthme text,
    transfusion text,
    autres_antecedants_medico_sociaux text,
    precision_autres_antecedants_medico_sociaux text,
    type_diabete text,
    maladie_rhumatologique text,
    maladie_hematologique_chronique text,
    type_hematophathie text,
    demence text,
    vih_sida text,
    obesite text,
    fumeur text,
    tumeur_maligne text,
    denutrition text,
    fatigue text,
    asthenie text,
    anorexie text,
    agueusie text,
    type_toux text,
    prurit_gorge text,
    rhinorrhee text,
    anosmie text,
    douleur_oreille text,
    sifflement text,
    douleur_thoracique text,
    tiraillement_paroi_thoracique_inferieure text,
    myalgie text,
    arthralgie text,
    dyspnee text,
    dysphonie text,
    dysphagie text,
    eruption_cutanee text,
    ulcerations_cutanees text,
    conjonctivite text,
    lymphadenopathie text,
    alteration_conscience_confusion text,
    hemoragie text,
    precision_site_hemoragie text,
    obstruction_nasale text,
    autres_signes_clinique text,
    precision_autres_signes_clinique text,
    etat_general text,
    conscience text,
    conjonctives text,
    etat_hydratation text,
    temperature_investigation smallint,
    score_glasgow smallint,
    freq_cardiaque smallint,
    freq_respiratoire smallint,
    saturation_en_oxygene smallint,
    tension_arterielle_systolique smallint,
    tension_arterielle_diastolique smallint,
    temps_recoloration_ungueale character varying,
    appareil_respiratoires_signes text,
    systeme_cardio_vasculaire text,
    autres_appareils_et_systemes text,
    taux_hemoglobine smallint,
    volume_globulaire_moyen smallint,
    globules_blancs smallint,
    lymphocytes smallint,
    neutrophiles smallint,
    monocytes smallint,
    plaquettes smallint,
    c_reactive_protein smallint,
    aspartate_aminotransferases smallint,
    alanine_aminotransferases smallint,
    creatinemie smallint,
    goutte_epaisse text,
    natremie text,
    kaliemie text,
    calcemie text,
    resultat_radio_thoracique text,
    resultat_scanner text,
    PRIMARY KEY (patient_id)
);
END;