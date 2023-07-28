def students_credits(*students):
    NEED_CREDITS = 240
    all_courses = {}
    total_credits = 0
    for data in students:
        course_name, credit, max_test_point, diyans_points = data.split("-")
        curse_credit = int(credit) * (int(diyans_points) / int(max_test_point))
        all_courses[course_name] = curse_credit
        total_credits += curse_credit

    result = []

    if total_credits >= NEED_CREDITS:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {NEED_CREDITS - total_credits:.1f} credits more for a diploma.")

    sorted_courses = dict(sorted(all_courses.items(), key=lambda x: (-x[1], x[0])))

    for course, credits in sorted_courses.items():
        result.append(f"{course} - {credits:.1f}")

    return '\n'.join(result)


print(students_credits(
    "Computer Science-12-300-250",
    "Basic Algebra-15-400-200",
    "Algorithms-25-500-490"
))
