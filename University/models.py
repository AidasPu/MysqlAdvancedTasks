from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
# SQLAlchemy reikalavimas, kad galėtume paveldėti SQLAlchemy base funkcionaluma.
# Šiuo būdu pasakome SQLAlchemy bibliotekai, kad šios lentelės turi būti pridėtos į atpažystamų lentelių sarašą
Base = declarative_base()

# Modeliai
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    # __str__ metodas naudojamas, kad pakeisti reprezentacija kai naudojam print() metoda į mum reikiama formatą.
    # Yra daugelius šių metodų norint daugiau sužinoti galima pasiskaityti apie Python Dunder methods
    def __str__(self):
        return f"Student -> {self.id}, {self.first_name} ,{self.last_name}"


class Locker(Base):
    __tablename__ = "locker"
    number = Column(Integer, primary_key=True)
    student = Column(Integer, ForeignKey(Student.id), primary_key=True)

    def __str__(self):
        return f"Locker: {self.number} for student {self.student}"


class Address(Base):
    __tablename__ = "address"
    student = Column(Integer, ForeignKey(Student.id), primary_key=True)
    street_name = Column(String(100))
    house_number = Column(Integer)
    city = Column(String(100))

    def __str__(self):
        return f" student {self.student} address: {self.city} {self.street_name} {self.house_number}"


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, autoincrement=True)
    student = Column(Integer, ForeignKey(Student.id), primary_key=True)
    grade = Column(Integer)
    grade_date = Column(DateTime(timezone=True))

    def __str__(self):
        return f"{self.id}, {self.student}, {self.grade}, {self.grade_date}"
