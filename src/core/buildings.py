from typing import TypedDict

class BuildingDict(TypedDict):
    coins_per_second: int
    base_cost: int
    cost_growth: float # cost = base_cost * (growth^owned)

BUILDINGS: dict[str, BuildingDict] = {}

def add_building(name, base_cost, coins_per_second, cost_growth = 1.25):
    BUILDINGS[name] = {
        "coins_per_second": coins_per_second,
        "base_cost": base_cost,
        "cost_growth": cost_growth
    }
