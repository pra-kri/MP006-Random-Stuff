"""
Script to parse a list of URLs provided in a file, and count the number of times each host turns up in the file.
"""

import sys

# stores all unique hostnames. Global variable.
dict_of_hostnames = {}


def single_line_parser(url):
    """
    Parses a single url string input (url) and adds the hostname to the dict_of_hostnames.
    Assume url starts with either http:// or https://
    """
    url_host_str = url.split('/')[2] 
    url_host_seg = url_host_str.split('.') 
    
    if url_host_seg[0] == 'www':
        url_host_seg.pop(0)
    
    hostname = ".".join(url_host_seg)
    
    # update count: how many times has this hostname turned up in this file?
    if hostname in dict_of_hostnames:
        dict_of_hostnames[hostname] = dict_of_hostnames[hostname] + 1
    else:
        dict_of_hostnames[hostname] = 1
    
    return None


def file_parser():
    """ 
    Opens up the file and processes it, line by line.
    Then prints the final results to the command line output.
    """
    
    with open(sys.argv[1], 'r') as f:
        for line in f:
        
            # doesnt allow urls to be processed unless they start with http:// or https://
            if line.startswith('https://'):
                single_line_parser(line)
                
            elif line.startswith('http://'):
                single_line_parser(line)
            
            else:
                pass
    
    # sorts results, reverse order by count, then by alphabetical order of hostname.
    sorted_final = sorted(dict_of_hostnames.items(), key=lambda x: (x[1], x[0]), reverse = True)
    
    # command line output: 
    for i in sorted_final:
        print("{0} {1} ".format(i[1], i[0]))
                



if __name__ == "__main__":

    print("\n\nProcessing the following file: %s" %sys.argv[1])
    print("----------------------------\n")
    file_parser()
    print("\nScript finished.\n\n")
   
