import os
import shutil
import urbs


input_files = '1urbs_Germany_NUTS2_2050_full_dc.xlsx'  # for single year file name, for intertemporal folder name
input_dir = 'Input'
input_path = os.path.join(input_dir, input_files)

result_name = 'single-year'
result_dir = urbs.prepare_result_directory(result_name)  # name + time stamp

# copy input file to result directory
try:
    shutil.copytree(input_path, os.path.join(result_dir, input_dir))
except NotADirectoryError:
    shutil.copyfile(input_path, os.path.join(result_dir, input_files))
# copy run file to result directory
shutil.copy(__file__, result_dir)

# objective function
objective = 'cost'  # set either 'cost' or 'CO2' as objective

# Choose Solver (cplex, glpk, gurobi, ...)
solver = 'glpk'

# simulation timesteps
(offset, length) = (0, 168)  # time step selection
timesteps = range(offset, offset+length+1)
dt = 1  # length of each time step (unit: hours)

# detailed reporting commodity/sites
report_tuples = [
    (2050, 'DE11', 'Elec'),
    (2050, 'DE12', 'Elec'),
    (2050, 'DE13', 'Elec'),
    (2050, 'DE14', 'Elec'),
    (2050, 'DE21', 'Elec'),
    (2050, 'DE22', 'Elec'),
    (2050, 'DE23', 'Elec'),
    (2050, 'DE24', 'Elec'),
    (2050, 'DE25', 'Elec'),
    (2050, 'DE26', 'Elec'),
    (2050, 'DE27', 'Elec'),
    (2050, 'DE30', 'Elec'),
    (2050, 'DE40', 'Elec'),
    (2050, 'DE50', 'Elec'),
    (2050, 'DE60', 'Elec'),
    (2050, 'DE71', 'Elec'),
    (2050, 'DE72', 'Elec'),
    (2050, 'DE73', 'Elec'),
    (2050, 'DE80', 'Elec'),
    (2050, 'DE91', 'Elec'),
    (2050, 'DE92', 'Elec'),
    (2050, 'DE93', 'Elec'),
    (2050, 'DE94', 'Elec'),
    (2050, 'DEA1', 'Elec'),
    (2050, 'DEA2', 'Elec'),
    (2050, 'DEA3', 'Elec'),
    (2050, 'DEA4', 'Elec'),
    (2050, 'DEA5', 'Elec'),
    (2050, 'DEB1', 'Elec'),
    (2050, 'DEB2', 'Elec'),
    (2050, 'DEB3', 'Elec'),
    (2050, 'DEC0', 'Elec'),
    (2050, 'DED2', 'Elec'),
    (2050, 'DED4', 'Elec'),
    (2050, 'DED5', 'Elec'),
    (2050, 'DEE0', 'Elec'),
    (2050, 'DEF0', 'Elec'),
    (2050, 'DEG0', 'Elec')]

# optional: define names for sites in report_tuples
report_sites_name = {}

# plotting commodities/sites
plot_tuples = [
#   (2019, 'North', 'Elec'),
#    (2019, 'Mid', 'Elec'),
#    (2019, 'South', 'Elec'),
#    (2019, ['North', 'Mid', 'South'], 'Elec')
    ]

# optional: define names for sites in plot_tuples
plot_sites_name = {('North', 'Mid', 'South'): 'All'}

# plotting timesteps
plot_periods = {
    'all': timesteps[1:]
}

# add or change plot colors
my_colors = {
    'South': (230, 200, 200),
    'Mid': (200, 230, 200),
    'North': (200, 200, 230)}
for country, color in my_colors.items():
    urbs.COLORS[country] = color

# select scenarios to be run
scenarios = [
             urbs.scenario_base,
#             urbs.scenario_stock_prices,
#             urbs.scenario_co2_limit,
#             urbs.scenario_co2_tax_mid,
#             urbs.scenario_no_dsm,
#             urbs.scenario_north_process_caps,
#             urbs.scenario_all_together
            ]

for scenario in scenarios:
    prob = urbs.run_scenario(input_path, solver, timesteps, scenario,
                             result_dir, dt, objective,
                             plot_tuples=plot_tuples,
                             plot_sites_name=plot_sites_name,
                             plot_periods=plot_periods,
                             report_tuples=report_tuples,
                             report_sites_name=report_sites_name
                                )
