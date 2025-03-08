package main

import (
	"database/sql"
	"fmt"
	"os"

	"libsqlDB/dbCredentials"

	_ "github.com/mattn/go-sqlite3"
	_ "github.com/tursodatabase/libsql-client-go/libsql"
)


func readTournamentsFromJSONFiles() string {
    return ""
}

func insertLocalDataIntoRemoteDB() {
    url := fmt.Sprintf("libsql://[%s].turso.io?authToken=[%s]", dbCredentials.DbName, dbCredentials.DbToken)

    libDB, err := sql.Open("libsql", url)
    if err != nil {
        fmt.Fprintf(os.Stderr, "failed to open db %s: %s", url, err)
        os.Exit(1)
    }
    defer libDB.Close()
    fmt.Println("closed remote db")
}

func main() {
    insertLocalDataIntoRemoteDB()
}
