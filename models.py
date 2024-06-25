from settings import Base
import sys, datetime, time
from sqlalchemy import create_engine, exc
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float, JSON


class agricultural_car(Base): 
    __tablename__ = 'Сельскохозяйственная_техника'
    id  = Column(Integer, primary_key=True)
    brand = Column(String)
    model = Column(String)
    year  = Column(String)
    program_data = Column(String)

    def __repr__(self): 
        return f"Сельскохозяйственная_техника(id=%d, brand=%s, model=%s, year=%s, program_data=%s)" % (self.id, self.brand, self.model, self.year, self.program_data)

class autobus(Base):
    __tablename__  =  'Автобусы'
    id   = Column(Integer, primary_key=True)
    brand  = Column(String)
    model   = Column(String)
    year   = Column(String)
    program_data  = Column(String)

    def  __repr__(self):
        return f"Автобусы(id=%d, brand=%s, model=%s, year=%s, program_data=%s)" % (self.id, self.brand, self.model, self.year, self.program_data)
     
class boats_hydrocycles(Base):
    __tablename__   =   'Моторные_лодки_гидроциклы_сне'
    id = Column(Integer, primary_key=True)
    brand   = Column(String)
    model    = Column(String)
    year    = Column(String)
    program_data   = Column(String)
    def __repr__(self):
        return f"Моторные_лодки_гидроциклы_сне(id=%d, brand=%s, model=%s, year=%s, program_data=%s)" % (self.id, self.brand, self.model, self.year, self.program_data)
    
class build_car(Base):
    __tablename__    =    'Строительная_техника'
    id    = Column(Integer, primary_key=True)
    brand    = Column(String)
    model     = Column(String)
    year     = Column(String)
    program_data      = Column(String)
    def  __repr__(self):
        return f"Строительная_техника(id=%d, brand=%s, model=%s, year=%s, program_data=%s)" % (self.id, self.brand, self.model, self.year, self.program_data)
    
class cargo_auto(Base):
    __tablename__    =    'Грузовые_автомобили'
    id     = Column(Integer, primary_key=True)
    brand      = Column(String)
    model      = Column(String)
    year       = Column(String)
    program_data        = Column(String)
    def   __repr__(self):
        return f"Грузовые_автомобили(id=%d, brand=%s, model=%s, year=%s, program_data=%s)" % (self.id, self.brand, self.model, self.year, self.program_data)
    

class communal_car(Base):
    __tablename__    =    'Коммунальная_техника'
    id      = Column(Integer, primary_key=True)
    brand       = Column(String)
    model       = Column(String)
    year        = Column(String)
    program_data         = Column(String)
    def    __repr__(self):
        return f"Коммунальная_техника(id=%d, brand=%s, model=%s, year=%s, program_data=%s)" % (self.id, self.brand, self.model, self.year, self.program_data)
    

class electric_pass_car(Base):
    __tablename__    =    'Электрические_легковые_автомоби'
    id      = Column(Integer, primary_key=True)
    brand        = Column(String)
    model        = Column(String)
    year         = Column(String)
    program_data          = Column(String)
    def    __repr__(self):
        return f"Электрические_легковые_автомоби(id=%d, brand=%s, model=%s, year=%s, program_data=%s)" % (self.id, self.brand, self.model, self.year, self.program_data)
    

class forest_car(Base):
    __tablename__     =     'Лесозаготовительная_техника'
    id      = Column(Integer, primary_key=True)
    brand      = Column(String)
    model       = Column(String)
    year        = Column(String)
    program_data           = Column(String)
    def    __repr__(self):
        return f"Лесозаготовительная_техника(id=%d, brand=%s, model=%s, year=%s, program_data=%s)"  %  (self.id, self.brand, self.model, self.year, self.program_data)
    
class motorcycles(Base):
    __tablename__      =     'Мотоциклы'
    id       = Column(Integer, primary_key=True)
    brand       = Column(String)
    model        = Column(String)
    year         = Column(String)
    program_data            = Column(String)
    def    __repr__(self):
        return f"Мотоциклы(id=%d, brand=%s, model=%s, year=%s, program_data=%s)" % (self.id, self.brand, self.model, self.year, self.program_data)
    

class pass_carr(Base):
    __tablename__        =       'Легковые_автомобили'
    id       = Column(Integer, primary_key=True)
    brand        = Column(String)
    model         = Column(String)
    year         = Column(String)
    program_data            = Column(String)
    def    __repr__(self):
        return f"Легковые_автомобили(id=%d, brand=%s, model=%s, year=%s, program_data=%s)" % (self.id, self.brand, self.model, self.year, self.program_data)
    

class special_car(Base):
    __tablename__       =      'Спецтехника'
    id       = Column(Integer, primary_key=True)
    brand        = Column(String)
    model          = Column(String)
    year          = Column(String)
    program_data            = Column(String)
    def    __repr__(self):
        return f"Спецтехника(id=%d, brand=%s, model=%s, year=%s, program_data=%s)" % (self.id, self.brand, self.model, self.year, self.program_data)
    

class tankers(Base):
    __tablename__          =       'Танкеры'
    id        = Column(Integer, primary_key=True)
    brand        = Column(String)
    model          = Column(String)
    year           = Column(String)
    program_data             = Column(String)
    def    __repr__(self):
        return f"Танкеры(id=%d, brand=%s, model=%s, year=%s, program_data=%s)" % (self.id, self.brand, self.model, self.year, self.program_data)
    


SHEET_NAME = {
    'Сельскохозяйственная техника'          :agricultural_car,
    'Автобусы'                              :autobus,
    'Моторные лодки, гидроциклы, сне'       :boats_hydrocycles,
    'Строительная техника'                  :build_car,
    'Грузовые автомобили'                   :cargo_auto,
    'Коммунальная техника'                  :communal_car,
    'Электрические легковые автомоби'       :electric_pass_car,
    'Лесозаготовительная техника'           :forest_car,
    'Мотоциклы'                             :motorcycles,
    'Легковые автомобили'                   :pass_carr,
    'Спецтехника'                           :special_car,
    'Танкеры'                               :tankers
}