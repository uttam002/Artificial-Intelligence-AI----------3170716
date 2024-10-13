from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Define the structure of the Bayesian Network for the Monty Hall Problem
def create_monty_hall_network():
    # Create a Bayesian network with edges indicating dependencies
    monty_hall_network = BayesianNetwork([('Car', 'Monty'), ('Choice', 'Monty')])
    return monty_hall_network

# Define the Conditional Probability Distributions (CPDs)
def define_cpds():
    # The probability that the car is behind each of the three doors (equal probability)
    cpd_car = TabularCPD(variable='Car', variable_card=3, values=[[1/3], [1/3], [1/3]])
    
    # The player chooses one of the three doors with equal probability
    cpd_choice = TabularCPD(variable='Choice', variable_card=3, values=[[1/3], [1/3], [1/3]])
    
    return cpd_car, cpd_choice

# Add CPDs to the Bayesian network
def add_cpds_to_network(network, cpds):
    for cpd in cpds:
        network.add_cpds(cpd)

# Main function to run the Monty Hall problem simulation
def main():
    # Create the Monty Hall Bayesian Network
    monty_hall_network = create_monty_hall_network()
    
    # Define the CPDs
    cpds = define_cpds()
    
    # Add CPDs to the network
    add_cpds_to_network(monty_hall_network, cpds)
    
    # Print the CPDs to verify
    print("Conditional Probability Distributions:")
    for cpd in monty_hall_network.get_cpds():
        print(cpd)

if __name__ == "__main__":
    main()
