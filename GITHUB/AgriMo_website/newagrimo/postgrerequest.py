import psycopg2

# Configuration from your Django settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'f31GBd5cBb1-gF26Ccgc*G6g3B353gf-',
        'HOST': 'monorail.proxy.rlwy.net',
        'PORT': '22467',
    }
}

def insert_record(name, value):
    try:
        conn = psycopg2.connect(
            dbname=DATABASES['default']['NAME'],
            user=DATABASES['default']['USER'],
            password=DATABASES['default']['PASSWORD'],
            host=DATABASES['default']['HOST'],
            port=DATABASES['default']['PORT']
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO main_statistics (name, value) VALUES (%s, %s)", (name, value))
        conn.commit()
        print("Record inserted successfully.")
    except psycopg2.Error as e:
        print("Error: Unable to insert record")
        print(e)
    finally:
        if conn:
            conn.close()

# Example usage
insert_record(4, 0)
insert_record(5, 0)
insert_record(6, 0)
insert_record(7, 0)
insert_record(8, 0)
insert_record(9, 0)
insert_record(10, 0)
insert_record(11, 0)
insert_record(12, 0)

