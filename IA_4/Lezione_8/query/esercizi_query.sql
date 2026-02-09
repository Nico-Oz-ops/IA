-- ### Esercizi

-- **Esercizio 1: KPI Generali**

-- Calcola:
-- - Numero totale di noleggi
SELECT COUNT(*) AS num_noleggi
FROM dw.fact_noleggi

-- - Durata media dei noleggi
SELECT ROUND(AVG(durata_minuti)::NUMERIC, 2) AS durata_media
FROM dw.fact_noleggi

-- - Distanza media percorsa
SELECT ROUND(AVG(distanza_km)::NUMERIC, 2) AS distanza_media
FROM dw.fact_noleggi

-- **Esercizio 2: Analisi Temporale**

-- Analizza:
-- - Numero di noleggi per anno
SELECT t.anno, COUNT(*) AS num_noleggi
FROM dw.fact_noleggi f
JOIN dw.dim_tempo t ON f.tempo_key = t.tempo_key
GROUP BY t.anno;

-- - Numero di noleggi per giorno della settimana
SELECT t.giorno_settimana, t.nome_giorno, COUNT(*)
FROM dw.fact_noleggi f
JOIN dw.dim_tempo t ON f.tempo_key = t.tempo_key
GROUP BY t.nome_giorno, t.giorno_settimana
ORDER BY t.giorno_settimana ASC;

-- **Esercizio 3: Analisi Geografica**

-- Identifica:
-- - Le 10 città con più noleggi
SELECT c.nome_sistema, COUNT(*) AS num_noleggi
FROM dw.fact_noleggi f 
JOIN dw.dim_citta c ON f.citta_key = c.citta_key
GROUP BY c.nome_sistema
ORDER BY num_noleggi DESC
LIMIT 10;

-- - Le 10 stazioni di partenza più popolari
SELECT id_stazione, COUNT(*) AS stazioni_partenza
FROM dw.fact_noleggi f 
JOIN dw.dim_stazione s ON f.stazione_partenza_key = s.stazione_key
GROUP BY s.nome_stazione, s.id_stazione
ORDER BY stazioni_partenza DESC
LIMIT 10

-- **Esercizio 4: Analisi degli Utenti**

-- Comprendi:
-- - Numero di noleggi per tipo di abbonamento
SELECT u.tipo_abbonamento_corrente, COUNT(*) AS num_noleggi
FROM dw.fact_noleggi f
JOIN dw.dim_utente u ON f.utente_key = u.utente_key
GROUP BY u.tipo_abbonamento_corrente

-- - Numero di noleggi per fascia d'età
SELECT u.fascia_eta, COUNT(*) AS num_noleggi
FROM dw.fact_noleggi f
JOIN dw.dim_utente u ON f.utente_key = u.utente_key
GROUP BY u.fascia_eta
ORDER BY u.fascia_eta DESC

-- **Esercizio 5: Analisi delle Biciclette**

-- Analizza:
-- - Numero di noleggi per tipo di propulsione
SELECT b.propulsione, COUNT(*) AS num_noleggi
FROM dw.fact_noleggi f
JOIN dw.dim_bicicletta b ON f.bicicletta_key = b.bicicletta_key
GROUP BY b.propulsione; 

-- - Durata e distanza media per tipo di propulsione
SELECT 
	b.propulsione, 
	ROUND(AVG(f.durata_minuti)::NUMERIC,2) AS durata_media, 
	ROUND(AVG(f.distanza_km)::NUMERIC, 2) AS distanza_media
FROM dw.fact_noleggi f
JOIN dw.dim_bicicletta b ON f.bicicletta_key = b.bicicletta_key
GROUP BY b.propulsione;