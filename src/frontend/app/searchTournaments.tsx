import { View, StyleSheet, TouchableOpacity, ScrollView} from "react-native";
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

  const toggleAgeClass = (ageClass: string) => {
    setSelectedAgeClasses((prev) =>
      prev.includes(ageClass)
        ? prev.filter((item) => item !== ageClass)
        : [...prev, ageClass]
    )
  }

  const removeSelectedAgeClasses = () => {
    setSelectedAgeClasses([])
    console.log("removed age classes")
  }

  const renderTournaments = async () => {
    setTournaments([])
    let allTournaments = []
    for (let selectedAgeClassesIndex = 0; selectedAgeClassesIndex < selectedAgeClasses.length; selectedAgeClassesIndex++) {
      let retrievedTournaments = await retrieveTournaments(selectedAgeClasses[selectedAgeClassesIndex])
      let tournamentData = [] 
      for (let tournamentIndex = 0; tournamentIndex < retrievedTournaments.length; tournamentIndex++) {
        for (let propertyIndex = 1; propertyIndex < retrievedTournaments[tournamentIndex].length; propertyIndex++) { // we start with the propertyIndex 1 as we do not want to store the ID of each tournament
        // because the IDs create problems when checking if there are duplicate tournaments 
          tournamentData.push(retrievedTournaments[tournamentIndex][propertyIndex].value)
        }

        allTournaments.push(tournamentData)
        tournamentData = [] 
      }
    }
    setTournaments(allTournaments)
    //removeDuplicateTournaments()
  }

  const removeDuplicateTournaments = () => {
    // todo: fix this (currently only returning an empty array )
    const uniqueTournaments = [];
    const seenEntryStrings = new Set<string>();

    for (const entry of tournaments) {
      const entryString = JSON.stringify(entry); 
      if (!seenEntryStrings.has(entryString)) {
        seenEntryStrings.add(entryString);
        uniqueTournaments.push(entry); 
      }
    }

    setTournaments(uniqueTournaments)
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
              onPress={renderTournaments}
            />
          </View>
        </View>

        <ScrollView className="tournaments" horizontal={false} showsVerticalScrollIndicator={false} style={{ marginTop: 10, marginLeft: 5, marginRight: 5}}>
        {tournaments.map((tournamentInformation, keyIndex) => (
          <View className="tournamentWindow" style={{ borderWidth: 0.85, marginBottom: 5, flexDirection: "column" }}>
            <Text key={keyIndex}>{tournamentInformation[0]}</Text>
            <View className="tournamentWindowSecondInformationRow" style={{ flexDirection: "row" }}>
              <Text key={keyIndex}>{tournamentInformation[1].slice(0, 6)}</Text>
              <Text key={keyIndex + 1}>{tournamentInformation[2]}</Text>
            </View>
          </View>
        ))} 
        </ScrollView>

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
                      alignSelf: "flex-start",
                    }}  
                    textColor="black"
                    contentStyle={{
                      flexDirection: "row",
                      justifyContent: "flex-start",
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

// todos:
// - make trash can icon bigger in filter screen
// - make the text to delete the selected age classes not bold 
// - add cache for selected age classes
