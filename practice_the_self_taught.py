import re

zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""

string = "Two too."

line = '123 hi 34 hello.'

t = '__one__ __two__ __three__'

challengeText = 'The ghost that says boo haunts the loo'

found = re.findall('.oo', challengeText)
for match in found:
    print(match)
