def optimise_list(lists):
    """Transform a redundant list to a non redundant one.
        """
    
    #Create an empty list
    optimised_list = []
    
    #Change the list to a set to delete repetitions
    sets = set(lists)
    new_list = list(sets)

    # while sets:
    #     #Transfer the set elements into the empty list.
    #     new_list=sets.pop()
    #     optimised_list.append(new_list)
    


    return print(f"The unique list is: {new_list}")
    
        
def print_modal_list(list):
    """Print the modal element of the redundant list"""
        #Create an empty dictionary
    element_occurences = {}

    #Loop through the input list
    #Store the number of occurences (count) in the element_occurences dictionary
    for element in list:
        count = list.count(element)
        element_occurences[element]= count

    #Create an empty list to store the key with the highest value from the element_occurences dictionary
    modal_element = []

    #Loop through the key-value pair in the dictionary
    #Check for the maximum value and store its key in the modal_element list
    for dictionary_key,occurence in element_occurences.items():
        if occurence is max(element_occurences.values()):
            modal_element.append(dictionary_key)

    return print(f"The modal element is/are: {modal_element}")

redundant_list =['a','b','a','a',3,3,2,'hello','b']
optimise_list(redundant_list)
print_modal_list(redundant_list)