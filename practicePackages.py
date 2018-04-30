import math, sys, os, logging, datetime, csv, json, sqlite3

def doThings(num1, num2):
	# find GCD with math package
	gcd = math.gcd(num1, num2)
	# find user ID with OS package
	print("Your effective user id: ", os.geteuid())
	# find size of GCD in bytes with sys package
	print("size of GCD: ", sys.getsizeof(gcd))
	# logging practice - creating a warning
	logging.warning("Look out! You are doing things!")
	# print day of the week
	print("Today is", datetime.date.today().strftime("%A"))
	# create CSV file and add spanish translations to it
	with open('spanishTranslator.csv', 'w') as csvfile:
		filewriter = csv.writer(csvfile, delimiter = ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow(['Hola', 'Hello'])
		filewriter.writerow(['Adios', 'Goodbye'])
		filewriter.writerow(['Rojo', 'Red'])
	with open('spanishTranslator.csv', 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			print(row)
	# create JSON file and add "data" to it
	with open('data.txt', 'w') as outfile:
		json.dump("data", outfile)
	with open('data.txt', 'r') as f:
		d = json.load(f)
		print(d)
	return gcd
	# sqlite3 practice
	sqFile = 'text.sqlite'
	conn = sqlite3.connect(sqFile)
	c = conn.cursor()
	c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
		.format(tn="Table", cn="Column", ct="INTEGER"))
	c.execute("UPDATE {tn} SET {cn}='Prices' WHERE {idf}=123456"\
		.format(tn="Table", idf="My Column", cn="Column"))
	c.execute('CREATE INDEX {ix} on {tn}({cn})'\
		.format(ix="thisIndex", tn ="Table", cn="Column"))
	c.execute('DROP INDEX {ix}'.format(ix="thisIndex"))
	conn.commit()
	conn.close()

def main():
	print("GCD is:", doThings(85, 400))
main()