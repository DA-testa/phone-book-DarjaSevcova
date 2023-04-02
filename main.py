# python3 Darja Ševcova 221RDC039

class Query:
    def __init__(self):
        self.book = {}
        
    def add(self, number, name):
        self.book[number] = name
        
    def delete(self, number):
        if number in self.book and self.book[number] is not None:
            self.book[number] = None
            
    def find(self, number):
        name = self.book.get(number)
        if name is None:
            return "not found"
        else:
            return name

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(contacts):
    print('\n'.join(contacts))

def process_queries(queries):
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        cur_query = queries[0]
        if cur_query.type == 'add':
            number = int(cur_query[1])
            name = cur_query[2]
            hash_table.add(number, name)
        elif cur_query.type == 'del':
            number = int(cur_query[1])
        else:
            number = int(querly[1])
            response = hash_table.find(number)
            contacts.append(response)
    return contacts

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

