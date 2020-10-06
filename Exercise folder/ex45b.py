#inserting elements in a dictionary
godmanLeader = {"presbyter":"Paul Afonu","date ordained":2019,"place of ordination":"Pantag Adenta","number of attendees":1890}

godmanLeader["leadership role"] = "Associate Pastor"
godmanLeader["cell"] = "Eternal Fellowhship"
godmanLeader["number of mentees"] = 12


leader_1 = godmanLeader.get("presbyter")
leader_1_do = godmanLeader.get ("date ordained")
leader_1_poo = godmanLeader.get("place of ordination")
leader_1_noa = godmanLeader.get("number of attendees")

print(f"""
    Item                  Detail   

Presbyter:            {godmanLeader["presbyter"]}
Leadership Role       {godmanLeader["leadership role"]}
Date Ordained:        {godmanLeader["date ordained"]}
Place of Ordination:  {godmanLeader["place of ordination"]} 
Number of Attendees:  {godmanLeader["number of attendees"]}
Cell :                 {godmanLeader["cell"]}
Number of Mentees:     {godmanLeader["number of mentees"]}



""")