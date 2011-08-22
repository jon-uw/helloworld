def nano() = {
	println("Getting nano")
	System.nanoTime
}

def delayed(t: => Long) = {
	println("In Delayed method")
	println("Param: " + t)
	t 
}

delayed(nano())

