val movies = <movies>
    <movie>The Incredibles</movie>
    <movie>WALL E</movie>
    <short>Jack jack Attack</short>
    <short>Geri's Game</short>
</movies>

(movies \ "_").foreach{movie =>
    movie match {
    	case <movie>{movieName}</movie> => println("movie: " + movieName)
    	case <short>{shortName}</short> => println("short: " + shortName)
    }
}