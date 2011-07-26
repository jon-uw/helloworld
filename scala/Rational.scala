//Rational 
class Rational(n: Int, d: Int) {
    require(d != 0)
	
	// greatest common divisor
	private val g = gcd(n.abs, d.abs)
	val number = n / g
	val denom = d / g
	
	// auxiliary constructor
	def this(n: Int) = {
	    // Can't do this: 
		// println("can we dosomething before auxiliary constructor?")
		this(n, 1)
	}               
	
    override def toString = if (denom == 1) number.toString else (number + "/" + denom)
	
	def add(another: Rational): Rational = 
	    new Rational(number * another.denom + another.number * denom,
		    denom * another.denom)
	
	// + = * /
	def +(another: Rational) = add(another)
	def +(another: Int) = new Rational(number + another * denom, denom)
	
	def *(another: Rational) = new Rational(number * another.number,
	    denom * another.denom)
	
	def lessThan(anther: Rational) = this.number * anther.denom < anther.number * this.denom
	
	private def gcd(a: Int, b: Int): Int = 
	    if (b == 0) a else gcd(b, a %b)
}
