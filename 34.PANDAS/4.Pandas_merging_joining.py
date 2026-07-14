import pandas as pd
import numpy as np

# This file shows how to combine datasets using concat and merge.
# These operations are useful when data is spread across multiple tables.
courses = pd.read_csv("courses.csv")
students = pd.read_csv("students.csv")
nov = pd.read_csv("reg-month1.csv")
dec = pd.read_csv("reg-month2.csv")

matches = pd.read_csv("matches.csv")
delivery = pd.read_csv("deliveries.csv")

# Output: December registrations data.
print(dec)

# pd.concat
# df.concat
# ignore_index
# df.append
# mullitindex -> fetch using iloc
# concat dataframes horizontally

# Output: combine November and December registrations into one table.
regs = pd.concat([nov, dec], ignore_index=True)
print(regs)

# FIXED: Replaced nov.append(dec, ignore_index=True) with pd.concat
# Output: same result using append, which is older syntax.
print(pd.concat([nov, dec], ignore_index=True))

# Output: combined data with a MultiIndex showing the month.
multi = pd.concat([nov, dec], keys=["Nov", "Dec"])
print(multi.loc[("Dec", 4)])

# Output: concatenation along columns instead of rows.
print(pd.concat([nov, dec], axis=1))

# inner join
# Output: students who have matching registration records.
print(students.merge(regs, how="inner", on="student_id"))

# left join
# Output: all courses with matching registration data, if available.
print(courses.merge(regs, how="left", on="course_id"))

# right join
# Output: all rows from the right table and matching rows from the left table.
temp_df = pd.DataFrame(
    {
        "student_id": [26, 27, 28],
        "name": ["Hanzala", "Saad", "Haris"],
        "partner": [28, 26, 17],
    }
)

students = pd.concat([students, temp_df], ignore_index=True)

# Output: last few rows after adding new students.
print(students.tail())

print(students.merge(regs, how="right", on="student_id"))

print(regs.merge(students, how="left", on="student_id"))

# outer join
# Output: all rows from both tables, with missing values where needed.
print(students.merge(regs, how="outer", on="student_id").tail(10))

# 1. find total revenue generated
# Output: total revenue from all registrations.
total = regs.merge(courses, how="inner", on="course_id")["price"].sum()
print(total)

# 2. find month by month revenue
# Output: revenue grouped by month.
temp_df = pd.concat([nov, dec], keys=["Nov", "Dec"]).reset_index()
print(temp_df.merge(courses, on="course_id").groupby("level_0")["price"].sum())

# 3. Print the registration table
# cols -> name -> course -> price
# Output: a clean table with student name, course name, and price.
print(
    regs.merge(students, on="student_id").merge(courses, on="course_id")[
        ["name", "course_name", "price"]
    ]
)

# 4 find students who enrolled in both the months
# Output: student IDs that appear in both registration files.
common_student_id = np.intersect1d(nov["student_id"], dec["student_id"])
print(common_student_id)

print(students[students["student_id"].isin(common_student_id)])

# 5. find course that got no enrollment
# courses['course_id']
# regs['course_id']

# Output: courses that do not appear in the registration table.
course_id_list = np.setdiff1d(courses["course_id"], regs["course_id"])
print(courses[courses["course_id"].isin(course_id_list)])

# 6. find students who did not enroll into any courses
# Output: number of students without any enrollment.
student_id_list = np.setdiff1d(students["student_id"], regs["student_id"])
print(students[students["student_id"].isin(student_id_list)].shape[0])

# Output: percentage of students who did not enroll.
print((10 / 28) * 100)

# Output: current student data after the updates.
print(students)

# 7. Print student name -> partner name for all enrolled students
# self join
# Output: each student with the name of their partner.
print(
    students.merge(students, how="inner", left_on="partner", right_on="student_id")[
        ["name_x", "name_y"]
    ]
)

# 8. find top 3 students who did most number enrollments
# Output: top 3 students by number of enrollments.
print(
    regs.merge(students, on="student_id")
    .groupby(["student_id", "name"])["name"]
    .count()
    .sort_values(ascending=False)
    .head(3)
)

# 9. find top 3 students who spent most amount of money on courses
# Output: top 3 students by total amount spent.
print(
    regs.merge(students, on="student_id")
    .merge(courses, on="course_id")
    .groupby(["student_id", "name"])["price"]
    .sum()
    .sort_values(ascending=False)
    .head(3)
)

# Alternate syntax for merge
# students.merge(regs)

# Output: merge using the pandas merge function.
print(pd.merge(students, regs, how="inner", on="student_id"))

# IPL Problems

# find top 3 studiums with highest sixes/match ratio
# find orange cap holder of all the seasons

# Output: match data table.
print(matches)

# Output: deliveries data table.
print(delivery)

temp_df = delivery.merge(matches, left_on="match_id", right_on="id")

six_df = temp_df[temp_df["batsman_runs"] == 6]

# stadium -> sixes
# Output: number of sixes per stadium.
num_sixes = six_df.groupby("venue")["venue"].count()

num_matches = matches["venue"].value_counts()

# Output: sixes per match ratio for each stadium.
print((num_sixes / num_matches).sort_values(ascending=False).head(10))

# Output: current match data.
print(matches)

# Output: top run scorer for each season.
print(
    temp_df.groupby(["season", "batsman"])["batsman_runs"]
    .sum()
    .reset_index()
    .sort_values("batsman_runs", ascending=False)
    .drop_duplicates(subset=["season"], keep="first")
    .sort_values("season")
)

# Output: all season-wise batting totals.
print(
    temp_df.groupby(["season", "batsman"])["batsman_runs"]
    .sum()
    .reset_index()
    .sort_values("batsman_runs", ascending=False)
)