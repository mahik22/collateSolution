# collateSolution
Solution

Points to consider:

1. Input argument:
    i. important_keys: String of important keys along with datatype
        Expected Format: "id:int,name:str,food:str,type:str"
    ii. hierarchies: String of type denoting hierarchy by  "->"
    Expected Format: "A->B->C"

2. Please check keysAndHierarchy.txt for sample input arguments

3. input.txt - Gets read in the python script itself. Hardcoded "input.txt" file name.

4. The processed data is outputted to stdout in the format:
    i. First line displays the important keys
    ii. Subsequent lines contains a valid line from input.txt which consists of values of important keys in the line.

5. process_file file - processes every line of the file and returns an dictionary which keeps track of all the lines with similar type. 

6. print_processed_data -  Prints the processed dictionary to stdout.