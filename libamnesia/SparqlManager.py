import random
import textwrap
from SPARQLWrapper import SPARQLWrapper, JSON

class SparqlManager():

    def __init__(self, endpoint, username, password, prefix, user_graph):

        self.endpoint = endpoint
        self.username = username
        self.password = password
        self.prefix = prefix
        self.user_graph = user_graph
        self.graphs_list = []

    def sparql_query(self, query):

        sparql = SPARQLWrapper(self.endpoint)
        sparql.setCredentials(self.username, self.password)
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()["results"]["bindings"]

        res_list = []
        seen = set()
        for result in results:
            res_dict = {}
            for key in result:
                res_dict[key] = result[key]['value']
            res_list.append(res_dict)
        return res_list



    def get_data_graphs(self):

        query = textwrap.dedent(
        '''
        PREFIX : <%s>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        SELECT ?g ?owner
        WHERE {
            GRAPH ?g {
                ?g :accessLevel "private" .
                ?g dc:creator ?owner .
            }

        }
        GROUP BY ?g
        ''' % (self.prefix, ))

        self.graphs_list = self.sparql_query(query)


    def drop_graphs(self):

        for graph in self.graphs_list:

            query = textwrap.dedent(
            '''
            DROP SILENT GRAPH <%s>
            ''' % (graph['g'],)) 
            print(query)
            self.sparql_query(query)

        
    def drop_metadata(self):

        for graph in self.graphs_list:

            query = textwrap.dedent(
            '''
            DELETE WHERE { GRAPH <%s:%s> { <%s> ?p ?o }}
            ''' % (self.user_graph, graph['owner'], graph['g']))
            print(query)
            self.sparql_query(query)