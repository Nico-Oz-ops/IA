-- ============================================================================
-- CASE STUDY: Sistema di Bike Sharing Europeo (Dataset Reale)
-- Parte 4: Esercizi di Analisi OLAP con SQL
-- ============================================================================

-- Descrizione: Query di analisi sul DWH (versione dataset reale)

-

-- ============================================================================
-- Esercizio 1: KPI Generali
-- Obiettivo: Calcolare i principali indicatori di performance (KPI) del servizio.
-- ============================================================================

-- 1.1: Numero totale di noleggi
SELECT
    COUNT(---) AS totale_noleggi
FROM dw.fact_noleggi;

-- 1.2: Durata media dei noleggi in minuti
SELECT
    AVG(--) AS durata_media_minuti
FROM dw.fact_noleggi;

-- 1.3: Distanza media percorsa per noleggio in km
SELECT
    AVG(---) AS distanza_media_km
FROM dw.fact_noleggi;

-- ============================================================================
-- Esercizio 2: Analisi Temporale
-- Obiettivo: Analizzare l'andamento dei noleggi nel tempo.
-- ============================================================================

-- 2.1: Numero di noleggi per anno
SELECT
    t.anno,
    COUNT(---) AS numero_noleggi
FROM dw.fact_noleggi f
JOIN dw.dim_tempo t ON f.tempo_key = t.tempo_key
GROUP BY t.anno
ORDER BY t.anno;

-- 2.2: Numero di noleggi per giorno della settimana
SELECT
    t.nome_giorno,
    COUNT(----) AS numero_noleggi
FROM dw.fact_noleggi f
JOIN ----- t ON f.--- = t.----
GROUP BY t.---, t.----
ORDER BY t.-----;

-- ============================================================================
-- Esercizio 3: Analisi Geografica (Città e Stazioni)
-- Obiettivo: Identificare le città e le stazioni più attive.
-- ============================================================================

-- 3.1: Le 10 città con più noleggi
SELECT
    ---
FROM dw.fact_noleggi f
JOIN dw.dim_citta c ON f.citta_key = c.citta_key
GROUP BY ---
ORDER BY ---
LIMIT 10;

-- 3.2: Le 10 stazioni di partenza più popolari in una città specifica (es. Berlino)
SELECT
    ---,
    COUNT--
FROM dw.fact_noleggi f
JOIN -- ON ---
JOIN ---- c ON --- = ----
WHERE c.nome_sistema = 'nextbike Berlin'
GROUP BY s.nome_stazione
ORDER BY numero_partenze DESC
LIMIT 10;

-- ============================================================================
-- Esercizio 4: Analisi degli Utenti (Sintetici)
-- Obiettivo: Comprendere il comportamento dei diversi segmenti di utenti.
-- ============================================================================

-- 4.1: Numero di noleggi per tipo di abbonamento
SELECT
    ----,
    COUNT(f.noleggio_key) AS numero_noleggi
FROM dw.fact_noleggi f
JOIN ----ON ---
GROUP BY ----
ORDER BY numero_noleggi DESC;

-- 4.2: Numero di noleggi per fascia d'età
SELECT
    ---,
    COUNT  ----AS ---
FROM dw.fact_noleggi f
JOIN ---ON ----
GROUP BY u.fascia_eta
ORDER BY u.fascia_eta;


-- ============================================================================
-- Fine degli esercizi
-- ============================================================================
