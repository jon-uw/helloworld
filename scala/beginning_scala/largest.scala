//show the usage of variable length argument
def largest(as: Int*): Int = as.reduceLeft((a,b) => a max b)

println(largest(1, 2, 3))
println(largest(22, 2, 56, 18))
