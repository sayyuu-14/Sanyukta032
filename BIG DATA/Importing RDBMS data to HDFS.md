
### Importing RDBMS Data into HDFS


  <img src="/Images/2.4.PNG" width="500">


  
### 1 ) Create a Table in MySQL
   
  <img src="/Images/2.7.PNG" width="500">
  
    
   ###  Import the Table into HDFS
a. Enter the following Sqoop command (all on a single line), which imports the
salaries table in the test database into HDFS:
    
   <img src="/Images/2.8.PNG" width="500">
   
   ### Select 10 items from the table to verify that it is populated:
   
   <img src="/Images/2.2.PNG" width="500">
   
 ###  You should see a new folder named salaries. View its contents:
     
   <img src="/Images/2.9.PNG" width="500">
   
 ### Use the cat command to view the contents of the files. For example:
      
   <img src="/Images/2.10.PNG" width="500">
   
 ### Specify Columns to Import
a. Using the ‐‐columns argument, write a Sqoop command that imports the salary
and age columns (in that order) of the salaries table into a directory in HDFS
named salaries2. In addition, set the ‐m argument to 1 so that the result is a single
file.
       
   <img src="/Images/2.11.PNG" width="500">
   
  ### Verify that the contents of part‐m‐00000 are only the two columns you specified:
        
   <img src="/Images/2.12.PNG" width="500">

   
    
  <img src="/Images/2.3.PNG" width="500">
  

   ### Importing from a Query
Write a Sqoop import command that imports the rows from salaries in MySQL whose
salary column is greater than 90,000.00.
a. Use gender as the --split-by value, specify only two mappers, and import the
data into the salaries3 folder in HDFS.

   <img src="/Images/2.13.PNG" width="500">
    
  ### View the contents of part‐m‐00000 and part‐m‐00001.
       
   <img src="/Images/2.14.PNG" width="500">
           
           
