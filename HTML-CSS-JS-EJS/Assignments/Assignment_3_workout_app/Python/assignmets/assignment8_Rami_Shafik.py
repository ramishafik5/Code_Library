#Rami Shafik 100971729

######################################## set.py #########################################

import string

def getStringInfo (*args):
    def analyze_string (s):
        num_words = len (s.split())
        chart_white = len (s)
        chart_without_white = len (s.replace (" ", ""))
        letters = sum (c.isalpha() for c in s)
        digits = sum (c.isdigit() for c in s)
        punctuations = sum (c in string.punctuation for c in s)
        is_number = s.isdigit()
        uppercase = sum (c.isupper() for c in s)
        lowercase = sum (c.islower() for c in s)
            
        return {
            "num_words": num_words,
            "chart_white": chart_white,
            "chart_without_white": chart_without_white,
            "letters": letters,
            "digits": digits,
            "punctuations": punctuations,
            "is_number": is_number,
            "uppercase": uppercase,
            "lowercase": lowercase,
            "uppercase_string": s.upper(),
            "lowercase_string": s.lower(),
            "reversed": s.swapcase(),
            "no_space": s.replace(" ", ""),
            "capitalized": s.title(),
            "reversed_string": s[::-1]
        }
    
    for s in args:
        info = analyze_string(s)
        
        print ()
        print (f"String: {s}")
        print (f"# Of Words                  - {info["num_words"]}")
        print (f"# Of characters             - {info["chart_white"]}")
        print (f"# Of characters (excl. w/s) - {info["chart_without_white"]}")
        print (f"# Of letters                - {info["letters"]}")
        print (f"# Of numbers                - {info["digits"]}")
        print (f"# Of punctuations           - {info["punctuations"]}")
        print (f"Is number                   - {info['is_number']}") 
        print (f"# Of uppercase characters   - {info["uppercase"]}")
        print (f"# Of lowercase characters   - {info["lowercase"]}")
        print (f"Uppercase                   - {info["uppercase_string"]}")
        print (f"Lowercase                   - {info["lowercase_string"]}")
        print (f"Reversed Case               - {info["reversed"]}")
        print (f"No Space                    - {info["no_space"]}")
        print (f"Title                       - {info["capitalized"]}")
        print (f"Reversed                    - {info["reversed_string"]}")
        print ()
        print ("#" * 70 )

getStringInfo("HeLlO wOrLd!!11", "Did you hear about the one-eyed one-horned Flying Purple People Eater?")