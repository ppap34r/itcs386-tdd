### How many tests did you write in Part A, and how many lines of production code? What is the ratio?
- Tests in Part A: 9 tests
- Production code: 56 lines in kitchen.py
- Ratio: (9/56 ~ 0.16) about 1 test per 6 lines of code

### When was your bar red for the longest time, and what made it last so long?
- Step A7 was the most challenging for me because I had difficulty understanding how Quantity, Sum, and Converter worked together to convert units correctly.

### Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right?
- Fake It: In A1, I used a fixed result of 600 to make the test pass first. 
- Triangulation: In A7, I tested adding grams and ounces together. 
- Obvious Implementation: In A4, for equality.

I think these choices were useful because they helped me develop and understand the code step by step.

### Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?
- The optional A8 test for multiplying a Sum was initially unfinished, but I implemented it. I also removed the redundant multiplication-by-two test from A2. I would keep the other planned behaviors because they are useful for testing the system.

### Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?
- Maybe not, because I thought unit conversion should only be handled by Converter. TDD helped me understand that Quantity and Sum also needed reduce() methods.

### In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design?
- Part 0 felt easier because the code already existed, while Part A was harder because I had to think about the expected behavior before writing the code. I think the multiplication and mixed-unit tests helped shape my design the most.