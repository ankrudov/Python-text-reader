from datetime import datetime
from operator import itemgetter
import sys

#Sort by gender female, male- then last name ascending
def space_separator():
    with open('./space.txt') as f:
        space_list = []
        space_list_separted = []
        space = f.readlines() #list

        for s in space:
            space_list.append(s)
        for name in space_list:
            space_list_separted.append(name.split())
        
 #testing for discrepancies  
        for list_elements in space_list_separted:
            if len(list_elements) > 6:
                sys.exit('ERROR FOUND: incorrect format, ensure txt file follows correct format: 6 elements and a space. Check space.txt file')
        sorted_space = sorted(space_list, key=itemgetter(0,3))
        output = [''.join(x)for x in sorted_space]
        for out in output:
            print(f'output 1: {out}')

#sort by birthdate ascending then last name ascending
def comma_separator():
    with open('./comma.txt') as e:
        comma_list = []
        name_list = []
        comma = e.readlines() #list
        for i in comma:
            comma_list.append(i.replace(',',''))
        for name in comma_list:
            name_list.append(name.split())

        #testing for discrepancies  
        for list_elements in name_list:
            if len(list_elements) > 5:
                sys.exit('ERROR FOUND: incorrect format, ensure txt file follows correct format: 5 elements and a comma. Check comma.txt file')
        
        sort_test= sorted(name_list,key= lambda x:(datetime.strptime(x[4],"%m/%d/%Y"),x[0]))
        out_value = [' '.join(x) for x in sort_test]
        for output in out_value:
            print(f'Output two: {output}')


#sort by last name descending
def pipe_separator():      
    with open('./pipe.txt') as d:
        pipe_list = []
        pipe_list_separated = []
        pipe = d.readlines() #list
        for i in pipe:
            pipe_list.append(i.replace('|',''))
        for name in pipe_list:
            pipe_list_separated.append(name.split())
        
        #testing for discrepancies 
        for list_elements in pipe_list_separated:
            if len(list_elements) > 6:
                sys.exit('ERROR FOUND: incorrect format, ensure txt file follows correct format: 6 elements and a pipe |, Check pipe.txt file')
                
        sorted_list = sorted(pipe_list_separated,key=itemgetter(0),reverse=True)
        output_list = [' '.join(x) for x in sorted_list]
        for out in output_list:
            print(f'Output three: {out}')
    

    



space_separator()
comma_separator()
pipe_separator()