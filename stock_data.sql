
CREATE TABLE stock_data (
    datetime TIMESTAMP PRIMARY KEY,
    open DECIMAL(10,2) NOT NULL,
    high DECIMAL(10,2) NOT NULL,
    low DECIMAL(10,2) NOT NULL,
    close DECIMAL(10,2) NOT NULL,
    volume INTEGER NOT NULL,
	instrument VARCHAR NOT NULL
);
COPY stock_data(datetime, open,close,high,low,volume,instrument)
FROM 'C:\Users\khush\OneDrive\Desktop\final_data.csv'
DELIMITER ','
CSV HEADER;
Alter TABLE stock_data DROP COLUMN instrument;
SELECT * FROM stock_data;
