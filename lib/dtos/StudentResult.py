from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class StudentResult(Base):
    def __int__(self, id=None, name=None):
        self.id = id

    __tablename__ = 'student_results'
    id = Column(String, primary_key=True)
    res_path = Column(String)

    student_id = Column(String, ForeignKey('students.id'))
    student = relationship('Student')
