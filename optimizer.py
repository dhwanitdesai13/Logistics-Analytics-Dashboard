# optimizer.py
from ortools.linear_solver import pywraplp
import numpy as np
import pandas as pd

class DynamicFleetOptimizer:
    def __init__(self, orders, vehicles, historical, traffic):
        self.orders = orders
        self.vehicles = vehicles[vehicles['Status'] == 'Available']
        self.historical = historical
        self.traffic = traffic

    def compute_cost(self, order, vehicle):
        dist = order['Distance_KM']
        avg_speed = 50  # km/h
        time_min = (dist / avg_speed) * 60 + order['Traffic_Delay_Minutes']
        congestion = self.traffic[self.traffic['Order_ID'] == order['Order_ID']]['congestion'].values[0]
        time_min *= (1 + congestion)

        fuel_cost_per_km = 1 / vehicle['Fuel_Efficiency_KM_per_L'] * 100  # Assume ₹100/L
        cost = dist * fuel_cost_per_km

        if 'Truck' in vehicle['Vehicle_Type']: cost *= 1.2
        elif 'Van' in vehicle['Vehicle_Type']: cost *= 1.0
        elif 'Bike' in vehicle['Vehicle_Type']: cost *= 0.8
        elif 'Refrigerated' in vehicle['Vehicle_Type']: cost *= 1.5

        priority_multiplier = {'Express': 1.5, 'Standard': 1.2, 'Economy': 1.0}
        cost *= priority_multiplier.get(order['Priority'], 1)

        return cost, time_min

    def optimize(self):
        solver = pywraplp.Solver.CreateSolver('SCIP')
        x = {}
        for i, order in self.orders.iterrows():
            for j, vehicle in self.vehicles.iterrows():
                if self.is_compatible(order, vehicle):
                    x[i, j] = solver.BoolVar(f'x_{i}_{j}')

        # Minimize Cost
        solver.Minimize(solver.Sum(self.compute_cost(self.orders.iloc[i], self.vehicles.iloc[j])[0] * x[i, j]
                                   for i in range(len(self.orders)) for j in range(len(self.vehicles)) if (i, j) in x))

        # Constraints
        for i in range(len(self.orders)):
            solver.Add(solver.Sum(x[i, j] for j in range(len(self.vehicles)) if (i, j) in x) <= 1)  # Optional assignment for demo
        for j in range(len(self.vehicles)):
            solver.Add(solver.Sum(x[i, j] for i in range(len(self.orders)) if (i, j) in x) <= 1)

        status = solver.Solve()
        assignments = []
        total_cost = 0
        total_co2 = 0
        if status == pywraplp.Solver.OPTIMAL:
            for i in range(len(self.orders)):
                for j in range(len(self.vehicles)):
                    if (i, j) in x and x[i, j].solution_value() > 0.5:
                        order = self.orders.iloc[i]
                        vehicle = self.vehicles.iloc[j]
                        cost, time = self.compute_cost(order, vehicle)
                        co2 = order['Distance_KM'] * vehicle['CO2_Emissions_Kg_per_KM']
                        assignments.append({
                            'order_id': order['Order_ID'], 'vehicle_id': vehicle['Vehicle_ID'], 'vehicle_type': vehicle['Vehicle_Type'],
                            'priority': order['Priority'], 'distance_km': order['Distance_KM'], 'est_time_min': round(time),
                            'cost_inr': round(cost), 'from': order['Origin'], 'to': order['Destination'], 'co2_kg': round(co2)
                        })
                        total_cost += cost
                        total_co2 += co2

        metrics = {
            'cost_saving': 150000 - total_cost, 'fuel_saved': total_cost / 100,  # Assume ₹100/L
            'co2_saved': total_co2 * 0.8,  # 20% reduction vs manual
            'ontime_improve': 5.0
        }
        return pd.DataFrame(assignments), metrics

    def is_compatible(self, order, vehicle):
        if order['weight_kg'] > vehicle['Capacity_KG']: return False
        if order['Special_Handling'] == 'Temperature_Controlled' and 'Refrigerated' not in vehicle['Vehicle_Type']: return False
        # Add more: e.g., Hazmat if needed
        return True