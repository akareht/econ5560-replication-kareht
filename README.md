## ECON 5560 Replication

Purpose: This code replicates the results from the paper "Non-Market Values in a Cost Benefit World: Evidence from a Choice Experiment" by Eppink et al 2016. (https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0165365)

Summary: This code replicates figure 1 and two conditional logit models from Eppink et al 2016. The first conditional logit model is almost spot on. In the second conditional logit model some coefficients are different from those reported in the paper. This code does not replicate the mixed logit models from the paper.

Data: The file titled S1Table.DTA provides the data that was published by the authors it can also be found at the link above.

run_all.py: loads and cleans data, replicates and saves figure 1 from the paper, and runs two conditional logit models and saves model summary tables.

replication.ipynb: loads and cleans data, shows more data exploration, replicates figure 1, and runs two conditional logit models.

Installation/Execution: The repo either be downloaded through the web interface or by using the common 'git clone https://github.com/akareht/econ5560-replication-kareht'. This will create a copy of this repo on your machine, this includes downloading the data. To run the code first ensure you navigate into the directory (eg 'cd econ5560-replication-kareht') otherwise the code will not be able to read the data. Then simply run 'python run_all.py'. (Provided you have all the necessary packages installed on your machine/in your enviroment).

Dependencies: Python (3.15), Juypter Notebooks, Numpy (2.5.4), Pandas (3.0.6), Matplotlib (3.11.2), Statsmodels (0.15.0), ipynbkernel (7.4.0).

Citation: Eppink, F. V., Winden, M., Wright, W. C. C., & Greenhalgh, S. (2016). Non-market values in a cost-benefit world: Evidence from a choice experiment. *PLOS ONE, 11*(10), e0165365. https://doi.org/10.1371/journal.pone.0165365
