import math
import pandas as pd
import numpy as np

questionList = [[22, 63, 53, 66], [22, 68, 51, 71], [22, 73, 53, 76], [22, 78, 47, 82], [181, 63, 192, 66], [181, 68, 206, 71], [181, 73, 220, 76], [181, 78, 220, 82], [234, 63, 255, 66], [181, 88, 229, 91], [67, 97, 133, 100], [220, 97, 298, 100], [22, 102, 36, 106], [22, 107, 42, 111], [181, 102, 194, 106], [181, 107, 200, 111], [22, 131, 35, 135], [181, 131, 192, 135], [75, 131, 98, 135], [128, 131, 139, 138], [234, 131, 255, 135], [286, 131, 298, 138], [29, 140, 40, 143], [75, 140, 99, 143], [135, 140, 145, 143], [161, 140, 171, 143], [189, 140, 197, 143], [208, 140, 231, 143], [236, 140, 255, 143], [280, 140, 316, 143], [94, 183, 106, 186], [208, 190, 284, 194], [147, 195, 212, 199], [22, 211, 143, 214], [22, 256, 49, 259], [22, 262, 55, 266], [22, 269, 50, 272], [22, 275, 65, 279], [234, 282, 336, 285], [22, 283, 49, 287], [266, 285, 303, 289], [22, 291, 122, 301], [160, 305, 199, 308], [260, 305, 309, 308]]
questionTokenList = ['Bill of Supply', 'Invoice Date', 'Date Of Issue', 'Vehicle No', 'State', 'State Code', 'DC No & DC Date', 'Customer Ref No', 'Karnataka', 'Customer PO/Ref No', 'Details Of Receiver/Billed to:', 'Details Of Consignee/Shipped  to:', 'Name', 'Address', 'Name', 'Address', 'State', 'State', 'Karnataka', 'State Code', 'Karnataka', 'State Code', 'S.No', 'Item Name', 'HSN', 'UoM', 'Qty', 'Unit Price', 'Dis Amt', 'Value of Supply', 'Total', 'Amount Payable After Round Off', 'Total Invoice Amount In Words', '1.Payment by Cash / Demand Draft / Bank Transfer only', 'Bank Name', 'Branch  Name', 'Bank Ac/No', 'Bank Branch IFSC', 'Certified that the perticulars given above are', 'Declaration', 'true and correct', 'We declare that this bill of supply shows the actual price of the goods described and that all particulars are true and correct', '( Common Seal )', 'Authorized Signatory']
answerList = [[81, 26, 278, 30], [152, 32, 207, 36], [142, 39, 217, 43], [93, 46, 266, 51], [75, 63, 112, 66], [75, 68, 103, 71], [75, 73, 103, 76], [234, 68, 239, 71], [234, 73, 308, 76], [234, 78, 270, 82], [260, 88, 307, 91], [75, 102, 163, 106], [75, 107, 171, 111], [234, 102, 321, 106], [234, 107, 327, 124], [234, 126, 278, 129], [75, 111, 175, 124], [75, 126, 120, 129], [22, 126, 49, 129], [49, 145, 125, 148], [33, 147, 36, 150], [136, 147, 144, 150], [162, 147, 170, 150], [185, 147, 200, 150], [212, 147, 226, 150], [241, 147, 250, 150], [288, 147, 308, 150], [74, 148, 101, 152], [49, 153, 125, 157], [33, 155, 36, 159], [136, 155, 144, 159], [162, 155, 170, 159], [186, 155, 199, 159], [212, 155, 226, 159], [241, 155, 250, 159], [289, 155, 307, 159], [78, 157, 97, 160], [184, 183, 202, 186], [241, 183, 250, 186]]
answerTokenList = ['No.1047/A, 1st Main, E cross, Goragunte Palya, Yeshwanthpur Bangalore 560022', 'Phone: ,080-22452332', 'Email: feedback@nandus.com', 'GSTIN :29AAHCN4098F1Z2, PAN :AHCN4098F1Z2', '11482/SI/270924', '27-Sep-2024', '27-Sep-2024', '29', '8347/MDC/270924 & 27-Sep-2024', 'SHRB74D4413D', '43214ISD47VOMP2Q', 'SHREYASH RETAIL PRIVATE LIMITED', '1st Floor, Building No./Flat No.: Cabin -BGL-', 'SHREYASH RETAIL PRIVATE LIMITED', 'Coldstar Logistics Pvt Ltd, C/O Freezesure Cold chain Logistics 70 /3, Tavarekere Village, Hobli, Tavarekere Bangalore 562130. ,MOB:', '29AAXCS0655F1ZU', 'BO_3,Unit No. 101, Survay No. 126/9,Prestige Nugget, Infantry Road, Bengaluru, Bengaluru Urban, Karnataka - 560001 Bengaluru,MOB:7019217173', '29AAXCS0655F1ZU', 'GSTIN/PAN', 'PC001 - Packed Chicken Curry Cut', '1', '207', 'Pcs', '170.00', '131.82', '0.00', '22409.40', 'without Skin', 'PC003 - Packed Chicken Curry Cut', '2', '207', 'Pcs', '37.00', '124.02', '0.00', '4588.74', 'with Skin', '207.000', '0.00']

def calc_center_of_right(box):
    x1, y1, x2, y2 = box
    center_x=(x2+x2)/2
    center_y=(y1+y2)/2
    return [center_x, center_y]

def calc_center_of_left(box):
    x1, y1, x2, y2 = box
    center_x=(x1+x1)/2
    center_y=(y1+y2)/2
    return [center_x, center_y]

def calc_center_of_box(box):
    x1, y1, x2, y2 = box
    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2
    return [center_x, center_y]

n = min(len(questionList), len(questionTokenList), len(answerList), len(answerTokenList))

data = []
for i in range(n):
    row = {
        "question_box": questionList[i],
        "question_right_center": calc_center_of_right(questionList[i]),
        "question_center": calc_center_of_box(questionList[i]),
        "question_token": questionTokenList[i],
        "answer_box": answerList[i],
        "answer_left_center": calc_center_of_left(answerList[i]),
        "answer_center": calc_center_of_box(answerList[i]),
        "answer_token": answerTokenList[i]
    }
    data.append(row)

question_right_center_ = [calc_center_of_right(box) for box in questionList]
answer_left_center_ = [calc_center_of_left(box) for box in answerList]

df = pd.DataFrame(data)
print(df['question_right_center'])
print(df['answer_left_center'])

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def find_nearest_below_right_coords(list1, list2):
    list1_points = []
    matched_list2_points = []
    
    for p1 in list1:
        valid_points = [p2 for p2 in list2 if p2[0] > p1[0] and p2[1] >= p1[1]]
        
        list1_points.append(p1)
        
        if not valid_points:
            matched_list2_points.append(None)
        else:
            nearest = min(valid_points, key=lambda p2: euclidean_distance(p1, p2))
            matched_list2_points.append(nearest)
    
    return list1_points, matched_list2_points

op,op1=find_nearest_below_right_coords(question_right_center_, answer_left_center_)
print("Question Right Center:", op)
print("Answer Left Center:", op1)


'''def find_nearest_answer():
    nearest_question = []
    nearest_answer = []
    
    for i in range(len(question_right_center_)):
        arr1 = question_right_center_
        min_distance = float('inf')
        nearest_coord = None
        for j in range(len(answer_left_center_)):
            arr2 = answer_left_center_
            distance = ((arr1[i][0] - arr2[j][0]) ** 2 + (arr1[i][1] - arr2[j][1]) ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
                nearest_coord = arr2[j]
            nearest_answer.append(nearest_coord)
            nearest_question.append(arr1[i])
    return nearest_question, nearest_answer'''



def find_answers_for_centers(center_coords_a,center_coords_q, answer_boxes, answer_tokens,questions_boxes, questions_tokens):
    results_a = []
    results_q=[]
    for cx, cy in center_coords_a:
        matched = False
        for i, (x1, y1, x2, y2) in enumerate(answer_boxes):
            if x1 <= cx <= x2 and y1 <= cy <= y2:
                results_a.append(answer_tokens[i])
                matched = True
                break
        if not matched:
            results_a.append(None)
    for cx, cy in center_coords_q:
        matched = False
        for i, (x1, y1, x2, y2) in enumerate(questions_boxes):
            if x1 <= cx <= x2 and y1 <= cy <= y2:
                results_q.append(questions_tokens[i])
                matched = True
                break
        if not matched:
            results_q.append(None)
            
    return results_q, results_a      

"""questions,answers=find_answers_for_centers(op,op1,answerList,answerTokenList,questionList,questionTokenList)
for i in range(len(questions)):
    print(f"Question: {questions[i]}, Answer: {answers[i]}")"""

    




    