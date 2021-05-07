import psycopg2


commands = (
    """
    CREATE TABLE sequence (
        seq_key VARCHAR PRIMARY KEY,
        count INTEGER NOT NULL,
        pgen_human_basic   FLOAT8
    )
    """)

conn = psycopg2.connect("dbname=seqdb user=postgres ")
cur = conn.cursor()
cur.execute(commands)
nb=100000
value = nb
seqlist=[]
with open("/mnt/mukkuri/RepSeq/RS_Tools/TCR_Synthetic_Repertoire/human/default_models/1e10/test.csv") as seq_file:
    for row in seq_file.readlines():
        seq,count=row.split(",")
        count = int(count) 
        seqlist.append((seq,count,0))
        value = value-1
        if value==0:
            query = "INSERT INTO sequence (seq_key, count, pgen_human_basic) VALUES (%s, %s, %s)"
            cur.executemany(query, seq)
            value = nb
            seq=[]






# query = "INSERT INTO sequence (seq_key, count, pgen_human_basic) VALUES (%s, %s, %s)"

# cur.executemany(query, seq)