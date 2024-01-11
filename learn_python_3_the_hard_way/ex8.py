formatter = "{one} {two} {three} {four}"

print(formatter.format(one=1, two=2, three=3, four=4))
print(formatter.format(four="one", three="two", two="three", one="four"))
print(formatter.format(one=True, two=False, three=False, four=True))
print(formatter.format(one=formatter, two=formatter, three=formatter, four=formatter))
print(
    formatter.format(
        one="Try your",
        two="Own text here",
        three="Maybe a poem",
        four="Or a song about fear",
    )
)
