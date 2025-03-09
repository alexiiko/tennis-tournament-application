package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"os"

	"libsqlDB/dbCredentials"

	// _ "github.com/mattn/go-sqlite3"
	_ "github.com/tursodatabase/libsql-client-go/libsql"
)


type Tournament struct {
    Title string `json:"tournament_title"`
    Link string `json:"tournament_link"`
    EventDate string `json:"tournament_date"`
    RegisStart string `json:"tournament_registration_end"`
    RegisEnd string `json:"tournament_registration_start"`
    Draw string `json:"tournament_draw_date"`
    PLZ string `json:"tournament_plz"`
    Street string `json:"tournament_street"`
}



func insertLocalDataIntoRemoteDB() {
    url := fmt.Sprintf("libsql://%s.turso.io?authToken=%s", dbCredentials.DbName, dbCredentials.DbToken)

    libDB, err := sql.Open("libsql", url)
    if err != nil {
        fmt.Fprintf(os.Stderr, "failed to open db %s: %s", url, err)
        os.Exit(1)
    }

    // read local tournament data from json files
    ageClasses := [12]string{"M11", "M12", "M13", "M14", "M16", "M18", "W11", "W12", "W13", "W14", "W16", "W18"}
    
    for _, ageClass := range ageClasses {
        jsonFile, err := os.Open(fmt.Sprintf("../tournament_data/%s.json", ageClass))
        if err != nil {
            fmt.Println(fmt.Sprintf("Error opening the %s json file: ", ageClass), err)
            os.Exit(1)
        }

        defer jsonFile.Close()

        var tournaments []Tournament
        decoder := json.NewDecoder(jsonFile)
        err = decoder.Decode(&tournaments)
        if err != nil {
            fmt.Println(fmt.Sprintf("Error decoding the %s json file: ", ageClass), err)
            os.Exit(1)
        }
        
        for _, tournament := range tournaments {
            _, err = libDB.Exec(fmt.Sprintf(`
                INSERT INTO %s (title, event_date, regis_start_date, regis_end_date, draw_date, street, plz, link)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            `, ageClass), tournament.Title, tournament.EventDate, tournament.RegisStart, tournament.RegisEnd, tournament.Draw, tournament.Street, tournament.PLZ, tournament.Link)
            if err != nil {
                fmt.Println("There was an error inserting the data into the remote DB:", err)
                os.Exit(1)
            }
            fmt.Println(fmt.Sprintf("Inserted data from json file: %s into table %s from remote db", ageClass, ageClass))
            fmt.Println()
        }

    }
    defer libDB.Close()
}


func main() {
    insertLocalDataIntoRemoteDB()
}
