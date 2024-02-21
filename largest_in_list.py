def largest_number(numbers):
    largest=numbers[0];

    for x in numbers:
        if x>largest:
            largest=x;
            #continue;
    return largest;




a=[3,2,25,6,243]
b=largest_number(a);
print (b);