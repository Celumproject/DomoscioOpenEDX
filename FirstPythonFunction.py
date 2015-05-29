import requests
import json
from pprint import pprint

def createKnowledgeNode(uid) :
    # Create a KnowledgeNode given the content parameter
    r = requests.post("http://stats-engine.domoscio.com/v1/companies/32/knowledge_nodes?uid=" + str(uid) + "&knowledge_graph_id=57&token=cd841abb68694c5c7a44d17af1a12582")
    return json.loads(r.text)["id"]
    
                                                
def createStudent(uid) :
    # Create a KnowledgeNode given the content parameter
    data = {
        "student_group_id": 1,
        "uid" : uid,
        "civil_profile_attributes": {
            "name": "Nadra",
            "sexe": "female",
            "day_of_birth": "2015-05-29",
            "place_of_birth": "FR",
            "country_of_residence": "FR",
            "city_of_residence": "Paris"
        }
    }
    params = {
        "token": "cd841abb68694c5c7a44d17af1a12582",
        "knowedge_graph_id": 57
    }

    r = requests.post("http://stats-engine.domoscio.com/v1/companies/32/students", params=params, json=data)
    return json.loads(r.text)["id"]

def createKnowledgeNodeStudent(student_id, knowledge_node_id) :
    # Create a KnowledgeNode given the content parameter
    r = requests.post("http://stats-engine.domoscio.com/v1/companies/32/knowledge_node_students?student_id=%s&knowledge_node_id=%s&token=cd841abb68694c5c7a44d17af1a12582" % (student_id, knowledge_node_id))
    return json.loads(r.text)["id"]
    

def createResult(uid1, uid2, result) :
    # Create a KnowledgeNode given the content parameter
    r = requests.post("http://stats-engine.domoscio.com/v1/companies/32/results?knowledge_node_uid=%s&value=%s&token=cd841abb68694c5c7a44d17af1a12582&student_uid=%s" % (uid1, result, uid2))

    return json.loads(r.text)["id"]

                                                
def fetchAllReviews(uid) :
    # Fetch all the knowledgeNodes that are to be reviewed
    r = requests.get("http://stats-engine.domoscio.com/v1/companies/32/review_utils/fetch_reviews?student_uid=" + str(uid) + "&token=cd841abb68694c5c7a44d17af1a12582")
    pprint(r.text)
    return json.loads(r.text)

uid = 12323
student_id = createStudent(uid)
knowledge_node_id = createKnowledgeNode(uid)

print "Created student = %s" % student_id
knowledge_node_uid = createKnowledgeNodeStudent(student_id, knowledge_node_id)
print "Created knowledge_node_uid = %s" % knowledge_node_uid
result = createResult(uid, uid, 1)
print "Created result = %s" % result

print fetchAllReviews(uid)