def test(str: String, tester: String => Boolean): Boolean = {
    if (tester(str)) {
        println("that's it: " + str)
	true
    } else false
}

def smatch(s: String, s2: String): Boolean = (s == s2)

test("abc", _ == "abc")
test("ccav", smatch(_, "ccav"))

