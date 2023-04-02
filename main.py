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
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else: # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

