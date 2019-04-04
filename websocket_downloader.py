# [] Downloads JSON files from websocket, and saves to SQLite database
# [] Tailored specifically for JSON data from websocket: ws://wikimon.hatnote.com:9000


import sqlite3
import json
from websocket import create_connection

# global variables: path of database file and the table name.
database_001 = r"C:\Users\Prabesh K\Desktop\Projects\db_ex_002.db"
table_001 = "table_001"



def create_table(db_file, table_name):
    """ 
    Creates db and table at path provided.
    If database and table already exist, then function does nothing.
    
    :: input :: db_file        --> This is the path of the database file to create.
    :: input :: table_name     --> Name of SQL table to create.
    """
    
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    
    columns = ['action', 'change_size INTEGER', 'flags', 'geo_ip', 'hashtags',
              'is_anon', 'is_bot', 'is_minor', 'is_new',
              'is_unpatrolled', 'mentions', 'ns', 'page_title',
              'parent_rev_id', 'rev_id', 'summary', 'url', 'user']
    
    query_part_a = "CREATE TABLE IF NOT EXISTS " + table_name 
    query_part_b = " (" + ','.join(columns) + ");"
    
    sql_create_base_table = query_part_a + query_part_b
    
    c.execute(sql_create_base_table)
    conn.commit()
    conn.close()
	
    return None
    

def commit_json_to_table(db_file, table_name, json_data):
    """ 
    Takes in a json file and inserts the data into the SQL table given.
    
    :: input :: db_file     --> Database to write to.
    :: input :: table_name  --> Table to write to.
    :: input :: json_data   --> json data to insert into database.
                                json data must represent a single dictionary.
                                
    """
    
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    
    # convert json to python dictionary format.
    dictionary_data = json.loads(json_data)
    
    # columns in sql table - for reference.
    columns = ['action', 'change_size', 'flags', 'geo_ip', 'hashtags',
              'is_anon', 'is_bot', 'is_minor', 'is_new',
              'is_unpatrolled', 'mentions', 'ns', 'page_title',
              'parent_rev_id', 'rev_id', 'summary', 'url', 'user']
    
    keys_list = dictionary_data.keys()
    
    
    # Need to use if x in keys_list else None condition.
    # Sometimes WEbsocket doesnt provide full json data.
    # e.g. Websocket may provide json with the 'geo_ip' section missing.
    action = str(dictionary_data["action"]) if "action" in keys_list else None
    change_size = str(dictionary_data["change_size"]) if "change_size" in keys_list else None
    flags = str(dictionary_data["flags"]) if "flags" in keys_list else None
    geo_ip = str(dictionary_data["geo_ip"]) if "geo_ip" in keys_list else None
    hashtags = str(dictionary_data["hashtags"]) if "hashtags" in keys_list else None
    is_anon = str(dictionary_data["is_anon"]) if "is_anon" in keys_list else None
    is_bot = str(dictionary_data["is_bot"]) if "is_bot" in keys_list else None
    is_minor = str(dictionary_data["is_minor"]) if "is_minor" in keys_list else None
    is_new = str(dictionary_data["is_new"]) if "is_new" in keys_list else None
    is_unpatrolled = str(dictionary_data["is_unpatrolled"]) if "is_unpatrolled" in keys_list else None
    mentions = str(dictionary_data["mentions"]) if "mentions" in keys_list else None
    ns = str(dictionary_data["ns"]) if "ns" in keys_list else None
    page_title = str(dictionary_data["page_title"]) if "page_title" in keys_list else None
    parent_rev_id = str(dictionary_data["parent_rev_id"]) if "parent_rev_id" in keys_list else None
    rev_id = str(dictionary_data["rev_id"]) if "rev_id" in keys_list else None
    summary = str(dictionary_data["summary"]) if "summary" in keys_list else None
    url = str(dictionary_data["url"]) if "url" in keys_list else None
    user = str(dictionary_data["user"]) if "user" in keys_list else None
    # TODO: change data-types from all str to the appropriate types, such as INT or BOOL.
    # TODO: Add a second table, for geo_ip. Link that table to this table. 
    # For now, sticking with str, since I'm getting lots of errors when converting, and not enough time to fix.
    
    
    # Put variables in a list, in the same order as the columns of the sql table.
    # TODO: Can improve this whole process if I used SQLAlchemy instead.
    data = [action, change_size, flags, geo_ip, hashtags,is_anon, 
            is_bot, is_minor, is_new,
            is_unpatrolled, mentions, ns, page_title,
            parent_rev_id, rev_id, summary, url, user]
    
    c.execute("INSERT INTO " + table_name +" values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
    conn.commit()
    conn.close()
    
    return None




def websocket_dl(db_file, table_name, N = 20):
    """
    Downloads N json packets from the wikimon.hatnote.com:9000 websocket.
    Each json packet is a single dictionary. - e.g. "{key1:value1, key2:value2 ...etc}"
    :: input :: db_file     --> database path, to write to.
    :: input :: table_name  --> table name, to write to.
    :: input :: N           --> no. of json dictionaries to download.
    """
    
    # to limit no. of downloads, so testing doesnt take too long, stop function if N>50.
    if N> 50:
        print("More than 50 downloads set. Too much (for testing purposes). Use a smaller value pls.")
        return None # limits to 50 dls per run of the functoin - just for testing purposes.
    
    
    print("You will download %s json dictionaries from ws://wikimin.hatnote.com:9000 " %N)
    ws = create_connection("ws://wikimon.hatnote.com:9000")
    counter = 0
    
    while counter < N:
        result_json = ws.recv()
        result_dict = json.loads(result_json)
        counter+=1
        
        # saves json data to SQL database.
        commit_json_to_table(db_file, table_name, result_json)
        print("json packets downloaded to Database so far: %s"  % counter)
        
    print("Download complete.")
    
    return None





if __name__ == "__main__":
    print("Will now run the json downloader script.")
    print("Your database path global variable is: %s" % database_001)
    print("Your table name global variable is: %s" % table_001)
	
    create_table(database_001, table_001)
    websocket_dl(database_001, table_001, N = 45)

    print("Json download script complete.")
    
    
	
	
