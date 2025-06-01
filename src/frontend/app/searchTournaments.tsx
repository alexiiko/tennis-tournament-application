import { View, StyleSheet, TouchableOpacity, ScrollView, ActivityIndicator} from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { Button, Card, Divider, Text} from "react-native-paper";
import Ionicons from '@expo/vector-icons/Ionicons'
import { useState } from "react";
import { retrieveTournaments } from "../services/fetchDataDB.js"
import { retrieveDistanceAndTimeBetweenTournamentAndUser } from "../services/fetchDistanceTimeTournaments.js"

export default function main() {
  const [showFilters, setShowFilters] = useState(false)
  let [selectedAgeClasses, setSelectedAgeClasses] = useState(["M11"])
  let [tournaments, setTournaments] = useState<string[][]>([])
  let [loadingTournamentsInformation, setLoadingTournamentsInformation] = useState(false)
  let [loadedTournamentsAmount, setLoadedTournamentsAmount] = useState(0)
  let [currentlySearching, setCurrentlySearching] = useState(false)

  const addDurationsAndDistances = async (tournamentsData: any) => {
    let allTournaments = [...tournamentsData]
    
    for (let tournamentIndex = 0; tournamentIndex < tournamentsData.length; tournamentIndex++) {
      const distanceAndDuration = await retrieveDistanceAndTimeBetweenTournamentAndUser(
        "An der Geisel 10", 
        tournamentsData[tournamentIndex][5]
      );
      
      if (Array.isArray(distanceAndDuration)) {
        allTournaments[tournamentIndex] = [
          ...allTournaments[tournamentIndex],
          distanceAndDuration[0], 
          distanceAndDuration[1]  
        ];
      } else {
        allTournaments[tournamentIndex] = [
          ...allTournaments[tournamentIndex],
          "N/A", 
          "N/A"  
        ];
      }
      setLoadedTournamentsAmount(tournamentIndex)
    }

    setTournaments(allTournaments);
    return allTournaments;
  }

  const toggleAgeClass = (ageClass: string) => {
    setSelectedAgeClasses((prev) =>
      prev.includes(ageClass)
        ? prev.filter((item) => item !== ageClass)
        : [...prev, ageClass]
    )
  }

  const removeSelectedAgeClasses = () => {
    setSelectedAgeClasses([])
  }

  const renderTournaments = async () => {
    setTournaments([])
    let allTournaments = []
    
    for (let selectedAgeClassesIndex = 0; selectedAgeClassesIndex < selectedAgeClasses.length; selectedAgeClassesIndex++) {
        let retrievedTournaments = await retrieveTournaments(selectedAgeClasses[selectedAgeClassesIndex])
        
        for (let tournamentIndex = 0; tournamentIndex < retrievedTournaments.length; tournamentIndex++) {
          let tournamentData = [] 
          for (let propertyIndex = 1; propertyIndex < retrievedTournaments[tournamentIndex].length; propertyIndex++) {
            tournamentData.push(retrievedTournaments[tournamentIndex][propertyIndex].value)
          }
          allTournaments.push(tournamentData)
        }
    }
    
    setTournaments(allTournaments)
    return allTournaments;
  }

  const searchTournaments = async () => {
    setLoadingTournamentsInformation(true)
    setCurrentlySearching(true)
    
    const tournamentsData = await renderTournaments()
    
    if (tournamentsData.length > 0) {
      await addDurationsAndDistances(tournamentsData)
    } else {
      setTournaments([])
    }
    setLoadingTournamentsInformation(false)
    setCurrentlySearching(false)
  }

  const formatCurrentDate = (date: Date) => {
    const day = String(date.getDate()).padStart(2, '0')
    const month = String(date.getMonth() + 1).padStart(2, '0')
    const year = date.getFullYear()
    return `${day}.${month}.${year}`
  }

  const parseDateStringsToDateObjects = (date: string): Date => {
    const [day, month, year] = date.split('.')
    return new Date(Number(year), Number(month) - 1, Number(day))
  }

  const calculateDaysUntilTournamentSignUp = (tournamentDate: string) => {
    const currentDate = new Date()
    const currentParsed = parseDateStringsToDateObjects(formatCurrentDate(currentDate))
    const tournamentParsed = parseDateStringsToDateObjects(tournamentDate)

    const oneDay = 1000 * 60 * 60 * 24
    const deltaDays = tournamentParsed.getTime() - currentParsed.getTime()

    if (deltaDays <= 0) {
      return "Vorbei!"
    } else {
      return String(Math.round(deltaDays / oneDay)) + " Tage"
    }
  }

  return (
    <SafeAreaView>
      <View>
        <View className="searchBarBorder"
          style={{
            borderWidth: 1,
            borderColor: "grey",
            padding: 10,
            borderRadius: 7,
            marginLeft: 5,
            marginRight: 5,
            height: 65
          }}>
          <View className="searchBarIconsAndSelectedAgeClasses" style={{ flexDirection: "row"}}>
            <Button
              icon={() => <Ionicons name="options-outline" size={24} color="black" />}
              textColor="black"
              buttonColor="transparent"
              contentStyle={{
                marginLeft: 12
              }}
              onPress={() => setShowFilters((prev) => !prev)}
            />
            {selectedAgeClasses.slice(0,2).map((ageClass) => (
            <Button
              key={ageClass + "_selected"}
              mode="outlined"
              style={{ 
                borderColor: "black",
                borderWidth: 0.85,
                borderRadius: 12,
                backgroundColor: "white",
                marginLeft: 5,
              }}
              textColor="black"
              onLongPress={() => toggleAgeClass(ageClass)}>
              {ageClass}
            </Button>
            ))}
            {selectedAgeClasses.length > 2 && (
              <TouchableOpacity
                style={{
                  backgroundColor: "white",
                  borderWidth: 1,
                  borderColor: "black",
                  borderRadius: 12,
                  paddingVertical: 4,
                  paddingHorizontal: 6,
                  marginLeft: 5,
                  width: 50,
                  justifyContent: "center",
                  alignItems: "center"
                }}
                onPress={() => setShowFilters((prev) => !prev)}
              >
                <Text style={{ color: "black", fontSize: 24}}>...</Text>
              </TouchableOpacity>
            )}
            <Button
              icon={() => (<Ionicons name="search-outline" size={24}/>)}
              textColor="black"
              buttonColor="transparent"
              style={{ 
                position: "absolute",
                right: 0,
              }}
              contentStyle={{
                marginLeft: 12
              }}
              onPress={searchTournaments}
              disabled={currentlySearching}
            />
          </View>
        </View>

        { loadingTournamentsInformation ? (
          <View>
            <ActivityIndicator size={"large"} color={"black"} style={{ marginTop: 20}}></ActivityIndicator>
            <Text>{loadedTournamentsAmount}/{tournaments.length}</Text>
          </View>
        ) : (
        <ScrollView className="tournaments" horizontal={false} showsVerticalScrollIndicator={false} style={{ marginTop: 10, marginLeft: 5, marginRight: 5}}>
        {tournaments.map((tournamentInformation, keyIndex) => (
          <View key={keyIndex} className="tournamentWindow" style={{ borderWidth: 0.85, marginBottom: 10, flexDirection: "column", }}>
            <Text >{tournamentInformation[0]}</Text>
            <View className="tournamentWindowSignUpDaysOccuringDate" style={{ flexDirection: "row", marginBottom: 5 }}>
              <Text>{calculateDaysUntilTournamentSignUp(tournamentInformation[4].slice(0,10) || "")}</Text>
              <Text>{tournamentInformation[1].slice(0, 6) || ""}</Text>
            </View>
              {tournamentInformation[8] == "N/A" ? null : (
                <View className="tournamentWindowDistanceAndDuration" style={{ flexDirection: "row"}}>
                    <Text>{tournamentInformation[8]} km</Text>
                    <Text>{tournamentInformation[9]} min</Text>
                </View>
              )}
          </View>
        ))} 
        </ScrollView>
        )}

        {showFilters && (
          <Card style={styles.filterWindow}>
            <View className="ageClassButtons">
              <Card.Content>
                <View className="removeSelectedAgeClassesButton">
                  <Button 
                    icon="trash-can-outline"
                    mode="outlined"
                    style={{
                      borderColor: "black",
                      borderWidth: 0.85,
                      backgroundColor: "transparent",
                      marginTop: 15,
                    }}  
                    textColor="black"
                    contentStyle={{
                      flexDirection: "row",
                      marginRight: 8
                    }}
                    labelStyle={{
                      marginRight: 8,
                      fontSize: 16,
                      fontWeight: "100"
                    }}
                    onPress={removeSelectedAgeClasses}>
                    Filter löschen
                  </Button>
                </View>    
              <View className="ageClassButtonsLayout" style={{ flexDirection: "column"}}>
                <View className="maleJuniorsAgeClassesWrapper">
                  <View className="headerMaleJuniorsHeaderWrapper" style={{flexDirection: "row"}}>
                    <Button icon="face-man" contentStyle={{marginLeft: 12, marginTop: 3}} textColor="black"> </Button>
                    <Text style={{marginTop: 10, fontSize: 18}}>Junioren</Text>
                  </View>
                  <Divider />
                  <ScrollView horizontal={true} showsHorizontalScrollIndicator={false} >
                    <Button key={"M11"} onPress={() => toggleAgeClass("M11")}
                      style={[styles.firstAgeClassButton, selectedAgeClasses.includes("M11") && {backgroundColor: "lightgrey"}]}
                      textColor="black"
                    >M11</Button> 
                    {["M12", "M13", "M14", "M16"].map((ageClass) => (
                      <Button
                        key={ageClass}
                        onPress={() => toggleAgeClass(ageClass)}
                        style={[styles.ageClassButton, selectedAgeClasses.includes(ageClass) && {backgroundColor: "lightgrey"}]}
                        textColor="black"
                      >{ageClass}</Button>
                    ))}
                    <Button key={"M18"} onPress={() => toggleAgeClass("M18")}
                      style={[styles.lastAgeClassButton, selectedAgeClasses.includes("M18") && {backgroundColor: "lightgrey"}]}
                      textColor="black"
                    >M18</Button>
                  </ScrollView>
                </View>

                <View className="femaleJuniorsAgeClassesWrapper" style={{ marginBottom: 10 }}>
                  <View className="headerFemaleJuniorsHeaderWrapper" style={{flexDirection: "row"}}>
                    <Button icon="face-woman" contentStyle={{marginLeft: 12, marginTop: 3}} textColor="black"> </Button>
                  <Text style={{marginTop: 10, fontSize: 18}}>Juniorinnen</Text>
                  </View>
                  <Divider />
                  <ScrollView horizontal={true} showsHorizontalScrollIndicator={false} >
                    <Button key={"W11"} onPress={() => toggleAgeClass("W11")}
                      style={[styles.firstAgeClassButton, selectedAgeClasses.includes("W11") && {backgroundColor: "lightgrey"}]}
                      textColor="black"
                    >W11</Button> 
                    {["W12", "W13", "W14", "W16"].map((ageClass) => (
                      <Button
                        key={ageClass}
                        onPress={() => toggleAgeClass(ageClass)}
                        style={[styles.ageClassButton, selectedAgeClasses.includes(ageClass) && {backgroundColor: "lightgrey"}]}
                        textColor="black"
                      >{ageClass}</Button>
                    ))}
                    <Button key={"W18"} onPress={() => toggleAgeClass("W18")}
                      style={[styles.lastAgeClassButton, selectedAgeClasses.includes("W18") && {backgroundColor: "lightgrey"}]}
                      textColor="black"
                    >W18</Button>
                  </ScrollView>
                </View>
              </View>
            </Card.Content>
          </View>
        </Card>
      )}
      </View>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  filterWindow: {
    position: "absolute",
    top: 70,
    left: 10,
    right: 10,
    backgroundColor: "white",
    elevation: 4,
    borderRadius: 10,
  },
  ageClassButton: {
    borderColor: "black",
    borderWidth: 0.85,
    marginTop: 5,
    marginBottom: 3,
    marginRight: 5,
    borderRadius: 12,
  },
  firstAgeClassButton: {
    borderColor: "black",
    borderWidth: 0.85,
    marginTop: 5,
    marginBottom: 3,
    marginRight: 5,
    borderRadius: 12
  },
  lastAgeClassButton: {
    borderColor: "black",
    borderWidth: 0.85,
    marginTop: 5,
    marginBottom: 3,
    borderRadius: 12
  }
})
