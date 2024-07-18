from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from database import Base


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)


class CustomerRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_customer(self, customer_id: int):
        return self.db.query(Customer).filter(Customer.id == customer_id).first()

    def get_customers(self, skip: int = 0, limit: int = 10):
        return self.db.query(Customer).offset(skip).limit(limit).all()

    def create_customer(self, customer_name: str):
        db_customer = Customer(customer_name=customer_name)
        self.db.add(db_customer)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def update_customer(self, customer_id: int, customer_name: str):
        db_customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        if db_customer:
            db_customer.customer_name = customer_name
            self.db.commit()
            self.db.refresh(db_customer)
        return db_customer

    def delete_customer(self, customer_id: int):
        db_customer = self.db.query(Customer).filter(Customer.id == customer_id).first()
        if db_customer:
            self.db.delete(db_customer)
            self.db.commit()
        return db_customer
