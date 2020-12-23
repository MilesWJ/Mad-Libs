name = str(input("Enter your name here: ")).lower()

noun1 = str(input("Enter a singular noun here: ")).lower()
noun2 = str(input("Enter a plural noun here: ")).lower()

verb1 = str(input("Enter a present tense verb here: ")).lower()
verb2 = str(input("Enter a present tense verb here: ")).lower()

part_of_the_body = str(input("Enter a plural part of the body here: ")).lower()

adjective1 = str(input("Enter an adjective here: ")).lower()

noun3 = str(input("Enter a plural noun here: ")).lower()

adjective2 = str(input("Enter an adjective here: ")).lower()


def mad_lib():
    print("Hello " + name + ",")
    print("Today, every student has a computer small enough to fit into his")
    print(noun1 + ". He can solve any math problem by simply pushing the computer's")
    print("little " + noun2 + ". Computers can add, subtract, multiply and " + verb1 + ".")
    print("They can also " + verb2 + " better than a human. Some computers are " + part_of_the_body + ".")
    print("Others have a/an " + adjective1 + " screen that shows all kinds of " + noun3 + " and " + adjective2 + " figures.")


mad_lib()
