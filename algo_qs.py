# TASK 1 -> 
# Given an adjacency list, write a function to print the 
# topological ordering of its vertices
# a) Also: Think of edge cases, and how to take care of those.


def topological_sort(nested_list):
    """ Returns topological order of vertices in graph """
    
    no_of_nodes = len(nested_list)
    answer = []
    
    while len(answer) < no_of_nodes:
        
        # Search for nodes with no dependencies.
        # These nodes get added to a final 'answer' list.
        for counter, i in enumerate(nested_list):
            if not i:
                if counter not in answer:
                    answer.append(counter) #adds node to final answer list
        
        # If a node was added to the final 'answer' list,
        # remove that node from the graph
        for j in nested_list:
            for k in answer:
                if k in j:
                    j.remove(k)
                    
    return answer, len(answer)

graph_0 = [[1,2,3],[4,5], [6,7], [7],[7],[6],[7],[]]
print(topological_sort(graph_0))

graph_1 = [[1,2,3],[4,5], [6,7], [7],[7],[6],[],[]]
print(topological_sort(graph_1))



# ===================================================================
# ===================================================================
# TASK 2 -> 
# Convert phone-number into all possible combinations of letters.

def combine_lists(list_1, list_2):
    """ 
    Returns possible combinations of elements in two input list.
    Can also use itertools.product() instead for production code.
    """
    all_combinations = []
    
    for i in list_1:
        for j in list_2:
            all_combinations.append(i+j)
            
    return all_combinations
    
    
    
def phone_combination(phone_number):
    
    # Use list with an empty string. Cant use empty list.
    final_answer = ['']
    
    numbers_to_letters = {'0':[''],
                         '1':[''],
                         '2':['A','B','C'],
                         '3':['D','E','F'],
                         '4':['G','H','I'],
                         '5':['J','K','L'],
                         '6':['M','N','O'],
                         '7':['P','Q','R','S'],
                         '8':['T','U','V'],
                         '9':['W','X','Y','Z'],}
    
    for i in str(phone_number):
        final_answer = combine_lists(final_answer, numbers_to_letters[i])
   
    
    return final_answer
    


print(phone_combination('0757212'))
