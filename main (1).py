from faker import Faker

from database import Base, engine, SessionLocal
from models import CustomerRepository

Base.metadata.create_all(bind=engine)

db = SessionLocal()
fake = Faker()

customer_repo = CustomerRepository(db)


def populate_database():
    for _ in range(1500):
        company_name = fake.company()
        customer_repo.create_customer(customer_name=company_name)
        print(f"{company_name} was inserted")


if __name__ == "__main__":
    populate_database()
