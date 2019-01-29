grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print grade

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total
    
def grades_average(scores):
  sum_of_grades = grades_sum(scores)
  average = sum_of_grades / float(len(scores))
  return average

def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    variance += ((average - score) ** 2)
  return variance / float(len(scores))

def grades_std_deviation(variance):
  return variance ** 0.5

print "Score of class Exam: "
print "Total Input %d" % float(len(grades))
print grades
print "---------------------"

for grade in grades:
 print "Score for each student: %.2f" %grade
print "Sum of class Exam     		: %.2f" %grades_sum(grades)
print "Average of class Exam 		: %.2f" %grades_average(grades)
variance = grades_variance(grades)
print "Variance of class Exam		: %.2f" %variance
print "Standar Deviation of class Exam	: %.2f" %grades_std_deviation(variance)
