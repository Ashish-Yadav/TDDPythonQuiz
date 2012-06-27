"""
Q1. Why is the report method untestable ? [2 pts]
Ans:- The report method has external depndencies.
  It depends on the "open function" and the Txt file.



Q2. How will you change the api of the report method to make it more testable ? [2 pts]
Ans:- The API of the report method can be changed by the the number of arguments it accepts as
    "report(self,numbers,filehandler)"
where "filehandler" will be used for creating an impression of reading values from file.

"""
class FizzBuzz(object):
    def report(self, numbers,opener):

        report_file = opener('c:/temp/fizzbuzz_report.txt', 'w')

        for number in numbers:
            msg = str(number) + " "
            fizzbuzz_found = False
            if number % 3 == 0:
                msg += "fizz "
                fizzbuzz_found = True
            if number % 5 == 0:
                msg += "buzz "
                fizzbuzz_found = True

            if fizzbuzz_found:
                report_file.write(msg + "\n")

        report_file.close()

if "__main__" == __name__:
    fb = FizzBuzz()
    fb.report(range(100))

            
