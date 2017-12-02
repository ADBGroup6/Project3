# Association Rule Extraction
## COMS E6111 Advanced Database System - Project 3 
### a) Project 3 Group6
  Wanheng Li (wl2573)    
  Yibo Xu (yx2387)
### b) List of Files    
main.py   
INTEGRATED-DATASET.csv
### c) Instruction for Running the Program
**Command:**    
Please run the program with following commond:    
[Directory] [data_file] [min_sup] [min_conf].         
**min_sup** is the support threshold for frequent itemsets.    
**min_conf** is threshold for confidence of association rule.     
e.g. python main.py INTEGRATED-DATASET.csv 0.10 0.7
### d) Integrated Dataset Description        
a) The NYC Open Data set we chose to generate the INTEGRATED-DATASET file is from Government- NYC Jobs. Details for this dataset can be found here: https://data.cityofnewyork.us/City-Government/NYC-Jobs/kpav-sd4t        
b) **High-level procedure to generate INTEGRATED-DATASET.** To better get the rule extraction result, we will remove some columns with almost all elements empty, and those with distinct value for all elements like job description, which will not satisfy the min support or contribute to extraction rule at all. Then we map column with single number to more meaningful descriptive string and categorize the value for some columns.      
**Detailed explanation of INTEGRATED-DATASET file.** Firstly, we remove some columns not useful for rule extraction, which are listed as follows. Job id, Posting Type, Title Code No, Job Description, Minimum Qual Requirements, Preferred Skills, Additional Information, To Apply, Hour/Shift, Work Location, Recruitment Contact, Post Until, Posting Update, Process Date, Salary Frequency and Residency Requirement. Then, for remaining columns, we use the script to categorize column like #of Position to get more meaningful result and map the number 0 in the level column to "level0" to get meaningful result. Also, we combine the column of SalaryFrom and SalaryTo, and round up the number by thousand to categorize the salary range and get more meaningful result for later rule extraction.       
c) Choice of INTEGRATED-DATASET     
The dataset contains many columns, thus various items will guarantee association rules extracted using a-priori algorithm. The association extracted are meaningful using the NYC job dataset, as we can expect some meaningful rule extracted between item from "Business Title" and "Job category", or "level" and "Salary Range".
### e) Internal Design         
There are mainly two phases for a-priori algorithm, and the implementation of this project based on a-priori algorithm is stated as below:    
1. Iteratively find all item-sets that are greater than or equal to **min_sup**. Beginning with large 1-itemsets L1, find the large (k-1)-itemsets until large k itemset is empty.
2. With Apriori candidate genration function, generate candidate itemsets. In the join step, superset of the set of all large k-itemsets are generated by joining L(k-1) with L(k-1). In the prune step, delete all itemsets such that some (k-1)-subset of c is not in L(k-1). Only the itemsets greater or equal to minimum support are reamined.    
3. Only the association rule exceeding the min_conf will be extracted from the itemset.
### f) Command Line Specification of Sample Run    
       
Here are some interesting association rules extracted:     
