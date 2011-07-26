def forLoop {
    println("for loop using java-style iteration")
        // strange syntax
	for (i <- 0 until args.length)
	    println(args(i))
}

forLoop
