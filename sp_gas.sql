-- SP consumo de gas: LISTO y probado
SELECT idvbox, SUM(litros) AS total FROM lecturas GROUP BY idvbox;
