load data 
infile 'Library_Usage.csv' "str '\n'"
append
into table LIBRARY
fields terminated by ','
OPTIONALLY ENCLOSED BY '"' AND '"'
trailing nullcols
           ( COLUMN1 CHAR(20)
           )
