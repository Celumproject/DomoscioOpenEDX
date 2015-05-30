import json

def parseReviews(string_to_parse):
    
    d = json.loads(string_to_parse)
    r = []

    for item in d :
        r.append(str(item["knowledge_node_uid"]) + ", on " + str(item["next_review_at"]))

    return r



print ' --------- '.join(parseReviews('[{"history": "0","knowledge_node_uid": "i4x://edX/DemoX/problem/75f9562c77bc4858b61f907bb810d974","id": 142,"knowledge_node_id": 129,"student_uid": "domoscio","next_review_at": "2015-05-31T10:12:35.497Z","student_id": 51}]'))