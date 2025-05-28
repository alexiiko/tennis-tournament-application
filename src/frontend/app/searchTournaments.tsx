import { retrieveDBData } from "../services/fetchDataDB.js";
import { View, StyleSheet } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { Button, Card } from "react-native-paper";
import { useState } from "react";


export default function main() {
  const [showFilters, setShowFilters] = useState(false);
  const [selectedAgeClasses, setSelectedAgeClasses] = useState([]);

  const toggleAgeClass = (ageClass) => {
    setSelectedAgeClasses((prev) =>
      prev.includes(ageClass)
        ? prev.filter((item) => item !== ageClass)
        : [...prev, ageClass]
    );
  };

  return (
    <SafeAreaView>
      <View>
        <View
          style={{
            borderWidth: 1,
            borderColor: "grey",
            padding: 10,
            borderRadius: 7,
            marginLeft: 5,
            marginRight: 5,
          }}
        >
          <View style={{ justifyContent: "center" }}>
            <Button
              icon="filter"
              textColor="black"
              buttonColor="transparent"
              style={{ position: "absolute", left: 0 }}
              onPress={() => setShowFilters((prev) => !prev)}
            />
            <Button
              icon="magnify"
              textColor="black"
              buttonColor="transparent"
              style={{ position: "absolute", right: 0 }}
              onPress={() => {console.log(selectedAgeClasses)}}
            />
          </View>
        </View>

        {showFilters && (
          <Card style={styles.popup}>
            <View>
              <Card.Content>
                <Button 
                  key="M11"
                  onPress={() => toggleAgeClass("M11")}
                  style={styles.ageClassButton}
                >M11</Button>
               <Button 
                  key="M12"
                  onPress={() => toggleAgeClass("M12")}
                  style={styles.ageClassButton}
                >M12</Button>
             </Card.Content>
            </View>
          </Card>
        )}
      </View>
    </SafeAreaView>
  );
}


const styles = StyleSheet.create({
  popup: {
    width: 200,
    position: "absolute",
    top: 30,
    left: 10,
    right: 10,
    backgroundColor: "white",
    elevation: 4,
    borderRadius: 10,
  },
  ageClassButton: {
    borderColor: "black",
    borderWidth: 0.75,
    marginTop: 3,
    // change text color and add coloring when button is pressed 
  }
});

