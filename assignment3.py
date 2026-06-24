import numpy as np
#Problem Statement 1: Marks of 5 students are stored in a NumPy array

marks = np.array([45,78,62, 90, 55])
avg_marks = np.mean(marks)
print("Average marks:", avg_marks)
highest_marks = np.max(marks)
print("Highest marks:", highest_marks)
above_avg_students = np.sum(marks > avg_marks)
print("Number of students above average marks:", above_avg_students)

#Problem Statement 2: Temperature of a city for 5 days (in Celsius) is stored in a NumPy array

temp = np.array([25, 28, 30, 27, 29])

temp_in_fahrenheit = (temp * 9/5) + 32
print("Temperature in Fahrenheit:", temp_in_fahrenheit)

highest_temp = np.max(temp)
print("Hottest Day:", highest_temp)
lowest_temp = np.min(temp)
print("Coldest day:", lowest_temp)

temp_above_34 = np.sum(temp > 34)
print("Number of days with temperature above 34°C:", temp_above_34)

#Problem Statement 3: Daily sales of 3 shops for 5 days are stored in a 2D NumPy array:
sales = np.array([[[200, 250, 300, 280, 260],
                    [180, 220, 270, 260, 240],
                    [210, 260, 310, 290, 270]]])
total_sales = np.sum(sales)
print("Total sales of all shops for 5 days:", total_sales)
shop_with_highest_sales = np.argmax(np.sum(sales, axis=2))
print("Shop with highest sales:", shop_with_highest_sales + 1)
average_sales_per_day = np.mean(sales, axis=2)
print("Average sales per day for each shop:", average_sales_per_day)

#Problem Statement 4: Prices of 5 products are stored in a NumPy array:

prices = np.array([150, 450, 600, 800, 300])

add_10_percent = prices * 1.10
print("Prices after adding 10%:", add_10_percent)

discount_20 = prices * 0.80
print("Prices after 20% discount:", discount_20)

Final_prices = add_10_percent - discount_20  
print("Final prices after adding 10% and applying 20% discount:", Final_prices)

#Problem Statement 5: Attendance of 5 students for 5 days is stored in a NumPy array (1 = Present, 0 = Absent):

attendance = np.array([[1, 1, 1, 0, 1],
                        [1, 0, 1, 1, 1],
                        [0, 1, 1, 0, 1],
                        [1, 1, 1, 1, 1],
                        [1, 0, 0, 1, 1]])

total_attendence_of_each_student = np.sum(attendance, axis=1)
print("Total attendance of each student:", total_attendence_of_each_student)

student_with_attendance_below_4_days = np.sum(total_attendence_of_each_student < 4)
print("Number of students with attendance below 4 days:", student_with_attendance_below_4_days)

most_present_student = np.argmax(total_attendence_of_each_student)
print("Student with most attendance:", most_present_student + 1)