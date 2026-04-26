"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .air_liquide import AirLiquideFetcher
from .air_products import AirProductsFetcher
from .ballard import BallardFetcher
from .bloom_energy import BloomEnergyFetcher
from .chart import ChartFetcher
from .cummins import CumminsFetcher
from .fuelcell import FuelcellFetcher
from .hyundai import HyundaiFetcher
from .itm_power import ItmPowerFetcher
from .linde import LindeFetcher
from .mcphy import McphyFetcher
from .nel import NelFetcher
from .nikola import NikolaFetcher
from .plug_power import PlugPowerFetcher
from .siemens_energy import SiemensEnergyFetcher
from .thyssenkrupp_nucera import ThyssenkruppNuceraFetcher
from .toyota import ToyotaFetcher

FETCHERS = {
    "air_liquide": AirLiquideFetcher,
    "air_products": AirProductsFetcher,
    "ballard": BallardFetcher,
    "bloom_energy": BloomEnergyFetcher,
    "chart": ChartFetcher,
    "cummins": CumminsFetcher,
    "fuelcell": FuelcellFetcher,
    "hyundai": HyundaiFetcher,
    "itm_power": ItmPowerFetcher,
    "linde": LindeFetcher,
    "mcphy": McphyFetcher,
    "nel": NelFetcher,
    "nikola": NikolaFetcher,
    "plug_power": PlugPowerFetcher,
    "siemens_energy": SiemensEnergyFetcher,
    "thyssenkrupp_nucera": ThyssenkruppNuceraFetcher,
    "toyota": ToyotaFetcher,
}
