package main

import (
  "database/sql"
  "fmt"
  "os"

  _ "github.com/tursodatabase/libsql-client-go/libsql"
  _ "github.com/mattn/go-sqlite3"
)


func readTournamentsFromLocalDatabase() map[string][]map[string]any {
    localDB, err := sql.Open("sqlite3", "tournaments.db")
    if err != nil {
        fmt.Println("Error connecting to the local database:", err)
    }
    defer localDB.Close()

    ageClasses := map[string][]map[string]any{
        "M18": {},
        "M16": {},
        "M14": {},
        "M13": {},
        "M12": {},
        "M11": {},
        "W18": {},
        "W16": {},
        "W14": {},
        "W13": {},
        "W12": {},
        "W11": {},
    }

    for ageClass := range ageClasses {
        rows, err := localDB.Query(fmt.Sprintf("SELECT * FROM %s", ageClass))
        if err != nil {
            fmt.Printf("Error retrieving data from the age class: %s with the error: %v\n", ageClass, err)
            continue
        }
        defer rows.Close()

        var tournaments []map[string]any
        columns, err := rows.Columns()
        if err != nil {
            fmt.Println("Error getting columns:", err)
            continue
        }

        for rows.Next() {
            values := make([]any, len(columns))
            valuePtrs := make([]any, len(columns))
            for i := range columns {
                valuePtrs[i] = &values[i]
            }

            if err := rows.Scan(valuePtrs...); err != nil {
                fmt.Println("Error scanning row:", err)
                continue
            }

            entry := make(map[string]any)
            for i, col := range columns {
                entry[col] = values[i]
            }
            tournaments = append(tournaments, entry)
        }

        if err := rows.Err(); err != nil {
            fmt.Println("Error during rows iteration:", err)
            continue
        }

        ageClasses[ageClass] = tournaments
    }
    
    return ageClasses 
}

func insertLocalDataIntoRemoteDB() {
    tournamentData := readTournamentsFromLocalDatabase()
    fmt.Println(tournamentData)

    dbToken := "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NDExMTY4NjUsImlkIjoiMDc1ZDQ5MTEtZDUzNS00Nzc5LWE0OTktMzZlYmE3YTEwNWQ2In0._5BR58POJ0aZYqciDxWVImP2IglQ1SjLXL7JJAobI6LZ27YesKCZAmXBksuiy3lk7BSRTg1ONFkwAMddwEisCA"

    dbName := "turso-tournaments"
    url := fmt.Sprintf("libsql://[%s].turso.io?authToken=[%s]", dbName, dbToken)

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
