object VarArgs {
    def main(args: String*) = args.foreach(println _)
    
    def main(args: Array[String]) = args.foreach(x => println("arg: " + x))
}