# Assignment 02 – Structured Programming & Data Modeling

## Data Structure Justification

---

## 1. Why Sets Are Used for Enrollment

Sets are used in the course enrollment system because enrollment must not contain duplicate students within the same course. A set automatically ensures uniqueness, which maintains data integrity without requiring additional duplicate-checking logic.

Sets also provide efficient membership testing (average O(1) time complexity). This makes operations such as checking whether a student is enrolled in a course very fast. Additionally, sets support operations like union and intersection, which are useful when identifying students enrolled in multiple courses or finding all unique students across courses.

For these reasons, sets are an appropriate choice for modeling enrollment relationships.

---

## 2. Why Tuples Are Used for Fixed Scores

Tuples are used to store student scores because the number of subjects is fixed (three subjects). Since tuples are immutable, they prevent accidental modification of scores after initialization. This ensures that academic records remain consistent and protected.

Using tuples also clearly indicates that the data is structured and fixed in size, unlike lists which are dynamic. This improves clarity in system design and expresses the intention that subject scores should not change arbitrarily.

Therefore, tuples are suitable for representing fixed and ordered data.

---

## 3. Why Dictionaries Are Suitable for Structured Mapping

Dictionaries are used to represent students and courses because they provide a clear key-value structure. Each student contains labeled attributes such as id, name, and scores. Similarly, each course contains structured information such as instructor and enrolled students.

Dictionaries allow fast key-based access (average O(1) time complexity), making retrieval of specific attributes efficient. They are also flexible and scalable, meaning new attributes can be added easily without changing the overall system structure.

Thus, dictionaries effectively model real-world structured data.

---

## 4. Why Classes Improve System Organization

Classes improve system organization by encapsulating both data and related operations within a single structure. Instead of spreading logic across multiple independent functions, classes group related behaviors together, making the system modular and easier to maintain.

Using classes:

- Improves code readability  
- Promotes modular programming  
- Supports reusability  
- Reduces repetition  
- Follows object-oriented principles  

Classes also make the system more scalable and closer to real-world analytics applications, where data and behavior are combined into organized units.

Therefore, classes enhance clarity, maintainability, and system design quality.