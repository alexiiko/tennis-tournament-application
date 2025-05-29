import { retrieveDBData } from "../services/fetchDataDB.js";
import { View, StyleSheet } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { Button, Card, Icon} from "react-native-paper";
import Ionicons from '@expo/vector-icons/Ionicons'
import { useState } from "react";

export default function main() {
  const [showFilters, setShowFilters] = useState(false);
  const [selectedAgeClasses, setSelectedAgeClasses] = useState([]);

  const toggleAgeClass = (ageClass: string) => {
    setSelectedAgeClasses((prev) =>
      prev.includes(ageClass)
        ? prev.filter((item) => item !== ageClass)
        : [...prev, ageClass]
    );
  };

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
          <View className="searchBarIconsAndSelectedAgeClasses">
            <Button
              icon={() => <Ionicons name="options-outline" size={24} color="black" />}              textColor="black"
              buttonColor="transparent"
              style={{ position: "absolute", left: 0 }}
              onPress={() => setShowFilters((prev) => !prev)}
            />
            <View className="showSelectedAgeClasses" style={{ flexDirection: "row", flexWrap: "wrap"}}>
              {selectedAgeClasses.map((ageClass) => (
              <Button
                key={ageClass + "_selected"}
                mode="outlined"
                style={{ 
                  borderColor: "black",
                  borderWidth: 0.85,
                  borderRadius: 12,
                  backgroundColor: "lightgrey",
                }}
                textColor="black"
                onPress={() => toggleAgeClass(ageClass)}>
                {ageClass}
              </Button>
              ))}
            </View>
            <Button
              icon={() => (<Ionicons name="search-outline" size={24}/>)}
              textColor="black"
              buttonColor="transparent"
              style={{ position: "absolute", right: 0 }}
              onPress={() => {console.log(selectedAgeClasses)}}
            />
          </View>
        </View>

        {showFilters && (
          <Card style={styles.filterWindow}>
            <View className="ageClassButtons">
              <Card.Content>
                <View className="ageClassButtonsLayout" style={{ flexDirection: "row"}}>
                  <View className="ageClassButtonsMen">
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
                  </View>
                  <View className="ageClassButtonsWomen">
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
                  </View>
                </View>
             </Card.Content>
            </View>
          </Card>
        )}
      </View>
    </SafeAreaView>
  );
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
    maxWidth: 165,
  },
  ageClassButton: {
    borderColor: "black",
    borderWidth: 0.85,
    marginTop: 3,
    marginBottom: 3,
    marginRight: 5,
    borderRadius: 12,
  },
  firstAgeClassButton: {
    borderColor: "black",
    borderWidth: 0.85,
    marginTop: 13,
    marginBottom: 3,
    marginRight: 5,
    borderRadius: 12
  },
  lastAgeClassButton: {
    borderColor: "black",
    borderWidth: 0.85,
    marginTop: 3,
    marginBottom: 13,
    marginRight: 5,
    borderRadius: 12
  }
});

// todos:
// - add clear all age classes button in filter window
//     -> this button removes all the selected age classes out of the selectedAgeClasses array
// - add headers for Herren and Damen in the filter window
// - add cache for selected age classes
