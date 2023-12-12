from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from src.utils.database import Base


class Import(Base):
    __tablename__ = "imports"
    import_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    import_date = Column(Date, nullable=False)
    file_name = Column(String, nullable=False)


class Project(Base):
    __tablename__ = "projects"
    project_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_code = Column(String, nullable=False)
    project_name = Column(String, nullable=False)


class DataValue(Base):
    __tablename__ = "data_values"
    value_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    import_id = Column(Integer, ForeignKey("imports.import_id"), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.project_id"), nullable=False)
    plan_date = Column(Date, nullable=False)
    plan_value = Column(Numeric)
    fact_date = Column(Date)
    fact_value = Column(Numeric)

    import_rel = relationship("Import", back_populates="data_values")
    project_rel = relationship("Project", back_populates="data_values")


Import.data_values = relationship("DataValue", back_populates="import_rel")
Project.data_values = relationship("DataValue", back_populates="project_rel")
