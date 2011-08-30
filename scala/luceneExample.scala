/**
  * Example Scala App with Lucene
  * By Marcus Kazmierczak
  * http://solog.co/ 
  */
import org.apache.lucene.index._
import org.apache.lucene.store._
import org.apache.lucene.util.Version
import org.apache.lucene.analysis.standard.StandardAnalyzer
import org.apache.lucene.search._
import org.apache.lucene.document._

object Indexer {
  
  val analyzer = new StandardAnalyzer(Version.LUCENE_CURRENT) 
  val filedir = new java.io.File("tmp/lucene")
  val directory = new NIOFSDirectory(filedir)
  
  def main(args: Array[String]) {
    if (args.length < 1) {
      println("Usage: run [index|query q|terms]")
    }
	  args(0) match {
	    case "index" => createIndex
	    case "query" => query(args(1))
	    case "terms" => terms
	    case _ =>
	      println("Usage: run [index|query q|terms]")
	  }
  }

  /** Get Popular Terms */
  private def terms {
    val allTerms = collection.mutable.HashMap[String, Int]()
    
    println("Popular Terms " )
    val reader = IndexReader.open(directory, true)

    // create map of popular terms
    val terms = reader.terms
    while (terms.next) {
      allTerms += terms.term.toString -> terms.docFreq()
    }  

    // sort map 
    allTerms.toList sortBy { _._2 } foreach {
      case (key, value) =>
        println(key + ": " + value)
    }
    reader.close
  }
  
  
  /** Perform Search Query */
  private def query(q: String) {
    println("-------------------------------------------------------------------------------")
    println("Query: " + q)
    println("-------------------------------------------------------------------------------")
    val searcher = new IndexSearcher(directory, true)
    val query = new TermQuery(new Term("tweet", q)) 
    
    // perform search, return top 10
    val docs = searcher.search(query, 10)
    docs.scoreDocs foreach { docId =>
      val d = searcher.doc(docId.doc)
      println(d.get("tweet"))
      println
    }
    
    searcher.close
  }
  
  
  /** Creates Index */
  private def createIndex {
    var count = 0
    
    if (!filedir.exists) { filedir.mkdir }
		val writer = new IndexWriter(directory, analyzer, IndexWriter.MaxFieldLength.UNLIMITED)

    // read in file
    val fileLines = io.Source.fromFile("data/tweets.txt", "UTF-8").getLines.toList

    // iterate over lines adding to index
    fileLines foreach { line => 
      count += 1
      writer.addDocument(simpleDoc(line))
    }
        
    // write to index
  	writer.commit
  	writer.close
  	
	println("Items Indexed: " + count)
  
  }
  
  /*** Simple Lucene Document
	 * One field for tweet
	 * Store Term Vector can be used to retrieve terms of tweet
	 */
  private def simpleDoc(text: String) = {
    val doc = new Document()
    doc.add(new Field("tweet", text, Field.Store.YES, Field.Index.ANALYZED, Field.TermVector.YES)) 
    doc
  } 

}