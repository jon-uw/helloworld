class Person(age: Int) {
    val name = "aPerson";
	
	override def toString = {
	    Person.nonsense
	    name + "[" + Person.clazz + "]" + age
		
	}
}

object Person {
    val clazz = "Person"
	
	def nonsense = println("waa, begin talking now.. omg!")
}

object PersonTest extends App {
    val p = new Person(20)
	println(p)
}