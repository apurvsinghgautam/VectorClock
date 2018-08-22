#This function returns maximum of two vectors
def vector_compare(vector1,vector2):
    vector = [max(value) for value in zip(vector1,vector2)]
    return vector


P = {1:{}, 2:{}, 3:{}} # Inititalized an empty dictionary having 3 process
inc = 0
e1 = int(input("Enter the no. of events in Process 1:"))
e1 = [i for i in range(1, e1 + 1)]
P[1] = {key: [inc + key, 0, 0] for key in e1}
e2 = int(input("Enter the no. of events in Process 2:"))
e2 = [i for i in range(1, e2 + 1)]
P[2] = {key: [0, inc + key, 0] for key in e2}
e3 = int(input("Enter the no. of events in Process 3:"))
e3 = [i for i in range(1, e3 + 1)]
P[3] = {key: [0, 0, inc + key] for key in e3}
comm = int(input("Enter the no of communication lines:"))
while inc < comm:
    sent = int(input("Enter the sending process number:"))
    recv = int(input("Enter the receiving process number:"))
    sent_event_no = int(input("Enter the sending event number:"))
    recv_event_no = int(input("Enter the receiving event number:"))
    if sent <= 3 and recv <= 3:
    	print ("P{} --> P{}".format(sent,recv))
    	new_vector = vector_compare(P[sent][sent_event_no],P[recv][recv_event_no])
    	P[recv][recv_event_no] = new_vector
    	print ("New vector value for P{} for event{} is: {}".format(recv,recv_event_no,P[recv][recv_event_no]))
    	if (recv_event_no+1) in P[recv]:
    		P[recv][recv_event_no+1] = vector_compare(P[recv][recv_event_no],P[recv][recv_event_no+1])
    else:
    	print ("Enter the sent/recv within existing process")
    inc += 1
    
    
