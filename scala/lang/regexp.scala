val reg = """^(F|f)\w*""".r  // .r change a string to a regular expression
println(reg.findFirstIn("Fantastic"))
println(reg.findFirstIn("not Fantastic"))

val reg2 = "the".r
reg2.findAllIn("the way the scissors trim the haire and the shrubs").foreach(println(_))