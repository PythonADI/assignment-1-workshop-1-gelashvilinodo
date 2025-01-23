def main() -> None:
    # Write your solution here
    pass

#1
first_name = "nodo"
last_name = "gelashvili"
full_name = first_name + " " + last_name
print(full_name)
#type of data: String

#2
age = 23
print("your are", age, "years old")
#type of data: integers

#3
temperature = 20.3
print("the temperature is", temperature, "degrees")
#type of data: floats

#4
is_hot = temperature > 20.3
print(is_hot)
#type of data: boolean

#5
#int is a whole numbers, like 256, 0 and even -4758.
number = 34

#float is numbers with decimal: 3.879, 0.298, -67.99
fraction_number = 7.34

#string is a text data, it can also hold numbers, but this numbers won't be accepted as number by computer
word = "universe <3"

#boolean can have only two values: true and false
is_grown = age > 18
print(is_grown)


if __name__ == '__main__':
    main()
