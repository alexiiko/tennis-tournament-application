package main

import (
  "database/sql"
  "fmt"
  "os"

  _ "github.com/tursodatabase/libsql-client-go/libsql"
  _ "github.com/mattn/go-sqlite3"
)


func readFromLocalDatabase() {

}

func insertLocalDataIntoRemoteDB() {

}

func main() {
    fmt.Println("test") 
    /*
    dbToken := "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NDExMTY4NjUsImlkIjoiMDc1ZDQ5MTEtZDUzNS00Nzc5LWE0OTktMzZlYmE3YTEwNWQ2In0._5BR58POJ0aZYqciDxWVImP2IglQ1SjLXL7JJAobI6LZ27YesKCZAmXBksuiy3lk7BSRTg1ONFkwAMddwEisCA"

    dbName := "turso-tournaments"

    url := fmt.Sprintf("libsql://[%s].turso.io?authToken=[%s]", dbName, dbToken)

    libDB, err := sql.Open("libsql", url)
    if err != nil {
        fmt.Fprintf(os.Stderr, "failed to open db %s: %s", url, err)
        os.Exit(1)
    }
    readFromLocalDatabase()
    insertLocalDataIntoRemoteDB()
    defer libDB.Close()
    */
}
