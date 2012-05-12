#!/usr/bin/env python
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class MixinObj(object):
	"""Table defaults"""
	@declared_attr
	def __tablename__(cls)
		return cls.__name__.lower()

	__table_args__ = {'mysql_engine': 'InnoDB'}
	__mapper_args__= {'always_refresh': True}

	id =  Column(Integer, primary_key=True)




class Series(MixinObj,Base):
	"""Represents a TV series"""
	name = Column(String)
	

class Episode(MixinObj,Base):
	"""Represents an episode of a tv show"""
	name = Column(String)
	series_id = Column(Integer, ForeignKey('Series.id'))

	series = relationship("Series", backref=backref('episodes', order_by=id))


	
	

