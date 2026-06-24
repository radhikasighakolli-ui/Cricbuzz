import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

password = quote_plus("Minsuga@9")

mysql_engine = create_engine(
    f"mysql+pymysql://root:{password}@localhost:3306/cricketdb"
)

sqlite_engine = create_engine("sqlite:///cricket.db")

tables = ["players", "performances", "matches", "venues"]

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", mysql_engine)
    df.to_sql(table, sqlite_engine, if_exists="replace", index=False)
    print(f"{table} migrated successfully!")

print("All tables migrated to cricket.db")