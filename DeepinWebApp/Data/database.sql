LOAD DATA INFILE '/Users/lydiaobeng/Documents/Projects/GitHub/BIO727P-Team-Deepin/DeepinWebApp/Data/modified_chr1_pca_with_population.tsv'
INTO TABLE Populations
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
IGNORE 1 LINES; -- Use this if your TSV file has a header row

CREATE USER 'deepinflaskapp'@'localhost' IDENTIFIED BY 'Deepin0324';
GRANT ALL PRIVILEGES ON deepin.* TO 'deepinflaskapp'@'localhost';
FLUSH PRIVILEGES;


SHOW VARIABLES LIKE 'secure_file_priv';
SELECT * from populations where pca1 is null;
drop table populations;

CREATE TABLE AnalysisResults (
    id INT AUTO_INCREMENT PRIMARY KEY,
    SAMPLE_ID VARCHAR(255),
    POP VARCHAR(50),
    SUPER_POP VARCHAR(50),
    Ancestry1 FLOAT,
    Ancestry2 FLOAT,
    Ancestry3 FLOAT,
    Ancestry4 FLOAT,
    Ancestry5 FLOAT,
    PCA1 FLOAT,
    PCA2 FLOAT,
    INDEX (SAMPLE_ID)
);


CREATE TABLE SampleTable (
    SAMPLE_ID VARCHAR(255) NOT NULL,
    POP VARCHAR(50),
    SUPER_POP VARCHAR(50),
    PRIMARY KEY (SAMPLE_ID)
);

