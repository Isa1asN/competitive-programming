class Solution(object):
    def __init__(self):
        self.numbers = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }
        self.suffixes = [" Billion", " Million", " Thousand", ""]
    def tripletsToWords(self, x):
        """
        :type num: int
        :rtype: str
        """
        result = []
        if x == 0:
            return ""
        hundreds = x / 100
        tens = (x % 100) / 10
        ones = x % 10
        
        if hundreds > 0:
            result.append(self.numbers[hundreds]+" Hundred")
        # Handle case for 11 - 19
        if tens == 1:
            result.append(self.numbers[x%100])
            return " ".join(result)
        if tens > 1:
            result.append(self.numbers[tens*10])
        if ones > 0:
            result.append(self.numbers[ones])
        return " ".join(result)
        
        
        
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        result = []
        denominator = 1000000000
        for i in range(4):
            quotient = num / denominator
            num = num % denominator
            if quotient > 0:
                result.append(self.tripletsToWords(quotient) + self.suffixes[i])
            denominator = denominator / 1000
        return " ".join(result)
