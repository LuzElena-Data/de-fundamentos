-- SP consumo de agua: A MEDIAS, falta el filtro de fechas
SELECT idvbox, SUM(m3) FROM
lecturas WHERE fecha >= '2026-10-01' GROUP BY idvbox;
