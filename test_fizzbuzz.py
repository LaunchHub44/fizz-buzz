import pytest
import fizzbuzz

def testGenFizzBuzz():
    assert fizzbuzz.genFizzBuzz(3) == "fizz"
    assert fizzbuzz.genFizzBuzz(5) == "buzz"
    assert fizzbuzz.genFizzBuzz(15) == "fizzbuzz"
    assert fizzbuzz.genFizzBuzz(2) == "2"

