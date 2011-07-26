def containsNeg(nums: List[Int]):Boolean = {
    var exists = false
    for (num <- nums)
        exists = num < 0
    exists
}

def containsNeg2(nums: List[Int]): Boolean = nums.exists(_ < 0)

val ints = List(1, 2, 3, -4)
println(containsNeg(ints))
println(containsNeg2(ints))
