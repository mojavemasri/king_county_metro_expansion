# King County Metro Expansion

<img width="841" alt="Screenshot 2024-05-08 at 4 54 24 PM" src="https://github.com/mojavemasri/king_county_metro_expansion/assets/56557136/621097eb-e0e7-4394-8506-e963b3b5f97f">



## Overview
This project aims to optimize the locations of metro stops in the Eastern King County metro area using a simulated annealing algorithm, since the current expansion is [under way](https://www.soundtransit.org/system-expansion/east-link-extension). By strategically placing metro stops using, we seek to improve the efficiency and accessibility of this expansion.

## Methods Utilized
### Simulated Annealing Algorithm
Simulated annealing is a probabilistic optimization algorithm inspired by the annealing process in metallurgy. It iteratively explores the solution space, allowing for movement towards better solutions while occasionally accepting worse solutions to escape local optima. By using this process, we can explore a complex state space such as transit networks in a flexible way.

### Data Collection
Data on income levels, population size, cultural areas, and regional division was collected from [King County GIS Data Hub](https://kingcounty.gov/en/legacy/services/gis/gisdata) to populate and train the model. Geographic Information System (GIS) tools such as geopandas and photon were also utilized to preprocess and visualize the data.

### Fitness Function
I designed a fitness function with the intent of aggregating a combination of metrics:
- a distance matrix between a weighted population sample and the candidate points
- the optimal route (calculated with a no return symmetric TSP with distance between points as the metric)
- a distance matrix between the stops and an unweighted "Points of Interest" distance matrix


## Limitations
### Data Quality
The data used for this project was publically available data, and was not as granular as it could have been. A more granular dataset with more subdivisions and more accurate figures would help tune this model better.

### Simplifying Assumptions
Certain simplifications and assumptions were made to facilitate the optimization process and for computational resourcefulness, such as Euclidean and uniform travel times, lack of constraints on viable construction sites and bottlenecks, uniform traffic burden, etc.. These simplifications may not fully capture the complexities of real-world transportation systems.

### Computational Complexity
Optimizing metro stop locations for a large geographic area involves a combinatorial optimization problem with a vast solution space. While simulated annealing offers an efficient alternative to traditional methods, the computational resources required can be significant. 

## Future Endeavors
### Genetic Algorithm
One alternative that could be interesting to explore once more constraints are introduced into this project is generating a finite sample of viable construction points, and running a genetic algorithm to determine the most effective combination of options. This would be more reflective of real world conditions, and would most likely save computational time. However, more data regarding traffic conditions, zoning areas, and geological sites would be required, as well as a manual process of selecting viable areas to build, such as manually adjusting the weighting on the "Points of Interest" to reflect areas which would be optimal for subway construction.

### Fine-Tuning Parameters
Further experimentation with the simulated annealing algorithm, including adjusting temperature schedules and neighborhood exploration strategies, could potentially improve the quality of the solutions obtained.

### Stakeholder Engagement
Engaging with local communities, transportation authorities, and urban planners will be crucial for ensuring that this optimized metro system meets the needs and preferences of the diverse stakeholders in the Eastern King County area.


## Required Packages:
- numpy
- pandas
- geopandas
- geodatasets
- geopy
- shapely
- tqdm
- matplotlib
- scipy
