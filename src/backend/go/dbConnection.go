package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"os"
	"strings"
	"time"

	"libsqlDB/dbCredentials"

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


func main() {
    url := fmt.Sprintf("libsql://%s.turso.io?authToken=%s", dbCredentials.DbName, dbCredentials.DbToken)

    libDB, err := sql.Open("libsql", url)
    if err != nil {
        fmt.Fprintf(os.Stderr, "failed to open db %s: %s", url, err)
        os.Exit(1)
    }

    // read local tournament data from json files
    ageClasses := [12]string{"M11", "M12", "M13", "M14", "M16", "M18", "W11", "W12", "W13", "W14", "W16", "W18"}
    
    for _, ageClass := range ageClasses {
        linkRows, err := libDB.Query(fmt.Sprintf("SELECT link FROM %s", ageClass))
        if err != nil {
            fmt.Println("Error selecting the links from the M11 table: ", err)
            os.Exit(1)
        }

        var tournamentlinks []string

        for linkRows.Next() {
            var link string
            err := linkRows.Scan(&link)
            if err != nil {
                fmt.Println("Error scanning the rows: ", err)
            }

            tournamentlinks = append(tournamentlinks, link)
        }

        jsonFile, err := os.Open(fmt.Sprintf("/tournament_data/%s.json", ageClass))
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
            var tournamentAlreadyInDB bool = false
            for _, tournamentLink := range tournamentlinks {
                tournamentAlreadyInDB = false
                if tournament.Link == tournamentLink {
                    tournamentAlreadyInDB = true
                    break
                }
            }

            if tournamentAlreadyInDB == false {
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
        
        idsRows, err := libDB.Query(fmt.Sprintf("SELECT id FROM %s", ageClass))
        if err != nil {
            fmt.Println("Error selecting the id and event_date from db rows: ", err)    
            os.Exit(1)
        }

        var ids[]string
        for idsRows.Next() {
            var id string
            err := idsRows.Scan(&id)
            if err != nil {
                fmt.Println("Error scanning the id and event_date: ", err)
                os.Exit(1)
            }

            ids = append(ids, id)
        }

        eventDateRows, err := libDB.Query(fmt.Sprintf("SELECT event_date FROM %s", ageClass))
        if err != nil {
            fmt.Println("Error selecting the event_date from db rows: ", err)    
            os.Exit(1)
        }

        var eventDates[] string
        for eventDateRows.Next() {
            var eventDate string
            err := eventDateRows.Scan(&eventDate)
            if err != nil {
                fmt.Println("Error scanning the event_date from db rows: ", err)
                os.Exit(1)
            }

            eventDates = append(eventDates, eventDate)
        }

        var tournamentsToBeDeleted[] string

        eventDatesIndex := 0
        for eventDatesIndex < len(eventDates) {
            currentId := ids[eventDatesIndex]
            currentEventDate, err := time.Parse("02-01-2006", strings.Replace(eventDates[eventDatesIndex][13:], ".", "-", -1))
            if err != nil {
                fmt.Println("Error parsing the currentEventDate: ", err)
                os.Exit(1)
            }
            currentDate, err := time.Parse("02-01-2006", time.Now().Format("02-01-2006"))
            if err != nil {
                fmt.Println("Error parsing the current date: ", err)
                os.Exit(1)
            }

            dateComparison := currentEventDate.Compare(currentDate)

            if dateComparison == -1 {
                tournamentsToBeDeleted = append(tournamentsToBeDeleted, currentId)
            }
            eventDatesIndex++
        }

        
        tournamentsToBeDeletedIndex := 0 
        for tournamentsToBeDeletedIndex < len(tournamentsToBeDeleted) {
            _, err := libDB.Exec(fmt.Sprintf("DELETE FROM %s WHERE id = %s", ageClass, tournamentsToBeDeleted[tournamentsToBeDeletedIndex]))
            if err != nil {
                fmt.Println(fmt.Sprintf("Error deleting the tournament id %s from the %s table: ", tournamentsToBeDeleted[tournamentsToBeDeletedIndex], ageClass), err)
                os.Exit(1)
            }
            tournamentsToBeDeletedIndex++
        }
    }

    defer libDB.Close()
}
