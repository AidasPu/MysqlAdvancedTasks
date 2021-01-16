from sqlalchemy import create_engine
from models import Base, Student, Locker, Grade
from sqlalchemy.orm import sessionmaker
# nepamirštam atsisiūsti pip install pymysql ir pip install SQLAlchemy.

# Connection string konstanta yra skirta nustatyti mūsų naudojama duombažės sistema.
# mysql + pymysql(biblioteka kuria naudojam pythone) :// (duombazes informacija)
CONNECTION_STRING = "mysql+pymysql://{user}:{password}@{host}/{database}"

# Sukuriamas variklis kuris naudos mūsų nustatymus.
engine = create_engine(CONNECTION_STRING.format(user="root", password="root", host="localhost", database="university"))

# iškviečiamas metodas kuris surenka informacija iš models failo ir sukuria lenteles duombazėje(Schemoje)
Base.metadata.create_all(engine)

# Sukuriame sesija ir pririšam variklį
Session = sessionmaker(bind=engine)

# Inicializuojame sesija
session = Session()

# try/except yra skirtas apsisaugoti nuo erroru. Jei iškyla netikėtas atvėjis galime atlikti atitinkančius vieksmus pagal tam tikrą error'a
try:
    # session.add_all funkcionalumas leidžia pridėti daug įrašų vienu metu. Tiesiog SQL naudojant prilygsta cursor.executeMany() funkcionalumui.
    session.add_all([
        Student(first_name="Mike", last_name="Wazowski"),
        Student(first_name="Netti", last_name="Nashe"),
        Student(first_name="Jessamine", last_name="Addison"),
        Student(first_name="Brena", last_name="Bugdale"),
        Student(first_name="Theobald", last_name="Oram"),])
    # session.commit() išsaugom informacija į duombaze
    session.commit()
# Šis Exception suveiks jei try bloke atsiras, bet kokia klaida. Jei žinotume kokių klaidų tikėtis galime iš vartotojų galime pakeisti Exception į pvz: IntegrityError
except Exception:
    # session.rollback() naudojamas kai žlugus mūsų norimam duombazės funkcionalumui galime atšukti visą padarytą darbą.
    session.rollback()
    print("rolled back")

try:
    session.add_all([Locker(number=1, student=4),
                     Locker(number=2, student=1),
                     Locker(number=3, student=5),
                     Locker(number=4, student=2),
                     Locker(number=5, student=3)])
    session.commit()
except Exception:
    session.rollback()
    print("rolled back")

# session.query naudojam kai norime gauti informacija iš duombazės. Viduje reikia paduoti Modeli kurį norime, kad naudotu.
# Paprastai paaiškinti mūsų modeliai veikia kaip lentelės SQL.
students = session.query(Student).all()

for row in students:
    print(row)

print("-----")
# Kaip ir sql galime naudoti mūsų pasirinkta ORM atlikti paprastus duombazės veiksmus šis pavizdys rodo Count() veikima
total = session.query(Student).count()
print(total)

print("-----")

# Priminimas, kad yra filter ir yra filter_by skiriasi tuo, kad su filter_by galime ieškoti naudojant kwargs ir jis skirtas paprastom užklausom.
# pvz:
# student = Student(first_name="Mike", last_name="Wazowski")
# session.query(Student).filter_by(id = student.id)
# session.query(Student).filter(Student.id == student.id)

query_data = session.query(Student).filter(Student.id < 2, Student.first_name.like("jo%"))

for row in query_data:
    print(row)
print("-----")

# session.query(Locker).all() gražina visus pasirinktos lentelės įrašus
lockers = session.query(Locker).all()
for row in lockers:
    print(row)

print("-----")
#  session.query(Student, Locker).join(Locker) naudojame kai norime sujungti lenteles
rows = session.query(Student, Locker).join(Locker).filter(Locker.number == 3)
for row in rows:
    student, locker = row
    print(f"locker {locker.number} with {student.first_name}")

print("-----")
query_result = session.query(Student, Grade).join(Grade)
for record in query_result:
    student, grade = record
    print(student.first_name, grade.grade, grade.grade_date)

session.close()
