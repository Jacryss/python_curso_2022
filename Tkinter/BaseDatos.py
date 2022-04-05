import psycopg2

# 1. Establecer conexion con la base 

conexion = psycopg2.connect(host='localhost', database = 'Usuarios', user='postgres', password='2105', port =5432 )

cursor = conexion.cursor
cursor.execute=('SELECT * FROM public. "Usuarios";')

for data in cursor.fetchall():
    print(data)

# Insert (sentencia insert)(valores)

sentenciaInsert = ''' INSERT INTO public.usuarios(
	nombre, apellido, edad, sexo)
	VALUES ('%s', '%s','%s', '%s');
'''

valores =('Janeth','Castillo',30,'M')
cursor.execute(sentenciaInsert, valores)

for data in cursor.fetchall():
    print(data)

# Insert (sentencia insert) (valores)

sentenciaInsert = '''INSERT INTO public."Usuarios"(
	nombre, apellido, edad, sexo)
	VALUES (%s, %s, %s, %s);
    '''
valores = ('Anderson2','Cardenas',22,'M')
valores2 = ('Anderson3','Cardenas',22,'M')
cursor.execute(sentenciaInsert,valores)
cursor.execute(sentenciaInsert,valores2)
conexion.commit()
registrosInsertados = cursor.rowcount
print('Se insertaron ', registrosInsertados)
