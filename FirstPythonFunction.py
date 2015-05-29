def createKnowledgeNode(content_name) :
    # Create a KnowledgeNode given the content parameter
    import requests
    import json
    
    r = requests.post("http://stats-engine.domoscio.com/v1/companies/32/knowledge_nodes?name=" + content_name + "&knowledge_graph_id=57&token=cd841abb68694c5c7a44d17af1a12582")
    return json.loads(r.text)["id"]
    
                                                
def createStudent() :
    # Create a KnowledgeNode given the content parameter
    import requests
    import json
    
    data = {
        "student_group_id": 1,
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

def createKnowledgeNodeStudent(student_id) :
    # Create a KnowledgeNode given the content parameter
    import requests
    import json
    
    r = requests.post("http://stats-engine.domoscio.com/v1/companies/32/knowledge_node_students?student_id=" + str(student_id) + "&knowledge_node_id=116&token=cd841abb68694c5c7a44d17af1a12582")
    
    return json.loads(r.text)["id"]
    

def createResult(knowledge_node_student_id, result) :
    # Create a KnowledgeNode given the content parameter
    import requests
    import json
    
    r = requests.post("http://stats-engine.domoscio.com/v1/companies/32/results?knowledge_node_student_id=" + str(knowledge_node_student_id) + "&value=" + str(result) + "&token=cd841abb68694c5c7a44d17af1a12582")

    return json.loads(r.text)["id"]

                                                
def fetchAllReviews(student_id) :
    # Fetch all the knowledgeNodes that are to be reviewed
    import requests
    import json
    
    r = requests.get("http://stats-engine.domoscio.com/v1/companies/32/review_utils/fetch_reviews?student_id=" + str(student_id) + "&token=cd841abb68694c5c7a44d17af1a12582")
    
    return json.loads(r.text)

student_id = createStudent()
knowledge_node_student_id = createKnowledgeNodeStudent(student_id)
createResult(knowledge_node_student_id, 1)

print fetchAllReviews(student_id)