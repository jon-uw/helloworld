trait Cat {
	def meow(): String
}

trait FuzzyCat extends Cat {
	override def meow = "Meeeow"
}

trait OtherThing {
	def hello() = 4
}

class Yep extends FuzzyCat with OtherThing

println((new Yep).hello())
println((new Yep).meow())
// object Test extends App {
// 	(new Yep).hello()
// 	(new Yep).meow()
// }