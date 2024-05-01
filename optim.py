import scipy.optimize as opt


# Calculate the individual system metrics using M/M/1 queue formulas
def system_metrics(lambd, mu):
    assert mu > lambd, "Service rate must be greater than arrival rate for stability."
    rho = lambd / mu  # Utilization
    R = 1 / (mu - lambd)  # Residence time including service and queue
    Q = lambd ** 2 / (mu * (mu - lambd))  # Average queue length
    return rho, R, Q

# Total system metrics
def total_system_metrics(params):
    service_rates = params[:3]
    transition_times = params[3:]
    
    # Enforce the throughput constraint for System 3
    arrival_rate_system_3 = min(theta3_fixed, service_rates[2])  # Limit arrival to System 3 to the fixed throughput
    
    # Metrics for each system
    metrics = [system_metrics(arrival_rate, mu) for mu in service_rates]
    metrics[2] = system_metrics(arrival_rate_system_3, service_rates[2])  # Update metrics for System 3 with constrained throughput
    
    total_residence_time = sum(metric[1] for metric in metrics) + sum(transition_times)
    total_queue_length = sum(metric[2] for metric in metrics)
    
    return total_residence_time  # Objective to minimize
# Parameters
arrival_rate = 9.9  # units per hour; example value
service_rates = [10, 10, 10]  # units per hour for each system
transition_times = [0.5, 0.5]  # hours to transition between systems
theta3_fixed = 7  # Fixed throughput for System 3 in units per hour

# Assert to prevent invalid entries
assert arrival_rate > 0, "Arrival rate must be positive."
assert all(mu > 0 for mu in service_rates), "Service rates must be positive."
assert all(t >= 0 for t in transition_times), "Transition times must be non-negative."
assert theta3_fixed > 0, "Throughput constraint for System 3 must be positive."

# Initial guess for optimization (service rates and transition times)
initial_guess = service_rates + transition_times

# Optimization constraints for service rates, especially for System 3
bounds = [(1, None), (1, None), (theta3_fixed, None)] + [(0, None)] * 2  # System 3's service rate must be at least the throughput

# Run optimization to find best service rates and transition times minimizing residence time
result = opt.minimize(total_system_metrics, initial_guess, bounds=bounds)

optimized_service_rates = result.x[:3]
optimized_transition_times = result.x[3:]
optimized_residence_time = result.fun

print("Optimized Service Rates:", optimized_service_rates)
print("Optimized Transition Times:", optimized_transition_times)
print("Optimized Total Residence Time:", optimized_residence_time)
