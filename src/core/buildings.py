BUILDINGS = {
    "clicker": {
        "base_cost": 10,
        "points_per_second": 1
    },
}

def add_buliding(name, base_cost, points_per_second):
    BUILDINGS[name] = {
        "base_cost": base_cost,
        "points_per_second": points_per_second
    }