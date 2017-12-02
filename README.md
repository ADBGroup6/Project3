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
e.g. python main.py INTEGRATED-DATASET.csv 0.04 0.7
### d) Integrated Dataset Description        
a) The NYC Open Data set we chose to generate the INTEGRATED-DATASET file is from Government- NYC Jobs. Details for this dataset can be found here: https://data.cityofnewyork.us/City-Government/NYC-Jobs/kpav-sd4t        
b) High-level procedure to generate INTEGRATED-DATASET.     
c) Detailed explanation of INTEGRATED-DATASET file. Firstly, we remove some columns not useful for rule extraction, which are listed as follows. Job id, Posting Type, Title Code No, Job Description, Minimum Qual Requirements, Preferred Skills, Additional Information, To Apply, Hour/Shift, Work Location, Recruitment Contact, Post Until, Posting Update, Process Date, Salary Frequency and Residency Requirement.Then, for remaining columns, we use the script to categorize column like #of Position to get more meaningful result and map the number 0 in the level column to "level0" to get meaningful result.
### e) Internal Design      
1.
### f) Command Line Specification of Sample Run    
       
