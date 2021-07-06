'''
Given a hotel which has 10 floors [0-9] and each floor has 26 rooms [A-Z]. You are given a sequence of rooms, where + suggests room is booked, 
- room is freed. You have to find which room is booked maximum number of times.

You may assume that the list describe a correct sequence of bookings in chronological order; that is, only free rooms can be booked 
and only booked rooms can be freeed. All rooms are initially free. Note that this does not mean that all rooms have to be free at the end. 
In case, 2 rooms have been booked the same number of times, return the lexographically smaller room.

You may assume:

N (length of input) is an integer within the range [1, 600]
each element of array A is a string consisting of three characters: "+" or "-"; a digit "0"-"9"; and uppercase English letter "A" - "Z"
the sequence is correct. That is every booked room was previously free and every freed room was previously booked.
Example:

Input: ["+1A", "+3E", "-1A", "+4F", "+1A", "-3E", ]
Output: "1A"
Explanation: 1A as it has been booked 2 times.

'''


book_dict = {}
# bookings = ["+9A", "+3E", "+4F", "+6A", "+8E","-9A", "-3E", "-4F", "-6A", "-8E"]
bookings = ['+4F',"+1A", "+3E", "-1A", "+4F",  "-3E", '+1A']

max_count = 0
res = None

for b in bookings:
    if b[0] =='+':
        if b in book_dict:
            book_dict[b]+=1
        else:
            book_dict[b]=1
        if max_count == book_dict[b]:
            # lexographically  order
            if b<res:
                print("A",b,res)
                res =b
        else:
            max_count = max(max_count,book_dict[b])
            res = b
            

        
