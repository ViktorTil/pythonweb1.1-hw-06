#Формирование базы данных (файл : studies.db) и заполнение фейковыми данными
import create_db, fill_data_fake


if __name__ == "__main__":
    create_db.create_db()
    fill_data_fake.main()
    
    