from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import registry, declarative_base


Base = declarative_base()
metadata = MetaData()

PLATFORM_CA = 'platform_ca'


class PlatformCA(Base):
    """
    Class for PlatformCA data.
    """
    __tablename__ = PLATFORM_CA

    id = Column(Integer, primary_key=True)
    structure = Column(String(255), nullable=False, default='')
    weight = Column(Integer, nullable=False, default=0)
    power_consumption_in_standby_mode = Column(Integer, nullable=False, default=0)
    power_consumption_in_the_high_speed_mode = Column(Integer, nullable=False, default=0)
    power_consumption_in_the_orbit_correction_mode = Column(Integer, nullable=False, default=0)
    power_consumption_in_safe_mode = Column(Integer, nullable=False, default=0)
    power_consumption_in_ca_operational_mode = Column(Integer, nullable=False, default=0)
    average_power_consumption_per_cycle = Column(Integer, nullable=False, default=0)
    mdr = Column(Integer, nullable=False, default=0)
    sac = Column(Integer, nullable=False, default=0)
    reliability_budget = Column(Integer, nullable=False, default=0)
    type_platform = Column(Integer, nullable=False, default=0)





    def to_dict(self):
        """
        Converts the attributes of the NamesConstants instance into a dictionary.
        """
        return {
            'id': self.id,
            'structure': self.structure,
            'weight': self.weight,
            'power_consumption_in_standby_mode': self.power_consumption_in_standby_mode,
            'power_consumption_in_the_high_speed_mode': self.power_consumption_in_the_high_speed_mode,
            'power_consumption_in_the_orbit_correction_mode': self.power_consumption_in_the_orbit_correction_mode,
            'power_consumption_in_safe_mode': self.power_consumption_in_safe_mode,
            'power_consumption_in_ca_operational_mode': self.power_consumption_in_ca_operational_mode,
            'average_power_consumption_per_cycle': self.average_power_consumption_per_cycle,
            'mdr': self.mdr,
            'sac': self.sac,
            'reliability_budget': self.reliability_budget,
            'type_platform': self.type_platform
        }